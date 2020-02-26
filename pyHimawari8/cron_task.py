
import subprocess
import toml
import os
from logger import logger
import datetime as dt
from bypy import ByPy
from visualizer import Visualizer
from helper import tRange, getH8ProdFile, getCBSettings
from colormap import target_classification_colormap


PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGFILE = os.path.join(PROJECTDIR, 'pyHimawari8', 'config', 'settings.toml')
tNow = dt.datetime.now()

# load configurations
with open(CONFIGFILE, 'r', encoding='utf-8') as fh:
    CONFIG = toml.loads(fh.read())

# mount JAXA FTP server
cmd = '/usr/bin/curlftpfs {0} {1} -o nonempty'.format(
    CONFIG['JAXAFTP_LINK'], CONFIG['JAXAFTP_MP'])
ret = subprocess.call(cmd, shell=True)

# create time list
tLapse = dt.timedelta(seconds=3600 * 6)
tStart = tNow - tLapse
tStartAtHour = dt.datetime(tStart.year, tStart.month, tStart.day, tStart.hour)
timeList = tRange(tStartAtHour, tNow, timedelta=1800)

updatedImgs = []   # updated images

for mTime in timeList:

    # create directory
    save_dir = os.path.join(CONFIG['IMG_DIR'], mTime.strftime('%Y%m%d'))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        logger.info('Create saving directory {0}'.format(save_dir))

    # copy true color image
    product = 'TRC'   # full disk true color image
    area = 'JP01'
    AHI_TC_Img = os.path.join(
        CONFIG['JAXAFTP_MP'], 'jma', 'hsd', mTime.strftime('%Y%m'),
        mTime.strftime('%d'), mTime.strftime('%H'),
        getH8ProdFile(mTime, product, area=area))
    if os.path.exists(AHI_TC_Img):
        updatedImgs.append([mTime, AHI_TC_Img])

    # create Cloud phase image
    product = 'CLP'
    variable = 'CLTYPE'
    version = '010'
    pLe = 'L2'
    imgFile = os.path.join(
        save_dir,
        'H8_{prod}_{var}_{HHMM}_{version}.png'.format(
            prod=product, var=variable, HHMM=mTime.strftime('%H%M'),
            version=version))
    CLPFile = os.path.join(
        CONFIG['JAXAFTP_MP'], 'pub', 'himawari', pLe, product, version,
        mTime.strftime('%Y%m'), mTime.strftime('%d'), mTime.strftime('%H'),
        getH8ProdFile(mTime, product, version=version, pLe=pLe))

    if os.path.exists(CLPFile):
        vis = Visualizer(
            CLPFile,
            latRange=CONFIG['LAT_RANGE'],
            lonRange=CONFIG['LON_RANGE'])
        vis.load_data(variable, mTime)

        CLTYPE_cbRange, CLTYPE_cbTick, CLTYPE_TL = getCBSettings('CLTYPE')
        vis.colorplot(
            imgFile,
            axLatRange=CONFIG['LAT_RANGE'],
            axLonRange=CONFIG['LON_RANGE'],
            vmin=CLTYPE_cbRange[0], vmax=CLTYPE_cbRange[1],
            cb_ticks=CLTYPE_cbTick, cb_ticklabels=CLTYPE_TL,
            cmap=target_classification_colormap())
        logger.info('Export to {0}'.format(imgFile))

        updatedImgs.append([mTime, imgFile])
    else:
        logger.warn('CLP file does not exist.\n{0}'.format(CLPFile))

    # create Cloud top height image
    product = 'CLP'
    variable = 'CLTH'
    version = '010'
    pLe = 'L2'
    imgFile = os.path.join(
        save_dir,
        'H8_{prod}_{var}_{HHMM}_{version}.png'.format(
            prod=product, var=variable, HHMM=mTime.strftime('%H%M'),
            version=version))
    CLPFile = os.path.join(
        CONFIG['JAXAFTP_MP'], 'pub', 'himawari', pLe, product, version,
        mTime.strftime('%Y%m'), mTime.strftime('%d'), mTime.strftime('%H'),
        getH8ProdFile(mTime, product, version=version, pLe=pLe))

    if os.path.exists(CLPFile):
        vis = Visualizer(
            CLPFile,
            latRange=CONFIG['LAT_RANGE'],
            lonRange=CONFIG['LON_RANGE'])
        vis.load_data(variable, mTime)

        vis.colorplot(
            imgFile,
            axLatRange=CONFIG['LAT_RANGE'],
            axLonRange=CONFIG['LON_RANGE'],
            vmin=0, vmax=15)
        logger.info('Export to {0}'.format(imgFile))

        updatedImgs.append([mTime, imgFile])
    else:
        logger.warn('CLP file does not exist.\n{0}'.format(CLPFile))

    # create AOD plot with radiance
    product = 'ARP'
    variable = 'AOT'
    version = '021'
    pLe = 'L2'
    HSD_Dir = os.path.join(
        CONFIG['JAXAFTP_MP'], 'jma', 'hsd', mTime.strftime('%Y%m'),
        mTime.strftime('%d'), mTime.strftime('%H')
    )
    imgFile = os.path.join(
        save_dir, 'H8_{prod}_{var}_{HHMM}_{version}.png'.format(
            prod=product, var=variable, HHMM=mTime.strftime('%H%M'),
            version=version))
    ARPFile = os.path.join(
        CONFIG['JAXAFTP_MP'], 'pub', 'himawari', pLe, product, version,
        mTime.strftime('%Y%m'), mTime.strftime('%d'), mTime.strftime('%H'),
        getH8ProdFile(mTime, product, version=version, pLe=pLe))

    if os.path.exists(ARPFile):
        vis = Visualizer(
            ARPFile,
            latRange=CONFIG['LAT_RANGE'],
            lonRange=CONFIG['LON_RANGE'])

        vis.load_data(variable, mTime)

        try:
            vis.colorplot_with_band(
                1, HSD_Dir, imgFile,
                axLatRange=CONFIG['LAT_RANGE'],
                axLonRange=CONFIG['LON_RANGE'],
                vmin=0, vmax=1,
                pixels=1000)
            logger.info('Export to {0}'.format(imgFile))

            updatedImgs.append([mTime, imgFile])
        except ValueError as e:
            logger.warn(e)
    else:
        logger.warn('ARP file does not exist.\n{0}'.format(ARPFile))

# push to baiduyun
bp = ByPy()
# You need to authorize the app manually at first time.
logger.info('Start to sync items to Baidu Yun!')
bp.mkdir(CONFIG['BDY_DIR'])
for item in updatedImgs:
    logger.info('Upload to BDY: {0}'.format(item[1]))
    BDY_Dir = os.path.join(CONFIG['BDY_DIR'], item[0].strftime('%Y%m%d'))
    bp.mkdir(BDY_Dir)
    bp.upload(item[1], BDY_Dir)

# umount ftp server
cmd = 'umount {0}'.format(CONFIG['JAXAFTP_MP'])
subprocess.call(cmd, shell=True)
