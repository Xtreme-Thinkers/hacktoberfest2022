from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def data_scraper(url, tag):
    res = []
    ua = UserAgent()
    headers = {'User-Agent':str(ua.random)}
    try:
        r = requests.get(url,headers=headers)
    except requests.exceptions.RequestException as e:
        return "\n Error: " + str(e)
    soup = BeautifulSoup(r.text,'html.parser')
    for data in soup.find_all(tag):
        res.append(data.text)
    return res

if __name__ == "__main__":
    url = input("[+] Enter/Paste The Url: ")
    tag = input("[+] Enter the tag you wanna scrape: ")
    scrapped_data = data_scraper(url, tag)
    if type(scrapped_data) is list:
        if len(scrapped_data) == 0:
            print("\n[-] Data not found with tag "+tag)
        else:
            print("\nScraped data: \n")
            for data in scrapped_data:
                print(data)
    elif scrapped_data:
        print(scrapped_data)

        
