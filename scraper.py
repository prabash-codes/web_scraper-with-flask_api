import requests
from  lxml import html
import sqlite3

conn = sqlite3.connect('database.sqlite3')

c = conn.cursor()

c.execute('''
            CREATE TABLE IF NOT EXISTS flaskapi_table(id INTEGER PRIMARY KEY AUTOINCREMENT, 
            quote TEXT, author TEXT)
            ''')

conn.commit()

def scrape(url):
    response = requests.get(url)
    r = html.fromstring(response.content)
    
    containers = r.xpath("//div[@class='quote']")

    for container in containers:
        quote = container.xpath(".//span[@class='text']/text()")
        if quote:
            quote = quote[0].replace("'", "''")
        else:
            quote = ''
        author = container.xpath(".//small[@class='author']/text()")
        if author:
            author = author[0].replace("'", "''")
        else:
            author = ''
        c.execute('''INSERT INTO flaskapi_table(quote, author) VALUES(?, ?)''', (quote, author))
        conn.commit()
        print(quote, author)
        print("scraped")

        next_page = r.xpath("//li[@class='next']/a/@href")

scrape("https://quotes.toscrape.com/")