def clean_string(input_string):
    stripped_string = input_string.strip()
    while '  ' in stripped_string:
        stripped_string = stripped_string.replace('  ', ' ')
    return stripped_string
user_input = input("Enter a string with extra spaces: ")
result = clean_string(user_input)
print("Cleaned string:", result)
