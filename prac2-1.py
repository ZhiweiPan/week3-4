legs = 94
head = 35
for rabbits in range(head):
    chicken = head - rabbits
    total_legs = chicken*2 + rabbits*4
    if total_legs == legs:
        print(str(chicken)+" Chickens and "+str(rabbits)+" Rabbits")
    else :
        continue