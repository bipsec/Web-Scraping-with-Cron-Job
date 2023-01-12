import csv
import threading
import time
import pandas as pd
from myapp.service.driver import Driver
from myapp.models import AirbnbData
from myapp.seralizers import AirbnbSeralizer
from myapp.service.csvDataToList import CsvToList

from myapp.management.commands.amenitiesScraper import AmenititesScraper
from myapp.management.commands.currentUrlScraper import CurrentURLScraper
from myapp.management.commands.descriptionScraper import DescriptionScraper
from myapp.management.commands.hostedByScraper import HostedByScraper
from myapp.management.commands.houseRulesScraper import HouseRulesScraper
from myapp.management.commands.imageScraper import ImageScraper
from myapp.management.commands.locationScraper import LocationScraper
from myapp.management.commands.priceScraper import PriceTagScraper
from myapp.management.commands.ratingScraper import RatingScraper
from myapp.management.commands.reviewScraper import ReviewScraper
from myapp.management.commands.safetyAndPropertyScraper import SafetyAndPropertyScraper
from myapp.management.commands.titleScraper import TitleScraper

from myapp.service.convert import Converter

# create object of different class of Scraper

title = TitleScraper()
urls = CurrentURLScraper()
price = PriceTagScraper()
review = ReviewScraper()
rating = RatingScraper()
amenities = AmenititesScraper()
descriptions = DescriptionScraper()
hostname = HostedByScraper()
houseRules = HouseRulesScraper()
location = LocationScraper()
safetyAndProperty = SafetyAndPropertyScraper()
images = ImageScraper()
convert = Converter()

# File Path

csvFilePath = "myapp/management/App Data/CSVDIR/sitemap-airbnb_luxe-urls-1.xml___.csv"


csvData = CsvToList()
lock = threading.Lock()


urlList = csvData.csvToListOfUrl(csvFilePath)


class Scraper:

    def __init__(self):
        self.driver = Driver()
        

    def saveScrapData(self):
        ################### saving data to csv files  ##########################

        

        for url in urlList:
            
            self.driver.getDriver(url)

            
            # import class name of scraping functions
            Categories = title.titleScrap(self.driver)
            Price = price.priceTagScrap(self.driver)
            Reviews = review.reviewScrap(self.driver)
            Rating = rating.ratingScrap(self.driver)
            Description = descriptions.descriptionScrap(self.driver)
            URL = urls.currentURLScrap(self.driver)
            Amenities = amenities.amenitiesScrap(self.driver)
            Location = location.locationScrap(self.driver)
            SafetyProperty = safetyAndProperty.safetyAndPropertyScrap(self.driver)
            Image = images.imageScrap(self.driver)

        

            # field names
            fields = {
                'Categories': Categories,
                'Price': convert.convertPriceListToFloat(Price),
                'Reviews': convert.convertListToString(Reviews),

                'Rating': convert.convertRatingListToFloat(Rating),

                'Description': convert.convertListToString(Description),
                'URL': URL,
                'Amenities': convert.convertListToString(Amenities),
                'Location': convert.convertListToString(Location),
                'SafetyProperty': convert.convertListToString(SafetyProperty),
                'Image': convert.urlConverter(Image),
                

            }

            with lock:
                with open('airbnb.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([fields])
            

            serializer = AirbnbSeralizer(data=fields)
            existing_data = AirbnbData.objects.filter(pk=None)
            # print(type(fields))
            old_data = existing_data.__dict__
            # print(type(old_data))
            print("Data Valid:" , serializer.is_valid())
            print("Adding to database")
            # breakpoint()
            if serializer.is_valid():
                
                serializer.save()
            else:
                serializer = AirbnbSeralizer(old_data, data=fields)
                if serializer.is_valid():
                    
                    serializer.save()

        self.driver.quit()
         

################# Checking whether functions works or not ###############

# scrapItems = ScrapingFunctions()
# print(scrapItems.CategoriesScraper())
# print(scrapItems.currentUrlScraper())
# print(scrapItems.reviewScraper())
# print(scrapItems.priceTageScraper())
# print(scrapItems.ratingScraper())
# print(scrapItems.hostedByScraper())
# print(scrapItems.amenitiesScraper())
# print(scrapItems.descriptionScraper())
# print(scrapItems.locationScraper())
# print(scrapItems.houseRulesScraper())
# print(scrapItems.safetyAndPropertyScraper())
# print(scrapItems.imageScraper())




# title = CurrentURLScraper()
# print(title.currentURLScrap(driver))