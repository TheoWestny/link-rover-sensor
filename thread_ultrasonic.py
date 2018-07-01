import RPi.GPIO as GPIO
import time
import threading
GPIO.setmode(GPIO.BCM)



class Ultrasonic(threading.Thread):
    def __init__(self, name, trig, echo):
        threading.Thread.__init__(self)
        self.name = name
        self.trig_pin = trig
        self.echo_pin = echo
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(16, GPIO.IN)


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
        while True:
            try:
                distance = self.distance()
                if distance > 1000:
                    pass
                else:
                    print(str(self.name) + " Distance: " + str(distance) + " cm \n")
                time.sleep(0.1)
            except KeyboardInterrupt:
                break



                       
def main():
    class1 = Ultrasonic("App1", 5, 16)
    class2 = Ultrasonic("App2", 6, 15)
    class1.start()
    class2.start()

try:
    main()
    print("Running!")
except KeyboardInterrupt:
    class1.terminate()
    class2.terminate()
    GPIO.cleanup()
    print("Done!")

