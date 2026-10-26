#დაწერეთ პითონის კოდი რომელიც მომხმარებელს input-ის საშვალებით შეეკითხება და ცვლადში შეინახავს შემდეგ ინფორმაციას:

#Name
#Surname
#age
#location
#Occupation
#Hobby

#ამ ცვლადების საშვალებით კი გამოიტანს ერთ წინადადებას რომელშიც ყველა მიღებული ინფორმაცია იქნება გამოყენებული. 

#მაგალითად:

#Enter your name: Alex  
#Enter your surname: Johnson  
#Enter your age: 25  
#Enter your location: New York  
#Enter your occupation: Engineer  
#Enter your hobby: Playing guitar  

#Alex Johnson is 25 years old, lives in New York, works as an Engineer, and enjoys Playing guitar.


name= input("Enter your name : " )
surname= input("Enter your surname : " )
age= input("Enter your age: " )
location= input("Enter your location : " )
occupation= input("Enter your occupation : " )
hobby= input("Enter your hobby : " )

print( name + " " + surname + " " + (" is ") + age + (" years old ") +  " "  + (" he lives in  , ")  +  "  " +  location   + "  " + (" works as an ") +"  " + occupation + "  " + (" his hobby is ") +hobby   )