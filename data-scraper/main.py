from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def data_scraper(url, tag):
    '''This function takes url and tag as parameters
    and returns the scrapped data with respective to the url 
    and later on we can probably play with the returned data'''
    pass


if __name__ == "__main__":
    url = input("Enter/Paste The Url")
    tag = input('Enter the tag you wanna scrape')
    scrapped_data = data_scraper(url, tag)
