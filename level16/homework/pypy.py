#9) შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები


even_count=0
odd_count=0
num=int(input("enter your number"))
while num>= 0:
    if num%2  ==0:
        even_count+=1
    else:
        odd_count+=1
    num = int(input("enter your number: "))

print("count of even num:", even_count)
print("count of odd num:", odd_count)


#10) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები



pin = "goa_is_best_1212"
attempts = 1
max_attempts = 3

enter = input("enter pin: ")
while enter != pin and attempts < max_attempts:
    print("pin is incorrect")
    attempts+=1
    enter=input("enter pin:")
if enter == pin:
    print("Access Granted")
else:
    print("Access Denied")