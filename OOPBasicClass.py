
class Car:
    def GetOwner(self):
        print("Owner is ",self._Name)
    def SetOwner(self,Name):
        self._Name=Name



def main():
    mycar=Car()
    mycar.SetOwner("Hussein Alrubaye")
    mycar.GetOwner()
    Jencar=Car()
    Jencar.SetOwner("Jen Alrubaye")
    Jencar.GetOwner()



if __name__ == '__main__':main()