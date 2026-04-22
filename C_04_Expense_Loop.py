def num_check(question, num_type="float", exit_code=None):
    """check that response is a float / integer more than zero"""

    if num_type == "float":
        error ="please enter a number more than 0."
    else:
        error = "please enter an integer more than 0."

    if num_type == "float":
        error = "please enter an integer more than 0. "

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

                if response > 0:
                    return response
                else:
                    print(error)

        except ValueError:
            print(error)


def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("sorry, this cant be blank. ")


def get_expenses(exp_type):
    """gets variable / fixed expenses and output
    panda (as a string) and a subtotal of the expenses"""

    # list for panda
    all_item = []

    # expenses dictionary

    # loop to get expenses
    while True:
        item_name = not_blank("item name: ")

        # check users enter at least one variable expense
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_item) == 0:
            print("Oop - you have not entered anything.  "
                  "you need at least one item.")
            continue

        elif item_name == "xxx":
            break

        all_items.append(item_name)

    # return all item for now so we can check loop.
    return all_items


# main routine goes here

# Loop for testing purposes
while True:
    product_name = not_blank("product name: ")
    quantity_made = num_check("quantity being made: ", "integer")
    print(f"you are making {quantity_made} {product_name}")
    print()