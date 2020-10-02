def main():
    Age=input("enter your Age:")
    if(int(Age)>18):
        print("welcome")
    else:
        print("Not Welcome")
        
    # Single line comprehension
    print("Welcome" if int(Age) > 18 else "Not Welcome")






if __name__ == '__main__':main()
