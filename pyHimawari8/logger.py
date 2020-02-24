import logging
import os
import sys

LOG_MODE = 'INFO'
LOGFILE = 'log'
PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# initialize the logger
logFile = os.path.join(PROJECTDIR, LOGFILE)
logModeDict = {
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'DEBUG': logging.DEBUG,
    'ERROR': logging.ERROR
    }

logFile = os.path.join(
    PROJECTDIR, LOGFILE)
logger = logging.getLogger(__name__)

fh = logging.FileHandler(logFile)
fh.setLevel(logModeDict[LOG_MODE])
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logModeDict[LOG_MODE])

formatterFh = logging.Formatter('%(asctime)s - %(name)s - ' +
                                '%(funcName)s - %(lineno)d - %(message)s')
formatterCh = logging.Formatter('%(message)s')
fh.setFormatter(formatterFh)
ch.setFormatter(formatterCh)

logger.addHandler(fh)
logger.addHandler(ch)

logger.setLevel(logModeDict['DEBUG'])
