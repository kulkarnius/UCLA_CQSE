import xml_class as xm

#Eventually need to using argparse here to make it work
templateFile = xm.xml_parser("test.xml")
sweepFile = xm.xml_parser("testSweep.xml")

def generateSweeps(subDirectoryName):

    if xm.subDirectoryExistence(subDirectoryName) != True: #Checks to see if Directory exists
        xm.createSubDirectory("/{}".format(subDirectoryName))

    
    # Eventually want to build-in functionality that lets us directily overwrite the entire directory

    """
    Hierachy of Checks:
        Check for Links
        Check for Multiple Nested Loops
        Check for Single Nested Loops
    """
    if sweepFile.doesItExist("link") == []:
        parents = []
        parentsInc = sweepFile.getParent("increment") #Checking for both increments
        parentsInt = sweepFile.getParent("intervals") #And intervals
        parentsBool = sweepFile.getParent("boolSweep") #And boolean values

        minsInc = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in parentsInc])
        maxsInc = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in parentsInc])
        inc = xm.chaining([sweepFile.getValues("{}//increment".format(parentName)) for parentName in parentsInc])

        minsInt = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in parentsInt])
        maxsInt = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in parentsInt])
        inter = xm.chaining([sweepFile.getValues("{}//intervals".format(parentName)) for parentName in parentsInt])

        parents.append(parentsInc)
        parents.append(parentsInt)
        parents.append(parentsBool)

        parents = xm.chaining(parents)

        sweeps = []
        sweeps.append([[xm.truncate(minsInc[i] + n*inc[i]) for n in range(1 + int((maxsInc[i]-minsInc[i])/inc[i]))] for i in range(len(minsInc))])
        sweeps.append([[xm.truncate(minsInt[i] + n*((maxsInt[i]-minsInt[i])/inter[i])) for n in range(1 + int(inter[i]))] for i in range(len(minsInt))])

        if len(parentsBool) != 0:
            sweeps.append([['true','false']])

        combinations = xm.nestedLoops(xm.chaining(sweeps))


        for i in range(len(combinations)):
            for j in range(len(parents)):
                templateFile.setValue(parents[j],combinations[i][j])  #Need to add valid path checking to here at some point
            templateFile.writeToFile('{}/output{}{}.xml'.format(subDirectoryName, str(i),str(j)))
    else:
        parents = []
        lparentsInc = sweepFile.getParent("link//increment") #Checking for both increments
        lparentsInt = sweepFile.getParent("link//intervals") #And intervals
        lparentsBool = sweepFile.getParent("link//boolSweep") #And boolean values

        lminsInc = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in lparentsInc])
        lmaxsInc = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in lparentsInc])
        linc = xm.chaining([sweepFile.getValues("{}//increment".format(parentName)) for parentName in lparentsInc])

        lminsInt = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in lparentsInt])
        lmaxsInt = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in lparentsInt])
        linter = xm.chaining([sweepFile.getValues("{}//intervals".format(parentName)) for parentName in lparentsInt])

        parents.append(lparentsInc)
        parents.append(lparentsInt)
        parents.append(lparentsBool)

        uLinkedParams = xm.getTags(sweepFile.getChilds("parameterSweeps"))
        uLinkedParams.remove("link")

        parentsInc = []
        parentsInt = []
        parentsBool = []
        
        for parent in uLinkedParams:
            if sweepFile.doesItExist("{}/increment".format(parent)) != []:
                parentsInc.append(parent)
            elif sweepFile.doesItExist("{}/intervals".format(parent)) != []:
                parentsInt.append(parent)
            elif sweepFile.doesItExist("{}/boolSweep".format(parent)) != []:
                parentsBool.append(parent)


        minsInc = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in parentsInc])
        maxsInc = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in parentsInc])
        inc = xm.chaining([sweepFile.getValues("{}//increment".format(parentName)) for parentName in parentsInc])

        minsInt = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in parentsInt])
        maxsInt = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in parentsInt])
        inter = xm.chaining([sweepFile.getValues("{}//intervals".format(parentName)) for parentName in parentsInt])

        
        parents.append(parentsInc)
        parents.append(parentsInt)
        parents.append(parentsBool)

        parents = xm.chaining(parents)

        lsweeps = []
        lsweeps.append([[xm.truncate(lminsInc[i] + n*linc[i]) for n in range(1 + int((lmaxsInc[i]-lminsInc[i])/linc[i]))] for i in range(len(lminsInc))])
        lsweeps.append([[xm.truncate(lminsInt[i] + n*((lmaxsInt[i]-lminsInt[i])/linter[i])) for n in range(1 + int(linter[i]))] for i in range(len(lminsInt))])

        if len(lparentsBool) != 0:
            lsweeps.append([['true','false']])

        sweeps = []
        sweeps.append([[xm.truncate(minsInc[i] + n*inc[i]) for n in range(1 + int((maxsInc[i]-minsInc[i])/inc[i]))] for i in range(len(minsInc))])
        sweeps.append([[xm.truncate(minsInt[i] + n*((maxsInt[i]-minsInt[i])/inter[i])) for n in range(1 + int(inter[i]))] for i in range(len(minsInt))])

        if len(parentsBool) != 0:
            sweeps.append([['true','false']])

        ulcombinations = xm.nestedLoops(xm.chaining(sweeps))
        
        lsweeps = xm.chaining(lsweeps)
        lcombinations = [(i,j) for i,j in zip(lsweeps[0], lsweeps[1])]


        tuples = list(xm.nestedLoops([lcombinations, ulcombinations])) #Defines tuples

        combinations = [tuples[i][0] + tuples[i][1] for i in range(len(tuples))] #Brings all of the values together


        for i in range(len(combinations)):
            for j in range(len(parents)):
                templateFile.setValue(parents[j],combinations[i][j])  #Need to add valid path checking to here at some point
            templateFile.writeToFile('{}/output{}{}.xml'.format(subDirectoryName, str(i),str(j)))

generateSweeps("what")