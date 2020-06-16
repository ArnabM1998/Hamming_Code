import re


# Function for take input a 7 bit hamming code
def myInput():
    while True:
        inStr = input("Please Enter the Information Bits : ")
        if re.match("[0-1]*$", inStr) and len(inStr) == 7:
            break
        else:
            print ("Error! Only 0 and 1 are allowed and Only 7 bit allowed !!!")
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


# check error syndrome
def error_Dec(inMsg):
    i = [int(x) for x in inMsg]
    e0 = str(i[6] ^ i[4] ^ i[2] ^ i[0])
    e1 = str(i[5] ^ i[4] ^ i[1] ^ i[0])
    e2 = str(i[3] ^ i[2] ^ i[1] ^ i[0])
    e = e2 + e1 + e0
    return e


# Generate error free hamming code
def error_Cor(inMsg):
    i = [int(x) for x in inMsg]
    error_Syn = error_Dec(inMsg)
    a = [int(x) for x in error_Syn]
    outMsg = ""
    if error_Syn != "000":
        pos_Error = (4 * a[2]) + (2 * a[1]) + a[0]
        print ("Error Present!!! In Bit Position : " + str(pos_Error))
        i[7 - pos_Error] = int(not(i[7 - pos_Error]))
        for x in i:
            outMsg = outMsg + str(x)
        return outMsg
    else:
        outMsg = inMsg
        return outMsg


def info_Dec(inMsg, parity):
    print ("The Entered Hamming Code : " + inMsg)
    information = ""
    if parity == "1":
        Err_Free_Msg = error_Cor(inMsg)
        print ("The Error Free Hamming Code : " + Err_Free_Msg)
        information = Err_Free_Msg[0:3] + Err_Free_Msg[4]
    elif parity == "0":
        myst = ""
        st = ""
        i = [int(x) for x in inMsg]
        i[3] = int(not (i[3]))
        i[5] = int(not (i[5]))
        i[6] = int(not (i[6]))
        for x in i:
            myst = myst + str(x)
        Err_Free_Msg = error_Cor(myst)
        j = [int(x) for x in Err_Free_Msg]
        j[3] = int(not (j[3]))
        j[5] = int(not (j[5]))
        j[6] = int(not (j[6]))
        for x in j:
            st = st + str(x)
        print ("The Error Free Hamming Code : " + st)
        information = st[0:3] + st[4]
    print ("The Information Bit Stream for the entered Hamming Code is : " + information)


if __name__ == "__main__":
    hammingCode = myInput()
    parity_Type = parityTypeInput()
    info_Dec(hammingCode, parity_Type)
