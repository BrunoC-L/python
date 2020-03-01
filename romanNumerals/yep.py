class RomanNumeralConverter:
    def __init__(self, value):
        if (type(value) == str):
            self.romanNumeral = value
            self.toDecimal()
        if (type(value) == int):
            if (value >= 4000 or value < 0):
                print("Input a decimal value between 0 and 3999")
                return
            self.decimal = value
            self.toRoman()

    def getDecimal(self):
        return self.decimal

    def getRoman(self):
        return self.romanNumeral

    def toRoman(self):
        self.romanNumeral = ""
        tempDecimal = self.decimal
        while (self.decimal >= 1000):
            self.romanNumeral += "M"
            self.decimal -= 1000
        if (self.decimal >= 900):
            self.romanNumeral += "CM"
            self.decimal -= 900
        if (self.decimal >= 500):
            self.romanNumeral += "D"
            self.decimal -= 500
        if (self.decimal >= 400):
            self.romanNumeral += "CD"
            self.decimal -= 400
        while (self.decimal >= 100):
            self.romanNumeral += "C"
            self.decimal -= 100
        if (self.decimal >= 90):
            self.romanNumeral += "XC"
            self.decimal -= 90
        if (self.decimal >= 50):
            self.romanNumeral += "L"
            self.decimal -= 50
        if (self.decimal >= 40):
            self.romanNumeral += "XL"
            self.decimal -= 40
        while (self.decimal >= 10):
            self.romanNumeral += "X"
            self.decimal -= 10
        if (self.decimal >= 9):
            self.romanNumeral += "IX"
            self.decimal -= 9
        if (self.decimal >= 5):
            self.romanNumeral += "V"
            self.decimal -= 5
        if (self.decimal == 4):
            self.romanNumeral += "IV"
            self.decimal -= 4
        while (self.decimal >= 1):
            self.romanNumeral += "I"
            self.decimal -= 1
        print(self.romanNumeral)
        self.decimal = tempDecimal

    def accept(self, letter):
        times = 0
        while (len(self.romanNumeral) > 0 and self.romanNumeral[0] == letter):
            times += 1
            self.romanNumeral = self.romanNumeral[1:]
        return times

    def lookahead(self, letters):
        return self.romanNumeral.find(letters) == 0

    def toDecimal(self):
        self.sum = 0
        tempNumeral = self.romanNumeral
        try:
            self.thousands()
            self.fiveHundreds()
            self.hundreds()
            self.fifties()
            self.tens()
            self.fives()
            self.units()
            print(f"{self.romanNumeral} = {self.sum}")
            self.decimal = self.sum
            self.romanNumeral = tempNumeral
        except Exception as err:
            print(err)
            self.decimal = None
            self.romanNumeral = None

    def thousands(self):
        toAdd = 1000 * self.accept("M")
        if (self.lookahead("CM")):
            self.romanNumeral = self.romanNumeral[2:]
            toAdd += 900
            if (self.lookahead("C")):
                raise Exception("Invalid syntax while parsing thousands")
        if (toAdd > 3900):
            raise Exception("Invalid syntax while parsing thousands")
        else:
            self.sum += toAdd

    def fiveHundreds(self):
        toAdd = 500 * self.accept("D")
        if (self.lookahead("CD")):
            self.romanNumeral = self.romanNumeral[2:]
            toAdd += 400
            if (self.lookahead("C")):
                raise Exception("Invalid syntax while parsing five hundreds")
        if (toAdd > 500):
            raise Exception("Invalid syntax while parsing five hundreds")
        else:
            self.sum += toAdd
    
    def hundreds(self):
        toAdd = 100 * self.accept("C")
        if (self.lookahead("XC")):
            self.romanNumeral = self.romanNumeral[2:]
            toAdd += 90
            if (self.lookahead("X")):
                raise Exception("Invalid syntax while parsing hundreds")
        if (toAdd > 390):
            raise Exception("Invalid syntax while parsing hundreds")
        else:
            self.sum += toAdd

    def fifties(self):
        toAdd = 50 * self.accept("L")
        if (self.lookahead("XL")):
            self.romanNumeral = self.romanNumeral[2:]
            toAdd += 40
            if (self.lookahead("X")):
                raise Exception("Invalid syntax while parsing fifties")
        if (toAdd > 50):
            raise Exception("Invalid syntax while parsing fifties")
        else:
            self.sum += toAdd

    def tens(self):
        toAdd = 10 * self.accept("X")
        if (self.lookahead("IX")):
            self.romanNumeral = self.romanNumeral[2:]
            toAdd += 9
            if (self.lookahead("O")):
                raise Exception("Invalid syntax while parsing tens")
        if (toAdd > 39):
            raise Exception("Invalid syntax while parsing tens")
        else:
            self.sum += toAdd

    def fives(self):
        toAdd = 5 * self.accept("V")
        if (self.lookahead("IV")):
            self.romanNumeral = self.romanNumeral[2:]
            toAdd += 4
            if (self.lookahead("I")):
                raise Exception("Invalid syntax while parsing fives")
        if (toAdd > 5):
            raise Exception("Invalid syntax while parsing fives")
        else:
            self.sum += toAdd

    def units(self):
        toAdd = self.accept("I")
        if (toAdd > 3):
            raise Exception("Invalid syntax while parsing units")
        else:
            self.sum += toAdd
        if (len(self.romanNumeral) > 0):
            raise Exception("reached end of parsing order and there were digits remaining")

    def valueAndSubstract(self, c):
        if (c == "I"):
            return 1
        if (c == "V"):
            return 5
        if (c == "X"):
            return 10
        if (c == "L"):
            return 50
        if (c == "C"):
            return 100
        if (c == "D"):
            return 500
        if (c == "M"):
            return 1000

tests = [
    "MDCLXVI", 1666,
    "IV", 4,
    "XIV", 14,
    "XVI", 16,
    "LXIV", 64,
    "XCIX", 99,
    "CMXCIX", 999,
    "MMMCMXCIX", 3999,
    "MMMCIX", 3109,
    "XXX", 30,
    "XXXIV", 34,
    "XXXVI", 36,
    "XLVI", 46,
    "DLVIII", 558,
    "MMMDCXLIV", 3644,
    "MDCCCXXXVII", 1837,
    "XXXVII", 37,
    "XXIX", 29,
    "XXII", 22,
    "XXIII", 23,
    "MCDLVI", 1456,
    "MCDXLI", 1441,
    "MCDLI", 1451,

    "MXXC", None,
    "XVX", None,
    "IIV", None,
    "MCMC", None,
    "MDCCCXXXIVI", None,
    "VX", None,
    "IVI", None,
    "IXD", None,
    "XKV", None,
    "VV", None,
]

for i in range(int(len(tests) / 2)):
    assert(RomanNumeralConverter(tests[2 * i]).getDecimal() == tests[2 * i + 1])
    assert(RomanNumeralConverter(tests[2 * i]).getRoman() == (tests[2 * i] if tests[2 * i + 1] is not None else tests[2 * i + 1]))
    if (tests[2 * i + 1] is not None):
        assert(RomanNumeralConverter(tests[2 * i + 1]).getRoman() == tests[2 * i])
        assert(RomanNumeralConverter(tests[2 * i + 1]).getDecimal() == tests[2 * i + 1])