products = {'Bubblegum': 202,
            'Toffee': 118,
            'Ice cream': 2250,
            'Milk chocolate': 1680,
            'Doughnut': 1075,
            'Pancake': 80}

total_income = sum(products.values())
print('Earned amount:')
for key, value in products.items():
    print(f'{key}: ${value}')
print()
print(f'Income: ${total_income}')
stuff_expenses = input('Staff expenses:\n')
other_expenses = input('Other expenses:\n')
total_expenses = int(stuff_expenses) + int(other_expenses)

print(f'Net income: ${total_income - total_expenses}')