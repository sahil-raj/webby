from bs4 import BeautifulSoup
import requests
import json


class Webby:
    def __init__(self, u):
        self.url = u

    def getHtmlData(self):
        d = requests.get(self.url)
        return d.content
    
    def getTables(self, x):
        mySoup = BeautifulSoup(x, "html5lib")
        return mySoup.find_all("table")
            



if __name__ == "__main__":
    myObj = Webby("https://trends.builtwith.com/websitelist/Responsive-Tables")
    t = myObj.getHtmlData()
    print(myObj.getTables(t))
