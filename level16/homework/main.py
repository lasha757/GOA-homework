#2) for ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე, შეამოწმეთ თითოეული რიცხვი ლუწია თუ კენტი, თუ ლუწია დაბეჭდეთ "even" თუ კენტია დაბეჭდეთ odd და გვერდზე მიუწერეთ ეს რიცხვი თითოეულ შემთხვევაში


#for

for i in range(0,20):
    if i %2 ==0:
        print("even", i)
    else: 
        print("odd", i)

#while

num=0
while num <20 :
    if num %2 ==0:
        print("even", num)
    else:
        print("odd", num)
    num += 1


#4) მომხმარებელს შემოატანინეთ სახელი და თუ ის თქვენს სახელს ემთხვევა დაბეჭდეთ "coincidence"

name="lasha"
user_name=input("enter your name:")

while user_name != name:
    print("name is incorrect")
    user_name = input("next name:")
print("coincidence")