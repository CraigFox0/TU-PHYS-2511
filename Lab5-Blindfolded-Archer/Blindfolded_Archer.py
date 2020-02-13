import random as rand
import math

#All measurements in meters and seconds

def shootArrow(gravity, drag, timeSize, heightOfShooter, initAngle, initMagnitude):
    time = 0
    xPosition = 0

    gravitationConstant = gravity
    dragCoefficient = drag
    timeStepSize = timeSize
    yPosition = heightOfShooter
    initialAngle = initAngle
    initialMagnitude = initMagnitude

    xVelocity = initialMagnitude * math.cos(math.radians(initialAngle))
    yVelocity = initialMagnitude * math.sin(math.radians(initialAngle))
    xAcceleration = 0
    yAcceleration = -gravitationConstant

    while yPosition > 0:
        xPosition = xPosition + (xVelocity * timeStepSize)
        yPosition = yPosition + (yVelocity * timeStepSize)
        xVelocity = xVelocity + (xAcceleration * timeStepSize)
        yVelocity = yVelocity + (yAcceleration * timeStepSize)
        xAcceleration = -dragCoefficient * xVelocity
        yAcceleration = -gravitationConstant + (-dragCoefficient * yVelocity)
        time = time + timeStepSize
    return xPosition

targetXPosition = rand.randint(1, 100) #can change params
print("Target is at " + str(targetXPosition) + " m")
targetAcceptanceRange = .5 #distance from center
lastDistanceFromTarget = []
shootingVelocity = 20
lastDistanceFromTarget.append(abs(shootArrow(9.81, 0, .00001, 1, 45, shootingVelocity) - float(targetXPosition)))
print("You shot with " + str() + " m/s initial speed and " + str() + " degrees initial angle and were " + str(round(lastDistanceFromTarget[-1], 1)) + " m from the target")
while lastDistanceFromTarget[-1] > targetAcceptanceRange:
    shootingVelocity = abs(shootingVelocity + (rand.randint(-1000, 1000)/1000)) #randomly guesses
    lastDistanceFromTarget.append(abs(shootArrow(9.81, 0, .00001, 1, 45, shootingVelocity) - float(targetXPosition)))
    print("You shot with " + str(shootingVelocity) + " m/s initial speed and " + str(45) + " degrees initial angle and were " + str(round(lastDistanceFromTarget[-1], 2)) + " m from the target")
print("Congratulations! You hit the target of " + str(targetXPosition) + " m with " + str(len(lastDistanceFromTarget)) + " tries")
