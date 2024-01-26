from bs4 import BeautifulSoup
import requests
import json


class Webby:
    def __init__(self, u):
        self.url = u

    def getHtmlData(self):
        d = requests.get(self.url)
        return d.content
    
    def getTable(self, x):
        mySoup = BeautifulSoup(x, "html5lib")
        for table in mySoup.find_all("table"):
            head = table.find_all('th')
            print(head)



if __name__ == "__main__":
    myObj = Webby("https://trends.builtwith.com/websitelist/Responsive-Tables")
    t = myObj.getHtmlData()
    print(myObj.getTables(t))
