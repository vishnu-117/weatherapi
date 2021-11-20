import requests
from bs4 import BeautifulSoup
import csv

weather_data_list = []
def weatherdata():
    data = {}
    page = requests.get("https://www.bbc.com/weather/1275339")
    print(page)
    soup = BeautifulSoup(page.text, 'html.parser')

    weather=soup.find(class_="wr-day-carousel__scrollable")

    days=weather.find_all('li')
    print(len(days))

    # Open writer with name
    file_name = "weather.csv"
    # set newline to be '' so that that new rows are appended without skipping any
    f = csv.writer(open(file_name, 'w', newline=''))

    # write a new row as a header
    f.writerow(['Day', 'Description', 'Temperature'])

        
    for weather in days:

        day=weather.find(class_="wr-date").get_text()
        #print(day)
        description=weather.find(class_="wr-day__weather-type-description-container").get_text()
        #print(desc)
        temp=weather.find(class_="wr-day-temperature").get_text()
        #print(temp)


        print('day', day)
        print('desc', description)
        print('temp', temp)

        print('Writing rows')
        # add the information as a row into the csv table
        f.writerow([day, description, temp])
        data['day'] =  day
        data['description'] = description
        data['temperature'] = temp
        weather_data_list.append(data)

    return {'data':weather_data_list}
