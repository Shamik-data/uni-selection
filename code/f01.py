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
    df.to_csv(f'{path}/data/unis.csv', index=False)


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

def google_scraping():
    df= pd.read_csv(f'{path}/data/filtered_unis.csv')
    unis= df['University']
    try:
        if not os.path.isdir(f'{path}/scraped_data'):
            os.mkdir(f'{path}/scraped_data')
    except FileNotFoundError:
        os.mkdir(f'{path}/scraped_data')
    for i in unis:
        if not os.path.isdir(f'{path}/scraped_data/{i}'):
            os.mkdir(f'{path}/scraped_data/{i}')
        url_data=[]
        for url in search(f'{i} pg syllabus', stop=10):
            if '.in' in url:
                url_data.append(url)
        pd.DataFrame(url_data, columns= ['urls']).to_csv(f'{path}/scraped_data/{i}/urls.csv', index= False)

def data_gathering():
    df= pd.read_csv(f'{path}/data/filtered_unis.csv')
    unis= df['University']
    csv_paths=[]
    for i in unis:
        urls= pd.read_csv(f'{path}/scraped_data/{i}/urls.csv')['urls']
        for index in range(len(urls)):
            try:
                for df in pd.read_html(urls[index]):
                        df.columns= df.iloc[0]
                        df= df.iloc[1:]
                        df.to_csv(f'{path}/scraped_data/{i}/url{index}.csv', index= False)
                        csv_paths.append(f'{path}/scraped_data/{i}/url{index}.csv')
            except:
                pass
    check_str= ''
    checked= []
    for i in csv_paths:
        if i!=check_str:
            checked.append(i)
        check_str= i
    pd.DataFrame(checked, columns=['path']).to_csv(f'{path}/data/paths.csv', index= False)

def check():
    s= pd.read_csv(f'{path}/data/paths.csv')
    paths= []
    dict0= {}
    for i in s.path:
        df= pd.read_csv(i)
        for col in df.columns:
            if 'syllabus' in col:
                paths.append(i)
            elif 'Syllabus' in col:
                paths.append(i)
    for path0 in paths:
        df= pd.read_csv(path0)
        dict0[path0]= list(df.columns)
    subdict0= []
    subdict1= []
    subdict2= []
    lens= [len(dict0[i]) for i in dict0.keys()]
    for f in range(4):
        print(f'{f}: {lens.count(f)}')
    for key in dict0.keys():
        if len(dict0[key])==1:
            x=[key]
            x+= dict0[key]
            subdict0.append(x)
        elif len(dict0[key])==2:
            x=[key]
            x+= dict0[key]
            subdict1.append(x)
        elif len(dict0[key])==3:
            x=[key]
            x+= dict0[key]
            subdict2.append(x)
    print(subdict0)
    pd.DataFrame(subdict0, columns= ['path', 'col0']).to_csv(f'{path}/data/col1.csv', index=False)

    pd.DataFrame(subdict1, columns= ['path', 'col0', 'col1']).to_csv(f'{path}/data/col2.csv', index=False)
    pd.DataFrame(subdict2, columns= ['path', 'col0', 'col1', 'col2']).to_csv(f'{path}/data/col3.csv', index=False)
check()