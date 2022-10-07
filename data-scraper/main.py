from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.error
import re


def data_scraper(url, tag):
    '''This function takes url and tag as parameters
    and returns the scrapped data with respective to the url 
    and later on we can probably play with the returned data'''
    url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
    
    # Checking url is in correct format or not
    if not(re.match(url_pattern, url)):
        print(f'ERROR: \"{url}\" URL SHOULD BE IN CORRECT FORMAT[EXAMPLE: https://google.com, https://stackoverflow.com/, ..]')
        return -1
    
    # Send Request To URL
    print('Sending Request........')
    try:
        req = urlopen(url)
    except urllib.error.URLError as e:
        print(f"ERROR: {e}")
        print(f"Failed to Send Request To Web Page \"{url}\", Check The URL That You Entered Is Correct.")
        return -1
    
    print(f'[+] Request Send Successfully')
    
    #Check Status code
    if req.code != 200:
        print(f"ERROR: Failed To Load Web Page -> {url}")
        return -1
    
    print(f'[+] Web Page Loaded Successfully')
    
    # get the data in string format
    charset = req.info().get_content_charset()
    content = req.read().decode(charset)
    
    soup = BeautifulSoup(content, 'html.parser')
    data = soup.find_all(tag)
    
    # Collecting the data of the tag
    uncleaned_data = []
    for i in data:
        data_uc = i.text.strip()
        uncleaned_data.append(data_uc)
    
    print(f'[+] Data Stored Successfully')
    
    # Removing all the unnecessary space, empty data
    tag_content = []
    
    print(f'[+] Cleaning The Stored data')
    
    for i in uncleaned_data:
        data_c = i.split('\n')
        cleaned_data = ''
        for j in data_c:
            temp_str = j.strip()
            if temp_str:
                cleaned_data += temp_str + " "
        if cleaned_data:
            tag_content.append(cleaned_data.strip())
    
    data_check = input('Do you want to print the data which is collected. Type "YES" otherwise "NO": ')
    data_check = data_check.upper()
    
    while(data_check != 'YES' and data_check != 'NO'):

        print(f'Input is not in correct format')
        data_check = input('Do you want to print the data which is collected. Type "YES" otherwise "NO": ')
        data_check = data_check.upper()

    # Print the data
    if data_check.upper() == 'YES':

        print()
        for i in range(len(tag_content)):
            print(f'{i+1}: {tag_content[i]}')
        print()

    print(f'[+] Execution Completed')
    return tag_content



if __name__ == "__main__":
    url = input("Enter/Paste The Url ")
    tag = input('Enter the tag you wanna scrape ')
    scrapped_data = data_scraper(url, tag)
