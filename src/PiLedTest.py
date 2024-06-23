import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins
LED_PIN = 24
SWITCH_PIN = 22

def init():
    GPIO.setmode(GPIO.BCM)  # choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT)  # set LED_PIN as output
    GPIO.setup(SWITCH_PIN, GPIO.IN)  # set SWITCH_PIN as input

def read_slide_switch():
    return GPIO.input(SWITCH_PIN)

def blink_led():
    while True:
        if read_slide_switch() == GPIO.HIGH:
            for _ in range(25):  
                GPIO.output(LED_PIN, GPIO.HIGH)  
                sleep(0.1)  
                GPIO.output(LED_PIN, GPIO.LOW)  
                sleep(0.1)  
        else:
            for _ in range(100):  
                GPIO.output(LED_PIN, GPIO.HIGH)  
                sleep(0.05)  
                GPIO.output(LED_PIN, GPIO.LOW)  
                sleep(0.05)  

def main():
    init()  
    blink_led()  


main()