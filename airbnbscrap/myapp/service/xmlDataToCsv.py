import os
import pandas as pd
import gzip

from lxml import etree

xmlDirectory = ""


class XmlToCsv:
    def __init__(self):
        pass

    def saveCsvOfUrl(self, xmlDir=None):

        for filename in os.listdir(xmlDir):
            try:
                if filename.endswith('.xml'):
                    fullname = os.path.join(xmlDir, filename)
                    result = pd.read_xml(fullname)
                    urlData = result["loc"]
                    dataframe = pd.Series(urlData, name="Link")
                    dataframe.to_frame()
                    dataframe.to_csv(f"{fullname}___.csv")

                    return dataframe

            except Exception as e:
                print(f"A {e} error reading the xml files.")

    def gzipedFileToCSV(self):
        with gzip.open('file.xml.gz', 'rb') as f:
            xml_bytes = f.read()

        xml = etree.fromstring(xml_bytes)
        items = xml.xpath('//item')

        df = pd.DataFrame(columns=['items'])

        for item in items:
            df = df.append({'items': item.text}, ignore_index=True)

            df.to_csv('file.csv', index=False)
        return df


############### Cross Checking function working or not ##########
test = XmlToCsv()
print(test.saveCsvOfUrl(xmlDirectory))
