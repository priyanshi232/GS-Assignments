class IntegerToRoman:
    def __init__(self):
        self.values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        self.roman_numerals = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
    def int_to_roman(self, num):
        roman_numeral = ""
        i = 0
        while num > 0:
            for _ in range(num // self.values[i]):
                roman_numeral += self.roman_numerals[i]
                num -= self.values[i]
            i += 1
        return roman_numeral
