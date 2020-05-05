import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
    'https://forecast.weather.gov/MapClick.php?lat=40.71455000000003&lon=-74.00713999999994#.XqCWSMgzY2w')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast-body')



items = week.find_all(class_='tombstone-container')

print(items[1].find(class_='period-name').get_text())
period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
weather_stuff = pd.DataFrame({
    'Period':period_names,
    'Description':short_description,
    'Temperatures':temperatures})
weather_stuff.set_index('Period', inplace=True)
print(weather_stuff)
# weather_stuff.to_csv('weekly_weather_report.csv')
