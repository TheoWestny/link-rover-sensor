import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


class Ultrasonic:
    def __init__(self, echo,  *trig):
        self.trigger1 = trig[0]
        self.trigger2 = trig[1]
        self.echo = echo
        self.__next__()

    def __next__(self):
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.setup(self.trigger1, GPIO.OUT)
        GPIO.setup(self.trigger2, GPIO.OUT)
        GPIO.output(self.trigger1, 0)
        GPIO.output(self.trigger2, 0)

    def distance(self, channel):
        GPIO.output(channel, 1)
        time.sleep(0.00001)
        GPIO.output(channel, 0)
        while GPIO.input(self.echo) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance


def main():
    class1 = Ultrasonic(24, 23, 4)
    while True:
        print(class1.distance(23))
        time.sleep(2)
        print(class1.distance(4))
        time.sleep(2)


try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done!")
