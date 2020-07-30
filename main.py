callist=["(",")","+",".","*"]
varlist=[]
outlist=[]
jalan =True

def logika(mode,inp1,inp2):
    has=[]
    for i in range(len(inp1)):
        if(mode == "*" or mode == "."):
            if inp1[i] == 1 and inp2[i] == 1:
                has.append(1)
            else:
                has.append(0)
        elif(mode == "+"):
            if inp1[i] == 1 or inp2[i] == 1:
                has.append(1)
            else:
                has.append(0)
    return has

def rumcal(mas):
    print(mas)
    for i in range(len(mas)):
        if mas[i] in callist:
            in1= mas[0:i]
            in2=mas[i+1:len(mas)]
            cal = mas[i]
            break
    if in1[0]=="-":
        x=in1[1]
    else:
        x=in1[0]
    print(x,end=" = ")
    for i in range(len(varlist)):
        if x==varlist[i]:
            has1=outlist[i].copy()

    if in1[0]=="-":
        for j in range(len(has1)):
            if has1[j]==1:
                has1[j]=0
            else:
                has1[j]=1
    print(has1)

    if in2[0]=="-":
        x=in2[1]
    else:
        x=in2[0]
    print(x,end=" = ")
    for i in range(len(varlist)):
        if x==varlist[i]:
            has2=outlist[i].copy()
            break
    if in2[0]=="-":
        for j in range(len(has2)):
            if has2[j]==1:
                has2[j]=0
            else:
                has2[j]=1
    print(has2)
    res=logika(cal,has1,has2)
    x=chr(ord(varlist[-1])+1)
    print(x,end=" = ")
    print(res)
    varlist.append(x)
    outlist.append(res)

def teslist(jum,num):
    n=pow(2,jum)
    b=j=pow(2,num)
    out=[]
    type=False
    for i in range(n):
        if(b == 0):
            type=not(type)
            b=j
        if type:
            out.append(1)
        else:
            out.append(0)
        b=b-1
    return out



bakrum=rumus=input("Masukan Rumus Gerbang Logika:\n")
print("\nHasil:")
for i in rumus:
    if not(i in varlist) and not(i in callist) and i != "-":
        varlist.append(i)

for i in range(len(varlist)):
    x=teslist(len(varlist),i)
    outlist.append(x)

while jalan:
    batas=[0,0]
    for i in range(len(bakrum)):
        if bakrum[i] == "(":
            batas[0]=i
        if bakrum[i] == ")":
            batas[1]=i
            break
    if batas[0]==batas[1]:
        jalan = False
        cal=bakrum
        rumcal(cal)
    else:
        cal=bakrum[batas[0]+1:batas[1]]
        rumcal(cal)
        bakrum=bakrum[0:batas[0]] + varlist[-1] + bakrum[batas[1]+1:len(bakrum)]
