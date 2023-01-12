


class HostedByScraper:
    def __init__(self) -> None:

        title = 'host name scrap'

    def hostedByScrap(self, driver):
        try:
            hostedBy = driver.findElementsByXpath(
                'html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[3]/div/div[1]/div/div[1]/div/div/section/div/div/div/div[1]/div/h2')

            return hostedBy

        except Exception as e:
            print(f"An error occurred in the hostedByScrap", e)


################### function checking #############

# title = HostedByScraper()
# print(title.hostedByScrap())