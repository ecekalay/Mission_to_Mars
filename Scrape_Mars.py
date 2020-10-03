from splinter import Browser
from bs4 import BeautifulSoup
import time

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "C:/Users/eceka/chromedriver_win32/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()


    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all elements that contain book information
    articles = soup.find_all('div', class_='list_text')    
    
    # Iterate through each book
    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
     
        title = article.find('a').text
        teaser = article.find('div', class_="article_teaser_body").text
               
        Mars_data = {
            'title': title,
            'teaser': teaser
        }


    # Close the browser after scraping
    browser.quit()

    # Return results
    return Mars_data
