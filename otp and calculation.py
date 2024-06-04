import random
def genotp(size,qty):
    n=size
    for i in range(0,qty):
        otp=random.randint(10*(n-1),(10*n)-1)
        print(otp)
    print("\n")
list1=["HDFC", "ICICI", "SBI","HSBC","Kotak","IDFC","Canara","BOB","Karnataka","JPMorgan","GoldmanSachs","WellsFargo"]
list2=[6,4,5,8,6,6,6,6,6,6,6,6]
list3=[]
list4=[500, 500, 500,235,500,500,500,500,500,500,500,500]
list5=[]
base1=[10,10,10,10,10,10,10,10,10,100,100,100]
for i in range(0,len(list2),1):
    list3.append(base1[i]+list2[i])
for i in range(0,len(list3),1):
    list5.append(list4[i]*list3[i])
amt_day = sum(list5)/100
amt_month= amt_day*30
amt_3months=amt_month*3
print(list3)
print(list5)
print(amt_day)
print(amt_month)
print(amt_3months)
