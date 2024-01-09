class Car:
    def __init__(self,name):
        self.name = name
        print(self.name)
    def start(self,on,off):
        self.on = on
        self.off = off
        print(self.on)
    def light (self,lon,loff):
        self.lon =lon
        self.loff =loff
        if self.on =="on":
            print(self.lon)
        else:
            print(self.loff)    



Ford = Car(name="ford")
Ford.start(on ="",off = "off")
Ford.light(lon="light is on",loff="light is  off")



