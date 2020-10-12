

import xml.etree.ElementTree as ET 
import os
import itertools as it
import math


def createSubDirectory(subDirectoryName):
    currentPath = os.getcwd()
    os.mkdir(currentPath + '/{}'.format(subDirectoryName))

def subDirectoryExistence(subDirectoryName):
    currentPath = os.getcwd()
    return os.path.isdir(currentPath + "/{}".format(subDirectoryName))

def truncate(number):
    factor = 10.0 ** 2
    return math.trunc(number * factor) / factor

def nestedLoops(array):
    return list(it.product(*array))

def getTags(elements):
        return [elem.tag for elem in elements]

def chaining(iterable):
    return list(it.chain.from_iterable(iterable))

def zip_longest(listA, listB):
    return it.zip_longest(listA, listB)



class xml_parser:
    def __init__(self, fileName):
        self.tree = ET.parse(fileName)
        self.root = self.tree.getroot()

    def getValues(self,valueName):
        return [float(elem.get("value")) for elem in self.root.findall(".//{}".format(valueName))]
    
    def getValueString(self,valueName):
        return [elem.get("value") for elem in self.root.findall(".//{}".format(valueName))]
    

    def setValue(self, targetValuePath, value):
        self.root.find('.//{}'.format(targetValuePath)).set('value', str(value))

    def getParent(self, valueName):
        return [elem.tag for elem in self.root.findall(".//{}/..".format(valueName))]

    def writeToFile(self, outputFilePath):
        self.tree.write(outputFilePath)
    
    def getRunParameters(self):
        return self.root.findall('.//runParameters/*')
    
    def doesItExist(self, parameterName):
        return self.root.findall(".//{}".format(parameterName))

    def getChilds(self, parameterName):
        return self.root.findall(".//{}/*".format(parameterName))
    
    def getType(self, parameterName):
        return self.root.find(".//runParameters/{}".format(parameterName)).get("type")


    
    

    




    

        
