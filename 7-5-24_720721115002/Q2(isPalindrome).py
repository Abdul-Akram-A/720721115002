def isPalindrome(x: int) -> bool:
      x=str(x)
      x_new=x[::-1]
      if x == x_new:
          return True
      else:
          return False

Test_Case={"Case_1":{"num":121},
           "Case_2":{"num":-121},
           "Case_3":{"num":10}}

for Case,Parameter in Test_Case.items():
    print(isPalindrome(Parameter["num"]))