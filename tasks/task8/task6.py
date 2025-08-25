student = {}
student["name"]= input("kindly enter your name: ")
student["age"]= int(input("kindly input your age: "))
student["waec_result"] =(input("do you pass all your waec at a credit level or A and B? input either True or False: ")).title()
student["jamb_score"] = int(input("kindly entr your jamb score: "))
student["post_utme"] = int(input("kindly input your post utme score here: "))

age_eligibility= student["age"] >=16
waec_eligibility = student["waec_result"] ==True
jamb_eligiblity = student["jamb_score"] >= 200
post_utme_eligibility = student["post_utme"] >= 70
total_eligibility = age_eligibility and waec_eligibility and jamb_eligiblity and post_utme_eligibility
print(f"Dear candidate you meet up the above department cutoff mark and you are qualify for this addimission.Here are your Biodata's Name::{student["name"]}\nAge:{student["age"]}\nWaec_result:{student["waec_result"]}\nJamb_score:{student["jamb_score"]}\n")
