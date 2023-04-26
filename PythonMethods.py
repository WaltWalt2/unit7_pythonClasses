class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

time_1 = Time(5, 32, 00)
time_2 = Time(23, 11, 11)
print(time_1)
print(time_2)


def yourcurrenttime():
    hour = int(input('enter your local hour'))
    minute = int(input('enter your local minutes'))
    class Time:
        def __init__(self,hour,minute):
            self.hour = hour
            self.minute = minute
        def __str__(self):
            return(f"{self.hour} : {self.minute} am")
        
    time_1 = Time(hour,minute) 
    print(time_1)

yourcurrenttime()