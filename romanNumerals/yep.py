class RomanNumeralConverter:
    def accept(self, letter):
        times = 0
        while (len(self.romanNumeral) > 0 and self.romanNumeral[0] == letter):
            times += 1
            self.romanNumeral = self.romanNumeral[1:]
        return times

    def lookahead(self, letters):
        return self.romanNumeral.find(letters) == 0

    def toDecimal(self, romanNumeral):
        self.sum = 0
        self.romanNumeral = romanNumeral
        try:
            self.thousands()
            self.fiveHundreds()
            self.hundreds()
            self.fifties()
            self.tens()
            self.fives()
            self.units()
            print(f"{romanNumeral} = {self.sum}")
            return self.sum
        except Exception as err:
            print(err)

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
    assert(RomanNumeralConverter().toDecimal(tests[2 * i]) == tests[2 * i + 1])