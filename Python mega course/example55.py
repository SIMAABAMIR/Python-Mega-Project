import datetime
import glob2
r""" This create an merger of existing 3 files
"""

filenames=glob2.glob("*.txt")
#creates timestamp filename upto miscrosec level
with open(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'.txt','w') as file:
    for files in filenames:
        with open(files,'r') as f:
            file.write(f.read()+'\n')
