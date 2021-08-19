# Simple HTML Parser, coded by Emre Demirbag https://github.com/emre-demirbag
# New York Times Mini Crossword Puzzle,by Joel Fagliano,(https://www.nytimes.com/crosswords/game/mini)
#requests:(http://docs.python-requests.org/en/master/),
#soup:(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


# Import the required modules
import requests
from bs4 import BeautifulSoup as Soup

#Checking Connection
def check(url):
	chkUrl=requests.get(url)
	if chkUrl.status_code == 200:
		print("HTTP 200 OK: Connection established")
	else:
		print("Oops! Something went wrong")

	return None

#Checking Connection

def check(url):
	chkUrl=requests.get(url)
	if chkUrl.status_code == 200:
		print("HTTP 200 OK: Connection established")
	else:
		print("Oops! Something went wrong")

	return None


session = requests.Session()



def getHTML(url):

# session.get(url) returns a response that is saved
# in a response object called resp.

    resp = session.get(url)

# BeautifulSoup will create a
# parsed tree in soup.

    soup = Soup(resp.content, "lxml")

    return soup



def getColoumns(soup):
    # soup.find_all finds the div's, all having the same
    # class "ClueList-wrapper--3m-kd" that is
    # stored NyTimes Mini Crosswords web site
    # https://www.nytimes.com/crosswords/game

    cluewrap = soup.find_all("div", {"class": "ClueList-wrapper--3m-kd"})
    # Initialise the required variables
    html = ""


# Iterate cluewrap and clutext check for the html tags
# to get the information of each clues.

    for i in cluewrap:

        clueListTitle = i.findAll("h3")

        title = i.find('h3', attrs={'class': 'ClueList-title--1-3oW'})

        html += "=== " + clueListTitle[0].text + " ===" + "\n"

        cluetext = i.findAll("li")

        for j in cluetext:
            span = j.findAll("span")
            title[0] = title.text.strip()
            html += " " + span[0].text.strip() + " " + span[1].text.strip() + "\n"

    print(html)

    return html

# Main Function
if __name__ == "__main__":
    url = "https://www.nytimes.com/crosswords/game/mini"
    # Enter the url of website
    check(url)
    s = getHTML(url)
    # Function will return a list of clues
    html = getColoumns(s)


    # export a list of clues to text file
    file_r = open("text.txt", "w")
    file_r.write(html)
    file_r.close()
    print("Created text file")

