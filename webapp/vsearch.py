def search4vowels(phrase: str) -> set:
    """Display any vowels found in an asked-for word."""
    vowels = set("aeiou")
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Display any specified letters specified in a word."""
    return set(letters).intersection(set(phrase))
