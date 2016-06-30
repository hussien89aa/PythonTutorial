
class Car:
    def __init__(self,**kwargs):
         self.Data=kwargs
    def GetOwner(self):
        print("Owner Name ",self.Data["Name"])
        print("Car Model ",self.Data["Model"])
        print("Year ",self.Data["Year"])
    def Set_Model(self,Model):
        self.Data["Model"]=Model
    def Get_Model(self):
        print("Car Model ",self.Data["Model"])




def main():
    mycar=Car(Name="Hussein Alrubaye",Model="camer 2015",Year=2015)
    mycar.GetOwner()
    Jencar=Car(Name="Jen Alrubaye",Model="sony x",Year=2015)
    Jencar.GetOwner()
    #jen model set
    Jencar.Set_Model("2016")
    Jencar.Get_Model()



if __name__ == '__main__':main()