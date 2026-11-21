#13) მომხმარებელს შემოატანინეთ რიცხვი. თუ რიცხვი დადებითია, შეამოწმეთ შიგნით მეორე if-ით არის თუ არა ლუწი, თუ ლუწია დაბეჭდეთ "Positive and even", თუ არა "Positive and odd". ხოლო თუ რიცხვი უარყოფითია, შეამოწმეთ მეორე if-ით არის თუ არა 10-ზე ნაკლები, თუ ნაკლებია დაბეჭდეთ "Negative and small", სხვა შემთხვევაში "Negative and large"

user=int(input("enter number:"))
if user >0:
    if user % 2 == 0:
        print("positive and even")
else:
    print("positive and odd")

if user <0 :
    if user<10:
        print("negative and small")
    else:
        print("negative and large")

#14) while ციკლის საშვალებით მომხმარებელს შეეკითხეთ რიცხვი ყოველ ჯერზე, თუ რიცხვი კენტია გააგრძელეთ ციკლი (გამოიყენეთ continue), თუ რიცხვი ლუწია დაბეჭდეთ "even number detected" და თუ რიცხვი 0-ის ტოლია შეწყვიტეთ ციკლი (გამოიყენეთ break)
while True:
    num=int(input("what your num:"))
    if num == 0:
        break
    elif num %2 == 0:
        print("even number detected")
    else:
        continue
