

class ImageScraper:
    def __init__(self) -> None:

        title = 'image scarp'

    def imageScrap(self, driver):
        images = driver.findElementsByIDForImages()
        return images

################### function checking #############

# title = ImageScraper()
# print(title.imageScrap(driver=chrome_driver))