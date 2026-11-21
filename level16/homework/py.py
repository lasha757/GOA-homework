#5) მოხმარებელს შემოატანინეთ გამოცდის ქულა და შეინახეთ score ცვლადში ინტეჯერად, თუ ქულა მეტია 70-ზე დაუბეჭდეთ რომ გამოცდა გადალახა "passed" სხვა შემთხვევაში კი რომ ჩაიჭრა "failed"




score=int(input("enter your score:"))
if score >70:
    print("passsed")
else:
    print("failed")





# 5) მომხმარებელს შემოატანინეთ ქულა score და შეინახეთ ცვლადში, როგორც integer.
#    შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (grade):
#    A – თუ score მეტია 80-ზე
#    B – თუ score მეტია 60-ზე
#    C – თუ score მეტია 40-ზე
#    D – თუ score მეტია 20-ზე
#    F – თუ score 20-ზე ნაკლებია

score=int(input("enter your score:"))
if score <80:
    print("A")
elif score <60:
    print("B")
elif score <40:
    print("C")
elif score <20:
    print("D")
else:
    print("F")