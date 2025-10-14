Roman = dict()
Roman["M"] = 1000
Roman["D"] = 500
Roman["C"] = 100
Roman["L"] = 50
Roman["X"] = 10
Roman["V"] = 5
Roman["I"] = 1
output = []
value = []

isitroman = 0

def res(n,howmntimessub):
   if n < len(input):
     letter = input[n]
     num = Roman[letter]
     if n == 0:
        value.append(num)
        output.append(num)
        return res(n + 1,howmntimessub)
     elif num <= output[n - (1 + howmntimessub)]:
        value.append(num)
        output.append(num)
        return res(n + 1,howmntimessub)
     elif num > output[n - (1 + howmntimessub)]:
        value.append(num)
        sub = num - output[n - (1 + howmntimessub)]
        del output[n - (1 + howmntimessub)]
        output.append(sub)
        return res(n + 1,howmntimessub + 1)
   else:
      return

mes = input("write roman numerals")
input = mes.upper()

i = 0
while i < len(input):
   if input[i] != "M" and input[i] != "D" and input[i] != "C" and input[i] != "L" and input[i] != "X" and input[i] != "V" and input[i] != "I":
     isitroman = 1
   i = i + 1

if isitroman == 1:
   print("try only roman numerals")
else:
   res(0,0)
   print(value)
   print(sum(output))
