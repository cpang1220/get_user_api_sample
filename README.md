# User List API

This API has the following functions:

- **Returns users who are listed as living in a city**

- **Returns users whose current coordinates are within 50 miles of a city**

## Requirements
The application requires:
1. Python version 3.7
2. Flask version 1.1.2


## Usage
API path which returns users who are listed as living in a city (HTTP GET method)
```
/users/live/city
```
API path which returns users whose current coordinates are within 50 miles of a city (HTTP GET method)
```
/users/current/vicinity
```

## Functions
Spatial functions are applied in the application using external libraries including GeoPandas, Shapely, GDAL.

The script can be found in the path: app/search_users.py
[get_user_data_by_vicinity](https://github.com/cpang1220/user_api/blob/master/app/search_users.py)

The GeoPandas framework applied the following spatial functions in this API application.
1. Execute a buffer polygon for a city buffer area(50 miles)
2. Execute an overlay(intersect) function between the user locations and a city buffer area to extract users located in the buffer area

Longitude and Latitude values of users are projected to projected coordinate system(WGS 84 Web Mercator) in the GeoDataFrame using GeoPandas to execute spatial analysis.

## Issue
JIRA issue: [UA-1](https://cp1220.atlassian.net/browse/UA-1)

The application requires GDAL package to be installed. There is an technical issue related to pip install GDAL.

Run the following commands the install the required packages.
```
sudo apt-get install libspatialindex-dev
pip install -r requirements.txt
sudo apt-get update && sudo apt-get install -y \
gdal-bin python-gdal python3-gdal
```

## API Documentation
The API reference can be found in the swagger.yml file [swagger.yml](https://github.com/cpang1220/user_api/blob/master/swagger.yml)

## Run application
Run application with commands using Flask
```
set FLASK_APP=run.py
flask run
```

## Test
In terminal, run the following command to execute unit test cases without coverage.
```
python manage.py test
```

In terminal, run the following command to execute test with coverage.
```
nosetests --with-coverage --cover-package=app
```

## Automation tools
1. The application includes a Procfile file for users to upload the API application to Heroku. [Procfile](https://github.com/cpang1220/user_api/blob/master/Procfile)
2. Circle CI has integrated in the application for automation build and test. The Circle CI settings are included in the config.yml file. [config.yml](https://github.com/cpang1220/user_api/blob/master/.circleci/config.yml)
3. JIRA has integrated with github to track issues. [JIRA Issue](https://cp1220.atlassian.net/browse/UA-1)
