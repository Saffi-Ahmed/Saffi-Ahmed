text_file = open("student.txt", "w")
with open('Student.txt') as f:
        for line in f:
            stdId, stdName = line.strip().split(" ", 1)
            # check if the student exist
            if userInput == stdId:
                print("Student found!")
                print("Student ID: " + stdId + "\nStudent Name: " + stdName)
            else:
                print("The student does not exist")


studentFinder = input("Please enter id: ")
studentInfo(studentFinder)
text_file.close()
