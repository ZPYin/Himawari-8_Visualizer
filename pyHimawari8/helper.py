#!/bin/local/python

import os
import datetime as dt
from logger import logger
import numpy as np


def getH8ProdFile(thisTime, product, *,
                  pLe='L2', version='021',
                  pixelNum='02401', lineNum='02401'):
    """
    get the Himawari-8 product filename.

    Parameters
    ----------
    thisTime: datetime
        query time.
    product: str
        product type.
        1. 'CLP': cloud property
        2. 'ARP': aerosol property
    Keywords
    --------
    pLe: str
        product level (default: 'L2'). ('L2' or 'L3')
    version: str
        algorithm version (default: '021'). ('010', '020' or '021')
    pixelNum: str
        pixel number (default: '02401').
    lineNum: str
        line number (default: '02401').
    Examples
    --------
    >>> import datetime as np
    >>> getH8ProdFile(dt.datetime(2011, 1, 1), 'CLP')
    'NC_H08_20110101_0000_L2CLP021_FLDK.02401_02401.nc'

    History
    -------
    2020-02-25 First version.
    """

    file = ''

    if product == 'CLP':
        # cloud product
        file = 'NC_H08_{yyyymmdd}_{HHMM}_{pLe}'.format(
                    yyyymmdd=thisTime.strftime('%Y%m%d'),
                    HHMM=thisTime.strftime('%H%M'),
                    pLe=pLe) +\
               '{product}{version}_FLDK.{pixelNum}_{lineNum}.nc'.format(
                   product=product,
                   version=version,
                   pixelNum=pixelNum,
                   lineNum=lineNum)
    elif product == 'ARP':
        # aerosol product
        file = 'NC_H08_{yyyymmdd}_{HHMM}_{pLe}'.format(
                    yyyymmdd=thisTime.strftime('%Y%m%d'),
                    HHMM=thisTime.strftime('%H%M'),
                    pLe=pLe) +\
               '{product}{version}_FLDK.{pixelNum}_{lineNum}.nc'.format(
                   product=product,
                   version=version,
                   pixelNum=pixelNum,
                   lineNum=lineNum)
    else:
        raise Exception('Unknown product {}'.format(product))

    return file


def tRange(tStart, tStop, *, timedelta=300):
    """
    Generate datetime list between tStart and tStop with fixed timedelta.

    Parameters
    ----------
    tStart: datetime
        start time.
    tStop: datetime
        stop time.
    Keywords
    --------
    timedelta: int
        time delta in seconds (default: 300).
    Returns
    -------
    tList: list
        datetime between tStart and tStop with fixed timedelta.
    Examples
    --------
    >>> import datetime as dt
    >>> tList = tRange(dt.datetime(2011, 1, 1), dt.datetime(2011, 1, 2), ...
    >>>                timedelta=3600 * 12)
    >>> tList
    [datetime.datetime(2011, 1, 1, 0, 0), datetime.datetime(2011, 1, 1, 12, 0),
    datetime.datetime(2011, 1, 2, 0, 0)]

    History
    -------
    2020-02-25 First version.
    """

    nTimedelta = int((tStop - tStart) / dt.timedelta(seconds=timedelta)) + 1
    tList = [tStart + dt.timedelta(seconds=timedelta * i)
             for i in range(0, nTimedelta)
             if tStart + dt.timedelta(seconds=timedelta * i) <= tStop]

    return tList


def parseTime(file, ft='CLP', pLe='L2'):
    """
    parse the measurement time from the filename string.

    Parameters
    ----------
    file: str
        filename
    ft: str
        file type: 
            1. 'CLP' (Cloud Property)
            2. 'ARP' (Aerosol Property)
            3. 'SST' (Sea Surface Temperature)
            4. 'WLF' (Wild Fire)
    pLe: str
        product level:
            1. 'L2' (Level 2)
            2. 'L3' (Level 3)
    Returns
    -------
    tObj: datetime
        measurement time of the file.

    Examples
    --------
    >>> parseTime('NC_H08_20200101_0000_L2CLP010_FLDK.02401_02401.nc')
    datetime.datetime(2015, 7, 27, 8, 0)

    References
    ----------
    1. ./doc/README_HimawariGeo_en.txt

    History
    -------
    2020-02-23 First version.
    """

    fileBaseName = os.path.basename(file)

    if ft == 'CLP' and pLe == 'L2':
        tObj = dt.datetime.strptime(fileBaseName[7:20], '%Y%m%d_%H%M')
    else:
        raise Exception('Unknown fileType or productLevel!')

    return tObj


def getCBSettings(product):
    """
    Return suitable colorbar settings for Himawari-8 classification products.

    Parameters
    ----------
    product: str
        product name. ('CLTYPE')
    Returns
    -------
    cbRange: list
        colorbar range. [vmin, vmax]
    cbTicks: list
        postion of each tick labels.
    cbTickLabels: list
        tick labels.
    Examples
    --------
    >>> cbRange, cbTicks, cbTickLabels = getCBSettings('CLTYPE)
    >>> cbRange
    [-0.5, 10.5]
    History
    -------
    2020-02-23 First version.
    """

    cbRange = None
    cbTicks = None
    cbTickLabels = None

    if product == 'CLTYPE':
        cbRange = [-0.5, 10.5]
        cbTicks = np.arange(0, 11)
        cbTickLabels = ['Clear', 'Ci', 'Cs', 'Deep Convection',
                        'Ac', 'As', 'Ns', 'Cu', 'Sc', 'St', 'Unknown']
    else:
        raise Exception('Unknown product: {0}'.format(product))

    return cbRange, cbTicks, cbTickLabels


def read_Himawari8(inFile):
    """
    read Himawari8 binary data.

    WARNING WARNING WARNING!!!
    Discarded since satpy provides easier interface to play with HSD dataset.

    Parameters
    ----------
    inFile: str
        filename.
    Returns
    -------
    Examples
    --------
    References
    ----------
    1. https://blog.csdn.net/qq_33339770/article/details/102708243
    """

    resolution = int(os.path.basename(inFile)[-12])

    if resolution == 1:
        res = 12100000
        nlin = 1100
        ncol = 11000
    elif resolution == 2:
        res = 3025000
        nlin = 550
        ncol = 5500
    else:
        res = 48400000
        nlin = 2200
        ncol = 22000

    band = int(os.path.basename(inFile)[-21:-19])
    if band < 7:
        formation = [
            ('Block number1', 'i1', 1),
            ('Block length1', 'i2', 1),
            ('Total number of header blocks ', 'i2', 1),
            ('Byte order', 'i1', 1),
            ('Satellite name', 'S1', 16),
            ('Processing center name', 'S1', 16),
            ('Observation area', 'S1', 4),
            ('Other observation information', 'S1', 2),
            ('Observation timeline', 'i2', 1),
            ('Observation start time', 'float64', 1),
            ('Observation end time', 'float64', 1),
            ('File creation time', 'float64', 1),
            ('Total header length', 'i4', 1),
            ('Total data length', 'i4', 1),
            ('Quality flag 1', 'i1', 1),
            ('Quality flag 2 ', 'i1', 1),
            ('Quality flag 3', 'i1', 1),
            ('Quality flag 4', 'i1', 1),
            ('File format version', 'S1', 32),
            ('File name ', 'S1', 128),
            ('Spare1', 'S1', 40),
            ('Block number2', 'i1', 1),
            ('Block length2', 'i2', 1),
            ('Number of bits per pixel', 'i2', 1),
            ('Number of columns', 'i2', 1),
            ('Number of lines', 'i2', 1),
            ('Compression flag for data', 'i1', 1),
            ('Spare2', 'S1', 40),
            ('Block number3', 'i1', 1),
            ('Block length3', 'i2', 1),
            ('sub_lon', 'float64', 1),
            ('Column scaling factor', 'i4', 1),
            ('Line scaling factor', 'i4', 1),
            ('Column offset', 'float32', 1),
            ('Line offset', 'float32', 1),
            ('Distance from Earth’s center to virtual satellite',
             'float64', 1),
            ('Earth’s equatorial radius', 'float64', 1),
            ('Earth’s polar radius', 'float64', 1),
            ('var1', 'float64', 1),
            ('var2', 'float64', 1),
            ('var3', 'float64', 1),
            ('Coefficient for sd', 'float64', 1),
            ('Resampling types', 'i2', 1),
            ('Resampling size', 'i2', 1),
            ('Spare3', 'S1', 40),
            ('Block number4', 'i1', 1),
            ('Block length4', 'i2', 1),
            ('Navigation information time', 'float64', 1),
            ('SSP longitude', 'float64', 1),
            ('SSP latitude', 'float64', 1),
            ('Distance from Earth’s center to Satellite', 'float64', 1),
            ('Nadir longitude', 'float64', 1),
            ('Nadir latitude', 'float64', 1),
            ('Sun’s position', 'float64', 3),
            ('Moon’s position', 'float64', 3),
            ('Spare4', 'S1', 40),
            ('Block number5', 'i1', 1),
            ('Block length5', 'i2', 1),
            ('Band number', 'i2', 1),
            ('Central wave length', 'float64', 1),
            ('Valid number of bits per pixel', 'i2', 1),
            ('Count value of error pixels', 'uint16', 1),
            ('Count value of pixels outside scan area', 'uint16', 1),
            ('Slope for count-radiance conversion equation ', 'float64', 1),
            ('Intercept for count-radiance conversion equation', 'float64', 1),
            ('Coefficient for transformation from radiance to albedo',
             'float64', 1),
            ('Update time of the values of the following No. 12 and No. 13',
             'float64', 1),
            ('Calibrated Slope for count-radiance conversion ' +
             'equation_updated value of No. 8 of this block ', 'float64', 1),
            ('Calibrated Intercept for count-radiance conversion ' +
             'equation_updated value of No. 9 of this block ', 'float64', 1),
            ('Spare5', 'S1', 80),
            ('Block number6', 'i1', 1),
            ('Block length6', 'i2', 1),
            ('GSICS calibration coefficient_Intercept', 'float64', 1),
            ('GSICS calibration coefficient_Slope', 'float64', 1),
            ('GSICS calibration coefficient_Quadratic term', 'float64', 1),
            ('Radiance bias for standard scene', 'float64', 1),
            ('Uncertainty of radiance bias for standard scene', 'float64', 1),
            ('Radiance for standard scene', 'float64', 1),
            ('Start time of GSICS Correction validity period', 'float64', 1),
            ('End time of GSICS Correction validity period', 'float64', 1),
            ('Radiance validity range of GSICS calibration ' +
             'coefficients_upper limit', 'float32', 1),
            ('Radiance validity range of GSICS calibration ' +
             'coefficients_lower limit', 'float32', 1),
            ('File name of GSICS Correction', 'S1', 128),
            ('Spare6', 'S1', 56),
            ('Block number7', 'i1', 1),
            ('Block length7', 'i2', 1),
            ('Total number of segments', 'i1', 1),
            ('Segment sequence number', 'i1', 1),
            ('First line number of image segment', 'i2', 1),
            ('Spare7', 'S1', 40),
            ('Block number8', 'i1', 1),
            ('Block length8', 'i2', 1),
            ('Center column of rotation', 'float32', 1),
            ('Center line of rotation', 'float32', 1),
            ('Amount of rotational correction', 'float64', 1),
            ('Number of correction information data for ' +
             'column and line direction', 'i2', 1),
            ('Line number after rotation', 'i2', 1),
            ('Shift amount for column direction', 'float32', 1),
            ('Shift amount for line direction8', 'float32', 1),
            ('Spare8', 'S1', 50),
            ('Block number9', 'i1', 1),
            ('Block length9', 'i2', 1),
            ('Number of observation times9', 'i2', 1),
            ('Line number9', 'i2', 1),
            ('Observation time9', 'float64', 1),
            ('Spare9', 'S1', 70),
            ('Block number10', 'i1', 1),
            ('Block length10', 'i4', 1),
            ('Number of error information data', 'i2', 1),
            ('Line number10', 'i2', 1),
            ('Number of error pixels per line10', 'i2', 1),
            ('Spare10', 'S1', 36),
            ('Block number11', 'i1', 1),
            ('Block length11', 'i2', 1),
            ('Spare11', 'S1', 256),
            ('Count value of each pixel', 'i2', res)]
    else:
        formation = [
            ('Block number1', 'i1', 1),
            ('Block length1', 'i2', 1),
            ('Total number of header blocks ', 'i2', 1),
            ('Byte order', 'i1', 1),
            ('Satellite name', 'S1', 16),
            ('Processing center name', 'S1', 16),
            ('Observation area', 'S1', 4),
            ('Other observation information', 'S1', 2),
            ('Observation timeline', 'i2', 1),
            ('Observation start time', 'float64', 1),
            ('Observation end time', 'float64', 1),
            ('File creation time', 'float64', 1),
            ('Total header length', 'i4', 1),
            ('Total data length', 'i4', 1),
            ('Quality flag 1', 'i1', 1),
            ('Quality flag 2 ', 'i1', 1),
            ('Quality flag 3', 'i1', 1),
            ('Quality flag 4', 'i1', 1),
            ('File format version', 'S1', 32),
            ('File name ', 'S1', 128),
            ('Spare1', 'S1', 40),
            ('Block number2', 'i1', 1),
            ('Block length2', 'i2', 1),
            ('Number of bits per pixel', 'i2', 1),
            ('Number of columns', 'i2', 1),
            ('Number of lines', 'i2', 1),
            ('Compression flag for data', 'i1', 1),
            ('Spare2', 'S1', 40),
            ('Block number3', 'i1', 1),
            ('Block length3', 'i2', 1),
            ('sub_lon', 'float64', 1),
            ('Column scaling factor', 'i4', 1),
            ('Line scaling factor', 'i4', 1),
            ('Column offset', 'float32', 1),
            ('Line offset', 'float32', 1),
            ('Distance from Earth’s center to virtual satellite',
             'float64', 1),
            ('Earth’s equatorial radius', 'float64', 1),
            ('Earth’s polar radius', 'float64', 1),
            ('var1', 'float64', 1),
            ('var2', 'float64', 1),
            ('var3', 'float64', 1),
            ('Coefficient for sd', 'float64', 1),
            ('Resampling types', 'i2', 1),
            ('Resampling size', 'i2', 1),
            ('Spare3', 'S1', 40),
            ('Block number4', 'i1', 1),
            ('Block length4', 'i2', 1),
            ('Navigation information time', 'float64', 1),
            ('SSP longitude', 'float64', 1),
            ('SSP latitude', 'float64', 1),
            ('Distance from Earth’s center to Satellite', 'float64', 1),
            ('Nadir longitude', 'float64', 1),
            ('Nadir latitude', 'float64', 1),
            ('Sun’s position', 'float64', 3),
            ('Moon’s position', 'float64', 3),
            ('Spare4', 'S1', 40),
            ('Block number5', 'i1', 1),
            ('Block length5', 'i2', 1),
            ('Band number', 'i2', 1),
            ('Central wave length', 'float64', 1),
            ('Valid number of bits per pixel', 'i2', 1),
            ('Count value of error pixels', 'i2', 1),
            ('Count value of pixels outside scan area', 'i2', 1),
            ('Slope for count-radiance conversion equation ', 'float64', 1),
            ('Intercept for count-radiance conversion equation', 'float64', 1),
            ('radiance to brightness temperature_c0', 'float64', 1),
            ('radiance to brightness temperature_c1', 'float64', 1),
            ('radiance to brightness temperature_c2', 'float64', 1),
            ('brightness temperature to radiance_C0', 'float64', 1),
            ('brightness temperature to radianceC1', 'float64', 1),
            ('brightness temperature to radianceC2', 'float64', 1),
            ('Speed of light', 'float64', 1),
            ('Planck constant', 'float64', 1),
            ('Boltzmann constant', 'float64', 1),
            ('Spare5', 'S1', 40),
            ('Block number6', 'i1', 1),
            ('Block length6', 'i2', 1),
            ('GSICS calibration coefficient_Intercept', 'float64', 1),
            ('GSICS calibration coefficient_Slope', 'float64', 1),
            ('GSICS calibration coefficient_Quadratic term', 'float64', 1),
            ('Radiance bias for standard scene', 'float64', 1),
            ('Uncertainty of radiance bias for standard scene', 'float64', 1),
            ('Radiance for standard scene', 'float64', 1),
            ('Start time of GSICS Correction validity period', 'float64', 1),
            ('End time of GSICS Correction validity period', 'float64', 1),
            ('Radiance validity range of GSICS calibration ' +
             'coefficients_upper limit', 'float32', 1),
            ('Radiance validity range of GSICS calibration ' +
             'coefficients_lower limit', 'float32', 1),
            ('File name of GSICS Correction', 'S1', 128),
            ('Spare6', 'S1', 56),
            ('Block number7', 'i1', 1),
            ('Block length7', 'i2', 1),
            ('Total number of segments', 'i1', 1),
            ('Segment sequence number', 'i1', 1),
            ('First line number of image segment', 'i2', 1),
            ('Spare7', 'S1', 40),
            ('Block number8', 'i1', 1),
            ('Block length8', 'i2', 1),
            ('Center column of rotation', 'float32', 1),
            ('Center line of rotation', 'float32', 1),
            ('Amount of rotational correction', 'float64', 1),
            ('Number of correction information data for column ' +
             'and line direction', 'i2', 1),
            ('Line number after rotation', 'i2', 1),
            ('Shift amount for column direction', 'float32', 1),
            ('Shift amount for line direction8', 'float32', 1),
            ('Spare8', 'S1', 50),
            ('Block number9', 'i1', 1),
            ('Block length9', 'i2', 1),
            ('Number of observation times9', 'i2', 1),
            ('Line number9', 'i2', 1),
            ('Observation time9', 'float64', 1),
            ('Spare9', 'S1', 70),
            ('Block number10', 'i1', 1),
            ('Block length10', 'i4', 1),
            ('Number of error information data', 'i2', 1),
            ('Line number10', 'i2', 1),
            ('Number of error pixels per line10', 'i2', 1),
            ('Spare10', 'S1', 36),
            ('Block number11', 'i1', 1),
            ('Block length11', 'i2', 1),
            ('Spare11', 'S1', 256),
            ('Count value of each pixel', 'i2', res)]

    data = np.fromfile(inFile, dtype=formation)
    return data
