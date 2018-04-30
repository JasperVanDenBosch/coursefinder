# coursefinder
Recommend courses from the unistats dataset for a given industry.

The data are presumed to be at `~/data/unistats/`. 

In the directory where this code is:

1. create a python3 virtualenv: `virtualenv env -p python3`
2. activate virtualenv: `source env/bin/activate`
3. install requirements: `pip install -r requirements.txt`


Server:

nginx python3-pip supervisor

## Example
```
$ coursefinder 9121 --regions Argyllshire Lothian

Industry name: Legislative bodies


score: 0.17
name: Accounting and Business
provider: University of Edinburgh


score: 0.15
name: Law
provider: Edinburgh Napier University


score: 0.14
name: Linguistics
provider: University of Edinburgh


score: 0.13
name: Communication, Advertising and Public Relations
provider: Edinburgh Napier University


score: 0.13
name: English and Film
provider: Edinburgh Napier University
```
