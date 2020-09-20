import xml_class as xm

templateFile = xm.xml_parser("test.xml")
sweepFile = xm.xml_parser("testSweep.xml")

def generateSweeps(subDirectoryName):
    mins = sweepFile.getValues("min")
    maxs = sweepFile.getValues("max")
    incres = sweepFile.getValues("increment")
    parents = sweepFile.getParent("min")

    sweeps = [[xm.truncate(mins[i] + n*incres[i]) for n in range(1 + int((maxs[i]-mins[i])/incres[i]))] for i in range(len(mins))]
    
    combinations = xm.nestedLoops(sweeps)


    if xm.subDirectoryExistence(subDirectoryName) != True: #Checks to see if Directory exists
        xm.createSubDirectory("/{}".format(subDirectoryName))
    
    # Eventually want to build-in functionality that lets us directily overwrite the entire directory

    """
    Hierachy of Checks:
        Check for Links
        Check for Multiple Nested Loops
        Check for Single Nested Loops
    """

    if len(mins) == 1: #The case for single sweeps.
        for n in range(1 + int((maxs[0]-mins[0])/incres[0])):
            value = xm.truncate(mins[0] + n*incres[0])
            templateFile.setValue("paramA",value)
            templateFile.writeToFile('{}/output{}.xml'.format(subDirectoryName, str(n)))
    elif len(mins) > 1:
        for i in range(len(combinations)):
            for j in range(len(parents)):
                templateFile.setValue(parents[j],combinations[i][j])  #Need to add valid path checking to here at some point
                templateFile.writeToFile('{}/output{}{}.xml'.format(subDirectoryName, str(i),str(j)))


generateSweeps("cheese")

