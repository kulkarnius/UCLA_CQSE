import xml.etree.ElementTree as ET 

"""
Parsing the XML file into the Python script.
There seem to be more efficient ways to do this depending on our use case.
What I do here seemd to effectively be a bulk parse.
"""
element_tree = ET.parse('PsiOpDev.xml')
root = element_tree.getroot() #Defining root of the tree

"""Modifying the name of the first material to Dr. Chris Anderson"""
for child in root.iter("Material"):
    for child in child.findall("name"):
        if child.get('value') == 'A':
            child.set('value','Dr. Chris Anderson')


"""Modifying the bandshift value of all materials to Atharva"""
for child in root.iter("Material"):
    for child in child.findall("bandShift"):
        child.set('value','Atharva')


"""Writing to a file"""
element_tree.write('output.xml')




