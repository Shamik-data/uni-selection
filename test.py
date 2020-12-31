from googlesearch import search

for url in search('Bankura University', tld='in', stop=10):
    print(url)