

def SumNumbers(n1,n2):
    z=n1+n2
    return z


def main():
    n1 = int(input("ENTER FIRST NUMBER"))
    n2 = int(input("ENTER SECOND NUMBER"))
    result= SumNumbers(n1,n2)
    print("z={}".format(result))




if __name__ == '__main__':main()
