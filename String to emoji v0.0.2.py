import clipboard

ipt = input("입려어억 : ")

iptSt = list(ipt)
iptcom = ""
nomList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
nomEngList = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
supportList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "+", "-", "*", "/", "=", "!", "?"]

for i in range(0, len(iptSt)):
    if iptSt[i].upper() in supportList:
        if iptSt[i] == " ":
            iptcom += " "
        elif str(iptSt[i]) in nomList:
            iptcom = iptcom + ":" + nomEngList[int(iptSt[i])] + ": "
        elif iptSt[i] == "+":
            iptcom += ":heavy_plus_sign: "
        elif iptSt[i] == "-":
            iptcom += ":heavy_minus_sign: "
        elif iptSt[i] == "/":
            iptcom += ":heavy_division_sign: "
        elif iptSt[i] == "*":
            iptcom += ":heavy_multiplication_x: "
        elif iptSt[i] == "=":
            iptcom += ":heavy_equals_sign: "
        elif iptSt[i] == "?":
            iptcom += ":question: "
        elif iptSt[i] == "!":
            iptcom += ":exclamation: "
        else:
            iptcom = iptcom + ":regional_indicator_" + str(iptSt[i]).lower() + ": "
    else:
        print(f"지원하지 않는 문자 {iptSt[i]} 발견. 출력 문자열에서 제외됩니다.")
        continue

if iptSt[i].upper() in supportList:
    print(iptcom)
    clipboard.copy(iptcom)
