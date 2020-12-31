import pandas as pd
from selenium import webdriver
import os
from googlesearch import search

path= 'C:/Users/User/Desktop/uni selection'

def data_input():
    df= pd.read_html('https://en.wikipedia.org/wiki/Universities_and_colleges_of_West_Bengal#List_of_universities')
    df= df[4]
    df.columns= df.iloc[0]
    df= df.iloc[1:]
    df= df.drop('Sources', axis= 1)
    df.to_csv(f'{path}/data/unis.csv')


def filter():
    df= pd.read_csv(f'{path}/data/unis.csv')
    subs= list(df['Specialization'])
    temp= [subs.index(i) for i in subs if 'Arts' or 'Science' in i]
    temp.sort()
    o= 100202
    indexes=[]
    for i in temp:
        if i!=o:
            indexes.append(i)
            o=i
    print(f'{temp}\n{indexes}')
    df= df.iloc[indexes]
    df= df.drop(['Type', 'Established'], axis= 1)
    df.to_csv(f'{path}/data/filtered_unis.csv', index= False)

def info():
    df= pd.read_html('https://www.google.com/search?q=bankura+university+pg+syllabus&oq=Bankura+University+pg+sy&aqs=chrome.0.0i457j69i57j0i22i30.4197j0j4&sourceid=chrome&ie=UTF-8')
    for i in range(len(df)):
        for col in df[i].columns:
            for j in df[i][col]:
                if 'economics' or'Economics' in j:
                    print(i, col, j)
    print(df)

def data_gathering():
    df= pd.read_csv(f'{path}/data/filtered_unis.csv')
    try:
        if os.path.isdir(f'{path}/scraped_data'):
            pass
        else:
            os.mkdir(f'{path}/scraped_data')
    except FileNotFoundError:
        os.mkdir(f'{path}/scraped_data')
    unis= df['University']
    for i in unis:
        os.mkdir(f'{path}/scraped_data/{i}')
        url_data=[]
        for url in search(f'{i} pg syllabus', stop=10):
            url_data.append(url)
        pd.Series(url_data).to_csv(f'{path}/scraped_data/{i}/urls.csv', index= False)


data_gathering()