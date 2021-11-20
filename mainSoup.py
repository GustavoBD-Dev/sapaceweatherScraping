# load the library
import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, time
from datetime import timedelta
import csv
from os import write

def Soup(URL):
    # download page 
    page = requests.get(URL)
    # souo the content 
    soup = BeautifulSoup(page.content, "html.parser")
    # Obtain the elements
    interplanetaryMagField = soup.find_all("span", class_="solarWindText")
    if len(interplanetaryMagField) != 0:
        # return the item that interests us is at the end of the list
        broken_html = str(interplanetaryMagField[-1])
        # parse HTML
        soup = BeautifulSoup(broken_html, 'html.parser')
        # this method will turn a Beautiful Soup parse tree into a nicely 
        # formatted Unicode string, with a separate line for each tag and each string
        fixed_html = soup.prettify()
        # return the elements in the fixed_html how a list of items 
        fixed_html = fixed_html.split()
        # the element that interests us is in position 14, 24 and 28 of the list
        Btotal = fixed_html[14]
        Bz = fixed_html[24]
        dirP = fixed_html[28]
        # return the string
        return [Btotal, Bz, dirP]
    else:
        return ['--', '--', '--']

def scrapSpaceweather():
    # current date 
    current_date = datetime.now()
    # open and write data in file
    with open('InterplanetariMagField.csv', 'w+', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['Date','Btotal', 'Bz', 'dirP'])
        # iterate the date, sub total days defined in variable i
        # get date with date while the date is older to date established by the year
        # set the value of sub date in 0
        i = 0
        while current_date.year >= 2017:
            # sub value of day in i to date current
            current_date = datetime.now() + timedelta(days = -i)
            # format to day and month for the values of a cipher 
            day = ('0' + str(current_date.day)) if current_date.day < 10 else str(current_date.day) 
            month = ('0' + str(current_date.month)) if current_date.month < 10 else str(current_date.month) 
            year = str(current_date.year)
            # concatenate the data of date and the URL
            URL = "https://spaceweather.com/archive.php?day=" + day + "&month=" + month +  "&year=" + year + "&view=view"
            # print(URL, end=' ')
            # get data with sraping web 
            data = Soup(URL)
            # write data in row file
            print([current_date.date(), data[0], data[1], data[2]])
            writer.writerow([current_date.date(), data[0], data[1], data[2]])
            # increment the value to i 
            i += 1


if __name__ == "__main__":
    scrapSpaceweather()

    
    

