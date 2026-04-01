name=str(input("Enter customer name: "))
items=[]
prices=[]
i=0
while True:
    items.append(input("Enter item name (or 'done' to finish): "))
    if items[i].lower()=="done":
        break
    prices.append(int(input("Enter price: ")))
    i+=1
print("CUSTOMER: ", name.upper(),"\n Items:",
      len(items)-1,"\n Subtotal:",sum(prices))
total=sum(prices)

time=int(input("Enter current hour (0-23): "))
print(("-"*30+"\n"+"Discount : "))
if time>=6 and time<12:
    print("Morning discount"+"\n"+"Discount: ",total*0.1," KZT")
    total*=0.9

elif time>=12 and time<17:
    print("No discount"+"\n"+"Discount: 0 KZT")
elif time>=17 and time<22:
    print("Evening discount"+"\n"+"Discount: ",total*0.05," KZT")
    total*=0.95
else:
    print("Closed")
print("TIP (10%) :",total*1.1)
print("total :",total)

print("Name uppercase: "+name.upper())
print("Name lowercase: "+name.lower())
print("Name length : ",len(name))
print("Vip customer" if name[0].upper()=='A' or name[0].upper()=='S' else "Regular customer")

