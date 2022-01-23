run = 1

while run > 0: 
  convertWhich = str(input("Would you like to convert to or from a Roman Numeral? "))  
  
  if convertWhich.upper() == "TO":
    def romanNumbers (num):
      value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
      symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
      roman = ""
      i = 0
      while num>0:
        div = num//value[i]
        num = num%value[i]
        while div:
          roman = roman+symbol[i] 
          div = div-1
        i =i+1 
      return roman
    num = int(input("Enter a whole number between 1 and 3999: "))
    print(romanNumbers(num))

  elif convertWhich.upper() == "FROM":
    def fromRoman(numeral):
      mapping = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
      ans = 0

      for i in range(len(s)):
        if i+1 != len(s) and mapping[s[i]]<mapping[s[i+1]]:
          ans = ans - mapping[s[i]]
        else:
          ans = ans + mapping[s[i]]
      return ans
    s = str(input("Enter a Roman Numeral: "))
    print(fromRoman(s))
  
  else:
    print("invalid input")

  keepGoing = str(input("Would you like to do another conversion?(Y/N) "))
  if keepGoing.upper() == "Y":
    run = 1
  elif keepGoing.upper() == "N":
    run = 0
  else:
    print("invalid input")