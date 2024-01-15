def roman_to_decimal(s):
    roman_numerals = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }

    result = 0
    i = 0

    while i < len(s):
        # Check for two-character Roman numerals first
        if i + 1 < len(s) and s[i:i + 2] in roman_numerals:
            result += roman_numerals[s[i:i + 2]]
            i += 2
        else:
            # Single-character Roman numeral
            result += roman_numerals[s[i]]
            i += 1

    return result

# Example usage:
print(roman_to_decimal('III'))  # Output: 3
print(roman_to_decimal('IX'))   # Output: 9
print(roman_to_decimal('MCMXCIV')) # Output: 42
