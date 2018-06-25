class Ultrasonic:
    def __init__(self, appId, *inp):
        self.name = appId
        self.channels = inp
        self.__next__()

    def __next__(self):
        try:
            if len(self.channels) % 2 == 0:
                j = 1
                for i in range(0, len(self.channels)):
                    if i%2 == 0:
                        setattr(self, "trigger" + str(j), self.channels[i])
                    else:
                        setattr(self, "echo" + str(j), self.channels[i])
                        j = j + 1
            else:
                raise TypeError
        except TypeError:
            print("Bad number of arguments")
