
class Car:
    def __init__(self,Name):
         self._Name=Name
    def GetOwner(self):
        print("Owner is ",self._Name)




def main():
    mycar=Car("Hussein Alrubaye")
    mycar.GetOwner()
    Jencar=Car("Jen Alrubaye")
    Jencar.GetOwner()



if __name__ == '__main__':main()