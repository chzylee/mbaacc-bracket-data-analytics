def get_brackets_with_over_20_entrants(brackets):
    """
    Filter brackets to only include those with more than 20 entrants.

    Args:
        brackets (list): List of Bracket objects.

    Returns:
        list: Filtered list of Bracket objects with more than 20 entrants.
    """
    return [bracket for bracket in brackets if bracket.total_entrants > 20]
