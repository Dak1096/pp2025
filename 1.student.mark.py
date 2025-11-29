student = []
course = []
mark ={}

SCount = int(input("No of students: "))
for i in range(SCount):
    id = str(input("Student id: "))
    name = input("Student name: ")
    dob = input ("Student dob: ")
    student.append({"ID": id, "Name": name, "DoB": dob})

CCount = int(input("No of course: "))
for i in range(CCount):
    id = str(input("Course id: "))
    name = input("Course name: ")
    course.append({"ID": id, "Name": name})

while True:
    cmd = str(input("Input command (c_list, s_list, input_mark, show_mark, stop): "))

    if cmd == "input_mark":
        CId = input("Course id to input marks: ")
        mark["CId"] = {}
        for s in student:
            mk = float(input(f"{s['ID']}_{s['Name']}'s mark: "))
            mark['CId'][s['ID']] = mk

    if cmd == "c_list":
        for i in course:
            print(f"{i['ID']}_{i['Name']}")

    if cmd == "s_list":
        for i in student:
            print(f"{i['ID']}_{i['Name']}")

    if cmd == "show_mark":
        CId = input("Course id to show marks: ")
        for i in student:
            print(f"{s['ID']}_{s["Name"]}: {mark["CId"][s['ID']]}")

    if cmd == "stop":
        print("Shutting down...")
        break
    

    

