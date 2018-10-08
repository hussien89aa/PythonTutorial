def main():
    Age=input("enter your Age:")
    if(int(Age)>=8 and int(Age)<=10):
        print("kids")
    elif(int(Age)>=11 and int(Age)<=15):
        print("children")
    elif(int(Age)>=16 and int(Age)<=18):
        print("Teenager")
    elif(int(Age)>=19 and int(Age)<=30):
        print("Young")
    elif(int(Age)>30 and int(age)<90):
        print("OLD")
    else:
        print("Death Range")
    print("End")





if __name__ == '__main__':main()
