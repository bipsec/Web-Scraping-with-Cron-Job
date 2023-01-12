class TitleScraper:
    def __init__(self) -> None:
        
        title = 'website title scrap'

    def titleScrap(self, driver):
    # try
        return driver.getTitle()

    # except Exception as e:
    #
    #     print("An error occurred in the titleScrap: ", e)

################### function checking #############

# title = TitleScraper()
# print(title.titleScrap())