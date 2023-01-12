import os
import pandas as pd

from pathlib import Path

CSVDIR = Path("")
xmlDirectory = ""


class XmlDataFormat:
    def __init__(self):
        title = 'make data into xml format of urls'

    def xmlToCsvFileOfUrl(self, xmlDir=None):
        try:
            for filename in os.listdir(xmlDir):
                if filename.endswith(".xml"):
                    fullname = os.path.join(xmlDir, filename)
                    # print(fullname)
                    df = pd.read_xml(fullname)
                    # print(df)
                    # df = pd.read_xml(path)
                    urlData = df['loc']
                    dataframe = pd.Series(urlData, name="Link")
                    dataframe.to_frame()
                    dataframe.to_csv(f"{fullname}___.csv")

                    return "XML to List of CSV is created."

        except Exception as e:
            print(f"A {e} error occurred in the xmlToCsvFileOfUrl")


############### Cross chcecking the functions ##########
#
#
# test = XmlDataFormat()
# print(test.xmlToCsvFileOfUrl(xmlDirectory))
