

import xml.etree.ElementTree as ET 


class xml_parser:
    def __init__(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def getTagList(self,parameterListName):
        parameterList = self.tree.find(parameterListName)
        if parameterList  == None:
            raise Exception("Not a valid parameterListName", parameterListName)
        parameters = [child.tag for child in parameterList]
        return parameterList.tag, parameters

    def getAttribsList(self,parameterListName):
        parameterList = self.tree.find(parameterListName)
        if parameterList  == None:
            raise Exception("Not a valid parameterListName", parameterListName)
        parameters = [child.attrib for child in parameterList]
        return parameterList.tag, parameters

    def getParameterValues(self, parameterName):
        children = [(child.tag, child.attrib) for child in self.root.iter(parameterName)]
        if self.root.iter(parameterName) == None:
            raise Exception("Not a valid parameterName", parameterName)
        return children
    
    def getChildValues(self, parameterList):
        childrenTags = [[(child.tag, child.attrib) for child in elem] for elem in self.root.iter(parameterList)]
        if self.root.iter(parameterList) == None:
            raise Exception("Not a valid parameterName", parameterList)
        return childrenTags
    
