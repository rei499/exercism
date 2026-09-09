EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.

    Parameters:
        number_of_layers (int): The number of layers of lasagna.

    Returns:
        int: The preparation time (in minutes) derived from 'PREPARATION_TIME'.

    Function that takes the actual number of layers the lasagna has as
    an argument and returns the total time (in minutes) needed to bake
    based on the `PREPARATION_TIME`.
    """
    return PREPARATION_TIME * number_of_layers

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate .

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The total time (in minutes) elapsed in cooking derived from 'EXPECTED_BAKE_TIME',     and 'PREPARATION_TIME'.

    Function that takes the actual minutes the lasagna has been prepared and baked in the oven     as an argument and returns the total time elapsed (in minutes) based on the                    `EXPECTED_BAKE_TIME`and 'PREPARATION_TIME'.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
