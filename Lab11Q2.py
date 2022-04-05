class ClockTime:
    hours = 0
    minutes = 0
    seconds = 0

    def setHours(self,hrs):
        self.hours = hrs

    def setMinutes(self,mins):
        self.minutes = mins

    def setHours(self,secs):
        self.seconds = secs

    def setTime(self,hrs,mins,secs):
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def showTime(self):
        print("The time set is: " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds))

clock1 = ClockTime()
hrs = int(input("Enter hours in 24h format (value 0-23): "))
if hrs < 0 and hrs > 23:
    print("Incorrect Format!")
mins = int(input("Enter minutes in 24h format (value 0-59): "))
if mins < 0 and mins > 59:  
    print("Incorrect Format!")
secs = int(input("Enter seconds in 24h format (value 0-59): "))
if secs < 0 and secs > 59:
    print("Incorrect Format!")

clock1.setTime(hrs, mins, secs)
clock1.showTime()    