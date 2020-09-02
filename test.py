
import xml.etree.ElementTree as ET 

tree = ET.parse("PsiOpDev.xml")
root = tree.getroot()

def getParameterList(parameterListName):
    parameterList = tree.find(parameterListName)

    if tree.find(parameterListName) == None:
        raise Exception("Don't be dumb")

    parameters = []

    for child in parameterList:
        parameters.append(child.tag)

    return parameterList, parameters

print(getParameterList("MaterialList"))