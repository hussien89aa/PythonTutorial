


def main():
    #Student={'Name':"hussein alrubaye",'Age':27,'Slary':232.5};
    Student=dict(Name="hussein alrubaye",Age=27,Slary=232.5);
    Student['Name']="Hussein Ahmed"
    Student["Dept"]="software engineer"
    print(Student,type(Student))
    del Student["Dept"]
    print(Student,type(Student))
    print(Student['Name'])
    print(Student['Age'])
    Student.clear()
    print(Student,type(Student))
    



if __name__ == '__main__':main()
