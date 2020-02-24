
def main():
    from colormap import target_classification_colormap
    from helper import getCBSettings

    axLatRange = [15, 58]
    axLonRange = [70, 140]

    cbRange, cbTicks, cbTickLabels = getCBSettings('CLTYPE')
    vis = Visualizer(
        os.path.join(PROJECTDIR,
                     'data',
                     'NC_H08_20200219_0400_L2ARP021_FLDK.02401_02401.nc'),
                     latRange=axLatRange, lonRange=axLonRange)
    # vis.list_product()
    vis.load_data('AOT')
    imgFile1 = os.path.join(PROJECTDIR, 'img', 'ARP_AOT_plot.png')
    vis.colorplot(imgFile1, axLatRange=axLatRange, axLonRange=axLonRange, vmin=0, vmax=1)
    imgFile2 = os.path.join(PROJECTDIR, 'img', 'ARP_AOT_B01_plot.png')
    vis.colorplot_with_band(1, imgFile2, axLatRange=axLatRange, axLonRange=axLonRange, vmin=0, vmax=1, pixels=1000, cmap='jet')

import subprocess
import toml
import os
from logger import logger
import datetime as dt


PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGFILE = os.path.join(PROJECTDIR, 'pyHimawari8', 'config', 'settings.toml')

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
tNow = dt.datetime.now()


# create RGB image

# create Cloud phase image

# create AOD plot with radiance

# push to baiduyun
