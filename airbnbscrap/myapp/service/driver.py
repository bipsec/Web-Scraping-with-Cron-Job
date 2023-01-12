import time
import urllib

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from myapp.service.proxyList import DynamicProxy
from selenium.webdriver.common.by import By


class Driver:

    def __init__(self):
        # self.driver = None
        # pr = DynamicProxy()
        # PROXY = pr.get_single_proxy()
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")
        # options.add_argument('--proxy-server=%s' % PROXY)

        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        title = 'Drive to scrap url'

    def getDriver(self, url=None):

        response =  self.driver.get(url)

        time.sleep(5)

        return response

    def quit(self):
        self.driver.close()

    def getTitle(self):
        return self.driver.title

    def getCurrentUrl(self):
        return self.driver.current_url

    def findElementsByXpath(self, xpath):
        try:
            items = self.driver.find_elements(By.XPATH, xpath)
            # houseXpath =   '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[7]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'
            getItems = []

            for item in items:
                getItems.append(item.text)

            return getItems

        except Exception as e:
            print(f"An error occurred in the findElementsByXpath", e)

    def findElementsByClassName(self, className):
        try:
            items = self.driver.find_elements(By.CLASS_NAME, className)
            # houseXpath =   '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[7]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'
            getItems = []

            for item in items:
                getItems.append(item.text)

            return getItems

        except Exception as e:
            print(f"An error occurred in the findElementsByClassName", e)

    def findElementsByID(self, ID):
        try:
            items = self.driver.find_elements(By.ID, ID)
            # houseXpath =   '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[7]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div'
            getItems = []

            for item in items:
                getItems.append(item.text)

            return getItems

        except Exception as e:
            print(f"An error occurred in the findElementsByID", e)

    def findElementsByIDForImages(self):
        try:
            # self.driver.find_elements(By.XPATH,
            #                          '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div[2]/button').click()
            # images = driver.find_elements(By.XPATH,
            #                     '/html/body/div[5]/div/div/div[1]/div/div[1]/div/div/div/div/div[1]/main/div/div[1]/div[1]/div[2]/div/div/div/div')
            # time.sleep(2)
            images = self.driver.find_elements(By.ID, 'FMP-target')
            # images = driver.find_elements(By.XPATH, '/html/body/div[10]/section/div/div/div[2]/div/div/div/div/section/div/div/div[2]/div/div[2]/section/div/div/div/div/section/div')
            #
            # print(images)

            getImages = []

            for img in images:
                getImages.append(img.get_attribute('src'))

            for i in range(len(getImages)):
                # urllib.request.urlretrieve(str(getImages[i]), f"images/image{i}.jpg")
                urllib.request.urlretrieve(str(getImages[i]), "image{}.jpg".format(i))
            return getImages

        except Exception as e:
            print("An error occured in the imageScrap: ", e)