

class DescriptionScraper:
    def __init__(self) -> None:

        title = 'Website Description Scrap'

    def descriptionScrap(self, driver):

        try:
            descriptions = driver.findElementsByXpath('/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[2]/div/div[2]')

            return descriptions

        except Exception as e:
            print("An error occurred in the descriptionScrap:", e)

################### function checking #############

# title = DescriptionScraper()
# print(title.descriptionScrap())