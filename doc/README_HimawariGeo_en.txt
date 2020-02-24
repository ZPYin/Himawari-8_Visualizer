********************************************************************************

README for the Himawari Geophysical Parameter Data
 through the JAXA's P-Tree System

Prepared by Earth Observation Research Center (EORC),
            Japan Aerospace Exploration Agency (JAXA).

Aug.31,2015: The Himawari-8 Aerosol Property and Sea Surface Temperature data 
             are released.
Mar.28,2015: The Himawari-8 Short Wave Radiation/Photosynthetically Available 
             Radiation data and Chlorophyll-a data are released.
Aug.31,2016: The Himawari-8 Cloud Property data are released.
Dec.21,2016: The Himawari-8 Wild Fire data are released.
Feb. 5,2018: The Himawari-8 Aerosol Property data (Ver. 2.0) are released.
Aug.10,2018: The Himawari-8 Aerosol Property data (Level2: Ver.2.1, Level3 Hourly: Ver.3.0),
             The Himawari-8 Daily data (Aerosol Property, Wild Fire),
             The Himawari-8 Monthly data (Sea Surface Temperature, Aerosol Property, Wild Fire)
             are released.
Oct.23,2018: Replacement of the Himawar-8 SST Level 2/3 (ver.1.2) files to reprocessed data (fv02) 
             for the period during Feb.15 to Jul.27, 2018 due to a problem in operational processing. 
Oct.31,2018: The Himawari-8 Cloud Property data (Ver. 1.0) are released.

********************************************************************************

In this directory, the Geophysical Parameter Data estimated from 
the geostationary Himawari-8 Standard Data and Model Paramteters are 
available in near-real-time. 
You can also download the past period data of the Geophysical Parameter Data
since Mar.20, 2015.

Please note that past period data of the JAXA Geophysical Parameter Data
will be uploaded to the ftp site upon completion of its processing.

********************************************************************************

# Available Geophysical Parameters

## Aerosol Property (day-time only)
 Latest version: Version 2.1 (Level 2), Version 3.0 (Level 3)
 Observation area: Full-disk
 Temporal resolution: 10-minutes (Level 2),1-hour (Level 3), 
                      1-day (Level 3), 1-month (Level 3)
 Spatial resolution: 5km (Pixel number: 2401, Line number: 2401)
 NOTE: Angstrom exponent included this product is under validation. 
       Users should keep in mind that the data is NOT quality assured. 

## Sea Surface Temperature
 Latest version: Version 1.2
 Observation area: Full-disk
 Temporal resolution: 10-minutes (Level 2), 1-hour (Level 3),
                      1-day (Level 3), 1-month (Level 3)
 Spatial resolution: 2km (Pixel number: 6001, Line number: 6001)

## Nighttime Sea Surface Temperature
 Latest version: Version 1.2
 Observation area: Full-disk
 Temporal resolution: 1-hour (Level 3)
 Spatial resolution: 2km (Pixel number: 6001, Line number: 6001)

## Short Wave Radiation / Photosynthetically Available Radiation
 Latest version: Version 1.0 
 Observation area: Full-disk
 Temporal resolution: 10-minutes (Level 2), 1-hour (Level 3), 
                      1-day (Level 3), 1-month (Level 3)
 Spatial resolution: 5km (Pixel number: 2401, Line number: 2401)
                     1km Japan* (Pixel number: 2701, Line number: 2601)
                     * This area coverd 24N-50N, 123E-150E.
 NOTE: This product is a beta version and is intended to show the
       preliminary result from Himawari-8. Users should keep in mind 
       that the data is NOT quality assured.

## Chlorophyll-a
 Latest version: 1.0 
 Observation area: Full-disk
 Temporal resolution: 1-hour (Level 3), 1-day (Level 3), 1-month (Level 3)
 Spatial resolution: 5km (Pixel number: 2401, Line number: 2401)
                     1km Japan* (Pixel number: 2701, Line number: 2601)
 NOTE: This product is a beta version and is intended to show the
       preliminary result from Himawari-8. Users should keep in mind 
       that the data is NOT quality assured.

## Cloud Property (day-time only)
 Latest version: 1.0 
 Observation area: Full-disk
 Temporal resolution: 10-minutes (Level 2)
 Spatial resolution: 5km (Pixel number: 2401, Line number: 2401)

## Wild Fire
 Latest version: Version Beta
 Observation area: Full-disk
 Temporal resolution: 10-minutes (Level 2), 1-hour (Level 3),
                      1-day (Level 3), 1-month (Level 3)
 Spatial resolution: 2km 
 NOTE: This product is a beta version and is intended to show the
       preliminary result from Himawari-8. Users should keep in mind 
       that the data is NOT quality assured.


********************************************************************************

# TOP FTP Directory

 /pub/

********************************************************************************

# Structure of FTP Directories

## Level 2 (every 10 minutes)
### Aerosol Property (ARP) Level 2
 /pub/himawari
       +---/L2
             +---/ARP
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]
                                        +---/[hh]

### Sea Surface Temperature (SST) Level 2 (near-real-time)
 /pub/himawari
       +---/L2
             +---/SST
                   +---/[VER]_nc4_normal_nrt
                          +---/[YYYYMM]
                                 +---/[DD]

### Short Wave Radiation(SWR)/Photosynthetically Available Radiation(PAR) Level 2
 /pub/himawari
       +---/L2
             +---/PAR
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]

### Cloud Property (CLP) Level 2
 /pub/himawari
       +---/L2
             +---/CLP
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]
                                        +---/[hh]

### Wild Fire (WLF) Level 2
 /pub/himawari
       +---/L2
             +---/WLF
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]
                                        +---/[hh]


## Level 3 (hourly, daily, monthly)
### Aerosol Property Level 3
 /pub/himawari
       +---/L3
             +---/ARP
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]
                                 +---/[daily]
                                 +---/[monthly]

### Sea Surface Temperature (SST) Level 3 (near-real-time)
 /pub/himawari
       +---/L3
             +---/SST
                   +---/[VER]_nc4_normal_nrt
                          +---/[YYYYMM]
                                 +---/[DD]
                   +---/[VER]_nc4_normal_nrt_daily
                          +---/[YYYYMM]
                                 +---/[DD]
                   +---/[VER]_nc4_normal_nrt_monthly
                          +---/[YYYYMM]

### Nighttime Sea Surface Temperature (SST) Level 3 (near-real-time)
 /pub/himawari
       +---/L3
             +---/SST
                   +---/[VER]_nc4_nightt_nrt
                          +---/[YYYYMM]
                                 +---/[DD]

### Short Wave Radiation(SWR)/Photosynthetically Available Radiation(PAR) Level 3
 /pub/himawari
       +---/L3
             +---/PAR
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]
                                 +---/[daily]
                                 +---/[monthly]

### Chlorophyll-a (CHL) Level 3
 /pub/himawari
       +---/L3
             +---/CHL
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]
                                 +---/[daily]
                                 +---/[monthly]

### Wild Fire (WLF) Level 3
 /pub/himawari
       +---/L3
             +---/WLF
                   +---/[VER]
                          +---/[YYYYMM]
                                 +---/[DD]
                                 +---/[daily]
                                 +---/[monthly]

 where VER: algorithm version;
       YYYY: 4-digit year observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline; and
       hh: 2-digit hour of timeline.

********************************************************************************

# File Naming Convention

## Level 2
### Aerosol Property
 NC_H08_YYYYMMDD_hhmm_L2ARPVER_FLDK.xxxxx_yyyyy.nc

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       VER: version;
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: H08_20150727_0800_L2ARP001_FLDK.02401_02401.nc

### Sea Surface Temperature
 YYYYMMDDhhmmss-JAXA-L2P_GHRSST-SSTskin-H08_AHI-vVER-v02.0-fvFVER.nc

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       ss: 2-digit seconds (fixed to "00");
       VER: algorithm version; and
       FVER: file version;.

 Example: 
 20150728081000-JAXA-L2P_GHRSST-SSTskin-H08_AHI-v1.0-v02.0-fv01.0.nc

### Short Wave Radiation/Photosynthetically Available Radiation
 H08_YYYYMMDD_hhmm_RFLVER_FLDK_xxxxx_yyyyy.nc (5km)
 H08_YYYYMMDD_hhmm_rFLVER_FLDK_xxxxx_yyyyy.nc (1km)

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       VER: algorithm version; 
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: NC_H08_20150727_0800_RFL001_FLDK_02401_02401.nc

### Cloud Property
 NC_H08_YYYYMMDD_hhmm_L2CLPVER_FLDK.xxxxx_yyyyy.nc

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       VER: version;
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: H08_20150727_0800_L2CLPbet_FLDK.02401_02401.nc

### Wildfire
 NC_H08_YYYYMMDD_hhmm_L2WLFVER_FLDK.xxxxx_yyyyy.csv

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       VER: version;
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: H08_20150727_0800_L2WLFbet_FLDK.06001_06001.csv


## Level 3
### Aerosol Property
 H08_YYYYMMDD_hhmm_LL_ARPVER_FLDK.xxxxx_yyyyy.nc (5km)

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       LL: 2-digit temporal resolution (L3:hourly, 1D:daily, 1M:monthly) 
       VER: algorithm version; 
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: H08_20150727_0800_1H_ARP001_FLDK.02401_02401.nc


### Sea Surface Temperature
 YYYYMMDDhhmmss-JAXA-L3C_GHRSST-SSTskin-H08_AHI-vVER-v02.0-fvFVER.nc (hourly)
 YYYYMMDDhhmmss-JAXA-L3C_GHRSST-SSTskin-H08_AHI-vVER_daily-v02.0-fvFVER.nc (daily)
 H08_YYYYMMDD_HHMM_1MSSTVER_FLDK.xxxxx_yyyyy.nc  (monthly)

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline (fixed to "00");
       ss: 2-digit seconds of timeline (fixed to "00");
       VER: algorithm version;
       FVER: file version;
       xxxxx: pixel number; and
       yyyyy: line number.

 Example:
 20180804000000-JAXA-L3C_GHRSST-SSTskin-H08_AHI-v1.2-v02.0-fv01.0.nc (hourly)
 20180804000000-JAXA-L3C_GHRSST-SSTskin-H08_AHI-v1.2_daily-v02.0-fv01.0.nc (daily)
 H08_20180701_0000_1MSST120_FLDK.06001_06001.nc (monthly)

### Nighttime Sea Surface Temperature
 YYYYMMDDhhmmss-JAXA-L3C_GHRSST-SSTskin-H08_AHI-vVER_nighttime-v02.0-fvFVER.nc

 where YYYY: 4-digit year observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline(fixed to "00");
       ss: 2-digit seconds of timeline(fixed to "00");
       VER: algorithm version; and
       FVER: file version;.

 Example: 
 20150728080000-JAXA-L3C_GHRSST-SSTskin-H08_AHI-v1.0_nighttime-v02.0-fv01.0.nc

### Short Wave Radiation/Photosynthetically Available Radiation
 H08_YYYYMMDD_hhmm_LL_RFLVER_FLDK.xxxxx_yyyyy.nc (5km)
 H08_YYYYMMDD_hhmm_LL_rFLVER_FLDK.xxxxx_yyyyy.nc (1km)

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       LL: 2-digit temporal resolution (L3:hourly, 1D:daily, 1M:monthly) 
       VER: algorithm version; 
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: H08_20150727_0800_1H_RFL001_FLDK.02401_02401.nc

### Chlorophyll-a
 H08_YYYYMMDD_hhmm_LL_ROCVER_FLDK.xxxxx_yyyyy.nc (5km)
 H08_YYYYMMDD_hhmm_LL_rOCVER_FLDK.xxxxx_yyyyy.nc (1km)

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       LL: 2-digit temporal resolution (1H:hourly, 1D:daily, 1M:monthly) 
       VER: algorithm version; 
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: H08_20150727_0800_1H_ROC001_FLDK.02401_02401.nc

### Wild Fire 
 H08_YYYYMMDD_hhmm_LLWLFVER_FLDK.xxxxx_yyyyy.nc

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-digit minutes of timeline;
       LL: 2-digit temporal resolution (L3:hourly, 1D:daily, 1M:monthly) 
       VER: algorithm version; 
       xxxxx: pixel number; and
       yyyyy: line number.

 Example: H08_20180501_0000_L3WLFbet_FLDK.06001_06001.csv

********************************************************************************

# Format

  All data except for Wild Fire is in NetCDF4 format and compressed with gzip.
  Please note that NetCDF format of SST (except monthly product) follows
  the GHRSST Data Specification (GDS) 2.0. Details of GDS2.0, see the Group of 
  High Resolution Sea Surface Temperature (GHRSST) web site
  (https://www.ghrsst.org/). 

  File format of Wild Fire product is CSV. Please see following file
  (H8_WLF_format.txt) for more details. 

********************************************************************************

# Documents

## Operational schedule of Himawari-8
 Operational schedule of the geostationary Himawari-8 is available from
 the JMA's web site;
 http://www.data.jma.go.jp/mscweb/en/operation8/bulletin_list_H8.html

# Timetable of Himawari-8 Imaging
 The Himawari-8 Imaging Schedule is available from the JMA's web site.
 Please note that no observations are planned at 0240-0250UTC and 1440-1450UTC
 everyday for house-keeping of the Himawai-8 satellite.
 http://www.data.jma.go.jp/mscweb/en/operation8/Himawari-8%20Imaging%20Schedule.pdf

********************************************************************************

# References

# About Himawari-8 satellite and instrument:
 K. Bessho et al., 2016: An introduction to Himawari-8/9 - Japan's
 new-generation geostationary meteorological satellites, J. Meteorol. Soc.
 Japan, 94, doi:10.2151/jmsj.2016-009.
 http://jmsj.metsoc.jp/EOR/2016-009.pdf

# About Sea Surface Temperature Algorithm:
 Y. Kurihara, H. Murakami, and M. Kachi, 2016: Sea surface temperature
 from the new Japanese geostationary meteorological Himawari-8 satellite.
 Geophys. Res. Letters. DOI: 10.1002/2015GL067159.
 http://onlinelibrary.wiley.com/doi/10.1002/2015GL067159/full

# About Aerosol Algorithm:
(L2 Aerosol Algorithm)
 Yoshida, M, M. Kikuchi, T. M. Nagao, H. Murakami, T. Nomaki, and A.Higurashi 2018, 
 Common retrieval of aerosol properties for imaging satellite sensors, J. Meteor. Soc. 
 Japan, doi:10.2151/jmsj.2018-039.
 https://www.jstage.jst.go.jp/article/jmsj/advpub/0/advpub_2018-039/_article/-char/en. 

(L3 Hourly Aerosol Algorithm)
 Kikuchi, M., H. Murakami, K. Suzuki, T. M. Nagao, and A. Higurashi, 
 Improved Hourly Estimates of Aerosol Optical Thickness using Spatiotemporal 
 Variability Derived from Himawari-8 Geostationary Satellite, IEEE Transactions 
 on Geoscience and Remote Sensing, accepted. 

# About Short Wave Radiation / Photosynthetically Available Radiation Algorithm:
 R. Frouin and H. Murakami, 2007: Estimating photosynthetically available
 radiation at the ocean surface from ADEOS-II global imager data. J.
 Oceanography, 63,  493-503.

# About Chlorophyll-a Algorithm:
 Murakami, H. (2016): Ocean color estimation by Himawari-8/AHI, Proc. SPIE
 9878, Remote Sensing of the Oceans and Inland Waters: Techniques,
 Applications, and Challenges, 987810 (May 7, 2016); doi:10.1117/12.2225422;
 http://dx.doi.org/10.1117/12.2225422.

# About Cloud Retrieval Algorithm:
(Cloud Flag Algorithm)
  Ishida, H., and T. Y. Nakajima, 2009: Development of an unbiased cloud detection 
  algorithm for a spaceborne multispectral imager, J. Geophys. Res., 114, D07206, 
  doi:10.1029/2008JD010710. 

  Ishida, H., T. Y. Nakajima, T. Yokota, N. Kikuchi, and H. Watanabe, 2011: 
  Investigation of GOSAT TANSO-CAI cloud screening ability through an inter-satellite
  comparison, J. Appl. Meteor. Climatol., 50, 1571?1586. doi:
  http://dx.doi.org/10.1175/2011JAMC2672.1. 

  Letu, H., T. M. Nagao, T. Y. Nakajima, and Y. Matsumae, 2014: Method for validating
  cloud mask obtained from satellite measurements using ground-based sky camera.
  Applied optics, 53(31), 7523-7533.

  Nakajima, T. Y., T. Tsuchiya, H. Ishida, and H. Shimoda, 2011: Cloud detection
  performance of spaceborne visible-to-infrared multispectral imagers. 
  Applied Optics, 50, 2601-2616.

(Cloud Retrieval Algorithm)
  Kawamoto, K., T. Nakajima, and T. Y. Nakajima, 2001: A Global Determination of
  Cloud Microphysics with AVHRR Remote Sensing, J. Clim., 14(9), 2054-2068,
  doi:10.1175/1520-0442(2001)014<2054:AGDOCM>2.0.CO;2. 

  Nakajima, T. Y., and T. Nakajima, 1995: Wide-Area Determination of Cloud
  Microphysical Properties from NOAA AVHRR Measurements for FIRE and ASTEX Regions,
  J. Atmos. Sci., 52(23), 4043-4059, doi:10.1175/1520-0469(1995)052<4043:WADOCM>2.0.CO;2. 

(Scattering property database for nonspherical ice particles)
  Ishimoto, H., K. Masuda., Y. Mano, N. Orikasa, and A. Uchiyama, 2012a, Optical
  modeling of irregularly shaped ice particles in convective cirrus. In radiation
  processed in the atmosphere and ocean (IRS2012): Proceedings of the International
  Radiation Symposium (IRC/IAMAS) 1531, 184-187. 

  Ishimoto, H., K. Masuda, Y. Mano, N. Orikasa, and A. Uchiyama, 2012b: Irregularly
  shaped ice aggregates in optical modeling of convectively generated ice clouds,
  J. Quant. Spectrosc. Radiat. Transfer, 113, 632-643.

  Masuda, K., H. Ishimoto, and Y. Mano, 2012: Efficient method of computing a
  geometric optics integral for light scattering, Meteorology and Geophysics .,
  63, 15-19. 

  Letu, H., T. Y. Nakajima, and T. N. Matsui, 2012: Development of an ice crystal
  scattering database for the global change observation mission/second generation
  global imager satellite mission: Investigating the refractive index grid system
  and potential retrieval error. Appl. Opt., 51, 6172-6178. 

  Letu, H. H. Ishimoto, J. Riedi, T. Y. Nakajima, L. C.-Labonnote, A. J.  Baran,
  T. M. Nagao, and M. Sekiguchi, 2016: Investigation of ice particle habits to
  be used for ice cloud remote sensing for the GCOM-C satellite mission.
  Atmos.  Chem. Phys, 16(18), 12287-12303.

  Letu, H., T. M. Nagao, T. Y. Nakajima J. Riedi, H. Ishimoto, A. J. Baran, H.
  Shang, M. Sekiguchi, and M. Kikuchi: Ice cloud properties from Himawari-8/AHI
  next-generation geostationary satellite: Capability of the AHI to monitor the
  DC cloud generation process. IEEE Transactions on Geoscience and Remote
  Sensing, in revision.

# Radiative Transfer Code
  Nakajima, T., and M. Tanaka (1986), Matrix formulation for the transfer of
  solar radiation in a plane-parallel scattering atmosphere, J. Quant.
  Spectrosc. Radiat. Transfer, 35, 13?21, doi:10.1016/0022-4073(86)90088-9.

  Nakajima, T., and M. Tanaka (1988), Algorithms for radiative intensity
  calculations in moderately thick atmospheres using a truncation approximation,
  J. Quant. Spectrosc. Radiat. Transfer, 40, 51?69, doi:10.1016/0022-4073(88)90031-3.

  Ota, Y., A. Higurashi, T. Nakajima, and T. Yokota (2009), Matrix formulations
  of radiative transfer including the polarization effect in a coupled
  atmosphere-ocean system, J. Quant. Spectrosc. Radiat. Transfer, 111, 878?894,
  doi:10.1016/j.jqsrt.2009.11.021. 

********************************************************************************
