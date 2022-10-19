## Let's proceed to collect or scrap the data.

![alt text](docs/../img/datacollection.jpg)

**Scraping data can be easily understood as grabbing or extracting some information from websites or application that are useful for Data Scientist or Machine Learning Engineers to analyze the problem statement. **

> No more talking in air now, let's code  <>

```python
# Importing Essential libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
```
- **[pandas](https://pandas.pydata.org/docs/user_guide/index.html)** - This library is useful for reading, transforming and analyzing the tabular data like csv ,xlsx etc.
- **[requests](https://requests.readthedocs.io/en/latest/)** - This library is used for fetching the HTML content using link which is passed to it.
- **[bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)** - Popularly known as beautiful soup used to extract the data by filtering some tags present in HTML.

```python
# Create some lists
name_of_movie = []
ranking = []
year_of_release = []
ratings = []
```

> Here we've created some list, which is used to store the extracted data in a csv format.

```python
try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    soup = bs(source.text,'html.parser')
    movies = soup.find('tbody',class_='lister-list').find_all('tr')
    for movie in movies:
        name_of_movie.append(movie.find('td',class_='titleColumn').a.text)
        ranking.append(movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0])
        year_of_release.append(movie.find('td',class_='titleColumn').span.text.strip('()'))
        ratings.append(movie.find('td',class_='ratingColumn imdbRating').strong.text)    
except Exception as e:
    print(e)
```

**Now let's understand functions used in each line of code**

* requests.get - Used to fetch the content which we can get through by going to it (HTML content). Just go to this [url](https://www.imdb.com/chart/top/), right click and inspect, therefore the html code which you've seen it is stored in **source** variable.
* raise_for_status - It is just for confirmation, that code is extracted or not. If not, it'll raise an error.
* bs - It takes two arguments (and many optional), one is content (.text is returning the content) and another is which type of content **bs** function need to parse or analyze, that is html parser. There are many parser available, you can check [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser).
  
> To understand the working of beautiful soup, you would've a brief understanding of HTML tags.

* soup.find - As we know, HTML is full of tags, now assume we need to find the title of picture,rating of picture and its ranking, so we need to find the parent tag inside which name, ranking and rating is plugged. In our case, inside **tbody** tag having class name **lister-list**, we have our all content. To get movies, every **tr** tag inside tbody tag has movies (and its all info). Purpose of these function is to return(in **movies** variable) the content of that tag specified having specified class name.
* In next line, we'll iterating more inside movies, to get each movies title, rating and ranking.

>             [**tbody(lister-list) -> tr -> td(titleColumns) -> a**] -> movie names
>             [**tbody(lister-list) -> tr -> td(titleColumns)] -> ranking (using split)
>             [**tbody(lister-list) -> tr -> td(ratingColumn imdbRating) -> strong**] -> ranking

> We've stored the movie title,ranking,year,ratings is variable **name_of_movie**, **ranking**, **year_of_release**, **ratings** respectively.

```python
data = pd.DataFrame({'Rank':ranking,'Movie':name_of_movie,'YearOfRelease':year_of_release,'Ratings':ratings})
data.head(10)
```

- Simply append the lists that we've created in a Dataframe.

**Output(1st 10 tuples)** - 

|Rank|	Movie|	YearOfRelease|	Ratings|
|----|-------|---------------|---------|
|1|	The Shawshank Redemption|	1994|	9.2|
|2|	The Godfather|	1972|	9.2|
|3|	The Dark Knight|	2008|	9.0|
|4|	The Godfather Part II|	1974|	9.0|
|5|	12 Angry Men|	1957|	8.9|
|6|	Schindler's List|	1993|	8.9|
|7|	The Lord of the Rings: The Return of the King|	2003|	8.9|
|8|	Pulp Fiction|	1994|	8.9|
|9|	The Lord of the Rings: The Fellowship of the Ring|	2001|	8.8|
|10|	Il buono, il brutto, il cattivo|	1966|	8.8|

> You can apply this type of procedure with little variation in any web scraping task.

**View on [Github](https://github.com/Hg03/Classification)**



