ipt = input("입려어억 : ")

iptSt = list(ipt)
iptcom = ""
nomList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nomEngList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
supportList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "+", "-", "*", "/", "=", "!", "?"]

for i in range(0, len(iptSt)):
    if iptSt[i].upper() in supportList:
        if iptSt[i] == " ":
            iptcom = iptcom + " "
        elif str(iptSt[i]) in nomList:
            iptcom = iptcom + ":" + nomEngList[int(iptSt[i])] + ": "
        elif iptSt[i] == "+":
            iptcom = iptcom + ":heavy_plus_sign: "
        elif iptSt[i] == "-":
            iptcom = iptcom + ":heavy_minus_sign: "
        elif iptSt[i] == "/":
            iptcom = iptcom + ":heavy_division_sign: "
        elif iptSt[i] == "*":
            iptcom = iptcom + ":heavy_multiplication_x: "
        elif iptSt[i] == "=":
            iptcom = iptcom + ":heavy_equals_sign: "
        elif iptSt[i] == "?":
            iptcom = iptcom + ":question: "
        elif iptSt[i] == "!":
            iptcom = iptcom + ":exclamation: "
        else:
            iptcom = iptcom + ":regional_indicator_" + str(iptSt[i]).lower() + ": "
    else:
        print("지원하지 않는 글자가 포함되어 있습니다.")
        break

if iptSt[i].upper() in supportList:
    print(iptcom)
