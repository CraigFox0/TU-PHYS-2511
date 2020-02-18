import math
import matplotlib.pyplot as plt

#uses rectangular approximation with center point
def integrateLine(size):
    area = 0
    startPoint = -5 + (.5*size) #gets first rectangle x value
    while startPoint < 5:
        area = area + (size * ((-0.5 * startPoint) + 4.0))
        startPoint = startPoint + size
    return area

def integrateParabola(size):
    area = 0
    startPoint = -5 + (.5*size) #gets first rectangle x value
    while startPoint < 5:
        area = area + (size * (-0.29*(startPoint**2) - startPoint + 12.5))
        startPoint = startPoint + size
    return area

def integrateComplicatedFunction(size):
    area = 0
    startPoint = -5 + (.5*size) #gets first rectangle x value
    while startPoint < 5:
        area = area + (size * (1.0 + 10*(startPoint + 1.0)*math.exp(-(startPoint**2))))
        startPoint = startPoint + size
    return area

xValues = [.001, .002, .005, .01, .02, .05, .1, .2, .5, 1]
yLinePercentDifference = []
yParabolaPercentDifference = []
yComplicatedPercentDifference = []
for x in xValues:
    yLinePercentDifference.append(round(abs(100-(100*integrateLine(x)/40.0)), 4))
    yParabolaPercentDifference.append(round(abs(100-(100*integrateParabola(x)/100.83)), 4))
    yComplicatedPercentDifference.append(round(abs(100-(100*integrateComplicatedFunction(x)/27.72)), 4))
plt.figure()
plt.xlabel(r"$Delta X$")
plt.ylabel(r"$Percent Difference$")
plt.xlim(0, 1)
plt.plot(xValues, yLinePercentDifference)
plt.show()
plt.plot(xValues, yParabolaPercentDifference)
plt.show()
plt.plot(xValues, yComplicatedPercentDifference)
plt.show()
