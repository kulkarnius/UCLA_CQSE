import xml.etree.ElementTree as ET
import os


tree = ET.parse('PsiOpDev.xml')
root = tree.getroot()


def biasSweep():
    mins = [float(elem.get('value')) for elem in root.findall(".//min")]
    maxs = [float(elem.get('value')) for elem in root.findall(".//max")]
    incre = [float(elem.get('value')) for elem in root.findall(".//increment")]
    
    currentPath = os.getcwd()
    os.mkdir(currentPath + '/sweepFiles')

    for n in range(1 + int((maxs[0]-mins[0])/incre[0])):
        topBias = mins[0] + n*incre[0]
        root.find('.//GateBias/topBias').set('value', str(topBias))
        for i in range(1 + int((maxs[1]-mins[1])/incre[1])):
            botBias = mins[1] + i*incre[1]
            root.find('.//GateBias/botBias').set('value', str(botBias))
            tree.write('sweepFiles/output{}{}.xml'.format(str(n),str(i)))
    
    return 

    

print(biasSweep())