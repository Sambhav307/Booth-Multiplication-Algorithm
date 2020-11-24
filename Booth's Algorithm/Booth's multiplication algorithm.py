import sys
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
n = int(input("Number of registers:"))
def checknumber(val):
    global n
    if val > 2**(n-1)-1 or val < -(2**(n-1)):
        print("Input value out of range ")
        print("Input must lie between " + str(2**(n-1)-1) + " to " + str(-(2**(n-1))))
        return -1000
    return val
def converttobin(s):
    while len(s) != n:
        s = "0" + s
    return s
def bincheck(s):

    if len(s) == n:
        return s
    elif len(s) > n:
        s = s[::-1]
        s[:n]
        s[::-1]
        return s
    elif len(s) < n:
        return converttobin(s)
def TwosCompliment (s):
    #help from geeksforgeeks
    n = len(s)
    i = n-1
    while i >= 0:
        if s[i] == '1':
            break
        i = i-1
    if i == -1:
        return '1' + s
    k = i-1
    while k >= 0:
        if s[k] == '1':
            s = list(s)
            s[k] = '0'
            s = ''.join(s)
        else:
            s = list(s)
            s[k] = '1'
            s = ''.join(s)

        k -= 1
    return s
def asr():
    global ac
    global q0
    global q1
    global plusM
    global minnusM

    statement = ac + q1 + q0
    statement= statement[:-1]
    if statement[0]=="1":
        statement= "1"+statement
    else:
        statement= "0"+ statement

    return statement
def summ( val):
    global ac
    global q0
    global q1
    global plusM
    global minnusM

    temp = "0"*n
    i = n-1
    while(i>-1):
        if i>0:
            if ac[i] == "0":
                if val[i] == "0":
                    if temp[i] == "0":
                        temp = temp[:i] + "0" + temp[i + 1:]
                    elif temp[i] == "1":
                        temp = temp[:i] + "1" + temp[i + 1:]
                elif val[i] == "1":
                    if temp[i] == "0":
                        temp = temp[:i] + "1" + temp[i + 1:]
                    elif temp[i] == "1":
                        temp = temp[:i] + "0" + temp[i + 1:]
                        temp = temp[:i-1] + "1" + temp[i :]

            elif ac[i] == "1":
                if val[i] == "0":
                    if temp[i] == "0":
                        temp = temp[:i] + "1" + temp[i + 1:]
                    elif temp[i] == "1":
                        temp = temp[:i] + "0" + temp[i + 1:]
                        temp = temp[:i-1] + "1" + temp[i :]
                elif val[i] == "1":
                    if temp[i] == "0":
                        temp = temp[:i] + "0" + temp[i + 1:]
                        temp = temp[:i-1] + "1" + temp[i :]
                    elif temp[i] == "1":
                        temp = temp[:i] + "1" + temp[i + 1:]
                        temp = temp[:i-1] + "1" + temp[i :]
        elif i==0:
            if ac[i] == "0":
                if val[i] == "0":
                    if temp[i] == "0":
                        temp = temp[:i] + "0" + temp[i + 1:]
                    elif temp[i] == "1":
                        temp = temp[:i] + "1" + temp[i + 1:]
                elif val[i] == "1":
                    if temp[i] == "0":
                        temp = temp[:i] + "1" + temp[i + 1:]
                    elif temp[i] == "1":
                        temp = temp[:i] + "0" + temp[i + 1:]
            elif ac[i] == "1":
                if val[i] == "0":
                    if temp[i] == "0":
                        temp = temp[:i] + "1" + temp[i + 1:]
                    elif temp[i] == "1":
                        temp = temp[:i] + "0" + temp[i + 1:]
                elif val[i] == "1":
                    if temp[i] == "0":
                        temp = temp[:i] + "0" + temp[i + 1:]
                    elif temp[i] == "1":
                        temp = temp[:i] + "1" + temp[i + 1:]

        i = i - 1
    ac =temp
def whichFlow():
    global ac
    global q0
    global q1
    global plusM
    global minnusM

    checkS = q1[-1] + q0

    if checkS == "10":
        summ( minnusM)
        return asr()
    elif checkS == "01":
        summ(plusM)
        return asr()
    else:
        return asr()
final_check = ""
final = True
if checknumber(num1) == -1000 or checknumber(num2) == -1000:
    final = False
if num1>0 and num2>0:
    plusM = str(bin(num1))
    plusM = plusM[2:]
    Q = str(bin(num2))
    Q = Q[2:]
    plusM = bincheck(plusM)
    Q = bincheck(Q)
    minnusM = TwosCompliment(plusM)
    final_check = "++"
elif num1>0 and num2<0:
    num2 = num2*-1
    plusM = str(bin(num1))
    plusM = plusM[2:]
    Q = str(bin(num2))
    Q = Q[2:]
    plusM = bincheck(plusM)
    Q = bincheck(Q)
    minnusM = plusM
    final_check = "+-"
    plusM = TwosCompliment(minnusM)
elif num1<0 and num2>0:
    num1 = num1*-1
    plusM = str(bin(num1))
    plusM = plusM[2:]
    Q = str(bin(num2))
    Q = Q[2:]
    plusM = bincheck(plusM)
    Q = bincheck(Q)
    minnusM = plusM
    final_check = "-+"
    plusM=TwosCompliment(minnusM)
else:
    num1 = num1 * -1
    num2 = num2 * -1
    plusM = str(bin(num1))
    plusM = plusM[2:]
    Q = str(bin(num2))
    Q = Q[2:]
    plusM = bincheck(plusM)
    Q = bincheck(Q)
    minnusM = plusM
    plusM= TwosCompliment(minnusM)
    final_check = "--"
    Q=TwosCompliment(Q)

q0 = "0"
q1 = Q
ac = "0"
ac = bincheck(ac)
i=0
while final and i<n:
    i=i+1
    statement= whichFlow()
    ac=statement[0:n]
    q1=statement[n:2*n]
    q0=statement[-1]
    print(ac,q1,q0)

if final:
    ans= ac+q1
    if final_check == "++" :
        print("+",int(ans,2))
    elif final_check == "-+" :
        print("-",int(TwosCompliment(ans),2))

    elif final_check ==  "+-":

        print("-",int(TwosCompliment(ans),2))
    elif final_check=="--":
        print("+",int(ans,2))

sys.exit()

