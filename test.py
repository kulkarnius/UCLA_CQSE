import xml.etree.ElementTree as ET


tree = ET.parse('PsiOpDev.xml')
root = tree.getroot()


def getType():


print(getLayer("Layer5"))