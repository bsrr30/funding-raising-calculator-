def num_check(question, num_type="float"):
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

# main routine goes here

# Loop for testing purposes
while True:
    product_name = not_blank("product name: ")
    quantity_made = num_check("quantity being made: ", "integer")
    print(f"you are making {quantity_made} {product_name}")
    print()