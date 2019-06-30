ss=str(input())
d=list(ss)
r=len(ss)
p=""
if r%2==0:
  d[int(r/2)]="*"
  d[int(r/2-1)]="*"
else:
   d[int(r/2)]="*"
p=p.join(d)
print(p)
