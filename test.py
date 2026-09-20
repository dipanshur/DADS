employees = [
    {"name": "Alice", "age": 30, "department": "HR", "salary": 50000},
    {"name": "Bob", "age": 25, "department": "Engineering", "salary": 70000},
    {"name": "Charlie", "age": 35, "department": "Sales", "salary": 80000},
]

def calculate_tax(salary):
    if salary >= 80000:
        tax  = salary * 20 / 100

    else: 
        tax = salary * 10 /100
    
    return tax

for emp in employees:
    tax = calculate_tax(emp["salary"])
    final_salary = emp["salary"] - tax

    print(emp["name"], final_salary)