import os
import fnmatch
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from netCDF4 import Dataset
from satpy import Scene, find_files_and_readers
from pyresample import create_area_def
from logger import logger
from colormap import chiljet_colormap
from helper import parseTime

plt.switch_backend('Agg')
PROJECTDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Visualizer(object):

    def __init__(self, file, *,
                 latRange=[20, 50], lonRange=[110, 130]):
        self.file = file
        self.latRange = latRange
        self.lonRange = lonRange
        try:
            self.fd = Dataset(file, 'r')
        except Exception as e:
            raise e

    def list_product(self):
        """
        list all the products in the file.
        """

        count = 1
        for variable in self.fd.variables.keys():
            logger.info('{0:2d}: {1:15s} {2}'.format(
                count,
                variable,
                getattr(self.fd.variables[variable], 'long_name')))
            count = count + 1

    def load_data(self, product, mTime):
        """
        load data to the workspace.
        """

        lat = self.fd['latitude'][:]
        lon = self.fd['longitude'][:]

        mask_lat = np.logical_and(lat >= self.latRange[0],
                                  lat <= self.latRange[1])
        mask_lon = np.logical_and(lon >= self.lonRange[0],
                                  lon <= self.lonRange[1])

        self.data = self.fd.variables[product][:, mask_lon][mask_lat]
        self.unit = getattr(self.fd.variables[product], 'units')
        self.long_name = getattr(self.fd.variables[product], 'long_name')

        self.lat = lat[mask_lat]
        self.lon = lon[mask_lon]

        self.mTime = mTime

    def colorplot_with_RGB(self, imgFile, *args,
                           axLatRange=[20, 60], axLonRange=[90, 140],
                           cmap=None, pixels=100, **kwargs):
        """
        load RGB data.

        TODO:
        Too time consuming in my local machine. (RAM > 10GB)
        Wait till I get a better PC!
        """

        pass

    def colorplot_with_band(self, band, HSD_Dir, imgFile, *args,
                            axLatRange=[20, 60], axLonRange=[90, 140],
                            cmap=None, pixels=100, **kwargs):
        """
        colorplot the variables together with radiance data.

        Parameters
        ----------
        band: int
            band number [1-16]. See band specification in
            `../doc/2018_A_Yamashita.md`
        HSD_Dir: str
            path for hosting the HSD files.
        imgFile: str
            filename of the exported image
        Keywords
        --------
        axLatRange: list
            latitude range of the plot (default: [20, 60]). [degree]
        axLonRange: list
            longitude range of the plot (default: [90, 140]). [degree]
        cmap: str
            colormap name.
        pixels: int
            resampled pixels of the band data (default: 100). Take care of
            time consumption when pixels > 1000!
        History
        -------
        2020-02-24 First version.
        """

        files = find_files_and_readers(
            start_time=(self.mTime - dt.timedelta(seconds=300)),
            end_time=(self.mTime + dt.timedelta(seconds=300)),
            base_dir=HSD_Dir,
            reader='ahi_hsd'
        )

        matched_files = []
        for file in files['ahi_hsd']:
            if fnmatch.fnmatch(os.path.basename(file),
               'HS_H08_*_B{0:02d}_FLDK_*_S0[1234]*DAT*'.format(band)):
                matched_files.append(file)

        h8_scene = Scene(filenames=matched_files,
                         reader='ahi_hsd', sensor='ahi')
        band_label = 'B{0:02d}'.format(band)
        h8_scene.load([band_label])

        roi = create_area_def('roi',
                              {'proj': 'eqc', 'ellps': 'WGS84'},
                              width=pixels, height=pixels,
                              area_extent=[axLonRange[0], axLatRange[0],
                                           axLonRange[1], axLatRange[1]],
                              units='degrees')
        roi_scene = h8_scene.resample(roi)

        # read China boundaries
        with open(os.path.join(PROJECTDIR,
                  'include', 'CN-border-La.dat'), 'r') as fd:
            context = fd.read()
            blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
            borders = [
                np.fromstring(block, dtype=float, sep=' ') for block in blocks]

        LON, LAT = np.meshgrid(self.lon, self.lat)
        fig = plt.figure(figsize=[8, 8])
        plt.tight_layout(False)

        # Set projection and plot the main figure
        ax1 = plt.axes([0.1, 0.1, 0.8, 0.8], projection=ccrs.PlateCarree())

        # Add ocean, land, rivers and lakes
        ax1.add_feature(cfeature.OCEAN.with_scale('50m'))
        ax1.add_feature(cfeature.LAND.with_scale('50m'))
        ax1.add_feature(cfeature.RIVERS.with_scale('50m'))
        ax1.add_feature(cfeature.LAKES.with_scale('50m'))

        # Plot border lines
        for line in borders:
            ax1.plot(line[0::2], line[1::2], '-', lw=1, color='k',
                     transform=ccrs.Geodetic())

        # loading colormap
        if cmap is None:
            cmap = chiljet_colormap()

        # Plot gridlines
        crs = roi.to_cartopy_crs()
        pcmesh_band = ax1.imshow(roi_scene[band_label],
                                 transform=crs, origin='upper',
                                 extent=crs.bounds, cmap='Greys')
        pcmesh = ax1.pcolormesh(
                                LON, LAT, self.data,
                                vmin=kwargs['vmin'],
                                vmax=kwargs['vmax'],
                                cmap=cmap,
                                transform=ccrs.PlateCarree())

        ax1.set_xticks(
            np.linspace(axLonRange[0], axLonRange[1], 5, endpoint=True))
        ax1.set_yticks(
            np.linspace(axLatRange[0], axLatRange[1], 5, endpoint=True))
        lon_formatter = LongitudeFormatter(number_format='.1f',
                                           degree_symbol='',
                                           dateline_direction_label=True)
        lat_formatter = LatitudeFormatter(number_format='.1f',
                                          degree_symbol='')
        ax1.xaxis.set_major_formatter(lon_formatter)
        ax1.yaxis.set_major_formatter(lat_formatter)
        ax1.set_ylim(axLatRange)
        ax1.set_xlim(axLonRange)

        ax1.set_title('{0} {1}'.format(
            self.mTime.strftime('%Y-%m-%d %H:%M (Himawari-8)'),
            self.long_name))

        if 'cb_ticks' not in kwargs.keys():
            kwargs['cb_ticks'] = np.linspace(
                kwargs['vmin'], kwargs['vmax'], 5, endpoint=True)

        cbar = fig.colorbar(
            pcmesh,
            fraction=0.03,
            ticks=kwargs['cb_ticks'],
            orientation='vertical'
            )
        cbar.ax.tick_params(direction='out', labelsize=15, pad=5)
        cbar.ax.set_title(self.unit, fontsize=10)

        if 'cb_ticklabels' in kwargs.keys():
            cbar.ax.set_yticklabels(kwargs['cb_ticklabels'])

        # Show figure
        # plt.show()
        plt.savefig(imgFile)
        plt.close()

    def colorplot(self, imgFile, *args,
                  axLatRange=[20, 60], axLonRange=[90, 140], cmap=None,
                  **kwargs):
        """
        colorplot the variables.

        Parameters
        ----------
        imgFile: str
            filename of the exported image
        Keywords
        --------
        axLatRange: list
            latitude range of the plot (default: [20, 60]). [degree]
        axLonRange: list
            longitude range of the plot (default: [90, 140]). [degree]
        cmap: str
            colormap name.
        History
        -------
        2020-02-24 First version.
        """

        # read China boundaries
        with open(os.path.join(PROJECTDIR,
                  'include', 'CN-border-La.dat'), 'r') as fd:
            context = fd.read()
            blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
            borders = [
                np.fromstring(block, dtype=float, sep=' ') for block in blocks]

        LON, LAT = np.meshgrid(self.lon, self.lat)
        fig = plt.figure(figsize=[8, 8])
        plt.tight_layout(False)

        # Set projection and plot the main figure
        ax1 = plt.axes([0.1, 0.1, 0.8, 0.8], projection=ccrs.PlateCarree())

        # Add ocean, land, rivers and lakes
        ax1.add_feature(cfeature.OCEAN.with_scale('50m'))
        ax1.add_feature(cfeature.LAND.with_scale('50m'))
        ax1.add_feature(cfeature.RIVERS.with_scale('50m'))
        ax1.add_feature(cfeature.LAKES.with_scale('50m'))

        # Plot border lines
        for line in borders:
            ax1.plot(line[0::2], line[1::2], '-', lw=1, color='k',
                     transform=ccrs.Geodetic())

        # loading colormap
        if cmap is None:
            cmap = chiljet_colormap()

        # Plot gridlines
        pcmesh = ax1.pcolormesh(
            LON, LAT, self.data,
            vmin=kwargs['vmin'],
            vmax=kwargs['vmax'],
            transform=ccrs.PlateCarree(),
            cmap=cmap)

        ax1.set_xticks(
            np.linspace(axLonRange[0], axLonRange[1], 5, endpoint=True))
        ax1.set_yticks(
            np.linspace(axLatRange[0], axLatRange[1], 5, endpoint=True))
        lon_formatter = LongitudeFormatter(number_format='.1f',
                                           degree_symbol='',
                                           dateline_direction_label=True)
        lat_formatter = LatitudeFormatter(number_format='.1f',
                                          degree_symbol='')
        ax1.xaxis.set_major_formatter(lon_formatter)
        ax1.yaxis.set_major_formatter(lat_formatter)
        ax1.set_ylim(axLatRange)
        ax1.set_xlim(axLonRange)

        ax1.set_title('{0} {1}'.format(
            self.mTime.strftime('%Y-%m-%d %H:%M (Himawari-8)'),
            self.long_name))

        if 'cb_ticks' not in kwargs.keys():
            kwargs['cb_ticks'] = np.linspace(
                kwargs['vmin'], kwargs['vmax'], 5, endpoint=True)

        cbar = fig.colorbar(
            pcmesh,
            fraction=0.03,
            ticks=kwargs['cb_ticks'],
            orientation='vertical'
            )
        cbar.ax.tick_params(direction='out', labelsize=15, pad=5)
        cbar.ax.set_title(self.unit, fontsize=10)

        if 'cb_ticklabels' in kwargs.keys():
            cbar.ax.set_yticklabels(kwargs['cb_ticklabels'])

        # Show figure
        # plt.show()
        plt.savefig(imgFile)
        plt.close()
