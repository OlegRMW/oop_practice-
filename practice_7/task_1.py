class Student:
    def __init__(self, first_name, last_name, student_id, major):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.major = major

    def ShowRecord(self):
        print(f"Студент: {self.first_name} {self.last_name}")
        print(f"ID: {self.student_id}")
        print(f"Специальность: {self.major}")
        print("-" * 30)


class GraduateStudent(Student):
    def __init__(self, first_name, last_name, student_id, major, thesis_topic):
        super().__init__(first_name, last_name, student_id, major)
        self.thesis_topic = thesis_topic

    def ShowRecord(self):
        print(f"Аспирант: {self.first_name} {self.last_name}")
        print(f"ID: {self.student_id}")
        print(f"Специальность: {self.major}")
        print(f"Тема диплома: {self.thesis_topic}")
        print("-" * 30)

if __name__ == "__main__":
    StudentsList = [
        Student("Иван", "Петров", "S001", "Информатика"),
        GraduateStudent("Анна", "Смирнова", "G001", "Математика", "Модели машинного обучения")
    ]

    for student in StudentsList:
        student.ShowRecord()
