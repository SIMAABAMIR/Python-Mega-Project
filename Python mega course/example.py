import datetime
r""" This create an empty file
"""

filename=datetime.datetime.now()
#create empty filename
def create_file():
    """"This function creates an empty file"""
    with open(filename.strftime('%Y-%m-%d') + '.txt', 'w') as file:
        file.write("") #writing empty string
create_file()
