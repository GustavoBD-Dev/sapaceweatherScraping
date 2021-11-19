# import the library
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import csv
from os import write

# function to scrap the URL
def Soup(URL):
    # download the page 
    page = requests.get(URL)
    # soup the content 
    soup = BeautifulSoup(page.content, "html.parser")
    # obtain the conditions 
    # the elements in span with name of class "solarWindText"
    current_conditions = soup.find(class_="solarWindText")
    # print the elements of list: contents[3] = speed, contents[7] = density
    print(current_conditions.contents[3].text, ' - ',current_conditions.contents[7].text)
    return current_conditions.contents

if __name__ == "__main__":
    # current date 
    new_date = datetime.now() 
    # set the value of sub the date in 0
    i = 0
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["DAY", "MONTH", "YEAR", "SPEED", "UNIT_MEASUREMENT_SPEED", "DENSITY", "UNIT_MEASUREMENT_DENSITY"])
        # iterate the date, sub one day for each cicle 
        # While the date is older to date (year) established
        while new_date.year != 2020:
            # sub value of day in i to date current
            new_date = datetime.now() + timedelta(days=-i)
            # format to day and month for the values of a cipher
            day = ('0' + str(new_date.day)) if new_date.day < 10 else str(new_date.day) 
            month = ('0' + str(new_date.month)) if new_date.month < 10 else str(new_date.month) 
            year = str(new_date.year)
            # concatenate the data of date and the URL
            URL = "https://spaceweather.com/archive.php?day=" + day + "&month=" + month +  "&year=" + year + "&view=view"
            # get data with sraping web 
            data = Soup(URL)
            # write data in row file
            writer.writerow([day, month, year, data[3].text, "km/sec", data[7].text, "protons/cm^3"])
            # increment the value to i 
            i += 1

