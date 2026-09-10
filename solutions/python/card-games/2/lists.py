"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    """
    :param number (int): The current round number.
    :returns (list): The current round number and the two that follow.
    """
    
    list_of_rounds = [number, number + 1, number + 2]
    return list_of_rounds

def concatenate_rounds(rounds_1, rounds_2):
    """
    :param rounds_1 (list): The first rounds played.
    :param rounds_2 (list): The second group of rounds played.
    :returns (list):  All rounds played.
    """

    return rounds_1 + rounds_2 

def list_contains_round(rounds, number):
    """
    :param rounds (list): The rounds played.
    :param number (int): The round number.
    :returns (bool): Was the round played?
    """

    played = True
    return played if number in rounds else False

def card_average(hand):
    """"
    :param hand (list): The cards in the hand.
    :returns (float): The average value of the cards in the hand.
    """

    return (sum(hand)) / (len(hand))

def approx_average_is_average(hand):
    """
    :param hand (list): The cards in the hand.
    :returns (bool): Does one of the approximate averages equal the `true average`?
    """

    is_equal = True
    true_average = (sum(hand)) / (len(hand))
    first_and_last = (hand[0] + hand[-1]) / 2
    average_index = int(((len(hand))/2) - 0.5)

    return is_equal if true_average in {hand[average_index], first_and_last} else False

def average_even_is_average_odd(hand):
    """
    :param hand (list): The cards in the hand.
    :returns (bool): Are the even and odd averages equal?
    """

    is_equal = True 
    return is_equal if sum(hand[::2])/len(hand[::2]) == sum(hand[1::2])/len(hand[1::2]) else False
    
def maybe_double_last(hand):
    """
    :param hand (list): The cards in the hand.
    :returns (list): The hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = 22
        return hand
    return hand