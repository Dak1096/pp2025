student = []
course = []
mark ={}

SCount = int(input("No of students: "))
CCount = int(input("No of course: "))
def StudentInput():
    for i in range(SCount):
        id = str(input("Student id: "))
        name = input("Student name: ")
        dob = input ("Student dob: ")
        student.append({"ID": id, "Name": name, "DoB": dob})

def CourseInput():
    for i in range(CCount):
        id = str(input("Course id: "))
        name = input("Course name: ")
        course.append({"ID": id, "Name": name})
def main():
    while True:
        cmd = str(input("Input command (s_input, c_input, s_list, c_list, input_mark, show_mark, stop): "))

        if cmd == "s_input":
            StudentInput()
            print("\n------------------------- \n")

        elif cmd == "c_input":
            CourseInput()
            print("\n------------------------- \n")

        elif cmd == "input_mark":
            CId = input("Course id to input marks: ")
            mark["CId"] = {}
            for s in student:
                mk = float(input(f"{s['ID']}_{s['Name']}'s mark: "))
                mark['CId'][s['ID']] = mk
            print("\n------------------------- \n")

        elif cmd == "c_list":
            for i in course:
                print(f"{i['ID']}_{i['Name']}")
            print("\n------------------------- \n")

        elif cmd == "s_list":
            for i in student:
                print(f"{i['ID']}_{i['Name']}")
            print("\n------------------------- \n")

        elif cmd == "show_mark":
            CId = input("Course id to show marks: ")
            for i in student:
                print(f"{s['ID']}_{s['Name']}: {mark['CId'][s['ID']]}")
            print("\n------------------------- \n")

        elif cmd == "stop":
            print("Shutting down...")
            break
        else:
            print("Invalid command!")
            print("\n------------------------- \n")
main()
