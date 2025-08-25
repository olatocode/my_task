#Task 4
# Student Record
#  create an empty dictionary called student
student= {}
name= input("kindly enter your name:")
age= int(input("kindly enter your age;"))
student.update({"Name": {name}})
student.update({"AGE": {age}})
# Add a list of score to the dictionary
student["score"]= list( 60, 65, 70, 77, 80)
print(student)
ave_score= sum(student["score"])/len(student["scorce"])
student["passed"] = ave_score >= 50
teenager = age >= 13 and age <= 19
print(f"Student Record: \nName: {name}\nAge: {age}\npassed: [student")