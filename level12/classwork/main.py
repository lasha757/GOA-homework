#) 1 ლოგიური ოპერატორების ყველა მაგალითი დაწერე პითონში, ესეიგი  not operator-ზე 2 მაგალითი, ხოლო or და and ოპერატორებზე 4 მაგალითი. დაბეჭდეთ თითოეულის შედეგი ყველა მაგლითში უნდა იყოს სხვდასხვა კომბინაცია true და false მნიშვნელობების. გვერდზე კომენტარის სახით მიუწერეთ პასუხი


#or
#print(True or False)
#print(False or True)
#print(True or True)
#print(False or False)

#and
#print(True and False)
#print(False and True)
#print(False and False)
#print(True and True)

#not
#print(not False)
#print(not True)


#2)for ციკლის მეშვეობით გამოიტანეთ შემდეგი დიაპაზონების რიცხვები:
#20-დან 40-მდე
#15-იდან 60-მდე ყოველი მეორე
#10-იდან 20-ის ჩათვლით


for num in range(20,40):
    print=(num)
for num2 in range(15,40,2):
    print(num2)
for num3 in range(10,20):
    print(num3)

#extra: for ციკლით შეკრიებთ კენტი რიცხვები 30-იდან 40-მდე
for num4 in range(30,40,2):
    print(num4)