import RPi.GPIO as GPIO
import time

def right():
    p.ChangeDutyCycle(9)
    time.sleep(1)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    
def left():
    p.ChangeDutyCycle(6)
    time.sleep(1)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)
    

servoPIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(7.5) # Initialization

    
while True:
    x = input()
    print(x)
    if x == 'r':
        print('Right Turn')
        right()
    elif x == 'l':
        print('Left Turn')
        left()
    elif x == 'e':
        p.stop()
        GPIO.cleanup()
        break