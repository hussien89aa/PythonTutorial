def main():
    Age=int(input("enter your Age:"))
    if(Age>=8 and Age<=10):
        print("children")

    elif(Age>=11 and Age<=15):
        print("kids")
    elif(Age>=16 and Age<=18):
        print("Teen-agers")
    elif(Age>=19 and Age<=30):
        print("Young")
    else:
        print("Out of range")
    print("End")





if __name__ == '__main__':main()
