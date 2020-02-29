def toDecimal(romanNumeral):
    thousandsString, romanNumeral = getThousandsString(romanNumeral)
    hundredsString, romanNumeral = getHundredsString(romanNumeral)

def getThousandsString(romanNumeral):
    thousandsString = ""
    i = 0
    length = len(romanNumeral)
    while(i < length):
        c = romanNumeral[i]
        if (not "MC".__contains__(c)):
            break
        thousandsString += c
        i += 1
    return thousandsString, romanNumeral[i:]

def getHundredsString(romanNumeral):
    thousandsString = ""
    i = 0
    length = len(romanNumeral)
    while(i < length):
        c = romanNumeral[i]
        if (not "DC".__contains__(c)):
            break
        thousandsString += c
        i += 1
    return thousandsString, romanNumeral[i:]

def valueAndSubstract(c):
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
    "MCDVLI", 1446,
    "MCDLI", 1451,
    "MLDXI", 1,

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

toDecimal("MCMLLC")

# for i in range(int(len(tests) / 2)):
#     assert(evaluate(tests[2 * i]) == tests[2 * i + 1])