#Dictionary is a key value pairs


def main():
    #Creating a dictionary
    Student=dict(Name="hussein alrubaye",Age=27,Slary=232.5);
    
    #it can also be created as:-
    #Student={'Name':"hussein alrubaye",'Age':27,'Slary':232.5};
    
    
    #we can assign a list,tuple or even a dictionary to a key in a dictionary
    
    #Replacing the value of a key
    Student['Name']="Hussein Ahmed"
    
    #Adding a key value pair in the dictionary
    Student["Dept"]="software engineer"
    
    #Printing the type of an dictionary
    print(Student,type(Student))
    
    #Deleting the a key from the dictonary
    del Student["Dept"]
    
    #Accessing the value from a key
    print(Student['Name'])
    print(Student['Age'])
    
    #Removing all the items from the dictionary
    Student.clear()
    
    print(Student,type(Student))
    



if __name__ == '__main__':
    main()
