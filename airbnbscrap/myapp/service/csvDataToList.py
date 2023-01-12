import pandas as pd

csvFilePath = ""


class CsvToList:
    def __init__(self):
        title = 'make a list of url'

    def csvToListOfUrl(self, csvFile=None):
        # making a list of the link from the csv dataset
        try:
            data = pd.read_csv(csvFile)

            urlList = []
            for url in data["Link"][2:]:
                urlList.append(url)

            return urlList

        except Exception as e:
            print(f"An error occurred in the csvToListOfUrl function.", e)

########### Cross Checking functions whether it works or not #################


# test = CsvToList()
# print(test.csvToListOfUrl(csvFilePath))
