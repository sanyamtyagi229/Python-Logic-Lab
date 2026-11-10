class Solution:

  def complexNumberMultiply(self, num1: str, num2: str) -> str:
    # 1. Split by '+'
    parts1 = num1.split('+')
    parts2 = num2.split('+')
    a1 = int(parts1[0])
    b1 = int(parts1[1][:-1])
    a2 = int(parts2[0])
    b2 = int(parts2[1][:-1]) 
    real_part = a1 * a2 - b1 * b2
    imag_part = a1 * b2 + a2 * b1
    return f"{real_part}+{imag_part}i"