import math
goal =85
state = [-1]*(goal+1)
state[2] = 0
for k in range (2,int(goal/2)+1):
    if state[k]<0:continue
    for pos, cost in [
        (k*2,k),
        (k*2+1,math.floor(k/2)),
        (k*2+2,k+2)]:
        if pos > goal :continue
        if state[pos] == -1 or state[pos] > state[k] +cost:
            state[pos] = state[k]+cost
print(state[goal])