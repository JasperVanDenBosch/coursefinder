import pandas
import pkg_resources
from os.path import join
datadir = pkg_resources.resource_filename('coursefinder', '../data')

levels = ['lvl0', 'lvl1', 'lvl2', 'lvl3']
# names for the hierarchy levels
industries = pandas.read_csv(join(datadir, 'industries.csv'))
# drop rows without SIC
industries.dropna(subset =['SIC'], inplace=True)
# drop rows without any label
industries.dropna(subset=levels, thresh=1, inplace=True)
# create a column with the hierarchy level 
level = industries[levels].stack().index.get_level_values(1)
industries['level'] = level.str[-1].astype(int)
industries.set_index('SIC', inplace=True)
industries['name'] = industries[levels].fillna('').sum(1)

def list_child_branches(industries, index, at_level):
    branches = []
    ngrantbranches = 0
    while index < industries.shape[0]:
        industry = industries.iloc[index]
        if industry.level == at_level:
            branch = {'text': industry['name']}
            children, n = list_child_branches(industries, index+1, at_level+1)
            if children:
                index += n
                branch['nodes'] = children
                branch['tags'] = [str(len(children))]
                ngrantbranches += n
            branches.append(branch)
            index += 1
        else:
            break
    return branches, len(branches) + ngrantbranches

def industries_as_tree():
    branches, _ = list_child_branches(industries, index=0, at_level=0)
    return branches
