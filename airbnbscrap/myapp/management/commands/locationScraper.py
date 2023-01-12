

class LocationScraper:
    def __init__(self) -> None:

        title = 'location scrap'

    def locationScrap(self, driver):
        try:
            locations = driver.findElementsByXpath("/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[8]/div/div/div/div[2]/div/section/div[2]")
            if len(locations) == 0:
                locations = driver.findElementsByXpath("/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[10]/div/div/div/div[2]/div/section/div[2]")
            elif len(locations) == 0:
                locations = driver.findElementsByXpath("/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[9]/div/div/div/div[2]/div/section/div[2]")
            return locations

        except Exception as e:
            print(f"An {e} error occured in the locationScrap")

################### function checking #############

# title = LocationScraper()
# print(title.locationScrap())