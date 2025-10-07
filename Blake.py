sprinters = ["Bolt","Blake","Tyson","Asafa"]
time = ["9.58","9.69","9.69","9.72"]

Fastest = dict()
Fastest["name"] = sprinters[0]
Fastest["time"] = time[0]

second = dict()
second["name"] = sprinters[1]
second["time"] = time[1]

third = dict()
third["name"] = sprinters[2]
third["time"] = time[2]

fourth = dict()
fourth["name"] = sprinters[3]
fourth["time"] = time[3]

all = []
all.append(Fastest)
all.append(second)
all.append(third)
all.append(fourth)
print(all)