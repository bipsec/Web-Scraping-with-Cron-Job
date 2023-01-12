


class ReviewScraper:
    def __init__(self) -> None:

        title = 'review scrap'

    def reviewScrap(self, driver):
        try:
            reviews = driver.findElementsByXpath('/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/span/button/span')

            return reviews

        except Exception as e:
            print(f"An {e} error occured in the reviewScrap")



################### function checking #############

# title = ReviewScraper()
# print(title.reviewScrap())