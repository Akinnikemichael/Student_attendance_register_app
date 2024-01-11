from typing import Any

student = input("Student name? ")
student_surname = input("student surname? ")
is_student_in_school = input("is student in school, True or False? ")
attendance1 = input("if student is in attendance enter +1, if absence enter -1 ")
Total_attendance1 = input("how many time did student attend school this term? ")
Total_absent_days1 = input("how many days was student absent in school this term? ")

present = bool(is_student_in_school)
attendance = int(attendance1)
Total_attendance = int(Total_attendance1)
Total_absent_days = int(Total_absent_days1)


if present == True and attendance == +1:
    Frequency =+ Total_attendance
#attendance) = sum(attendance1) if you connect code to DB and save attendance everyday
    print("Student is present today and Number of days present is " + " " + str(Frequency))


elif present == False and attendance == -1:
    Frequency =- Total_absent_days
    print("Student is absent today and Number of days absent is " + " " + str(Frequency))




