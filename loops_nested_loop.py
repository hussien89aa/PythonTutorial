


#main function starts 
def main():
    i=0
    while(i<5):  #outer while loop
        print("i={}".format(i))
        i+=1     #increment value of i by 1 i.e i = i+1      
        j=5
        while(j>i):  #inner while loop
            print("j={}".format(j))     #format() funtion used for format the string in python
            j-=1     #decrementing value of j by 1 i.e j=j-1       




if __name__ == '__main__':main()
