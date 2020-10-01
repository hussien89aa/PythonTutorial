def main():
    Degree=int(input("enter your Degree:"))
    if(Degree>=90 ):
        print("hi")
        
        if(Degree>94):
              print("Your Score is +A")
        else:
            print("Your Score is -A")
    elif(Degree>=80 and Degree<=89):
        print("Your Score is B")
    elif(Degree>=70 and Degree<=79):
        print("Your Score is C")
    elif(Degree>=60 and Degree<=69):
        print("Your Score is D")
    elif(Degree>=50 and Degree<=59):
        print("Your Score is E")
    else:
        print("You Fail")
        

if __name__ == '__main__':
    main()
