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
    parents = []
    parentsInc = sweepFile.getParent("increment") #Checking for both increments
    parentsInt = sweepFile.getParent("intervals") #And intervals

    minsInc = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in parentsInc])
    maxsInc = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in parentsInc])
    inc = xm.chaining([sweepFile.getValues("{}//increment".format(parentName)) for parentName in parentsInc])

    minsInt = xm.chaining([sweepFile.getValues("{}//min".format(parentName)) for parentName in parentsInt])
    maxsInt = xm.chaining([sweepFile.getValues("{}//max".format(parentName)) for parentName in parentsInt])
    inter = xm.chaining([sweepFile.getValues("{}//intervals".format(parentName)) for parentName in parentsInt])

    parents.append(parentsInc)
    parents.append(parentsInt)

    parents = xm.chaining(parents)
    if sweepFile.doesItExist("link") == []:

        sweeps = []
        sweeps.append([[xm.truncate(minsInc[i] + n*inc[i]) for n in range(1 + int((maxsInc[i]-minsInc[i])/inc[i]))] for i in range(len(minsInc))])
        sweeps.append([[xm.truncate(minsInt[i] + n*((maxsInt[i]-minsInt[i])/inter[i])) for n in range(1 + int(inter[i]))] for i in range(len(minsInt))])

        combinations = xm.nestedLoops(xm.chaining(sweeps))

        for i in range(len(combinations)):
            for j in range(len(parents)):
                templateFile.setValue(parents[j],combinations[i][j])  #Need to add valid path checking to here at some point
            templateFile.writeToFile('{}/output{}{}.xml'.format(subDirectoryName, str(i),str(j)))
    else:

        lmins = sweepFile.getValues("link//min")
        lmaxs = sweepFile.getValues("link//max")
        lincres = sweepFile.getValues("link//increment")
        
        lsweeps = [[xm.truncate(lmins[i] + n*lincres[i]) for n in range(1 + int((lmaxs[i]-lmins[i])/lincres[i]))] for i in range(len(lmins))]
        lcombinations = [[i,j] for i,j in zip(lsweeps[0], lsweeps[1])] 

        uLinkedParams = xm.getTags(sweepFile.getChilds("parameterSweeps"))
        uLinkedParams.remove("link")

        mins = xm.chaining([sweepFile.getValues("{}//min".format(name)) for name in uLinkedParams])
        maxs = xm.chaining([sweepFile.getValues("{}//max".format(name)) for name in uLinkedParams])
        incres = xm.chaining([sweepFile.getValues("{}//increment".format(name)) for name in uLinkedParams])
        
        ulsweeps = [[xm.truncate(mins[i] + n*incres[i]) for n in range(1 + int((maxs[i]-mins[i])/incres[i]))] for i in range(len(mins))]
        ulcombinations = [list(i) for i in xm.nestedLoops(ulsweeps)]

        tuples = list(xm.nestedLoops([lcombinations, ulcombinations])) #Defines tuples

        combinations = [tuples[i][0] + tuples[i][1] for i in range(len(tuples))] #Brings all of the values together

"""
        for i in range(len(combinations)):
            for j in range(len(parents)):
                templateFile.setValue(parents[j],combinations[i][j])  #Need to add valid path checking to here at some point
            templateFile.writeToFile('{}/output{}{}.xml'.format(subDirectoryName, str(i),str(j)))
"""

print(sweepFile.getType("paramA"))
