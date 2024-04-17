sayılar=[1,2,3,4,5,6,7,8,9,10]
sayılar2=[]
for asal in sayılar:
    if asal % len(sayılar):
        sayılar2.append(asal,[])
    else:
        print("Sayılar Aralarında Asal Değildir!")


for i in sayılar2:
    i*=sayılar2
    print(i)






