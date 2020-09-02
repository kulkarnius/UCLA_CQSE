

import xml.etree.ElementTree as ET 


class xml_parser:
    def __init__(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def getParameterList(self,parameterListName):
        parameterList = self.tree.find(parameterListName)

        parameters = []

        for child in parameterList:
            parameters.append(child)

        return parameterList, parameters
    
