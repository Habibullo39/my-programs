first = dict()
second = dict()
smth = input("write something")
smth2 = input("write something")
message = smth.upper()
message2 = smth2.upper()

if len(message) == len(message2):
 i = 0
 while i < len(message):
  letter = message[i]
  letter2 = message2[i]
  first[letter] = first.get(letter,0) + 1
  second[letter2] = second.get(letter2,0) + 1
  i = i + 1
if first == second:
  print("it is anagrams")
else:
  print("it is not anagrams")

print(first,second)
