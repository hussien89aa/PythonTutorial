

def main():
    #string
    Data="software engineer"
    print(Data[0:5])
    #List
    Ages=[44,33,45,33,54]
    Ages.append(100)
    Ages.insert(0,33)
    print(Ages)
    
    # Tuples     
    tuple_1 = (0, 1, 2, 3) 
    tuple_2 = ('Hello', 'World') 
    # Creating nested tuples 
    tuple_3 = (tuple_1, tuple_2) 
    print(tuple_3) 
    # Basic Operations
    print(tuple_1[1:]) 
    print(tuple_1[::-1]) 
    print(tuple_1[2:4]) 


if __name__ == '__main__':main()
