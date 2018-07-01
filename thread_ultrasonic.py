import RPi.GPIO as GPIO
import time
import threading

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(16, GPIO.IN)


class Ultrasonic(threading.Thread):
    def __init__(self, name, trig, echo):
        threading.Thread.__init__(self)
        self.name = name
        self.trig_pin = trig
        self.echo_pin = echo


    def distance(self):
        GPIO.output(self.trig_pin, 1)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, 0)
        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()
        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance

    def run(self):
        distance = self.distance()
        print(str(self.name) + " Distance: " + str(distance) + " cm \n")


def main():
    class1 = Ultrasonic("App1", 5, 16)
    class1.start()


try:
    main()
    GPIO.cleanup()
    print("Done!")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Done!")

