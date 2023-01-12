


class AmenititesScraper:
    def __init__(self) -> None:

        title = 'amenities scrap'

    def amenitiesScrap(self, driver):
        try:
            amenities = driver.findElementsByXpath(
                '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[6]/div/div')
            # print(amenities)
            # if len(amenities) == 0:
            #  amenities = driver.findElementsByXpath(
            #     '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[5]/div/div[2]')
            return amenities

        except Exception as e:
            print("An error occured in the amenitiesScrap: ", e)

################### function checking #############

# title = AmenititesScraper()
# print(title.amenitiesScrap())