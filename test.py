
import xml.etree.ElementTree as ET 

tree = ET.parse("PsiOpDev.xml")
root = tree.getroot()

def getParameterList(parameterListName):
    parameterList = tree.find(parameterListName)

    parameters = []

    for child in parameterList:
        parameters.append(child)

    return parameterList, parameters

getParameterList("Material List")