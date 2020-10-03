import pymongo
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/eceka/chromedriver_win32/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


def scrape_info():
    browser = init_browser()

    url = 'https://space-facts.com/mars/'
    browser.visit(url)

   
    tables = pd.read_html(url)

    type(tables)

    df = tables[2]
    df.columns = ['0','1']
    df.head()

    df = df.iloc[1:]
    df = df.set_index('0', inplace=True)

    data_dict = df.to_dict() 
    collection.insert_one(data_dict)

    Mars_data = db.collection.find()
    for m in Mars_data:
        print(Mars_data)

    # Close the browser after scraping
    browser.quit()
    return Mars_data



  


