# Task3
# Days and Activities Pairing
days_of_week= tuple(
    {"sunday"}, {"monday"}, {"tuesday"}, {"wednesday"}, {"thursday"}, {"friday"}, {"saturday"}
    )
# Collect activity  data from the user
Day_1= input("kindly input the day of the  week that activities will be perform: ")
Day_2= input("kindly input the day of the week to perform activities: ")
Day_3= input("kindly input the day of the week that activity will be perform: ")

# USE DICTIONARY COMPREHENSION TO PAIR DAYS AND ACTIVITIES
Days= (Day_1,)


# Activity for three days
activity_1= input("kindly input the activities of day one;")
activity_2= input("kindly enter activity for day two: ")
activity_3= input("kindly input hte activity for day three: ")

print(f"{days_of_week}: {activity_1}")