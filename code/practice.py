#Challenge for data manipulation
#import libraries
import pandas as pd #for working with data
from pathlib import Path #working with file paths
import statistics #for basic statistical code eg.stdev

#import data
data_file_path = Path("..", "data", "wt_ihc_microglia23.csv")
microglia_data = pd.read_csv(data_file_path)

#explore data
print(microglia_data)

def analytics(x):
    return ("avg =  " + str(sum(x) / len(x))), "n = " + str(len(x)), "stdev = " + str(statistics.stdev(x))
