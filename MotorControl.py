try:
    import RPi.GPIO as GPIO
    moduleLoaded = True
except:
    moduleLoaded = False

from PWM import PWM

class MotorControl:
    ACTIVE = 1
    INACTIVE = 0

    def __init__(self, pwmPin, forwardPin, backwardPin, activePin):
        self.pwm = PWM(pwmPin)
        self.direction = 0                  # 0 for forward 1 for backward
        self.forwardPin = forwardPin
        self.backwardPin = backwardPin
        self.activePin = activePin

    def stopMotor(self):
        if moduleLoaded:
            GPIO.output(self.activePin, MotorControl.INACTIVE)
        else:
            print("Stop Motor")

    def startMotor(self):
        if moduleLoaded:
            GPIO.output(self.activePin, MotorControl.ACTIVE)
        else:
            print("Start Motor")

    def getDirection(self):
        return self.direction
    
    def setDirection(self, direction):
        self.direction = direction
        if not moduleLoaded:
            print("Set Direction to " + str(self.direction))
            return
        if self.direction == 0:
            GPIO.output(self.backwardPin, MotorControl.INACTIVE)
            GPIO.output(self.forwardPin, MotorControl.ACTIVE)
        elif self.direction == 1:
            GPIO.output(self.forwardPin, MotorControl.INACTIVE)
            GPIO.output(self.backwardPin, MotorControl.ACTIVE)
        else:
            print("Unkown direction command")

    def setSpeed(self, speed):
        self.pwm.setDutycycle(speed * 100)

