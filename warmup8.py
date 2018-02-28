#Ryan Jones
#2/28/18

total = 0
for i in range (1,100000):
    if i%3==0 and i%10==0 and i%17==0:
        total = total+i
print(total)