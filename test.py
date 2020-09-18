import xml_class as xm

templateFile = xm.xml_parser("test.xml")
sweepFile = xm.xml_parser("testSweep.xml")

def generateSweepLists():
    mins = sweepFile.getValues("min")
    maxs = sweepFile.getValues("max")
    incres = sweepFile.getValues("increment")

    if len(mins) == 1:
        for n in range(1 + int((maxs[0]-mins[0])/incres[0])):
            topBias = mins[0] + n*incres[0]
            templateFile.setValue()