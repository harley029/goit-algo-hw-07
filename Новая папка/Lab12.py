import random
file=20
minv=1
maxv=100
cnt=50
winner_combo=[]
for i in range(20):
    v=random.randint(minv,maxv)
    while v in winner_combo:
        v=random.randint(minv,maxv)
    winner_combo.append(v)
scores={}
for number in range(file):
    fname=f"{number}.bingo"
    scores[number]=0
    with open(fname,'w+') as output:
        lst=[]
        for i in range(cnt):
            v=random.randint(minv,maxv)
            while v in lst:
                v=random.randint(minv,maxv)
            lst.append(v)
            if v in winner_combo:
                scores[number]+=1
        for i in lst:
            output.write(f"{i} ")
print(scores)
max_scores=max(scores.values())
for number in scores:
    if scores[number]==max_scores:
        print(f"{number} : {scores[number]}")