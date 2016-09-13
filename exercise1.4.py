def longest_common_substring(string_1, string_2):
    """find the longest common substring of two sequences"""
    # Figure out which string is shortest, save as search_string
    if len(string_1) <= len(string_2):
        short_string = string_1
        long_string = string_2

    elif len(string_1) > len(string_2):
        short_string = string_2
        long_string = string_1

    for short_string in long_string

    # Look for whole search_string ind
    for short_string
# Can I start making letters from one side lowercased, then search for uppercase portion of shorter string?
# figure out how to chop pieces off of the other side
# figure out how to chop both sides off at the same time
