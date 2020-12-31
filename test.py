import os
import pandas as pd
path= 'C:/Users/User/Desktop/uni selection'
df= pd.read_html('https://www.google.com/search?q=bankura+university+pg+syllabus&oq=Bankura+University+pg+sy&aqs=chrome.0.0i457j69i57j0i22i30.4197j0j4&sourceid=chrome&ie=UTF-8')
os.mkdir(f'{path}/data/random_folder')
for i in range(len(df)):
    df[i].to_csv(f'{path}/data/random_folder/i.csv', index= False)