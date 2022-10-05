import requests
from bs4 import BeautifulSoup
import csv

req = requests.get(
    url='https://www.jobbank.gc.ca/jobsearch/jobsearch?searchstring=database+&locationstring=' #Enter URL here
)
soup = BeautifulSoup(req.content, "html.parser") #Let BS parse 
soup.prettify()
mydivs = soup.find_all("article") #Find the article tag


header = ['business', 'date', 'location', 'salary', 'url']
content = []

for entry in mydivs: #Data clean up
        business = entry.find("li", {"class": "business"}).get_text()
        date = entry.find("li", {"class": "date"}).get_text().replace("\n", "")
        location = entry.find("li", {"class": "location"}).get_text().replace("Location","").replace("	", "").replace("\n", "")
        salary = entry.find("li", {"class": "salary"}).get_text().replace("	", "").replace("\n", "")
        url =  "https://www.jobbank.gc.ca" + entry.a['href']
        content.append([business, date, location, salary, url])

#Append to a CSV file.
with open('Jobs.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(content)):
        writer.writerow(content[i])

#Next step is upload