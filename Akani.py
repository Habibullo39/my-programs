words = []
howmany = int(input("How many words"))
i = 0
while i < howmany:
    word = input("write a word")
    words.append(word)
    i = i + 1

rabbit = 0
result = []

i = 0
while i < len(words):
    j = 0
    while j < len(words):
      first = words[i]
      another = words[j]
      if len(first) > len(another):
         rabbit = 1
      j = j + 1

    if rabbit == 0:
       mes = words[i]
       result.append(mes)

    rabbit = 0
    i = i + 1

if len(result) == howmany:
   print("No result")
else:
   i = 0
   while i < len(result):
      tada = result[i]
      print(tada,end=" ")
      i = i + 1
