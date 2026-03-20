# --coding:utf-8--

import os

os.system("cls")
print("Input the first integer number:")
iNum1 = int(input())
print("Input the second integer number:")
iNum2 = int(input())
iVal1 = abs(iNum1)
iVal2 = abs(iNum2)
if (iVal1 > 0 and iVal2 > 0):
    iVal3 = iVal1
    iVal4 = iVal2
    while (iVal1 != iVal2):
        if(iVal1 > iVal2):
            iVal1 -= iVal2
            iVal3 += iVal4
        else:
            iVal2 -= iVal1
            iVal4 += iVal3
    
    nLcm = (iVal3 + iVal4) / 2
    print(f"The Lcm of the numbers {iNum1} and {iNum2} is {nLcm}\r\n")
else:
    print("The numbers must not be equal 0")
