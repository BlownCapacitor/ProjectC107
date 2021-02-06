import csv
import numpy as np
def getDataSource(data_path):
    StudentMarks = []
    DaysPresent = []
    with open(data_path)  as csv_file :
        csvReader = csv.DictReader(csv_file)
        for row in csvReader:
            
            StudentMarks.append(float(row ['Marks In Percentage']))
            DaysPresent.append(float(row ['Days Present']))
            
        return {'x' : StudentMarks, 'y': DaysPresent}
def findCorrelation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print(correlation[0,1])

def setup():
    data_path = '/Users/swatiahuja/Desktop/CODE/StandardDeviation/StudentMarks.csv'
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

setup()


        
    
