def biasSweep(self):
        mins = [float(elem.get('value')) for elem in self.root.findall(".//min")]
        maxs = [float(elem.get('value')) for elem in self.root.findall(".//max")]
        incre = [float(elem.get('value')) for elem in self.root.findall(".//increment")]
        
        currentPath = os.getcwd()
        os.mkdir(currentPath + '/sweepFiles')

        for n in range(1 + int((maxs[0]-mins[0])/incre[0])):
            topBias = mins[0] + n*incre[0]
            self.root.find('.//GateBias/topBias').set('value', str(topBias))
            for i in range(1 + int((maxs[1]-mins[1])/incre[1])):
                botBias = mins[1] + i*incre[1]
                self.root.find('.//GateBias/botBias').set('value', str(botBias))
                self.tree.write('sweepFiles/output{}{}.xml'.format(str(n),str(i)))
        
        return 

    def getMaterial(self, materialName):
        for i in range(len(self.root[2].findall("Material"))):
            if self.root[2][i][0].attrib == {'value':materialName}:
                childrenTags = [(child.tag, child.attrib) for child in self.root[2][i].iter()]
                return childrenTags

    def getLayer(self, layerName):
        for i in range(len(self.root[3].findall("Layer"))):
            if self.root[3][i+1][0].attrib == {'value':layerName}:
                childrenTags = [(child.tag, child.attrib) for child in self.root[3][i+1].iter()]
                return childrenTags
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
    
    if len(mins) == 1: #The case for single sweeps.
        for n in range(1 + int((maxs[0]-mins[0])/incres[0])):
            value = xm.truncate(mins[0] + n*incres[0])
            templateFile.setValue("paramA",value)
            templateFile.writeToFile('{}/output{}.xml'.format(subDirectoryName, str(n)))
    elif len(mins) > 1: