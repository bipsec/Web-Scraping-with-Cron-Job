

class RatingScraper:
    def __init__(self) -> None:
        
        title = 'rating scrap'

    def ratingScrap(self, driver):
        try:

            ratings = driver.findElementsByXpath(
                '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/span/span[2]')
            if len(ratings) == 0:
                ratings = driver.findElementsByClassName("_12si43g")

            return ratings

        except Exception as e:
            print(f"An error occurred in the ratingScrap", e)

################### function checking #############

# title = RatingScraper()
# print(title.ratingScrap())