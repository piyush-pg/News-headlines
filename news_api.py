import requests

api_key = "dba134b2c0904e0f8c8f4213c8a386cd"


def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=dba134b2c0904e0f8c8f4213c8a386cd"
    news = requests.get(main_url).json()
    #print(news)
    article= news["articles"]
    #print(article)
    
    news_article=[]
    for arti in article:
        news_article.append(arti['title'])
        #print(news_article)
        
    for i in range(10):
        print(i+1,news_article[i])

news()
