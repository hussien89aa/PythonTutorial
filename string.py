def main():
    # string management
    string = "hola CARLOS"
    # conatenate
    print(string+" como estas")
    # replace
    print(string.replace("hola", 'hi'))
    # lower case
    print(string.lower())
    # upper case
    print(string.upper())
    # count
    print(len(string))
    # find get the position of charater
    # this method retunr -1 is string don't exist
    print(string.find("hola"))
    #split
    # transform string into array depending on the chain
    print(string.split(' '))

    #TODO: https://www.programiz.com/python-programming/methods/string FOR MORE INFORMATION
if __name__ == '__main__':
    main()
    