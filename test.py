import requests
import bs4
import pandas as pd
 
 
url = 'https://clutch.co/directory/mobile-application-developers'
result = requests.get(url)
 
 
soup = bs4.BeautifulSoup(result.text,'lxml')

company = []
location =[]
review =[]
rating=[]
project_size=[]
employee=[]
avgHr=[]

for hit in soup.findAll(attrs={'data-link_text' : 'Profile Title'}):
  hit = hit.text.strip()
  company.append(hit)


for hit in soup.findAll(attrs={'data-link_text' : 'Reviews Count'}):
  hit = hit.text.strip()
  review.append(hit)


for hit in soup.findAll(attrs={'class' : "rating sg-rating__number"}):
  hit = hit.text.strip()
  rating.append(hit)


for hit in soup.findAll(attrs={'class' : "locality"}):
  hit = hit.text.strip()
  location.append(hit)


emp = soup.find_all("div",{"data-content":"<i>Employees</i>"})

for i in emp:
    span = i.find('span')
    employee.append(span.string)

hr = soup.find_all("div",{"data-content":"<i>Avg. hourly rate</i>"})

for i in hr:
    span = i.find('span')
    avgHr.append(span.string)

ps = soup.find_all("div",{"data-content":"<i>Min. project size</i>"})

for i in ps:
    span = i.find('span')
    project_size.append(span.string)

df = pd.DataFrame()
pd.set_option('display.max_colwidth', 30)


df['Company'] = company
df['Employee'] = employee
df['Location'] = location
df['Rating'] = rating
df['Avg Hour'] = avgHr
df['Review'] = review
df['Project Size'] = project_size


df.to_excel('result.xlsx', index = False)
 