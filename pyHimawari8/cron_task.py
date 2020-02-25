
import subprocess
import toml
import os
from logger import logger
import datetime as dt
from bypy import ByPy
from helper import tRange, getH8ProdFile, getCBSettings
from visualizer import Visualizer


PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGFILE = os.path.join(PROJECTDIR, 'pyHimawari8', 'config', 'settings.toml')
tNow = dt.datetime.now()

# load configurations
with open(CONFIGFILE, 'r', encoding='utf-8') as fh:
    CONFIG = toml.loads(fh.read())

# mount JAXA FTP server
cmd = 'curlftpfs {0} {1}'.format(CONFIG['JAXAFTP_LINK'], CONFIG['JAXAFTP_MP'])
ret = subprocess.call(cmd)
if ret != 0:
    logger.error('Error in mount JAXA FTP server!')
    raise Exception('Error in running {0}'.format(cmd))

# create time list
tLapse = dt.timedelta(seconds=3600 * 12)
tStart = tNow - tLapse
tStartAtHour = dt.timedelta(tStart.year, tStart.month, tStart.day, tStart.hour)
timeList = tRange(tStartAtHour, tNow, timedelta=1800)

for mTime in timeList:

    # create directory
    save_dir = os.path.join(CONFIG['IMG_DIR'], mTime.strftime('%Y%m%d'))
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        logger.info('Create saving directory {0}'.format(save_dir))

    # create RGB image
    # TODO

    # create Cloud phase image
    product = 'CLP'
    variable = 'CLTYPE'
    verison = '010'
    imgFile = os.path.join(
        save_dir,
        'H8_{prod}_{var}_{HHMM}_{verison}.png'.format(
            prod=product,
            var=variable,
            HHMM=mTime.strftime('%H%M'),
            version=version
        ))
    CLPFile = getH8ProdFile(mTime, product, version=verison)
    CLTYPE_cbRange, CLTYPE_cbTick, CLTYPE_TL = getCBSettings('CLTYPE')
    vis = Visualizer(CLPFile,
                     latRange=CONFIG['LAT_RANGE'],
                     lonRange=CONFIG['LON_RANGE'])
    vis.load_data(variable, mTime)
    vis.colorplot(
        imgFile,
        axLatRange=CONFIG['LAT_RANGE'],
        axLonRange=CONFIG['LON_RANGE'],
        vmin=CLTYPE_cbRange[0], vmax=CLTYPE_cbRange[1],
        cb_ticks=CLTYPE_cbTick, cb_ticklabels=CLTYPE_TL)
    logger.info('Export to {0}'.format(imgFile))

    # create Cloud top height image
    product = 'CLP'
    variable = 'CLTH'
    verison = '010'
    imgFile = os.path.join(
        save_dir,
        'H8_{prod}_{var}_{HHMM}_{verison}.png'.format(
            prod=product,
            var=variable,
            HHMM=mTime.strftime('%H%M'),
            version=version
        ))
    CLPFile = getH8ProdFile(mTime, product, version=verison)
    vis = Visualizer(CLPFile,
                     latRange=CONFIG['LAT_RANGE'],
                     lonRange=CONFIG['LON_RANGE'])
    vis.load_data(variable, mTime)
    vis.colorplot(
        imgFile,
        axLatRange=CONFIG['LAT_RANGE'],
        axLonRange=CONFIG['LON_RANGE'],
        vmin=0, vmax=15)
    logger.info('Export to {0}'.format(imgFile))

    # create AOD plot with radiance
    product = 'ARP'
    variable = 'AOT'
    verison = '021'
    imgFile = os.path.join(
        save_dir,
        'H8_{prod}_{var}_{HHMM}_{verison}.png'.format(
            prod=product,
            var=variable,
            HHMM=mTime.strftime('%H%M'),
            version=version
        ))
    ARPFile = getH8ProdFile(mTime, product, version=verison)
    vis = Visualizer(ARPFile,
                     latRange=CONFIG['LAT_RANGE'],
                     lonRange=CONFIG['LON_RANGE'])
    vis.load_data(variable, mTime)
    vis.colorplot_with_band(
        1,
        imgFile,
        axLatRange=CONFIG['LAT_RANGE'],
        axLonRange=CONFIG['LON_RANGE'],
        vmin=0, vmax=1,
        pixels=1000,
        cmap='gist_gray')
    logger.info('Export to {0}'.format(imgFile))

# push to baiduyun
bp = ByPy()
# You need to authorize the app manually at first time.
bp.mkdir(CONFIG['BDY_DIR'])
bp.syncup(CONFIG['IMG_DIR'], CONFIG['BDY_DIR'])
logger.info('Successfully sync items to Baidu Yun!')
