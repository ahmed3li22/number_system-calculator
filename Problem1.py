# Malak Sabry Omar(20230531)
#Ahmed Ali Ahmed(20230525)
#Amir Fathi Hag(20230744)
def decimaltobinary(decimal):
    binary_result=""
    while decimal > 0:
        binary_result =str(decimal%2) + binary_result
        decimal//=2
    return binary_result
# covert from decimal to binary

def decimaltooctal(decimal):
    octal_chars="01234567"
    octal_result =""
    while decimal>0:
        octal_result =octal_chars[decimal%8] + octal_result
        decimal //=8
    return  octal_result  if octal_result else "0"
#convert from decimal to octal
def decimaltohex(decimal):
     hex_chars ="0123456789ABCDEF"
     hex_result=""
     while decimal>0:
         hex_result =hex_chars[decimal % 16] +hex_result
         decimal//=16
     return hex_result  if hex_result  else "0"
#convert from decimal to hexadecimal

def binarytodecimal(binary):
    decimal_result=0
    length =len(binary)
    for i in range(length):
        decimal_result +=int(binary[-(i+1)]) *(2**i)
    return decimal_result
#convert from Binary to decimal
def octaltodecimal(octal):

    decimal_result =0
    length =len(octal)

    for i in range(length):
          decimal_result +=int(octal[-(i+1)]) *(8**i)
    return decimal_result
#convert from octal to decimal
"""
def octaltodecimal(octal):
    oct_chars="01234567"
    decimal_result=0
    length=len(octal)
    for i in range(length):
        decimal_result+=oct_chars.index(octal[-(i+1)])*(8**i)

        return decimal_result
        """
def hextodecimal(hex):
     hex_chars = "0123456789ABCDEF"
     decimal_result =0
        #hex_str=str(n)
     length=len(hex)
     for i in range(length):
           decimal_result += hex_chars.index(hex[-(i+1)])*(16**i)
     return decimal_result
#convert from hexadecimal to decimal




def convert_number(num,from_base,to_base):

    if from_base=="A":
        from_base=10
    elif from_base=="B" :
        from_base=2
    elif from_base=="C":
        from_base=8
    elif from_base=="D":
        from_base=16

    if to_base =="A":
        to_base=10
    elif to_base=="B":
         to_base=2
    elif to_base=="C":
        to_base=8
    elif to_base=="D":
        to_base=16
    if from_base==10:
        if to_base==10:
            return num
        elif to_base==2:
            return decimaltobinary(int(num))
        elif to_base ==8:
            return decimaltooctal(int(num))
        elif to_base==16:
            return decimaltohex(int(num))
    elif from_base ==2:
        if to_base==10:
            return binarytodecimal(num)
        elif to_base==8:
            return decimaltooctal(binarytodecimal(num))  #covert from Binary to octal
        elif to_base ==16:
            return decimaltohex(binarytodecimal(num))    #convert from binary to hixadecimal
        elif to_base==2:
            return num
    elif from_base ==8:
        if to_base==10:
            return octaltodecimal((num))
        elif to_base==2:
            return decimaltobinary(octaltodecimal(num))   #convert from octal to Binary
        elif to_base==8:
            return num
        elif to_base==16:
            return decimaltohex(octaltodecimal(num))     #convert from octal to hexadecimal
    elif from_base==16:
        if to_base==10:
            return hextodecimal(num)
        elif to_base==2:
            return decimaltobinary(hextodecimal(num))   #convert from hexadecimal to Binary
        elif to_base==8:
            return decimaltooctal(hextodecimal(num))    #convert from hexadecimal to octal
        elif to_base==16:
            return num
    return "invalid input"

def main():
    while True:
        print("numbering system converter")
        print("A) insert a new number")
        print("B) Exit program")

        choice_menu1 = input("your choice:").upper()
        if choice_menu1=="A":
            print("please insert a number")
            num =input("number:")

            print("please select the base you want to convert a number from")
            print("A)decimal")
            print("B)binary")
            print("C)octal")
            print("D)hex")


            choice_menu2 =input("your choice:").upper()
            if choice_menu2 in["A","B","C","D"]:
                 print("please select the base you want to convert a numer to")
                 print("A)decimal")
                 print(" B)binary ")
                 print(" C)octal")
                 print(" D)hex")

                 choice_menu3 =input("your choice:")
                 if choice_menu3 in["A","B","C","D"]:
                     result =convert_number(num,choice_menu2 ,choice_menu3)
                     print("Result:",result)
                 else:
                     print("please select a valid choice")
            else:
                print("please select a valid choice")

        elif choice_menu1 =="B":
            break
        else:
            print("please select a valid choice")

if __name__ =="__main__":
    main()

