#11) მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო
count=0
total=0
user=int(input("enter number:"))
while user !=-1:
    total+= user
    count+=1
    user=int(input("enter number:"))

if count>0:
    print("average:",total/count)
else:
    print("no number entered:")

#12)მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)
volwels_count=0
consonants_count = 0
user1=input("შეიყვამე წინადადება")
for char in user1:
    if char == "a" or char == "e" or char=="i" or char=="o" or char=="u":
        volwels_count +=1
    else:
        consonants_count +=1

print("ხმოვანი",volwels_count)
print("თანხმოვანი",consonants_count)