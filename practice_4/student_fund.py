class StudentFund:
    def __init__(self):
        self.students = {}  
    
    def enroll_student(self, student_id, initial_grant):
        if student_id in self.students:
            raise ValueError(f"Студент с ID '{student_id}' уже зарегистрирован в фонде")
        
        if initial_grant < 0:
            raise ValueError("Начальный грант не может быть отрицательным")
        
        self.students[student_id] = initial_grant
        print(f"Студент {student_id} зачислен с начальным грантом: {initial_grant} руб.")
    
    def add_grant(self, student_id, amount):
        if student_id not in self.students:
            raise ValueError(f"Студент с ID '{student_id}' не найден в фонде")
        
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        
        self.students[student_id] += amount
        print(f"Счет студента {student_id} пополнен на {amount} руб. Новый баланс: {self.students[student_id]} руб.")
    
    def use_funds(self, student_id, amount):
        if student_id not in self.students:
            raise ValueError(f"Студент с ID '{student_id}' не найден в фонде")
        
        if amount <= 0:
            raise ValueError("Сумма списания должна быть положительной")
        
        if self.students[student_id] < amount:
            raise ValueError(f"Недостаточно средств. Баланс: {self.students[student_id]} руб., запрошено: {amount} руб.")
        
        self.students[student_id] -= amount
        print(f"Со счета студента {student_id} списано {amount} руб. Остаток: {self.students[student_id]} руб.")
    
    def view_student_balance(self, student_id):
        if student_id not in self.students:
            print(f"Ошибка: Студент с ID '{student_id}' не найден в фонде")
            return None
        
        balance = self.students[student_id]
        print(f"Баланс студента {student_id}: {balance} руб.")
        return balance

def main():
    sf = StudentFund()
    
    print("=== ЗАЧИСЛЕНИЕ СТУДЕНТОВ ===")
    
    sf.enroll_student("STU-01", 5000)
    sf.enroll_student("STU-02", 3000)
    
    print("\n=== ПОПОЛНЕНИЕ СЧЕТА ===")

    sf.add_grant("STU-01", 1000)
    
    print("\n=== ИСПОЛЬЗОВАНИЕ СРЕДСТВ ===")

    sf.use_funds("STU-02", 800)
    
    print("\n=== ПРОВЕРКА БАЛАНСОВ ===")

    sf.view_student_balance("STU-01")
    sf.view_student_balance("STU-02")
    
    print("\n=== ПРОВЕРКА ОШИБОЧНЫХ ОПЕРАЦИЙ ===")

    try:
        sf.use_funds("STU-02", 2500)  
    except ValueError as e:
        print(f"Ошибка при списании: {e}")
    
    sf.view_student_balance("STU-99")  
    
    print("\n=== ДОПОЛНИТЕЛЬНЫЕ ПРОВЕРКИ ===")

    try:
        sf.enroll_student("STU-01", 2000)
    except ValueError as e:
        print(f"Ошибка при регистрации: {e}")
    
    try:
        sf.add_grant("STU-99", 1000)
    except ValueError as e:
        print(f"Ошибка при пополнении: {e}")

