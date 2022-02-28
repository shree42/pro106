import numpy as np
import csv

def getDataSource(data_path):
    marks=[]
    dayspresent=[]

    with open(data_path)as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            marks.append(float(row['Marks In Percentage']))
            dayspresent.append(float(row['Days Present']))
    return{
        'x':marks,
        'y':dayspresent
    }

def correlation(datasource):
    findcoef=np.corrcoef(datasource['x'],datasource['y'])
    print(findcoef[0,1])
def setup():
    datapath='marks.csv'
    datasource=getDataSource(datapath)
    correlation(datasource)
setup()



