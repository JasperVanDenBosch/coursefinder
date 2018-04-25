import pandas

# names for the hierarchy levels
levels = ['lvl1', 'lvl2', 'lvl3']
industries = pandas.read_csv(
    'data/industries.csv',
    header=None,
    names=['SIC']+levels,
    converters={'SIC': lambda s: int(s) if s.isdigit() else None}
)
# drop rows without SIC
industries.dropna(subset =['SIC'], inplace=True)
# drop rows without any label
industries.dropna(subset=levels, thresh=1, inplace=True)
# create a column with the hierarchy level 
level = industries[['lvl1', 'lvl2', 'lvl3']].stack().index.get_level_values(1)
industries['level'] = level



