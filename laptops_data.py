import requests
import pandas
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/search?q=dell+latitude+e6540+laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_17_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_17_na_na_na&as-pos=2&as-type=HISTORY&suggestionId=dell+latitude+e6540+laptop%7CLaptops&requestId=2e967a0e-61fe-436d-b09c-471567b9061f")

#print(response)

soup = BeautifulSoup(response.content,'html.parser')

#print(soup)

names=soup.find_all('div',class_='_4rR01T')
name=[]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)



prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices[0:10]:
    d=i.get_text()
    price.append(d)

#print(price)

ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings[0:10]:
    d=i.get_text()
    rate.append(float(d))

#print(rate)

reviews=soup.find_all('span',class_='_2_R_DZ')
review=[]
for i in reviews[0:10]:
    d=i.get_text()
    review.append(d)

#print(review)

features=soup.find_all('li',class_='rgWa7D')
feature=[]
for i in features[0:10]:
    d=i.get_text()
    feature.append(d)

#print(feature)


links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links[0:10]:
    d= "https://www.flipkart.com" + i['href']
    link.append(d)

#print(link)

images=soup.find_all('img',class_='_396cs4')
image=[]
for i in images[0:10]:
    d= i['src']
    image.append(d)

#print(image)


data = {'Names' : name,
        "Price" : price,
        "Ratings" : rate, 
        "Features":feature,
        "Reviews": review,
        "Images" : image,
        "Links": link
        }

df = pandas.DataFrame(data)

print(df)


df.to_csv("laptops_data.csv")
