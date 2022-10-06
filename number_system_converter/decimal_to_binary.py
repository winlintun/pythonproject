# Decimal (base 10) to Binary (base 2)

def decimal_to_binary_converter(decimalNum:int) -> str:
    """
    668/2 = 334 -> 0
    334/2 = 167 -> 0
    167/2 = 83.5 -> 1
    83/2 = 41.5 -> 1
    41/2 = 20.5 -> 1
    20/2 = 10 -> 0
    10/2 = 5 -> 0
    5/2 = 2.5 -> 1
    2/2 = 1 -> 0
    1/2 = 0.5 -> 1

    ans = 1010011100

    စားလို့ ပြတ်တယ်ဆိုရင် 0
    စားလို့ မပြတ်ဘူးဆိုရင် 1
    """

    mylist = []

    while decimalNum > 0:
        rem = decimalNum % 2 # remainder
        mylist.append(rem)
        decimalNum = decimalNum // 2

    binString = ''
    while len(mylist) > 0:
        binString = binString + str(mylist.pop())

    return binString



def decimal_to_octal_converter(decimalNum:int) -> str:
    """
    668/8 = 83.5 -> 0.5 * 8 = 4
    83/8 = 10.375 -> 0.375 * 8 = 3
    10/8 = 1.25 -> 0.25 * 8 = 2
    1/8 = 0.125 = 0.125 * 8 = 1

    ans = 1234

    စားလို့ရတဲ့အကြွင်းကို 8 နဲ့မြှောက်
    """

    mylist = []

    while decimalNum > 0:
        rem = decimalNum % 8
        mylist.append(rem)

        decimalNum //= 8

    octString = ''
    while len(mylist) > 0:
        octString += str(mylist.pop())

    return octString


def decimal_to_hexadecimal(decimalNum:int) -> str:
    """
    hexadecimal = [0,1,2,3,4,5,6,7,8,9,10=A,11=B,12=C,13=D,14=E,15=F]

    668/16 = 41.75 -> 0.75 * 16 = 12
    41/16 = 2.5625 -> 0.5625 * 16 = 9
    2/16 = 0.125 -> 0.125 * 16 = 2
    0/16 = 0

    ans = 2912 -> 29C

    စားလို့ရတဲ့အကြွင်းကို 16 နဲ့မြှောက်
    """

    mylist = []

    hexa = {10:"A", 11:'B', 12:"C", 13:"D", 14:"E", 15:"F"}

    while decimalNum > 0:
        rem = decimalNum % 16

        if rem > 9:
            for key, val in hexa.items():
                if rem == key:
                    mylist.append(val)
        else:
            mylist.append(rem)

        decimalNum //= 16

    hexaString = ''

    while len(mylist) > 0:
        hexaString += str(mylist.pop())

    return hexaString



def binary_to_decimal(binNum:int) -> int:
    binNum = str(binNum)
    p_cout = len(binNum)
    mylist = []

    for i in binNum:
        p_cout = p_cout - 1
        dec = int(i) * (2 ** p_cout)
        mylist.append(dec)

    decimalNum = 0

    while len(mylist) > 0:
        decimalNum = decimalNum + mylist.pop()

    return decimalNum


def binary_to_octal(binNum:int) -> int:
    binNum = str(binNum)
    p_cout = len(binNum)
    mylist = []

    # first we neet to convert decimal
    for i in binNum:
        p_cout = p_cout - 1
        dec = int(i) * (2 ** p_cout)
        mylist.append(dec)

    decimalNum = 0

    while len(mylist) > 0:
        decimalNum = decimalNum + mylist.pop()


    # decimal to octal
    # function call now
    octNumber = decimal_to_octal_converter(decimalNum)
    return octNumber

