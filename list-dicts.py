# here is a list of students
students = ["Kathryn" , "Wyatt" , "Andrew"]

for i in range(len(students)):
    print(students[i])

students1 = {"Kathryn" : "Female" , "Wyatt" : "Male" , "Andrew" : "Male"}

# I'm going to look up the gender for Kathryn
for i in students1:
    print(i , students1[i])


# Creating a dict with name gender, and age
students2 = [
    {"name" : "Kathryn", "gender" : "Female", "age" : 19},
    {"name" : "Wyatt", "gender" : "Male", "age" : 20},
    {"name" : "Andrew", "gender" : "Male", "age" : 19}
]

for i in range(len(students2)):
    print(students2[i]["name"] , students2[i]["gender"] , students2[i]["age"])