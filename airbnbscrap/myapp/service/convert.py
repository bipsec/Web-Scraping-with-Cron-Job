import urllib
from urllib.parse import quote

class Converter:
    def __init__(self) -> None:
        title = "convert list to string"

    def convertListToString(self, s):
        str1 = ""

        for item in s:
            str1 += item

        return str1
    
    # def is_float(s):
    #     result = False
    #     if s.count(".") == 1:
    #         if s.replace(".", "").isdigit():
    #             result = True
    #     return result
    
    def convertPriceListToFloat(self, listitem):
        try:
            price =  ' '.join([str(elem) for elem in listitem])
            price = price.replace("$",'').replace(",",'')

            return float(price)
        except Exception as e:
            return 0
        
    def convertRatingListToFloat(self, item):
        try:
            price =  ' '.join([str(elem) for elem in item])
            price = price[:-1]

            return float(price)
        except Exception as e:
            return 0
        

    def urlConverter(self, string):

        url = ' '.join([str(elem) for elem in string])

        val = urllib.parse.quote(url)

        return val
