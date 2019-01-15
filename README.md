# iReporter_Challenge
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.
[![Build Status](https://travis-ci.org/k7ko/iReporter_Challenge.svg?branch=api)](https://travis-ci.org/k7ko/iReporter_Challenge)
[![Coverage Status](https://coveralls.io/repos/github/k7ko/iReporter_Challenge/badge.svg?branch=patch-1)](https://coveralls.io/github/k7ko/iReporter_Challenge?branch=patch-1)
[![Maintainability](https://api.codeclimate.com/v1/badges/7e7520f2fd1984a9b2e5/maintainability)](https://codeclimate.com/github/k7ko/iReporter_Challenge/maintainability)

This API is currently hosted [here](https://kikoireporter.herokuapp.com/api/v1/red-flags "iReporter on Heroku")

## Features
This iReporter API end points that can be used to do the following;
1) POST /api/v1/red-flags - Create a red-flag record
2) GET /api/v1/red-flags - Get all red-flag records
3) GET /api/v1/red-flags/<red_flag_id> - Get a specific red-flag record
4) PATCH /api/v1/red-flags/<red_flag_id> - Edit a red-flag record
5) DELETE /api/v1/red-flags - Delete a red-flag record

## Requirements
* `Python3`
* `Flask`
* `Virtualenv` 
* `Git`
## Installation
Follow the following instructions to run the API;
* Install the above requirements
* Clone this [repository](https://github.com/k7ko/iReporter_Challenge.git "iReporter Repository") onto your computer
* Navigate to the root directory, create a virtual environment and activate it
```bash
$ cd iReporter_Challenge
$ virtualenv venv
$ venv/Scripts/activate
```
* Install the required dependencies;
```bash
$ pip install -r requirements.txt
```
* Run application
```bash
$ python main.py
```

## Authors
Patrick Kikomeko Kakembo - pkikomeko1@gmail.com

## License
No license is needed