

def main():
    #string
    Data="software engineer"
    #String Slicing
    print(Data[0:5])
    #List
    Ages=[44,33,45,33,54]
    Ages.append(100)
    Ages.insert(0,33)#insert with index value
    print(Ages)
    #Tuples
    Ages_tp=(44,33,45,33,54)#A tupple is immutable i.e, it cannot be changed
    Ages_tp.append(100)
    Ages_tp.insert(0,33)
    print(Ages_tp)



if __name__ == '__main__':main()
