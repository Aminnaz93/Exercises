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

'''from functions import *

sum1 = add(2,4)

print(sum1)

sum2 = sum([3,4])

print(sum2)'''

#################################

'''import math

faktoriell_siffra_summa = str(math.factorial(100))

print("Produkten av den faktoriella siffran 100: ",faktoriell_siffra_summa)

print()

summa_siffra = sum(int(siffra) for siffra in faktoriell_siffra_summa)

print(summa_siffra)'''

##################################

'''for num in range(1,101):
    string = ""
    if num % 3 == 0:
        string = string + "Fizz"
    if num % 4 == 0:
        string = string + "Whoops"
    if num % 5 == 0:
        string = string + "Buzz"
    if num % 7 == 0:
        string = string + "Max"
    if string == "":
        string = string + str(num)
    print(string)'''
    
##################################

'''file = open("demofile.txt", "w")

file.write("Detta är en ny rad med text")

file.close()'''

##################################

'''file = open("demofile.txt")

print(file.read())'''

##################################

'''print("Detta kommer alltid att köras.")

def Hello():
    print("första modulen")


if __name__ == "__main__":
    Hello()
else: 
    print("Från andra modulen")'''

#################################

'''class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def getName(self):
        return self.name
    
    def getDesctription(self):
        return self.description



class Weapon(Item):
    def __init__(self, name, description, damage):
        Item.__init__(self, name, description)
        self.damage = damage

    def getDamage(self):
        return self.damage

    

bottle = Item("Bottle", "A bottle with blue fluid")
sword = Weapon("Sword", " A wooden sword", 10)

print(sword.getName() + sword.getDesctription())
print("Damage:", sword.getDamage())

print(bottle.getName(), bottle.getDesctription())'''


#################################

'''my_list = [1,2,3,4,5,6,7,8,9,10]
my_str = "Hej hur är det med dig idag."


print(my_list)
print(*my_list)

print()

print(my_str)
print(*my_str)

def summera(*args):
    total = 0
    for num in args:
        total += num
    return total
    
print(summera(1,2,3))

def dic(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

dic(namn = "Amin", ålder = 31)'''

##################################
'''import pprint


my_dict = {'name': 'Andreas', 'age': 37, 'email': 'andreas.nilssonstrom@kyh.se'}

print(my_dict)
print()

pprint.pprint(my_dict)
print()
pprint.pprint(my_dict, width=1)'''


###################################

'''def walk(step):
    if step == 0:
        return 
    walk(step - 1)
    print(step)


walk(3)'''

###################################

'''file = open("Hello.txt", "x")  # Skapa en ny fil med namnet "Hello.txt"
file.close()  # Stäng filen

# Öppna filen igen i läget "w" (för att skriva till filen)
file = open("Hello.txt", "w")
file.write("Hello, how are you today?")  # Skriv texten till filen
file.close()  # Stäng filen när du är klar med att skriva

# Öppna filen för läsning
file = open("Hello.txt", "r")
print(file.read())  # Läs och skriv ut innehållet i filen
file.close()'''  # Stäng filen när du är klar med att läsa

##################################


'''file = open("Hello.txt", "r")
print(file.read())'''

##################################

'''import sys

def summa_av_argument():

    argument = map(int,sys.argv[1:])

    total_summa = sum(argument)

    print("Summan är:", total_summa)


if __name__ == "__main__":
    summa_av_argument()'''


#################################

'''import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["city"])'''

##################################

'''def take_away_4_in_loops():
    for i in range(1,21):
        if i == 4 or i == 1:
            continue
        print(i)


take_away_4_in_loops()'''

##################################

'''file = open("demofile.txt")

content = file.read()

print(len(content))

print(type(content))'''

#################################

'''total = 0

for num in range(1,1001):
    total += pow(1,1)

total = total % 10**10

print(total)'''

##################################
 
'''import math

resultat = 2520

for i in range(1,21):
    resultat = resultat * i // math.gcd(resultat, i)

    print(resultat)'''


##################################

'''import time 

counter = 0

print(counter)

counter = counter + 1

time.sleep(1)'''

#################################


'''my_list = [1,2,3,4,5]
my_str = ["hello", "hajbajs"]

for x in my_str:
    my_list.append(x)

print(my_list)'''

##################################

'''my_tuple = (2,3,4532,54,352,4)

my_tuple2 = ("HELOO", "JDKLJA", "nfdjlks")

my_tuple3 = my_tuple + my_tuple2

print(my_tuple3)

print()

my_set = {1,2,3,4,5,5,5,5,5}

print(my_set)
print(type(my_set))'''

###############################

'''my_dict = {"Name" : "Amin", "Age" : 31}

for x,y in my_dict.items():
    print(x,y)'''

###############################

'''count = 0

while count < 10:
    count += 1
    if count == 3:
        continue
    elif count == 6:
        break
    print(count)'''
   
##############################

'''def my_function(n):
    return n

cars = ["Mercedes", "Toyota", "Rolls Royce"]

print(cars[2])

x = cars[0]

print(x)

print()

cars.append("BMW")
index_list = cars.index("BMW")

print(index_list)

for i in range(len(cars)):
    print(cars[i])'''

##############################

'''while True:
    answer = int(input("Ge mig ett tal mellan 1-5:"))

    if answer != 4 and answer < 2:
        print("Du har tryckt in 1.")
    elif answer > 3:
        print("Du har tryckt en siffra större än 3.")
    else: 
        print("Tryck vad du vill.")
        break'''

##########################

'''import platform


x = platform.system()

print(x)

y = dir(platform)

print(y)'''

############################

'''import datetime

x = datetime.datetime.now()

print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.second)'''

############################

'''try:
    print(x)
except:
    print("Detta skrivs ut eftersom x är inte definierad. ")
'''

############################

'''file = open("demofile.txt", "w")

file.write("Hej på dig. allt bra med dig ?")

file = open("demofile.txt", "r")

print(file.read())

file.close()'''

############################

'''file = open("demofile.txt", "a")

file.write("\nNu finns det en ny rad med text.")
file.close()

file = open("demofile.txt" , "r")

print(file.read())'''

#############################

'''my_list = [1,2,3,4,5,6,7,8,9,10]

my_list.reverse()

for i in my_list:
    print(i)'''

###########################

'''def nummer_till_tal(n):
    num_to_19 = {1: "one", 2: "two",3: "three", 4: "four",5: "five",6: "six",7: "seven",8: "eight",9: "nine",10: "ten",11: "eleven",12: "twelve",13: "thirteen",14: "fourteen",15: "fifthteen",16: "sixteen",17: "seventeen",18: "eighteen",19: "nineteen"}
    twenty_to_hundred = {20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    hundred_to_ninehundred = {100: "hundred", 200: "twohundred", 300: "threehundred", 400: "fourhundred", 500: "fivehundred", 600: "sixhundred", 700: "sevenhundred", 800: "eighthundred", 900: "ninehundred"}
    thousand = {1000: "thousand"}


    
def ord(n):
    if n < 20:
       return #någonting
    elif n < 100:
       return #någonting
    elif n < 1000:
       return  #någonting
    elif n == 1000:
        return''' #någonting

'''def number_to_words():
    num_to_19 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                 "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "onehundred", "twohundred", "threehundred", "fourhundred", "fivehundred",
                "sixhundred", "sevenhundred", "eighthundred", "ninehundred"]
    
    def words(n):
        if n < 20:
            return num_to_19[n]
        elif n < 100:
            return tens[n // 10] + (num_to_19[n % 10] if n % 10 != 0 else "")
        elif n < 1000:
            return hundreds[n // 100] + ("and" + words(n % 100) if n % 100 != 0 else "")
        elif n == 1000:
            return "onethousand"
        return ""

    # Räknar bokstäverna för talen från 1 till 1000
    return sum(len(words(i).replace(" ", "")) for i in range(1, 1001))

# Anropa funktionen och skriv ut resultatet
print(number_to_words())'''

############################


'''import datetime

x = datetime.datetime.now()

print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.second)'''

############################


'''sentence = input("Write something: ")

words = sentence.split()

for i,word in enumerate(sentence.split()):
    if not i % 2 == 0:
        print(word[::-1], end= " ")
    else:
        print(word)'''

##############################

'''Start

1. Fråga användaren vilken operation de vill utföra (t.ex. addition, subtraktion, multiplikation, division)
2. Läs in två tal från användaren (num1 och num2)
3. Utför den valda operationen på num1 och num2
4. Skriv ut resultatet
5. Fråga användaren om de vill fortsätta att använda räknaren
   a. Om ja, gå till steg 1
   b. Annars, avsluta programmet

Slut'''


'''def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Error"
    else:
        return a / b


while True:
    print("Välj operation:")
    print("1. Addition")
    print("2. Subtraktion")
    print("3. Multiplikation")
    print("4. Division")
    print("5. Avsluta")

    choice = input("Ange ditt val mellan 1-5: ")

    if choice in ("1", "2", "3", "4", "5"):
        if choice == '5':
            print("Avslutar programmet.")
            break

        num1 = int(input("Ange första talet: "))
        num2 = int(input("Ange det andra talet: "))
        if choice == '1':
            print("Resultat: ", add(num1,num2))
        elif choice == '2':
            print("Resultat:", sub(num1, num2))
        elif choice == '3':
            print("Resultat:", mult(num1, num2))
        elif choice == '4':
            print("Resultat:", div(num1, num2))
    else:
        print("Ogiltigt val.")'''

###############################

'''1. Funktion SummaAvJämnaTal(lista):
2.     skapa en variabel summa och sätt den till 0
3.     för varje tal i listan:
4.         om talet är jämnt:
5.             lägg till talet till summa
6.     returnera summa
7. Slut på funktion'''


'''def SummaAvJämnaTal(lista):
    summa = 0
    for tal in lista:
        if tal % 2 == 0:  # Kolla om talet är jämnt
            summa += tal   # Lägg till talet till summan
    return summa


tal_lista = [2,2,2]

resultat = SummaAvJämnaTal(tal_lista)

print("Resultatet av listan är: ", resultat)'''


###############################

'''import tkinter as tk

def click():
    global counter
    try:
        num = int(txt.get())  # Get the string from Entry and convert to int
        if num > 0:
            counter += num  # Increase counter by the specified number of clicks
            lbl.configure(text=f"Someone just clicked the button {counter} times")
        else:
            lbl.configure(text="Invalid input. Enter a positive integer.")
    except ValueError:
        lbl.configure(text="Invalid input. Enter a valid integer.")

root = tk.Tk()
root.title("Our first GUI")
root.geometry("800x600")

# Label widget with grid layout
lbl = tk.Label(root, text="Hello World")
lbl.grid(column=0, row=0)

counter = 0

# Button widget with command assigned
btn = tk.Button(root, text="Change text", foreground="Green", command=click)
btn.grid(column=0, row=1)

# Entry widget for user input
txt = tk.Entry(root)
txt.grid(column=1, row=1)

root.mainloop()'''


################################

'''import requests

respons = requests.get("https://api.sr.se/api/v2/channels/'")

print(respons.status_code)
print(respons.text)'''

###############################

'''print("Welcome to the Quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play: ")
score = 0


answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect") 

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect") 

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect") 

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect") 

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100)  + "% ")'''

#################################

'''import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()
else:
    print("Please type a number next time. ")
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)     
    else:
        print("Please type a number next time. ")
        continue

    if user_guess == random_number:
        print("You got it! ")
        break
    elif user_guess > random_number:
        print("You were above the number! ")
    else: 
        print("You were below the number! ")


print("You got it in", guesses, "guesses.")'''
    
######################################

'''import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2) #Rock: 0, paper: 1, scissor: 2
    
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_wins += 1
      
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        
    elif user_input == "scissor" and computer_pick == "paper": 
        print("You won!")
        user_wins += 1
    
    else: 
        print("You lost!")
        computer_wins += 1
    

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye")'''


###################################

'''x = 10

y = 100

if x < y:
    print("we are here now")
elif y < x:
    print("The second one now")
else:
    print("fuck u")'''


##################################

name = input("Type your name: ")
print("Welcome", name, "to this adventure!")
print()

while True:
    answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

    if answer == "left":
        print()
        answer = input("You come to a river, you can walk around it or swim across? Type 'walk' to walk and 'swim' to swim across: ").lower()
        
        if answer == "swim":
            print("You swam across and were eaten by an alligator. You lose.")
            break
        
        elif answer == "walk":
            print("You walked for many miles, ran out of water and you lost the game.")
            break
        
        else:
            print("Not a valid option. Please enter 'walk' or 'swim'.")
            continue

    elif answer == "right":
        print()
        answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/back) ").lower()

        if answer == "back":
            print("You go back and lose.")
            break

        elif answer == "cross":
            answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no) ").lower()

            if answer == "yes":
                print("You talk to the stranger and they give you gold. You WIN!")
                break

            elif answer == "no":
                print("You ignore the stranger and they are offended and you lose.")
                break

            else:
                print("Not a valid option. Please enter 'yes' or 'no'.")
                continue

        else:
            print("Not a valid option. Please enter 'cross' or 'back'.")
            continue

    else:
        print("Not a valid option. Please enter 'left' or 'right'.")
        continue

print("Thank you for playing", name)
