output = []
def binary(n):
    if n < 0:
     print("try positive number")
     return
    elif n == 0 or n == 1:
     output.append(n)
     return n
    else:
     output.append(n%2)
     return binary(n//2)
    
number = int(input("write a number"))
binary(number)

i = len(output) - 1
while i > -1:
  print(output[i],end="")
  i = i - 1