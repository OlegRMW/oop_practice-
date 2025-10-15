class Ticket:

    database = {}

    def __new__(cls, name, priority):

        if not name[:7] == "ticket_":
            raise ValueError("Тикет должен иметь префикс 'ticket_'")
        
        ticket_id = name[7:]  
        
        instance = super().__new__(cls)
        
        cls.database[ticket_id] = instance
        
        setattr(instance, f"t{ticket_id}", priority)
        
        return instance

t1 = Ticket("ticket_001", "High")

t2 = Ticket("ticket_002", "Low")

try:
    t3 = Ticket("issue_003", "Medium")
except ValueError as e:
    print("Ошибка:", e)

print("t1.t001:", t1.t001)  # High
print("t2.t002:", t2.t002)  # Low

print("Ticket.database:", Ticket.database)