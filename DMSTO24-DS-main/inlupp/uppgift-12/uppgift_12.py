# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.

def create_student_register(students):
    # Skapa en dictionary där namnet är nyckeln och åldern är värdet
    student_register = {name: age for name, age in students}
    return student_register


students = [("Jonas", 40), ("Thomas", 45), ("Mary", 32), ("Liam", 20)]
print(create_student_register(students))
