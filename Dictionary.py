


def main():
    
    
    #Student={'Name':"hussein alrubaye",'Age':27,'Salary':232.5};
    
    Student=dict(Name="hussein alrubaye",Age=27,Salary=232.5);
    # 'Name','Age','Salary' are keys and "hussein alrubaye",27,232.5 are their respective values
    
    # We can access value from key like this
    Student['Name']="Hussein Ahmed"
    
    # Creating a New key in Student
    Student["Dept"]="software engineer"
    print(Student,type(Student))
    
    # Deleting reference of 'Dept' Key
    del Student["Dept"]
    print(Student,type(Student))
    print(Student['Name'])
    print(Student['Age'])
    
    # Clearing All dictionary
    Student.clear()
    print(Student,type(Student))
    



if __name__ == '__main__':main()
