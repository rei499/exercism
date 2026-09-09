"""Functions to help edit essay homework using string manipulation."""

def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title (str): Essay title
    :returns (str): The title string in title case (first letters capitalized)."""

    return title.title()

def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence (str): A sentence to check.
    :returns (bool): Is the sentence punctuated correctly?"""

    return sentence.endswith(".")

def clean_up_spacing(sentence):
    """Trim any leading or trailing whitespace from the sentence.

    :param sentence (str): A sentence to clean of leading and trailing space characters.
    :returns (str): A sentence that has been cleaned of leading and trailing space characters."""

    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence (str): A sentence to replace words in.
    :param old_word (str): The word to replace.
    :param new_word (str): The replacement word.
    :returns (str): Input sentence with new words in place of old words."""

    return sentence.replace(old_word, new_word)
