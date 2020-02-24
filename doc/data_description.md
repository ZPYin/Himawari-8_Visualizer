# Data Description

## Level 2 (L2) Cloud Property (CLP)

|name|description|Unit|example|
|:--:|:----------|:--:|:-----:|
|latitude|latitude (-60° - 60°)|degree|40|
|longitude|longitude (80° - 200°)|degree|100|
|CLOT|Cloud Optical Thickness|none|1|
|CLER_23|Cloud Effective Radius using band 6|micron|5|
|CLTH|Cloud Top Height|km|10|
|CLTT|Clou Top Temperature|Kelvin|240|
|CLTYPE|Cloud Type under ISCCP Cloud Type Classification Definition: `0=Clear`, `1=Ci`, `2=Cs`, `3=Deep convection`, `4=Ac`, `5=As`, `6=Ns`, `7=Cu`, `8=Sc`, `9=St`, `10=Unknown`, `255=Fill`|none|1|
|Hour|Observation Hour (UT)|hours|0.027862|
|QA|There are 16 bits for each bin, the meaning of which is listed as below:<ul><li>(2,1,0) Cloud Retrieval Algorithm Flag: 000=Outside of Scan, 001=No Cloud Mask, 010=Clear, 011=Failed, 100=Successful: Low Confidence, 101=Successful: High Confidence, 110=TBD, 111=TBD;</li> <li>(4,3) Cloud Mask Confidence Level Flag: 00=Clear, 01=Probably Clear, 10=Probably Cloudy, 11=Cloudy;</li> <li>(6,5) Cloud Retrieval Phase Flag: 00=Clear, 01=Liquid Water, 10=Mixed or Uncertain, 11=Ice;</li> <li>(7) Spare: 0=TBD, 1=TBD;</li> <li>(8) Sunglint Flag: 0=Yes, 1=No;</li> <li>(9) Snow Ice Background Possibility Flag: 0=Yes, 1=No;</li> <li>(11,10) Land/Water Flag: 00=Water, 01=Coastal, 10=TBD, 11=Land;</li> <li>(12) SOZ>80 or SAZ>70: 0=Yes, 1=No;</li> <li>(13) Subpixel Inhomogeneity Flag: 0=Yes, 1=No;</li> <li>(14) Multilayer Cloud Flag: 0=Yes, 1=No;</li> <li>(15) Inversion Layer Flag: 0=Yes, 1=No</li></ul>|none|1|

## L2 Aerosol Property (ARP)

## Raw data