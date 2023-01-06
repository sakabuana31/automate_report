import pandas as pd
import glob
import os

def append_all_files(filename) :
    data = pd.read_csv(filename)

    print(data)
    return data

if __name__ == '__main__' :
    append_all_files('/mnt/f/DigitalSkola/2.Project_1/automate_report/data/sales_product_data/Sales_April_2019.csv')