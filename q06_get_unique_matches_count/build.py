# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

from pprint import pprint
def get_unique_matches_count():
    ipl_matches_array=read_ipl_data_csv(path,'|S50')


    all1=ipl_matches_array[:,0]

    newlst=[]
    for ids in all1:
        if ids not in newlst:
            newlst.append(ids)


    cnt=0
    for item in newlst:
        cnt=cnt+1
    return cnt


# Enter Code Here
