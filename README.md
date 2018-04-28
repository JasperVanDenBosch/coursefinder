# coursefinder
Recommend courses from the unistats dataset for a given industry.

The data are presumed to be at `~/data/coursefinder/`. 

In the directory where this code is:

1. create a python3 virtualenv: `virtualenv env -p python3`
2. activate virtualenv: `source env/bin/activate`
3. install requirements: `pip install -r requirements.txt`


Server:

nginx python3-pip supervisor

## Example
```
$ coursefinder 9411
Industry name: Admin. of educational programs


score: 0.27
name: Accounting
provider: University of the Highlands and Islands


score: 0.24
name: Accounting and Finance
provider: University of Central Lancashire


score: 0.23
name: Business and Human Resource Management
provider: University of Huddersfield
```
