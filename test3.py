students = {
    "rahul":85, "priya":92, "aman":78, "sam":95, "riya":88
}
total = 0
for score in students.values():
    total += score 

print("average:", total / len(students))
print("topper:", max (students.values()))
print("bottom:", min(students.values()))

name = input ("search student:")
print("score:", students.get(name, "not found"))