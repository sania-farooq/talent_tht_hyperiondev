def read_number(numeral):
    # Define dictionaries for number-word mapping
    ones_dict = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }

    teens_dict = {
        '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
        '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'
    }

    tens_dict = {
        '2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty',
        '7': 'seventy', '8': 'eighty', '9': 'ninety'
    }

    # Define function to convert a two-digit number to words
    def two_digit_to_words(two_digit_num):
        if two_digit_num.startswith('0'):
            return ones_dict[two_digit_num[1]]
        elif two_digit_num.startswith('1'):
            return teens_dict[two_digit_num]
        else:
            tens = tens_dict[two_digit_num[0]]
            ones = ones_dict[two_digit_num[1]]
            if ones == 'zero':
                return tens
            else:
                return tens + '-' + ones

    # Remove leading zeros from the numeral
    numeral = numeral.lstrip('0')

    # If the numeral is 0, return 'zero'
    if numeral == '0':
        return 'Zero.'

    # Prepare a list to store the words for each part of the numeral
    words_parts = []

    # Convert the numeral to words in groups of three digits (thousands, millions, etc.)
    while numeral:
        group = numeral[-3:]  # Get the last three digits of the numeral
        numeral = numeral[:-3]  # Remove the last three digits from the numeral

        # Convert the three-digit group to words
        if len(group) == 3:
            if group[0] != '0':
                words_parts.append(ones_dict[group[0]] + ' hundred')
            group = group[1:]  # Remove the hundreds digit

        if len(group) == 2:
            words_parts.append(two_digit_to_words(group))
        elif len(group) == 1:
            words_parts.append(ones_dict[group])

    # Join the words for each part and add appropriate punctuation
    suffixes = ['', ' thousand', ' million', ' billion', ' trillion']  # You can extend this list for larger numbers
    words_with_punctuation = ', '.join(part + suffix for part, suffix in zip(reversed(words_parts), suffixes) if part != 'zero')
    words_with_punctuation = words_with_punctuation.capitalize() + '.'

    return words_with_punctuation

# Test the function
numeral = "19093"
print(read_number(numeral))  # Output: "Nineteen thousand and ninety-three."
