try:
    import RPi.GPIO as GPIO
    moduleLoaded = True
except:
    moduleLoaded = False

class PWM:

    def __init__(self, pin, dutycycle = 0) -> None:
        self.pin = pin	
        self.dutycycle = dutycycle	
        if moduleLoaded:
            GPIO.setwarnings(False)			        #disable warnings
            GPIO.setmode(GPIO.BOARD)		        #set pin numbering system
            GPIO.setup(self.pin,GPIO.OUT)
            self.pwm = GPIO.PWM(self.pin,1000)		#create PWM instance with frequency
            self.pwm.start(0)
            self.dutycycle = dutycycle
        else:
            print("Init PWM on Pin " + str(pin) + "\n")
            print("Set Dutycle to " + str(dutycycle))
        		             

    def stopPWM(self):
        if moduleLoaded:
            self.pwm.stop()
        else:
            print("Stopped PWM")

    def startPWM(self):
        if moduleLoaded:
            self.pwm.start(self.dutycycle)
        else: 
            print("Stopped PWM")

    def setDutycycle(self, dutycycle):
        self.dutycycle = dutycycle
        if moduleLoaded:
            self.pwm.ChangeDutyCycle(self.dutycycle)
        else:
            print("Changed Dutycle to " + str(self.dutycycle))
    