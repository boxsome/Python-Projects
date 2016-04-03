def change_return(cost, given):
    if given < cost:
        raise ValueError("Given amount must be more than cost!")

    return given - cost
