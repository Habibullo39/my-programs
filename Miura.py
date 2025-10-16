howmany = int(input("How many words do you wanna write"))
words = []
i = 0
while i < howmany:
    mes = input("write a word")
    words.append(mes)
    i = i + 1

isitover = 0

i = 0
while isitover == 0:
    j = 1
    while j < len(words) and isitover == 0:
        first = words[0]
        another = words[j]
        if i < len(first) and i < len(another):
         if first[i] == another[i]:
            j = j + 1
         else:
            isitover = 1
        else:
           isitover = 1

    if isitover == 0:
      letter = first[i]
      print(letter,end="")
    else:
       if i == 0:
          print("No common prefix")

    i = i + 1