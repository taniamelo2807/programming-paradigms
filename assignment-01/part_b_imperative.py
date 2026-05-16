expenses = [
    {"date": "2024-01-05", "category": "Food", "amount": 42.50, "description": "Groceries"},
    {"date": "2024-01-07", "category": "Transport", "amount": 15.00, "description": "Bus pass"},
    {"date": "2024-01-09", "category": "Entertainment", "amount": 60.00, "description": "Concert ticket"},
    {"date": "2024-01-10", "category": "Food", "amount": 8.75, "description": "Coffee & snack"},
    {"date": "2024-01-12", "category": "Utilities", "amount": 120.00, "description": "Electricity bill"},
    {"date": "2024-01-14", "category": "Food", "amount": 55.20, "description": "Restaurant dinner"},
    {"date": "2024-01-15", "category": "Transport", "amount": 30.00, "description": "Taxi"},
    {"date": "2024-01-17", "category": "Entertainment", "amount": 14.99, "description": "Streaming subscription"},
    {"date": "2024-01-20", "category": "Food", "amount": 38.00, "description": "Groceries"},
    {"date": "2024-01-22", "category": "Utilities", "amount": 45.00, "description": "Internet bill"},
    {"date": "2024-01-25", "category": "Transport", "amount": 22.00, "description": "Train ticket"},
    {"date": "2024-01-28", "category": "Entertainment", "amount": 25.00, "description": "Book"},
]

# total and count

final_total = 0
total_records = 0

for expense in expenses:

    final_total = final_total + expense["amount"]
    total_records = total_records + 1

print("Total expenses:", format(final_total, ".2f"))
print("Number of records:", total_records)

# category totals

totals_by_category = {}

for expense in expenses:

    current_category = expense["category"]

    if current_category not in totals_by_category:
        totals_by_category[current_category] = 0

    totals_by_category[current_category] = (
        totals_by_category[current_category] + expense["amount"]
    )

print("\nCategory breakdown:")

ordered_categories = list(totals_by_category.keys())
ordered_categories.sort()

for category in ordered_categories:

    print(
        category,
        ":",
        format(totals_by_category[category], ".2f")
    )

# highest and lowest expense

highest = expenses[0]
lowest = expenses[0]

for expense in expenses:

    if expense["amount"] > highest["amount"]:
        highest = expense

    if expense["amount"] < lowest["amount"]:
        lowest = expense

print("\nMost expensive:")
print(
    highest["description"],
    "(" + highest["category"] + ")",
    "-",
    format(highest["amount"], ".2f")
)

print("\nLeast expensive:")
print(
    lowest["description"],
    "(" + lowest["category"] + ")",
    "-",
    format(lowest["amount"], ".2f")
)

# average and above average

average_total = 0

for expense in expenses:
    average_total = average_total + expense["amount"]

average_result = average_total / len(expenses)

print("\nAverage expense:", format(average_result, ".2f"))

print("Expenses above average:")

for expense in expenses:

    if expense["amount"] > average_result:

        print(
            "-",
            expense["description"],
            "(" + format(expense["amount"], ".2f") + ")"
        )