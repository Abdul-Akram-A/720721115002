def RomanNumerals(s:str):
    RomanPairs={
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }
    s=s.replace("IV","IIII").replace("IX","VIIII")
    s=s.replace("XL","XXXX").replace("XC","LXXXX")
    s=s.replace("CD","CCCC").replace("CM","DCCCC")
    total=0
    
    for letters in s:
        total+=RomanPairs[letters]
    return total
print("TestCase_1:",RomanNumerals("III"))
print("TestCase_2:",RomanNumerals("LVIII"))
print("TestCase_3:",RomanNumerals("MCMXCIV"))
    

    