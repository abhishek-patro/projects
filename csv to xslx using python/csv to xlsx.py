import pandas as pd
import os
import subprocess


path = os.getcwd()
os.chdir(path)
print(path)

# List all files in the directory
files = os.listdir()
print(files)

for file in files:
    if file.endswith('.csv'):
        xlsx_name = file[:-4]+'.xlsx'
        # print(file)
        # print(xlsx_name)
        try:
            df = pd.read_csv(file, encoding='utf-8')
        except UnicodeDecodeError:
            df = pd.read_csv(file, encoding='ISO-8859-1')
        df.to_excel(xlsx_name) 
        print("Successfully converted", file,"to",xlsx_name)
