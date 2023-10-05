from bs4 import BeautifulSoup
import requests

URL = "https://www.glassdoor.com/Job/united-states-software-engineer-jobs-SRCH_IL.0,13_IN1_KO14,31.htm" 
 
payload = { 
	"password": "Tklol123@#!", 
	"username": "khantamjid314@gmail.com" 
}

s = requests.session() 
response = requests.get("https://www.glassdoor.com/Job/united-states-software-engineer-jobs-SRCH_IL.0,13_IN1_KO14,31.htm")
print(response.status_code) # If the request went Ok we usually get a 200 status. 

from bs4 import BeautifulSoup 
soup = BeautifulSoup(response.content, "html.parser") 
print("Title: " + str(soup.title.string))

with open("Glassdoor.html", "w", encoding="UTF-8") as file:
    file.write(soup.prettify())