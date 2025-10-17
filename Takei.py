howmany = int(input("How many words do you wanna write"))
words = []
i = 0
while i < howmany:
    mes = input("write a word")
    words.append(mes)
    i = i + 1

colle = dict()
res = []

i = 0
while i < len(words):
    word = words[i]
    j = 0
    while j < len(word):
        letter = word[j]
        if letter not in res:
         res.append(letter)
        colle[letter] = colle.get(letter,0) + 1
        j = j + 1

    i = i + 1

dou = 0
out = []

i = 0
while i < len(res):
   moji = res[i]
   num = colle[moji]
   j = 0
   while j < len(res) and dou == 0:
      moji2 = res[j]
      num2 = colle[moji2]
      if num < num2:
         dou = 1
      else:
         j = j + 1

   if dou == 0:
      out.append(moji)
   dou = 0
   i = i + 1


letter = out[0]
num = colle[letter]
mooji = ",".join(out)
print(f"The most common letter is {mooji} and it appeared {num} times.")