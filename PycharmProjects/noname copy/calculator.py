import sys
import math

def pythag(a, b) :
    a_squared = math.pow(a, 2)
    b_squared = math.pow(b, 2)

    added = a_squared + b_squared

    return math.sqrt(added)

def main():
    userInput = sys.argv[1]

    if (sys.argv[1] == "add") :
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x+y)

    if (sys.argv[1] == "sub") :
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x-y)

    if (sys.argv[1] == "multiply") :
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x * y)

    if (sys.argv[1] == "divide") :
         x = int(sys.argv[2])
         y = int(sys.argv[3])
         print(x/y)

    if (sys.argv[1] == "power") :
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(x ** y)

    if (sys.argv[1] == "repeat") :
        x = (sys.argv[2])
        y = int(sys.argv[3])
        for i in range(y) :
            print(x)


    if (userInput == "countto"):
        x = int(sys.argv[2])

        for i in range(x + 1):
            print(i)

    if(userInput == "hypot") :
        x = int(sys.argv[2])
        y = int(sys.argv[3])
        print(pythag(x, y))


if __name__ == "__main__":
    main()


