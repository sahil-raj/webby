# from bs4 import BeautifulSoup
# import requests
# import json


# class Webby:
#     def __init__(self, u):
#         self.url = u

#     def getHtmlData(self):
#         return requests.get(self.url)
    
#     def getTable(self, x):
#         mySoup = BeautifulSoup(x.content, "html5lib")
#         # for table in mySoup.find_all("table"):
#         #     head = table.find_all('th')
#         #     for tr in 
#         for table in mySoup.find_all("table"):
#             jsonD = json.dumps(table)
#             print(jsonD)



# if __name__ == "__main__":
#     myObj = Webby("https://trends.builtwith.com/websitelist/Responsive-Tables")
#     t = myObj.getHtmlData()
#     myObj.getTable(t)

from bs4 import BeautifulSoup
import requests
import json

class Webby:
    def __init__(self, u):
        self.url = u
        self.tables = []
    
    def getHtmlData(self):
        return requests.get(self.url).text
    
    def getTablesFromHtml(self):
        mySoup = BeautifulSoup(self.getHtmlData(), "html5lib")
        # for t in mySoup.find_all("table"):
        #     self.tables.append(t)
        # print(mySoup.table.th)
        for t in mySoup.table:
            print(t)

if __name__ == "__main__":
    o = Webby("https://datatables.net/examples/basic_init/multiple_tables.html")
    o.getTablesFromHtml()
