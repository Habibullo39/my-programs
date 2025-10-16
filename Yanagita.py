num = dict()
num[1] = "one"
num[2] = "two"
num[3] = "three"
num[4] = "four"
num[5] = "five"
num[6] = "six"
num[7] = "seven"
num[8] = "eight"
num[9] = "nine"

exception = dict()
exception[10] = "ten"
exception[11] = "eleven"
exception[12] = "twelve"
exception[13] = "thirteen"
exception[14] = "fourteen"
exception[15] = "fifteen"
exception[16] = "sixteen"
exception[17] = "seventeen"
exception[18] = "eighteen"
exception[19] = "nineteen"

second = dict()
second[2] = "twenty"
second[3] = "thirty"
second[4] = "forty"
second[5] = "fifty"
second[6] = "sixty"
second[7] = "seventy"
second[8] = "eighty"
second[9] = "ninety"

mes = int(input("write a number"))

if mes > 99:
    bolt = mes//100
    rashid = num[bolt]
    print(rashid,"hundred",end=" ")

if mes%100 > 9:
    if mes%100 > 9 and mes%100 < 20:
        blake = mes%100
        yanagita = exception[blake]
        print(yanagita,end=" ")
    else:
        blake = (mes%100)//10
        kiryu = second[blake]
        print(kiryu,end=" ")

if mes%10 > 0 and (mes%100 < 10 or mes%100 > 19):
    asafa = mes%10
    tada = num[asafa]
    print(tada)

if mes == 0:
    print("zero")
