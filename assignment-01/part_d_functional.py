from part_c_procedural import (
    get_total,
    get_category_totals,
    get_above_average
)

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


def get_total_functional(expense_list):
    """
    Return total expense amount using functional style.
    """

    return sum(
        expense["amount"]
        for expense in expense_list
    )


def get_category_totals_functional(expense_list):
    """
    Return category totals using dict comprehension.
    """

    unique_categories = {
        expense["category"]
        for expense in expense_list
    }

    return {
        category: sum(
            expense["amount"]
            for expense in expense_list
            if expense["category"] == category
        )

        for category in unique_categories
    }


def get_above_average_functional(expense_list):
    """
    Return expenses above average using filter and lambda.
    """

    average = (
        get_total_functional(expense_list)
        / len(expense_list)
    )

    filtered = filter(
        lambda expense: expense["amount"] > average,
        expense_list
    )

    return list(filtered)


def format_expenses(expense_list):
    """
    Return formatted expense lines using map and lambda.
    """

    formatted = map(

        lambda expense:
        f"{expense['date']} | "
        f"{expense['category']} | "
        f"{expense['description']} | "
        f"${expense['amount']:.2f}",

        expense_list
    )

    return list(formatted)


if __name__ == "__main__":

    assert round(get_total_functional(expenses), 2) == round(get_total(expenses), 2), \
        "D1 total mismatch"

    assert get_category_totals_functional(expenses) == get_category_totals(expenses), \
        "D2 category totals mismatch"

    procedural_ids = {
        id(expense)
        for expense in get_above_average(expenses)
    }

    functional_ids = {
        id(expense)
        for expense in get_above_average_functional(expenses)
    }

    assert procedural_ids == functional_ids, \
        "D3 above average mismatch"

    print("All assertions passed.")

    print("\nFormatted expenses:")

    for line in format_expenses(expenses):
        print(line)