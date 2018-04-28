Unistats structure: https://www.hesa.ac.uk/collection/c17061/unistats_dataset_file_structure


I've exported the Trees.xlsx file to one .csv file per sheet, 
and stored them in the data/ directory of this repository.

Industry: SIC 1987


Industry classification systems

- SIC 1987
- NAICS
- ISIC
- NACE
- UK SIC


Occupation classification systems

- SOC2010 (US) https://www.bls.gov/soc/2010/home.htm
- SOC2010 (UK)
- ISCO08 (international)

Industry-Occupation matrices

- 2011 census (ISIC Rev. 4, SOC2010)
- matrix (NAICS2012, US-SOC2010

Learning Providers:
- data from  http://learning-provider.data.ac.uk/


KISCOURSEID is not unique:

In [8]: courses.KISCOURSEID.unique().shape
Out[8]: (32417,)

also depends on KISMODE and sometimes simply short and other inst has it too
