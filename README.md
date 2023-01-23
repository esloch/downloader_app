# Satellite Weather Downloader

| Xarray | Copernicus |
|:-------------------------:|:-------------------------:|
|<img width="1604" alt="Xarray" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fxray.readthedocs.io%2Fen%2Fv0.9.0%2F_images%2Fdataset-diagram-logo.png&f=1&nofb=1&ipt=4f24c578ee40cd8ac0634231db6bd24d811fe59658eb2f5f67181f6d720d3f20&ipo=images"> |  <img width="1604" alt="Copernicus" src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.eea.europa.eu%2Fabout-us%2Fwho%2Fcopernicus-1%2Fcopernicus-logo%2Fimage&f=1&nofb=1&ipt=56337423b2d920fcf9b4e9dee584e497a5345fc73b20775730740f0ca215fb38&ipo=images">|

SWD is a system for downloading, transforming and analysing Copernicus weather data using Xarray. It consists in two major apps, `satellite_downloader` and `satellite_weather`. `downloader` is responsible for extracting NetCDF4 files from Copernicus API, and the `weather` implements Xarray extensions for transforming and visualizing the files.

## Installation
The app is available on PYPI, you can use the package without deploying the containers with the command in your shell:
``` bash
$ pip install satellite-weather-downloader
```

## Requirements
For downloading data from Copernicus API, it is required an account. The credentials for your account can be found in Copernicus' User Page, in the `API key` section. User UID and API Key will be needed in order to request data. Paste them when asked in `satellite_downloader` connection methods.


## Notes
Python Versions = [3.10, 3.11]
Version 1.X includes only methods for Brazil's data format and cities.

## Usage of `copebr` extensions
``` python
import satellite_downloader
import satellite_weather

file = satellite_downloader.download_br_netcdf('2023-01-01', '2023-01-07')
br_dataset = satellite_weather.load_dataset(file)
rio_dataset = br_dataset.copebr.ds_from_geocode(3304557) # Rio de Janeiro's geocode
rio_dataframe = rio_dataset.to_dataframe()
```

It is also possible to create a dataframe directly from the National-wide dataset:
```
br_dataset.copebr.to_dataframe(3304557)
```

All Xarray methods are extended when using the `copebr` extension:
```
rio_dataset.precip_med.to_array()
rio_dataset.temp_med.plot()
```
