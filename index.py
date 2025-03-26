#print("hello world")


#age=27
#print (age)
#list
#languages = ["python","html","css", True]
#print (languages)
#print (languages[2])
#print(languages[-1])
#week 2 tupples
#car = ("toyota", "ford", "bmw")
#print(car)
#print(car[2])
#week 2 dictionary stores values in a key element value
capital_cities ={
    "kenya":"nairobi",
    "uganda":"kampala",
    "tanzania":"dodoma"
}
print(capital_cities)
print(capital_cities["uganda"])
#sets collection of unique data dont duplicate items on set
employee_ids = {1,2,5,8,}
print (employee_ids)

marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
 print("invalid marks")
if marks <= 20:
 print("grade =E")
elif marks <= 40:
 print("grade =D")
elif marks <= 60:
 print("grade =C")
elif marks <= 80:
 print("grade =B")
else:
 print("grade =A")
