



def main():
    try:
        readFile=open("test.txt","r")
        for line in readFile:
            print(line)
        readFile.close()
    except IOError:
        print("File not found")
    else:
      print("File is readed")



if __name__ == '__main__':main()
