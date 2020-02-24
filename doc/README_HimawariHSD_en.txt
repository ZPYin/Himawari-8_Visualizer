********************************************************************************

README for the Himawari Standard Data (HSD) by JMA
 through the JAXA's P-Tree System

Prepared by Earth Observation Research Center (EORC),
            Space Technology Directorate I,
            Japan Aerospace Exploration Agency (JAXA).

Aug.31,2015: Himawari-8 Standard Data are released through the P-Tree system.
Aug.31,2016: Himawari L1 Gridded Data are released through the P-Tree system.

********************************************************************************

In this directory, the geostationary Himawari Standard Data (HSD) 
of the latest 30 days provided by the Japan Meteorological Agency (JMA) 
is available in near-real-time. 

********************************************************************************

# Available Himawari Standard Data

## Full-disk
 Observation area: Full-disk
 Temporal resolution: 10-minutes
 Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

## Japan Area
 Observation area: Japan area (Region 1 & 2)
 Temporal resolution: 2.5-minutes
 Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

## Target Area
 Observation area: Target area (Region 3)
 Temporal resolution: 2.5-minutes
 Spatial resolution: 0.5km (band 3), 1km (band 1,2,4), 2km (band 5-16)

## Color Image Data
 png images of Full-disk, Japan area and Target area, compositing three visible
 bands (blue: 0.47 micron; green: 0.51 micron; red: 0.64 micron).

********************************************************************************

# TOP FTP Directory

 /jma/

********************************************************************************

# Structure of FTP Directories

 /jma/hsd
       +---/[YYYYMM]
              +---/[DD]
                     +---/[hh]

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline; and
       hh: 2-digit hour of timeline.

********************************************************************************

# File Naming Convention

## Full-disk
 HS_H08_YYYYMMDD_hhmm_Bbb_FLDK_Rjj_Skkll.DAT

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;
       bb: 2-digit band number (varies from "01" to "16");
       jj: spatial resolution ("05": 0.5km, "10": 1.0km, "20": 2.0km);
       kk: segment number (varies from "01" to "10"); and
       ll: total number of segments (fixed to "10").

 example: HS_H08_20150728_2200_B01_FLDK_R10_S0110.DAT

## Japan Area
 HS_H08_YYYYMMDD_hhmm_Bbb_JPee_Rjj_S0101.DAT

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;
       bb: 2-digit band number (varies from "01" to "16");
       ee: observation number on the timeline (varies from "01" to "04"); and
       jj: spatial resolution ("05": 0.5km, "10": 1.0km, "20": 2.0km);

 example: HS_H08_20150728_2200_B01_JP01_R10_S0101.DAT

## Target Area
 HS_H08_YYYYMMDD_hhmm_Bbb_R3ee_Rjj_S0101.DAT

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;
       bb: 2-digit band number (varies from "01" to "16");
       ee: observation number on the timeline (varies from "01" to "04"); and
       jj: spatial resolution ("05": 0.5km, "10": 1.0km, "20": 2.0km);

 example: HS_H08_20150728_2200_B01_R301_R10_S0101.DAT

## Color Image Data
 PI_H08_YYYYMMDD_hhmm_TRC_FLDK_Rjj_PGPDF,png (Full-disk)
 PI_H08_YYYYMMDD_hhmm_TRC_JPee_Rjj_PLLJP.png (Japan Area)
 PI_H08_YYYYMMDD_hhmm_TRC_R3ee_Rjj_PLLTG.png (Target Area)

 where YYYY: 4-digit year of observation start time (timeline);
       MM: 2-digit month of timeline;
       DD: 2-digit day of timeline;
       hh: 2-digit hour of timeline;
       mm: 2-gidit minutes of timeline;
       ee: observation number on the timeline (varies from "01" to "04"); and
       jj: spatial resolution ("05": 0.5km, "10": 1.0km, "20": 2.0km);

 example: PI_H08_20150728_2200_TRC_FLDK_R10_PGPFD.png (Full-disk)
          PI_H08_20150728_2200_TRC_JP01_R10_PLLJP.png (Japan Area)
          PI_H08_20150728_2200_TRC_R301_R10_PLLTG.png (Target Area)

********************************************************************************

# Format

 All data is in Himawari Standard Data (HSD) format and compressed with bzip2, 
 except the Color Image Data which is archived in png format.

********************************************************************************

# Documents

## Himawari Standard Data User's Guide
 Detailed information can be found in the JMA's Himawari HSD User's Guide.
 Available from the JMA's web site;
 http://www.data.jma.go.jp/mscweb/en/himawari89/space_segment/hsd_sample/HS_D_users_guide_en_v12.pdf

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
