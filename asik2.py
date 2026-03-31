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
      len(items),"\n Subtotal:",sum(prices))


# people=int(input("Enter number of people: "))
# subtotal = price1 + price2
# tip = subtotal*0.1
# total = subtotal + tip
# per_person = total / people
# print(
#     "=" * 30,
#     "\n        CAFE BILL\n"+
#     "=" * 30,
#     "\nCustomer : ", name,
#     "\n" + item1 + " : ", price1, "KZT",
#     "\n" + item2 + " : ", price2, "KZT",
#     "\n" + "-" * 30,
#     "\nSubtotal : ", subtotal, "KZT",
#     "\nTip (10%) : ", tip, "KZT",
#     "\nTotal : ", total, "KZT",
#     "\nPer person : ", per_person, "KZT",
#     "\n" + "=" * 30)
# print("Tip included:", tip > 0)
# print("Bill over 5000 KZT:", total > 5000)