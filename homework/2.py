students = [
    {

        "name": "Elif",
        "surname": "Gultekin",
        "midtern": 5,
        "final": 1,
        "homework" : 1 
    },
    {

        "name": "Burak",
        "surname": "Yıldırım",
        "midtern": 1,
        "final":1,
        "homework" : 2 
    }
]

maxGrade = 0;
bestStudent = 0;

for s in range(len(students)):
    grade = ( students[s]['midtern'] 
            + students[s]['final'] 
            + students[s]['homework'] ) / 3
    if grade > maxGrade:
        bestStudent = s
    maxGrade = grade
    
    
print(students[bestStudent]["name"])
    