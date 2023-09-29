from django.shortcuts import render
from django.http import HttpResponse
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pymongo import MongoClient
from django.http import JsonResponse
from django.views import View



driver = webdriver.Chrome()


url="https://www.magicbricks.com/property-for-sale/residential-real-estate?bedroom=2,3&proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&cityName=Mumbai"
driver.get(url)
print(driver.title)
time.sleep(10)
property_title = driver.find_elements(By.CLASS_NAME, 'mb-srp__card--title')
property_title_text = []

for element in property_title:
    property_title_text.append(element.text)
#print("property_title:", property_title_text)



property_area = driver.find_elements(By.CLASS_NAME, 'mb-srp__card__summary--value')
property_area_text = []

for element in property_area:
    property_area_text.append(element.text)
#print("property_area:", property_area_text)



property_price = driver.find_elements(By.CLASS_NAME, 'mb-srp__card__price--amount')  
property_price_text = []


for element in property_price:
    property_price_text.append(element.text)
#print("property_price:", property_price_text)



driver.quit()
merged_data_list = []
for i in range(len(property_title_text)):
    merged_data_list.append({
        "data_1": property_title_text[i],
        "data_2": property_area_text[i],
        "data_3": property_price_text[i]
    })

client = MongoClient('mongodb://localhost:27017/')
db = client['webscrapper']  # Replace with your actual database name
collection = db['magicbricks']

result = collection.insert_many(merged_data_list)
print("Inserted IDs:", result.inserted_ids)



