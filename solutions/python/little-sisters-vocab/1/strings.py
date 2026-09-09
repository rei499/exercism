"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word (str): The root word.
    :returns (str): Root word prepended with 'un'."""

    return "un" + word 

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words.

    :param vocab_words (list[str]): Vocabulary words with prefix at first index.
    :returns (str): Prefix followed by vocabulary words with prefix applied.

    This function takes a `vocab_words` list of strings and returns a string
    with the prefix and the words with prefix applied, separated by ' :: '."""

    separator = " :: " + vocab_words[0]
    return separator.join(vocab_words)
    
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.
    
    :param word (str): Word to remove suffix from.
    :returns (str): Word with suffix removed & spelling adjusted."""

    suffix_removed = word.replace("ness", "")
    if suffix_removed.endswith("i"):
        return suffix_removed.replace("i", "y")
    return suffix_removed

def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence (str): The word used in a sentence as an adjective.
    :param index (int): Index of the adjective to remove and transform.
    :returns (str): The extracted adjective in verb form."""

    adjective = sentence.split()[index]
    verb = adjective.replace(".", "") + "en"
    return verb  