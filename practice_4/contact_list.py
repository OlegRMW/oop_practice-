class ContactList:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone):
        for contact_name, _ in self.contacts:
            if contact_name == name:
                print(f"Контакт с именем '{name}' уже существует!")
                return False
        
        self.contacts.append((name, phone))
        print(f"Контакт '{name}' добавлен успешно!")
        return True
    
    def remove_contact(self, name):
        for i, (contact_name, phone) in enumerate(self.contacts):
            if contact_name == name:
                del self.contacts[i]
                print(f"Контакт '{name}' удален успешно!")
                return True
        
        print(f"Контакт с именем '{name}' не найден!")
        return False
    
    def contact_count(self):
        return len(self.contacts)
    
    def find_contact(self, name):
        for contact_name, phone in self.contacts:
            if contact_name == name:
                return phone
        return None
    
    def display_contacts(self):
        if not self.contacts:
            print("Список контактов пуст")
            return
        
        print("Список контактов:")
        print("-" * 25)
        for i, (name, phone) in enumerate(self.contacts, 1):
            print(f"{i}. {name} - {phone}")
        print("-" * 25)

def main():
    my_contacts = ContactList()
    
    print("=== ДОБАВЛЕНИЕ КОНТАКТОВ ===")
    my_contacts.add_contact("Анна", "+79001234567")
    my_contacts.add_contact("Борис", "+79007654321")
    my_contacts.add_contact("Виктория", "+79001112233")
    
    print("\n=== ТЕКУЩИЕ КОНТАКТЫ ===")
    my_contacts.display_contacts()
    
    print(f"\nОбщее количество контактов: {my_contacts.contact_count()}")
    
    print("\n=== УДАЛЕНИЕ КОНТАКТА ===")
    my_contacts.remove_contact("Борис")
    
    print("\n=== ОБНОВЛЕННЫЙ СПИСОК ===")
    my_contacts.display_contacts()
    
    print(f"\nОбщее количество контактов после удаления: {my_contacts.contact_count()}")
    
    print("\n=== ПОИСК КОНТАКТА ===")
    phone = my_contacts.find_contact("Анна")
    if phone:
        print(f"Найден контакт: Анна - {phone}")
    else:
        print("Контакт не найден")

if __name__ == "__main__":
    main()