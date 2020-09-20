import xml_class as xm

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
    mins = sweepFile.getValues("min")
    maxs = sweepFile.getValues("max")
    incres = sweepFile.getValues("increment")
    parents = sweepFile.getParent("min")
    
    if sweepFile.doesItExist("link") == []:

        sweeps = [[xm.truncate(mins[i] + n*incres[i]) for n in range(1 + int((maxs[i]-mins[i])/incres[i]))] for i in range(len(mins))]
    
        combinations = xm.nestedLoops(sweeps)
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

        tuples = list(xm.nestedLoops([lcombinations, ulcombinations]))

        combinations = [tuples[i][0] + tuples[i][1] for i in range(len(tuples))]

        for i in range(len(combinations)):
            for j in range(len(parents)):
                templateFile.setValue(parents[j],combinations[i][j])  #Need to add valid path checking to here at some point
            templateFile.writeToFile('{}/output{}{}.xml'.format(subDirectoryName, str(i),str(j)))


generateSweeps("cheeseman")

