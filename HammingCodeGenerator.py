import re


# Function for take input a 4 bit information bit stream
def myInput():
    while True:
        inStr = input("Please Enter the Information Bits : ")
        if re.match("[0-1]*$", inStr) and len(inStr) == 4:
            break
        else:
            print ("Error! Only 0 and 1 are allowed and Only 4 bit allowed !!!")
    return inStr


# Function for enter the parity choice
def parityTypeInput():
    while True:
        parity = input("For Even Parity enter 1 for Odd Parity enter 0 : ")
        if re.match("[0-1]$", parity) and len(parity) == 1:
            break
        else:
            print ("Error! Only 0 and 1 are allowed and Only 1 bit allowed !!!")
    return parity


# Generate even parity bits
def generateCodeEven(information):
    i = [int(x) for x in information]
    p0 = str(i[3] ^ i[2] ^ i[0])
    p1 = str(i[3] ^ i[1] ^ i[0])
    p2 = str(i[2] ^ i[1] ^ i[0])
    outMsg = information[0:3] + p2 + information[3] + p1 + p0
    return outMsg


# Generate odd parity bits
def generateCodeOdd(information):
    i = [int(x) for x in information]
    p0 = str(int(not (i[3] ^ i[2] ^ i[0])))
    p1 = str(int(not (i[3] ^ i[1] ^ i[0])))
    p2 = str(int(not (i[2] ^ i[1] ^ i[0])))
    outMsg = information[0:3] + p2 + information[3] + p1 + p0
    # print outMsg
    return outMsg


if __name__ == "__main__":
    inMsg = myInput()
    parity_Type = parityTypeInput()
    hammingCode = ""
    if parity_Type == "1":
        hammingCode = generateCodeEven(inMsg)
    elif parity_Type == "0":
        hammingCode = generateCodeOdd(inMsg)
    print("The Hamming Code for The Information Bit Stream " + inMsg + " is : " + hammingCode)
