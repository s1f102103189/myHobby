import sys

def main(lines):
    red = False
    red_count = 0
    white = False
    white_count = 0
    for i, v in enumerate(lines):
        #print("line[{0}]: {1}".format(i, v))
        if (i==0):
            x = v
        elif (i==1):
            y = list(map(int. v.split(" ")))
            for s in range(len(y)):
                if s[i] == "RU":
                    red = True
                    red_count += 1
                elif s[i] == "RD":
                    red = False
                    red_count -= 1
                elif s[i] == "WU":
                    white = True
                    white_count += 1
                elif s[i] == "WD":
                    white = False
                    white_count -= 1
        if ((red_count != 0) or (red_count != 1) or (white_count != 0) or (white_count != 1)):
            print("Alice")
        elif (((red_count == 0) or (red_count == 1)) and ((white_count != 0) or (white_count != 1))):
            print("Simon")
            if ((red == True) and (white == True)):
                print("UU")
            elif ((red == True) and (white == False)):
                print("UD")
            elif ((red == False) and (white == True)):
                print("DU")
            elif ((red == False) and (white == False)):
                print("DD")

import sys

def main(lines):
    mao = 0
    count = 0
    for i, v in enumerate(lines):
        #print("line[{0}]: {1}".format(i, v))
        if (i==0):
            x = v
        elif (i==1):
            y = list(map(int. v.split(" ")))
            mao = y[0]
            for i in range(10**18):
                mao -= y[1]
                if mao <= 0:
                    print("YES")
                    print(count+1)
                mao += y[2]
                count += 1
        print("NO")




