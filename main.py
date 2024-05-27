'''answer = input("Ange ditt namn: ")
print("hej", answer)'''

########################

'''x = input("Ange ett tal: ")
y = input("Ange ett till tal: ")

result = int(x) + int(y)

print("Summan är:",result)'''

##########################

'''name = input("Ange ditt namn: ")
age = input("Ange din ålder: ")

print(f"Hej {name}, du är {age} år gammal.")'''

#########################

'''def medelvärdet(x,y,z):
    return(x + y + z) / 3 

x = float(input("Ange det första talet: "))
y = float(input("Ange det andra talet: "))
z = float(input("Ange det tredje talet: "))

medelvärde_resultat = medelvärdet(x,y,z)

print("Medelvärdet av dem tre talen är:",medelvärde_resultat)'''

#########################

'''def celcius_till_farenheit(celcius):
    return (celcius * 9/5) + 32

celcius = float(input("Ange temperaturen i celcius: "))

farenheit = celcius_till_farenheit(celcius)

print(f"Temperaturen i farenheit är: {farenheit}.")'''

##########################

'''def farenheit_till_celcius(farenheit):
    return (farenheit - 32) * 5/9

farenheit = float(input("Ange temperaturen i farenheit: "))

celcius = farenheit_till_celcius(farenheit)

print(f"Temperaturen i celcius är: {celcius}")'''


##########################

'''def matskedar_till_teskedar(matskedar):
    return matskedar * 3

matskedar = float(input("Ange antalet matskedar: "))

teskedar = matskedar_till_teskedar(matskedar)

print(f"Det motsvarar {teskedar} teskedar.")'''

##########################

'''for x in range(1,21,1):
    print(x)'''

##########################

'''for x in range(1,21):
    if x % 2 == 0:
        print(x)'''

###########################

'''for x in range(1,21):
    if x % 2 != 0:
        print(x)'''

###########################

'''första_talet = float(input("Ange ett tal: "))
andra_talet = float(input("Ange det andra talet: "))

if första_talet > andra_talet:
    print("Första talet är större. ")
elif första_talet < andra_talet:
    print("Andra talet är större. ")
else:
    print("Dem är lika stora. ")'''

#############################


'''def ar_till_manader(ar):
    return ar * 12

def ar_till_dagar(ar):
    return ar * 365 

def ar_till_sekunder(ar):
    return ar * 365 * 24 * 60 * 60 

alder_ar = int(input("Hur gammal är du (i antal år)? "))


print("Du är", alder_ar, "år gammal.")
print("Det motsvarar", ar_till_manader(alder_ar), "månader.")
print("Det motsvarar", ar_till_dagar(alder_ar), "dagar.")
print("Det motsvarar", ar_till_sekunder(alder_ar), "sekunder.")

print()

if alder_ar >= 30:
    print("True")
else:
    print("False")'''

##################################

'''str = input("Vänligen och skriv en sträng: ")
str1 = input("Vänligen och skriv in en andra sträng: ")

if str == str1:
    print("Strängarna har samma innehåll.")
elif len(str) == len(str1):
    print("Lika långa strängar.")
else: 
    print("Default mode.")'''

##############################

'''count = 1

while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1'''

#############################

'''star = int(input("Ange en siffra: "))

i = 1
while i <= star:
    print("*" * i )
    i += 1'''

##############################

'''start = int(input("Ange en siffra: "))
stop = int(input("Ange den andra siffran: "))

while start <= stop:
    print("*" * start)
    start += 1'''

###############################

'''str = "Hej Amin, hur är det med dig?"

print(str.split())

print()

print("Vartannat ord: ")
for x in range(0,len(str),2):
    print(str[x])


print("Meningen i omvänd ordning:")
for x in reversed(str):
    print(x)'''

##############################

'''siffra1 = int(input("Ange en siffra: "))
siffra2 = int(input("Ange en till siffra: "))

import random

random_resultat = random.randint(siffra1,siffra2)

print(f"Random siffra: {random_resultat}")'''

##############################

'''import random

random_siffra = random.randint(1,10)

for tries in range(3):
    answer = int(input("Ange en siffra mellan 1-10: "))
    if answer == random_siffra:
        print("Grattis, du har vunnit!")
        break
    elif tries == 2:
        print(f"Tyvärr, du har inga försök kvar. Det rätta numret var: {random_siffra}.")
        break'''


##############################

'''list_of_integer = [23,4,35,45,4,6,45,7658,6856,432,414]
print("Skriv ut listan: ", list_of_integer)

totala_summan = sum(list_of_integer)

print(f"Summan av listan är: {totala_summan}")'''

###############################

'''answer = input("Ange ditt namn: ")
print("hej", answer)'''

########################

'''x = input("Ange ett tal: ")
y = input("Ange ett till tal: ")

result = int(x) + int(y)

print("Summan är:",result)'''

##########################

'''name = input("Ange ditt namn: ")
age = input("Ange din ålder: ")

print(f"Hej {name}, du är {age} år gammal.")'''

#########################

'''def medelvärdet(x,y,z):
    return(x + y + z) / 3 

x = float(input("Ange det första talet: "))
y = float(input("Ange det andra talet: "))
z = float(input("Ange det tredje talet: "))

medelvärde_resultat = medelvärdet(x,y,z)

print("Medelvärdet av dem tre talen är:",medelvärde_resultat)'''

#########################

'''def celcius_till_farenheit(celcius):
    return (celcius * 9/5) + 32

celcius = float(input("Ange temperaturen i celcius: "))

farenheit = celcius_till_farenheit(celcius)

print(f"Temperaturen i farenheit är: {farenheit}.")'''

##########################

'''def farenheit_till_celcius(farenheit):
    return (farenheit - 32) * 5/9

farenheit = float(input("Ange temperaturen i farenheit: "))

celcius = farenheit_till_celcius(farenheit)

print(f"Temperaturen i celcius är: {celcius}")'''


##########################

'''def matskedar_till_teskedar(matskedar):
    return matskedar * 3

matskedar = float(input("Ange antalet matskedar: "))

teskedar = matskedar_till_teskedar(matskedar)

print(f"Det motsvarar {teskedar} teskedar.")'''

##########################

'''for x in range(1,21,1):
    print(x)'''

##########################

'''for x in range(1,21):
    if x % 2 == 0:
        print(x)'''

###########################

'''for x in range(1,21):
    if x % 2 != 0:
        print(x)'''

###########################

'''första_talet = float(input("Ange ett tal: "))
andra_talet = float(input("Ange det andra talet: "))

if första_talet > andra_talet:
    print("Första talet är större. ")
elif första_talet < andra_talet:
    print("Andra talet är större. ")
else:
    print("Dem är lika stora. ")'''

#############################


'''def ar_till_manader(ar):
    return ar * 12

def ar_till_dagar(ar):
    return ar * 365 

def ar_till_sekunder(ar):
    return ar * 365 * 24 * 60 * 60 

alder_ar = int(input("Hur gammal är du (i antal år)? "))


print("Du är", alder_ar, "år gammal.")
print("Det motsvarar", ar_till_manader(alder_ar), "månader.")
print("Det motsvarar", ar_till_dagar(alder_ar), "dagar.")
print("Det motsvarar", ar_till_sekunder(alder_ar), "sekunder.")

print()

if alder_ar >= 30:
    print("True")
else:
    print("False")'''

##################################

'''str = input("Vänligen och skriv en sträng: ")
str1 = input("Vänligen och skriv in en andra sträng: ")

if str == str1:
    print("Strängarna har samma innehåll.")
elif len(str) == len(str1):
    print("Lika långa strängar.")
else: 
    print("Default mode.")'''

##############################

'''count = 1

while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1'''

#############################

'''star = int(input("Ange en siffra: "))

i = 1
while i <= star:
    print("*" * i )
    i += 1'''

##############################

'''start = int(input("Ange en siffra: "))
stop = int(input("Ange den andra siffran: "))

while start <= stop:
    print("*" * start)
    start += 1'''

###############################

'''str = "Hej Amin, hur är det med dig?"

print(str.split())

print()

print("Vartannat ord: ")
for x in range(0,len(str),2):
    print(str[x])


print("Meningen i omvänd ordning:")
for x in reversed(str):
    print(x)'''

##############################

'''siffra1 = int(input("Ange en siffra: "))
siffra2 = int(input("Ange en till siffra: "))

import random

random_resultat = random.randint(siffra1,siffra2)

print(f"Random siffra: {random_resultat}")'''

##############################

'''import random

random_siffra = random.randint(1,10)

for tries in range(3):
    answer = int(input("Ange en siffra mellan 1-10: "))
    if answer == random_siffra:
        print("Grattis, du har vunnit!")
        break
    elif tries == 2:
        print(f"Tyvärr, du har inga försök kvar. Det rätta numret var: {random_siffra}.")
        break'''


##############################

'''list_of_integer = [23,4,35,45,4,6,45,7658,6856,432,414]
print("Skriv ut listan: ", list_of_integer)

totala_summan = sum(list_of_integer)

print(f"Summan av listan är: {totala_summan}")'''

###############################


'''answer = input("Ange ditt namn: ")
print("hej", answer)'''

########################

'''x = input("Ange ett tal: ")
y = input("Ange ett till tal: ")

result = int(x) + int(y)

print("Summan är:",result)'''

##########################

'''name = input("Ange ditt namn: ")
age = input("Ange din ålder: ")

print(f"Hej {name}, du är {age} år gammal.")'''

#########################

'''def medelvärdet(x,y,z):
    return(x + y + z) / 3 

x = float(input("Ange det första talet: "))
y = float(input("Ange det andra talet: "))
z = float(input("Ange det tredje talet: "))

medelvärde_resultat = medelvärdet(x,y,z)

print("Medelvärdet av dem tre talen är:",medelvärde_resultat)'''

#########################

'''def celcius_till_farenheit(celcius):
    return (celcius * 9/5) + 32

celcius = float(input("Ange temperaturen i celcius: "))

farenheit = celcius_till_farenheit(celcius)

print(f"Temperaturen i farenheit är: {farenheit}.")'''

##########################

'''def farenheit_till_celcius(farenheit):
    return (farenheit - 32) * 5/9

farenheit = float(input("Ange temperaturen i farenheit: "))

celcius = farenheit_till_celcius(farenheit)

print(f"Temperaturen i celcius är: {celcius}")'''


##########################

'''def matskedar_till_teskedar(matskedar):
    return matskedar * 3

matskedar = float(input("Ange antalet matskedar: "))

teskedar = matskedar_till_teskedar(matskedar)

print(f"Det motsvarar {teskedar} teskedar.")'''

##########################

'''for x in range(1,21,1):
    print(x)'''

##########################

'''for x in range(1,21):
    if x % 2 == 0:
        print(x)'''

###########################

'''for x in range(1,21):
    if x % 2 != 0:
        print(x)'''

###########################

'''första_talet = float(input("Ange ett tal: "))
andra_talet = float(input("Ange det andra talet: "))

if första_talet > andra_talet:
    print("Första talet är större. ")
elif första_talet < andra_talet:
    print("Andra talet är större. ")
else:
    print("Dem är lika stora. ")'''

#############################


'''def ar_till_manader(ar):
    return ar * 12

def ar_till_dagar(ar):
    return ar * 365 

def ar_till_sekunder(ar):
    return ar * 365 * 24 * 60 * 60 

alder_ar = int(input("Hur gammal är du (i antal år)? "))


print("Du är", alder_ar, "år gammal.")
print("Det motsvarar", ar_till_manader(alder_ar), "månader.")
print("Det motsvarar", ar_till_dagar(alder_ar), "dagar.")
print("Det motsvarar", ar_till_sekunder(alder_ar), "sekunder.")

print()

if alder_ar >= 30:
    print("True")
else:
    print("False")'''

##################################

'''str = input("Vänligen och skriv en sträng: ")
str1 = input("Vänligen och skriv in en andra sträng: ")

if str == str1:
    print("Strängarna har samma innehåll.")
elif len(str) == len(str1):
    print("Lika långa strängar.")
else: 
    print("Default mode.")'''

##############################

'''count = 1

while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1'''

#############################

'''star = int(input("Ange en siffra: "))

i = 1
while i <= star:
    print("*" * i )
    i += 1'''

##############################

'''start = int(input("Ange en siffra: "))
stop = int(input("Ange den andra siffran: "))

while start <= stop:
    print("*" * start)
    start += 1'''

###############################

'''str = "Hej Amin, hur är det med dig?"

print(str.split())

print()

print("Vartannat ord: ")
for x in range(0,len(str),2):
    print(str[x])


print("Meningen i omvänd ordning:")
for x in reversed(str):
    print(x)'''

##############################

'''siffra1 = int(input("Ange en siffra: "))
siffra2 = int(input("Ange en till siffra: "))

import random

random_resultat = random.randint(siffra1,siffra2)

print(f"Random siffra: {random_resultat}")'''

##############################

'''import random

random_siffra = random.randint(1,10)

for tries in range(3):
    answer = int(input("Ange en siffra mellan 1-10: "))
    if answer == random_siffra:
        print("Grattis, du har vunnit!")
        break
    elif tries == 2:
        print(f"Tyvärr, du har inga försök kvar. Det rätta numret var: {random_siffra}.")
        break'''


##############################

'''list_of_integer = [23,4,35,45,4,6,45,7658,6856,432,414]
print("Skriv ut listan: ", list_of_integer)

totala_summan = sum(list_of_integer)

print(f"Summan av listan är: {totala_summan}")'''

###############################
'''from functools import reduce


list_of_integer = [23,4,35,45,4,6,45,7658,6856,432,414]

print("Skriv ut listan: ",list_of_integer)
print()

produkt = reduce(lambda x, y: x * y, list_of_integer)

print("Produkten av alla tal i listan är:", produkt)'''

###############################

'''list_of_integer = [23,4,35,45,4,6,45,7658,6856,432,414]

biggest_number = list_of_integer[0]

for i in list_of_integer:
    if i > biggest_number:
        biggest_number = i

    
print(f"Det största siffran i listan är: {biggest_number}")'''

################################

'''import math

def area(radius):
    return math.pi * radius ** 2

print(area(1.1))'''

#################################

'''import random

def play():
    random_number = random.randint(1, 10)
    for attempt in range(3):
        guess = int(input("Gissa ett nummer mellan 1 och 10: "))
        if guess == random_number:
            print("Grattis! Du gissade rätt!")
            break
        else:
            print("Fel! Försök igen.")
    else:
        print(f"Tyvärr, du har inga försök kvar. Det rätta numret var {random_number}.")

    
def start_game():
    while True:
        command = input('Skriv "play" för att starta spelet: ')
        if command.lower() == "play":
            play()
            break 
        else:
            print("Ogiltigt kommando, försök igen.")

start_game()'''

####################################

'''class Dog:
    def __init__(self, name, age, race, sound):
        self.name = name
        self.age = age
        self.race = race
        self.sound = sound

    def bark(self):
        return f"The sound of the dog {self.name} is: {self.sound}"

    def age_in_dog_years(self):
        dog_years_age = self.age * 7
        return dog_years_age
        
    def print_info(self):
        dog_info = f"The dog's name is {self.name} and is {self.age} years old. The dog is a {self.race} and loves to bark... {self.bark()}"
        print(dog_info)

    @staticmethod
    def add(a, b):
        return a + b


mydog = Dog("Zizou", 10, "Labrador", "Vooooooffff")

mydog.print_info()

print((mydog.age_in_dog_years()))'''

######################################

'''class Employee:
    def __init__(self, name, email, phonenumber, salary, year_born):
        self.name = name
        self.email = email
        self.phonenumber = phonenumber
        self.salary = salary
        self.year_born = year_born

    def salary_after_taxes(self):
        base_tax = self.salary * 0.30

        extra_tax = 0
        if self.salary > 46200:
            extra_tax = (self.salary - 46200) * 0.20

        total_tax = base_tax + extra_tax 
        return self.salary - total_tax

    def print_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Phone Number: {self.phonenumber}, Salary after Taxes: ${self.salary_after_taxes()}, Birth Year: {self.year_born}")
    
employe1 = Employee("Amin", "Aminnazari040@hotmail.com", "0736123253", 500000, 1993)

salary_after = employe1.salary_after_taxes()

print(f"Lönen efter skatten: {salary_after}")

print()

print(employe1.print_info())'''

########################################

#print(help("modules"))

'''import func

resultat = func.add(10,1)

print(resultat)'''

######################################

'''def sum_of_multiples(limit):
    total = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

result = sum_of_multiples(100)
print("Summan av alla multipler av 3 och 5 under 1000 är:", result)'''

#####################################

'''def remove_duplicates(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

list1 = [3, 1, 2, 2, 1, 4]
list2 = [5, 'röda', 'elefanter', 2, 'blå', 'elefanter', 2, 'gul']

print(remove_duplicates(list1))
print(remove_duplicates(list2))'''

######################################

'''print(help("modules"))

import func'''

#####################################

'''def nth_prime(n):
    counter = 2
    for i in range(3, n**2, 2):
        k = 1
        while k*k < i:
            k += 2
            if i % k == 0:
               break
            else:
                counter += 1
        if counter == n:
            return i

print(nth_prime(10001))'''

######################################

'''f = open("demofile.txt")

print(f.read())

from func import dog

my_dog = dog("zizou", 31, "Labrador", "Vooooooffff")

print(my_dog.get_name())'''

#####################################

'''try:
    print(x)
except:
    print("No variabel is deklared...")'''

####################################

'''def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)'''

#####################################

'''def largest_prime_factor(n): 
	
	largest_prime = -1
	i = 2
	while i * i <= n: 
		while n % i == 0: 
			largest_prime = i 
			n = n // i 
		i = i + 1
	if n > 1: 
		largest_prime = n 
	return largest_prime 

n = 13195
print(largest_prime_factor(n)) 

n = 600851475143
print(largest_prime_factor(n))'''

#####################################

'''import random

for i in range(2,11,2):
    print(i)

str = "Hello zizou"

print("Hello" not in str)

a = str.isupper()

print(a)

for i in range(0,11,3):
    print(i)'''

####################################

'''i = 1

while i < 11:
    print(i)
    i += 1

str1 = input(str("Skriv något: "))
str2 = input(str("Skriv något annat: "))

if str1 == str2:
    print("Samma")
elif len(str1) == len(str2):
    print("Lika långa")
else: 
    print("Default..")'''


####################################

'''try:    
    num = int(input("ange en siffra: "))
    print(num)
except: 
    print("Not a integer... ")'''

####################################

'''str1 = "Hej alex. hur är det med dig idag?"

str1 = str1.split()

print(str1)'''

######################################

'''def user_input(int_check):
    int_check = False
    while int_check == False:
        answer = input("skriv ett tal: ")
        if answer.isdigit() == False:
            print("Du skrev inte in en siffra.")
        else:
            int_check = True

    
user_input(False)'''

######################################
'''try: 
    a = int(input("Ange en siffra: "))

    if a < 10:
        print("Användarens svar är mindre än 10")
    elif a > 10:
        print("Användarens svar är större än 10")
    else:
        print("Svaret är 10.")
except ValueError:
    print("Du skrev inte in en siffra. ")'''

######################################
'''str1 = "Hej på dig"
 
for i in range(0,len(str1),1):
    print(str1[i])

print()

for i in str1:
    print(i)

print()

for letter in str1:
    print(letter + " - ")'''

#####################################

'''str1 = "Hello"
str2 = "Hello"

print(str1 == str2)

print(len(str1) == len(str2))'''

####################################

'''row  = 0
while row < 5:
    num_stars = row + 1
    print("*" * num_stars)
    row += 1'''

####################################
'''j = 0
run = True
while run:
    j = j + 1
    print("While loop " + str(j))

    if(j < 10):
        run = False'''

####################################

'''row  = 2
while row < 5:
    num_stars = row + 1
    print("*" * num_stars)
    row += 1'''

####################################

'''color = ["red" , "apple" , "orange" , "banana"]

print(color[0])

print()

for i in color:
    print(i)

for i in range(len(color)):
    print(i)

print()

for i in (0,10):
    if i >= 4:
        print("Hej")
    elif i > 0:
        print("Hej då")


count = 1
while count < 11:
    if count == 4:
        count += 1
        continue
    print(count)
    count += 1'''

####################################

'''def user_input(int_check):
    int_check = False
    while int_check == False:
        answer = input("Skriv en siffra: ")
        if answer.isdigit()  == False:
            print("Du skrev inte in en siffra...")
        else:
            int_check == True


def user_input(int_check):
    int_check = False
    while int_check == False:
        answer = input("skriv ett tal: ")
        if answer.isdigit() == False:
            print("Du skrev inte in en siffra.")
        else:
            int_check = True
            


user_input(False)
'''

##################################

'''my_list = [1,2,3,4,5,6,7,8,9,10]
my_other_list = [11,12,13,14,15,16,17,18,19,20]

print(my_list + my_other_list)

print()

combined_list = my_list + my_other_list

for i in range(len(combined_list)):
    print(combined_list[i])'''


##################################

'''n = 5

# Upper half of the butterfly
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# Lower half of the butterfly
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    for j in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()'''


######################################

'''for i in range(5):
    for j in range(5):
        print("*", end="")
    print("")'''

#####################################

'''count = 0

while count < 10:
    if count != 4:
        print("hello")
    elif count > 3:
        print("Nooooo")
    count += 1'''


####################################

'''with open("demofile.txt") as file:
    file = file.read()
    print(file)

print(file)'''

###################################

'''user_input = int(input("Skriv in en siffra: "))
user_input1 = int(input("Skriv in en annan siffra: "))

for i in range(user_input, user_input1 + 1):
    print("*" * i)'''

##################################

'''class student():
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = float(grade)

    
        def get_name():
            return name
        
        def get_age():
            return age
        
        def get_grade():
            return grade
    

student1 = student("Passi", 25, 3.2)
student2 = student("Amin", 31, 9.2)

print(student1.name ,"have" , student1.grade, "grade")
print(student2.name ,"have" , student2.grade, "grade")'''

###################################

'''my_tuple = ("orange", "apple", "banana")
my_list = list(my_tuple)

my_list.append("yellow")

my_list = tuple(my_list)

print(type(my_list))

print(my_list)'''

######################################

'''import random

my_tuple = ("banana", "orange", "apple")

my_tuple2 = (1,2,3,4,5,6)

two_tuple = my_tuple + my_tuple2

print(two_tuple)

print(random.randint(0,23))'''

######################################

'''def name(a):
    return print("name is:",a)

name("Amin")

def add(a,b):
    product = a + b
    return product


print(add(4,5))'''

####################################

'''def func(*args):
    for arg in args:
        print(arg)
    return "Value", "value2"



func(3,4,23,13,4,1,4)'''

#####################################
'''import random

def numbergame():
    number = random.randint(0,13)
    attemps = 0 

    print("GISSA NUMRET")
    print("Gissa ett nummer mellan 0-13")

    while True:
        guess = int(input("Skriv din gissning: "))
        attemps += 1

        if guess < number:
            print("För lågt.")
        elif guess > number:
            print("För högt")
        else: 
            print(f"Grattis. Det tog dig {attemps} gissningar att gissa rätt.")



numbergame()'''

###################################


'''def func(**kwargs):
    for i in kwargs.values():
        print(i)



func(a = "hello" , b = "Hej då", c = "Shake")'''


###################################

'''my_list = [1,2,3,2,33,432,342,123,4,5,6,7,8,9,10]

for i in my_list:
    print(i, end=" ")

print()

my_list.sort()

print(my_list)

print()

str1 = "hej på dig hur är det med dig"

str1 = str1.split()

print(str1)'''

###################################

'''from func import dog

dog1 = dog("zizou", 31, "Labrador", "voff voff")

print(dog1.get_name())'''

##################################

'''def sum_of_multiples(limit):
    total_sum = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum

# Anropa funktionen med 1000 som argument
result = sum_of_multiples(1000)
print("Summan av alla multipler av 3 och 5 under 1000 är:", result)'''

######################################

'''print("Hello world... this will always run...")

import random

def numbergame():
    number = random.randint(0,13)
    attemps = 0 

    print("GISSA NUMRET")
    print("Gissa ett nummer mellan 0-13")

    while True:
        guess = int(input("Skriv din gissning: "))
        attemps += 1

        if guess < number:
            print("För lågt.")
        elif guess > number:
            print("För högt")
        else: 
            print(f"Grattis. Det tog dig {attemps} gissningar att gissa rätt.")


if __name__ == "__main__":

    numbergame()'''


##########################################

'''def multiply(a, b):
    
    This function takes two arguments, `a` and `b`, and multiplies them together.
    It returns the product of the two arguments.
    
    Parameters:
        a (int or float): The first number to be multiplied.
        b (int or float): The second number to be multiplied.
    
    Returns:
        int or float: The product of `a` and `b`.
    
    return a * b'''

#############################################

'''def loop_with_jump():

    for i in range(1, 101, 3):
        print(i)


loop_with_jump()'''

############################################
'''class Student:
    def __init__(self, name, age, grade):
         self.name = name
         self.age = age
         self.grade = float(grade)

    def get_grade(self):
        return self.grade
    
    def set_grade(self, new_grade):
        self.grade = new_grade

    def __str__(self):
        return f"{self.name} is {self.age} years old and has a grade of {self.grade}"


student = Student("Amin", 22, 4.0)


print(student)'''

###########################################

'''def are_strings_equal_length(string1, string2):
    return len(string1) == len(string2)


print(are_strings_equal_length("hello", "world"))'''

##########################################

'''from func import cat

def main():
    cat1 = cat("Zizou", 31, "Persian cat", "meow meow")

if __name__ == "__main__":'''


######################################

# Skapa en set från en lista
'''my_set = set([1, 2, 3, 2, 1,3,4,6,8,8,90,3,2,3,45,6,7,8,3,4,5])
print(my_set)  # Output: {1, 2, 3}
print(type(my_set))

print()

my_dict = {"Name": "Zizou", "Age": 31, "City": "Malmö"}
print(my_dict)
print(type(my_dict))'''

######################################

'''def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

# Testa funktionen med exempel från uppgiften
list1 = [3, 1, 2, 2, 1, 4]
list2 = [5, 'röda', 'elefanter', 2, 'blå', 'elefanter', 2, 'gul']

# Anropa funktionen och skriv ut resultatet
print(remove_duplicates(list1))  # Output: [3, 1, 2, 4]
print(remove_duplicates(list2))'''  # Output: [5, 'röda', 'elefanter', 2, 'blå', 'gul']

########################################

'''import pprint

data = {
    'name': 'John Doe',
    'age': 30,
    'children': [
        {'name': 'Jane Doe', 'age': 10},
        {'name': 'Doe John', 'age': 8}
    ],
    'pets': {'dog': 'Fido', 'cat': 'Whiskers'}
}

# Använda pprint för att skriva ut datastrukturen på ett snyggt sätt
pprint.pprint(data)'''

##################################

'''file = open("demofile.txt")

print(file.read())
file.close()'''

#################################

'''def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a+b

for index, number in enumerate(fibonacci()):
    if len(str(number)) == 1000:
        print(index)
        break


fibonacci()'''

###############################

'''def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print("Listan innehåller:" , lista)
    
    while True:
        try:
            index = int(input("Ange en index för att hämta ett element från listan: "))
            print(f"Elementet på index {index} är: {lista[index]}")
            break
        except IndexError:
            print("Fel: Indexet bör vara mindre och inte negativt än listans längd.")
        except ValueError:
            print("Fel: Ange en giltig heltal.")
        
if __name__ == "__main__":
    main()'''


################################

'''my_list  = [1,2,3,4,5,6]
new_list = my_list[1:-2]

print(new_list)'''

################################

'''a = 0
b = 1

sum = 0

while True:
    a,b = b, a + b
    
    if b >= 4000000:
        break

    if b % 2 == 0:
        sum += b


print(sum)'''

#############################

'''import sys

def summa_av_argument():

    argument = map(int,sys.argv[1:])

    total_summa = sum(argument)

    print("Summan är:", total_summa)


if __name__ == "__main__":
    summa_av_argument()'''


##############################
'''import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])'''

#################################

'''def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print("Elementen i listan är: ", lista)

    while True:
        try:
            index = int(input("Ange en index för att hämta ett element från listan: "))
            print(f"Elementet på index {index} är: {lista[index]}")
            break
        except IndexError:
            print("Fel: Indexet bör vara mindre och inte negativt än listans längd.")
        except ValueError:
            print("Fel: Ange en giltig heltal. ")

if __name__ == "__main__":
    main()'''

##############################

'''from func import dog

dog1 = dog("zizou", 31,"Pitbull" , "voff voff")

print(dog1.get_name())'''

#############################

'''import sys

file = open(sys.argv[1])
lines = file.readlines()

print("Antal rader: ", len(lines))'''

#############################

'''resultat = 2 ** 1000

resultat_str = str(resultat)

summa_siffror = sum(int(siffra) for siffra in resultat_str)

print("Summa av 2^1000 är: ", summa_siffror)'''

##############################

'''print(sum([2,3]))

sum1 = sum([3,4])

print(sum1)'''

###############################

from functions import *

sum1 = add(2,4)

print(sum1)