import numpy as np

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {}
        roman_dict['I'] = 0 #1
        roman_dict['IV'] = 0 #4
        roman_dict['V'] = 0 #5
        roman_dict['IX'] = 0 #9
        roman_dict['X'] = 0 #10
        roman_dict['XL'] = 0 #40
        roman_dict['L'] = 0 #50
        roman_dict['XC'] = 0 #90
        roman_dict['C'] = 0 #100
        roman_dict['CD'] = 0 #400
        roman_dict['D'] = 0 #500
        roman_dict['CM'] = 0 #900
        roman_dict['M'] = 0 #1000
        res = ''
        while num > 0:
            if num >= 1000:
                roman_dict['M'] += 1
                res += 'M'
                num -= 1000
            elif num >= 900:
                roman_dict['CM'] += 1
                res += 'CM'
                num -= 900
            elif num >= 500:
                roman_dict['D'] += 1
                res += 'D'
                num -= 500
            elif num >= 400:
                roman_dict['CD'] += 1
                res += 'CD'
                num -= 400
            elif num >= 100:
                roman_dict['C'] +=1
                res += 'C'
                num -= 100
            elif num >= 90:
                roman_dict['XC'] += 1
                res += 'XC'
                num -= 90
            elif num >= 50:
                roman_dict['L'] += 1
                res += 'L'
                num -= 50
            elif num >= 40:
                roman_dict['XL'] += 1
                res += 'XL'
                num -= 40
            elif num >= 10:
                roman_dict['X'] += 1
                res += 'X'
                num -= 10
            elif num >= 9:
                roman_dict['IX'] += 1
                res += 'IX'
                num -=  9
            elif num >= 5:
                roman_dict['V'] += 1
                res += 'V'
                num -= 5
            elif num >= 4:
                roman_dict['IV'] += 1
                res += 'IV'
                num -= 4
            elif num >= 1:
                roman_dict['I'] += 1
                res += 'I'
                num -= 1



        return res

num = 1232

result, res = Solution().intToRoman(num)
print(result)
print(res)