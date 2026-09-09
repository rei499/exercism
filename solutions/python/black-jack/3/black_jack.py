"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card):
    """Determine the scoring value of a card.

    :param card (str): The given card.

    :returns (int): The value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value."""

    if card in {"J","K","Q",}:
        return 10
    if card == "A":
        return 1
    return int(card)

def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one (str): First card dealt in the hand.  See below for values.
    :param card_two (str): Second card dealt in the hand. See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.

    :returns (str or tuple): The resulting tuple contains both cards if they are of equal value."""

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two   
    return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    :param card_one (str): First card dealt in the hand.  See below for values.
    :param card_two (str): Second card dealt in the hand. See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.

    :returns (int): Either 1 or 11, which is the value of the upcoming ace card."""
    
    if value_of_card(card_one) == 1 or value_of_card(card_two) == 1:
        return 1
    if value_of_card(card_one) + value_of_card(card_two) >= 11:
        return 1
    return 11
        
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.
    
    :param card_one (str): First card dealt in the hand.  See below for values.
    :param card_two (str): Second card dealt in the hand. See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.

    :returns (bool): Is the hand is a blackjack (two cards worth 21)."""

    is_black = True

    if card_one == "A" and value_of_card(card_two) == 10:
        return is_black
    if card_two == "A" and value_of_card(card_one) == 10:
        return is_black 
    return False

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one (str): First card in the hand.
    :param card_two (str): Second card in the hand.

    :returns (bool): Can the hand be split into two pairs? (i.e. cards are of the same value)."""

    return True if value_of_card(card_one) == value_of_card(card_two) else False
        
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one (str): First card in the hand.
    :param card_two (str): Second card in the hand.

    :returns (bool): Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points)."""

    return (value_of_card(card_one) + value_of_card(card_two)) in {9, 10, 11}