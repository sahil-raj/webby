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
import pandas as pd

class Webby:
  def getTableData(self,url):
        r = requests.get(url)
        soup= BeautifulSoup(r.content,"html.parser")
        tableHead = soup.thead
        row_headers = []
        for rows in tableHead.find_all('tr'):
          for headers in rows.find_all('th'):
            row_headers.append(headers.text)
        print(row_headers)
        tableBody= soup.tbody
        table_body_values=[]
        for rows in tableBody.find_all('tr')[1:]:
          td_tags= rows.find_all('td')
          td_values =[headers.text  for headers in td_tags]
          table_body_values.append(td_values)
        print(table_body_values)
        df= pandas.DataFrame(table_body_values, columns=row_headers)
        df.head()


        

if __name__=="__main__":
  print_table_data=Webby()
  print_table_data.getTableData("https://trends.builtwith.com/websitelist/Responsive-Tables")

