print("####--Student Marks Analyzer--####")
my_dict={}
while True:
    subject=input("Enter the subject name: ")
    if subject == "maths" or subject == "Maths" or subject == "MATHS":
        marks=int(input("Enter the marks: "))
        my_dict[subject]=marks
    elif subject == "science" or subject == "Science" or subject == "SCIENCE":
        marks=int(input("Enter the marks: "))
        my_dict[subject]=marks
    elif subject == "english" or subject == "English" or subject == "ENGLISH":
        marks=int(input("Enter the marks: "))
        my_dict[subject]=marks
    elif subject == "social" or subject == "Social" or subject == "SOCIAL":
        marks=int(input("Enter the marks: "))
        my_dict[subject]=marks
    elif subject == "hindi" or subject == "Hindi" or subject == "HINDI":
        marks=int(input("Enter the marks: "))
        my_dict[subject]=marks
    elif subject == "exit" or subject == "EXIT" or subject == "Exit":
        break
    else:
        print("Invalid subject. Please enter a valid subject.")
print("The marks of the student are: ", my_dict)

#avg
print(my_dict)
total = sum(my_dict.values())
average = total / len(my_dict)
print("Total marks: ", total)
print("Average marks: ", average)

#Highest-scoring subject
mk = max(my_dict, key=my_dict.get)
mv = (my_dict[mk])
print("Max marks are in:",mk,"=",mv)
#Lowest-scoring subject
mk = min(my_dict, key=my_dict.get)
mv = (my_dict[mk])
print("Min marks are in:",mk,"=",mv)

#grade
# grade
if average >= 90:
    print("Grade: A")
elif average >=75 or average <= 89:
    print("Grade: B")
elif average >=60 or average <= 74:
    print("Grade: C")
else :
    print("Grade D")
