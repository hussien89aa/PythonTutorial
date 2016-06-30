class Operation:
    def Sum(self,n1,n2):
        SumResult=n1+n2
        print("Sum=",SumResult)
    def Sub(self,n1,n2):
        SubResult=n1-n2
        print("Sub=",SubResult)
class OperationWithMul(Operation):

    def Mul(self,n1,n2):
        MulResult=n1*n2
        print("Mul=",MulResult)


def main():
    #OP=Operation()
    #OP.Sub(4,2)
    #OP.Sum(10,15)
    OpMul=OperationWithMul();
    OpMul.Sub(4,2)
    OpMul.Sum(10,15)
    OpMul.Mul(10,2)





if __name__ == '__main__':main()
