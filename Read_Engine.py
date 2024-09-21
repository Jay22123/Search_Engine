import xml.etree.ElementTree as ET
import json
import os


class Reader():

    def ReadXML(self, filepath):
        for event, elem in ET.iterparse(filepath, events=['start']):
            if elem.tag == 'AbstractText':
                self._content = elem.text
            if elem.tag == 'Title':
                self._title = elem.text
        return [self._title, self._content, filepath]

    def ReadJASON(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
        if isinstance(data, dict):  # 如果是字典，使用 .items()
            for key, value in data.items():
                print(f"{key}: {value}")
        elif isinstance(data, list):  # 如果是列表，直接遍歷
            data = {str(index): item for index, item in enumerate(data)}
        else:
            print("Unknown data type")

         # 提取摘要的部分作為context

    def ReadDocument(self, datapath):
        if os.path.isfile(datapath):
            ext = os.path.splitext(datapath)[1]

            if ext == '.xml':
                datamessage = self.ReadXML(datapath)
            elif ext == '.json':
                self.ReadJASON(datapath)
            else:
                print("暫不支援的格式")
        return datamessage
