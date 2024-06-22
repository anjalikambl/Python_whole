#variable declaration
age=55   #scripting file
print(age)

age_2=60
print(age_2)

person_age=30
print(person_age)

#statment interpreter never execute comments

#assignment statement
#multiple values assigned to multiple values
phy=78
math,bio,chem=67,89,45
print(math,bio,chem)
#single value assigned to multiple variables
a=b=10
print(a,b)
a=b=c=55
print(a,b,c)

#Keyword
import keyword
print(keyword.kwlist)    #kwlist parameter keyword list
print(len(keyword.kwlist))