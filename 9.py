def replace_occurrences(original_string, search_term, replacement_term):
    """Replace all occurrences of search_term with replacement_term in the original_string."""
    return original_string.replace(search_term, replacement_term)
original_string = input("Enter the original string: ")
search_term = input("Enter the search term: ")
replacement_term = input("Enter the replacement term: ")
modified_string = replace_occurrences(original_string, search_term, replacement_term)
print("Modified string:", modified_string)