def evaluate(numeral):
    sum = 0
    last = None
    block = 0
    for c in numeral:
        if (not ("IVXLCDM".__contains__(c))):
            print("{} has Invalid characters!".format(numeral))
            return
        dec = decimal(c)
        if (block < dec):
            block = dec - block
        else:
            sum += block
            block = dec
    print("{} = {}".format(numeral, sum + block))

def decimal(c):
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

evaluate("MDCLXVI")
evaluate("IV")
evaluate("XIV")
evaluate("XVI")
evaluate("XVI")
evaluate("LXIV")
evaluate("LXVI")
evaluate("XCIX")
evaluate("CMXCIX")
evaluate("MMMCMXCIX")
evaluate("MMMCIX")