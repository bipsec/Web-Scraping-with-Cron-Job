

class SafetyAndPropertyScraper:
    def __init__(self) -> None:

        title = 'safety and property scrap'

    def safetyAndPropertyScrap(self, driver):
        try:

            houseProperties = driver.findElementsByXpath(
                '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[9]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div')
            if len(houseProperties) == 0:
                houseProperties = driver.findElementsByXpath("/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div[1]/main/div/div[1]/div[11]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div")
            
            elif len(houseProperties) == 0:
                houseProperties = driver.findElementsByClassName("c1e17v3g dir dir-ltr")
            return houseProperties

        except Exception as e:
            print(f"An error occured in the safetyAndPropertyScrap", e)

################### function checking #############

# title = SafetyAndPropertyScraper()
# print(title.safetyAndPropertyScrap(chrome_driver))