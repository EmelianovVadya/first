import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led,GPIO.OUT)
ent = 6
state = 0
GPIO.setup(ent,GPIO.IN)
while True:
    a=GPIO.input(ent)
    GPIO.output(led, not(a))