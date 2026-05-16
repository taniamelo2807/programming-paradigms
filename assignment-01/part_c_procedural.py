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


def get_total(expense_list):
    """
    Return the total amount of all expenses.
    """

    total_value = 0

    for item in expense_list:
        total_value += item["amount"]

    return total_value


def get_count(expense_list):
    """
    Return how many expense records exist.
    """

    counter = 0

    for item in expense_list:
        counter += 1

    return counter


def get_category_totals(expense_list):
    """
    Return totals for each expense category.
    """

    categories = {}

    for item in expense_list:

        category = item["category"]
        value = item["amount"]

        if category in categories:
            categories[category] += value

        else:
            categories[category] = value

    return categories


def get_most_expensive(expense_list):
    """
    Return the expense with the biggest amount.
    """

    top_expense = expense_list[0]

    for item in expense_list:

        if item["amount"] > top_expense["amount"]:
            top_expense = item

    return top_expense


def get_least_expensive(expense_list):
    """
    Return the expense with the smallest amount.
    """

    low_expense = expense_list[0]

    for item in expense_list:

        if item["amount"] < low_expense["amount"]:
            low_expense = item

    return low_expense


def get_average(expense_list):
    """
    Return the average expense value.
    """

    total = get_total(expense_list)
    amount = get_count(expense_list)

    average = total / amount

    return average


def get_above_average(expense_list):
    """
    Return expenses with values above average.
    """

    average = get_average(expense_list)

    result = []

    for item in expense_list:

        if item["amount"] > average:
            result.append(item)

    return result


def print_summary(expense_list):
    """
    Print all expense information.
    """

    total = get_total(expense_list)
    count = get_count(expense_list)

    print("Total expenses:", format(total, ".2f"))
    print("Number of records:", count)

    print("\nCategory breakdown:")

    category_totals = get_category_totals(expense_list)

    ordered = []

    for category in category_totals:
        ordered.append(category)

    ordered.sort()

    for category in ordered:

        print(
            category,
            ":",
            format(category_totals[category], ".2f")
        )

    highest = get_most_expensive(expense_list)

    print("\nMost expensive:")
    print(
        highest["description"],
        "(" + highest["category"] + ")",
        "-",
        format(highest["amount"], ".2f")
    )

    lowest = get_least_expensive(expense_list)

    print("\nLeast expensive:")
    print(
        lowest["description"],
        "(" + lowest["category"] + ")",
        "-",
        format(lowest["amount"], ".2f")
    )

    average = get_average(expense_list)

    print("\nAverage expense:", format(average, ".2f"))

    print("Expenses above average:")

    above_average = get_above_average(expense_list)

    for item in above_average:

        print(
            "-",
            item["description"],
            "(" + format(item["amount"], ".2f") + ")"
        )


if __name__ == "__main__":
    print_summary(expenses)