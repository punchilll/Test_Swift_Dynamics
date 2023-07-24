fac = "10!"
splt = fac.split("!")
number = int(splt[0])
sum = number
i = number
for x in range(number-1):
    sum = sum*(i-1)
    i = i-1

spltn = []
for char in str(sum):
    spltn.append(int(char))
spltn = list(map(int, str(sum)))
##print(spltn)

count = 0
length = len(spltn)
for x in range(len(spltn)):
    length = length-1
    ##print(spltn[length]);
    if spltn[length] == 0:
        count+=1
    else:
        break

print("มีเลข 0 ต่อท้าย",count,"ตัว")
