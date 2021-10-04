#! usr/bin/env python
"""Roman to Decimal Number converter"""

_romanvalue = { "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000 }

def roman(romannumber):
    decimalnumber = 0
    global _romanvalue
    for i in range(len(romannumber)-1):
        if _romanvalue[romannumber[i]] < _romanvalue[romannumber[i+1]]:
            decimalnumber -= _romanvalue[romannumber[i]]
        else:
            decimalnumber += _romanvalue[romannumber[i]]
    decimalnumber += _romanvalue[romannumber[-1]]
    return decimalnumber

def main():
    print("Welcome to this fun Roman to Decimal Number converter\n")
    romaninput = input("Please type your roman number here: ")
    print(f"The decimal number is: {roman(romaninput)}\n")
    return

if __name__ == "__main__":
    main()