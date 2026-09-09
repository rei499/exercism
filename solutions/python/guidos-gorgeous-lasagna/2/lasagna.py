EXPECTED_BAKE_TIME = 40    #Time in minutes the lasagna should be in the oven.
PREPARATION_TIME = 2    #Preparation time in minutes per layer of lasagna

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining
    
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time (in  minutes) derived from 'EXPECTED_BAKE_TIME'
    
    Function that takes the actual minutes the lasagna has been in the oven as an argument
    and returns how many minutes the lasagna still needs to bake based on the 
    'EXPECTED_BAKE_TIME'
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time 

def preparation_time_in_minutes(number_of_layers):
    """Calculates the preparation time.
    
    :param number_of_layers: int layer of lasagna to bake
    :return: int preparation time (in minutes) derived from multiplying
    'PREPARATION_TIME' to 'number_of_layers'
    
    Function that takes the number of layers the lasagna has as an argument
    and returns the total time (in minutes) needed for preparation."""

    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time baking (in minutes).
    
    :param number_of_layers: int layer of lasagna made
    :param elapsed_bake_time: int baking time already elapsed
    :return: int total baking time
    
    Function that takes the number of layer the lasagna has and
    the total time lasagna has been in the oven as its two arguments
    Then returns the actual minutes spent baking."""

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    