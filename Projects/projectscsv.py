import csv
import datetime
import pandas as pd

def project_gen():
    column=['Date', 'Projects', 'Difficulty']
    with open('Projects.csv','a') as file:
        read = csv.writer(file)
        read.writerow(column)
if __name__ == '__main__':
    project_gen()
