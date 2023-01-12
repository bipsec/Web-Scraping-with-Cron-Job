from myapp.service.convert import Converter

convert = Converter()


class PriceTagScraper:
    def __init__(self) -> None:
        
        title = 'price tag scrap'

    def priceTagScrap(self, driver):
        try:
            prices = driver.findElementsByXpath(
                '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div/span/div/span[1]')
            return prices

        except Exception as e:
            print(f"An error occurred in the priceTagScrap", e)

    # def priceTagFormat(self, prices):
    #     try:
    #         price = convert.convertListToFloat(prices)
    #         return price
    #     except ValueError as e:
    #         pass


################### function checking #############

# title = PriceTagScraper()
# print(title.priceTagScrap())