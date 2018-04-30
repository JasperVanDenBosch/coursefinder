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

## Approach

The goal is to recommend courses that would be a good match for work in a given
industry. One way to do this is a text-search approach, where by we find courses
of which the title contains (part of) the name of the industry.
However, even when using synonyms, this can be tricky.
For example "Cicero style argument construction" won't have much to do with
the "Construction" industry.

Instead I used the unistats JOBLIST data, which contains common occupations
of former students of the course. By connecting this with 2011 Census data,
which contains a breakdown of professions by industry sector, we can estimate
how many people that took a given course end up in a given industry.

One challenge is that the industry coding used here is not the same as the
classification used in the other data sets. I used lookup tables to "crosswalk"
the code to the target system.

For more information on the classification systems see `notes.md`.


