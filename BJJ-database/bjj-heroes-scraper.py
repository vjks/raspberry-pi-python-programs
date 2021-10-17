from selenium import webdriver # selenium had to be installed first using pip.exe install selenium
from bs4 import BeautifulSoup # BeautifulSoup4 had to installed first using pip.exe install beautifulsoup4
import pandas as pd # pandas had to be installed first using pandas.exe install pandas
from webdriver_manager.chrome import ChromeDriverManager

import requests # because using selenium for multiple pages on the website is too slow.

#driver = webdriver.Chrome(ChromeDriverManager().install()) #Chrome driver manager had to be installed. Giving it the location of Chrome.exe wasn't working

def get_player_page_contents( profileSubDirectory, playersWithStats, countLinks ):
    count = 0;
    for link in profileSubDirectory:
        if count > countLinks:
            break

        playerPageURL = "https://www.bjjheroes.com" + link
        print( "The full URL is: ", playerPageURL )
        myGetRequest = requests.get( playerPageURL )
        playerSoup = BeautifulSoup(myGetRequest.content, features="html.parser" )
        for tbody in playerSoup.findAll( 'tbody' ):
            playersWithStats += 1
            for tr in tbody.findAll( 'tr' ):
                winLoss = tr.findAll( 'td' )[2].text
                method = tr.findAll( 'td' )[3].text

                #print( winLoss, method )
                if winLoss == 'W':
                    if method.startswith( "Pts:"):
                        method = "Points"
                    if method not in winMethods:
                        winMethods[ method ] = 1
                    else:
                        winMethods[ method ] += 1
        count += 1
    return playersWithStats


url = 'https://www.bjjheroes.com/a-z-bjj-fighters-list'
myGetRequest = requests.get( url )


#print( myGetRequest.content )
#ChromeDriverManager().install()
#driver = webdriver.Chrome(C:/Program Files/Google/Chrome/Application/chrome.exe)

playerProfileLinks = []
countLinks = 0
playersWithStats = 0
winMethods = dict()

#driver.get("https://www.bjjheroes.com/a-z-bjj-fighters-list")

#content = driver.page_source
soup = BeautifulSoup(myGetRequest.content, features="html.parser" )

for td in soup.findAll( 'td', attrs={'class': 'column-1'}):
    #firstName.append( td.find( 'a' ) )
    playerProfileLinks.append( td.find( 'a' ).get('href') )
    countLinks += 1

print( playerProfileLinks )
print( "Total number of player links are ", countLinks )
print( "Total number of players with stats are: ", get_player_page_contents( playerProfileLinks, playersWithStats, countLinks ) )
print( winMethods )

lst = list()
for key, val in list( winMethods.items() ):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:]:
    print(val, key)
