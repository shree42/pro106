import numpy as np
import csv

def getDataSource(data_path):
    coffeeinml=[]
    sleep=[]

    with open(data_path)as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            coffeeinml.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return{
        'x':coffeeinml,
        'y':sleep
    }

def correlation(datasource):
    findcoef=np.corrcoef(datasource['x'],datasource['y'])
    print(findcoef[0,1])
def setup():
    datapath='cofeedata.csv'
    datasource=getDataSource(datapath)
    correlation(datasource)
setup()