

class HouseRulesScraper:
    def __init__(self) -> None:

        title = 'house rules includes check in-out time'

    def houseRulesScrap(self, driver):
        try:
            houseRules = driver.findElementsByXpath('/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[11]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div')

            return houseRules

        except Exception as e:
            print(f"An error occurred in the houseRulesScrap", e)

################### function checking #############

# title = HouseRulesScraper()
# print(title.houseRulesScrap())