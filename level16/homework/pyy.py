#7) შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს, შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით, თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ "The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."


num=int(input("enter your num:"))
if num > 0:


    if num %2==0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")

elif num<0:
    print("the num is negative")
else:
    print("the num is zero")


#8) მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად, საბოლოოდ დაბეჭდეთ ყველა მიღებული დადებითი რიცხვის ჯამი

total=0
user=int(input("enter your number"))
while user >= 0:
    if user >0:
        total+=user
    user = int(input("enter the number: "))

print("positive number sum:",total)