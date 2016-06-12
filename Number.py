## Copyright 2016 Javier Serrano and Adrian Serrano
##
## This file is part of PyBaseConverter.
##
## PyBaseConverter is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## PyBaseConverter is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with PyBaseConverter.  If not, see <http://www.gnu.org/licenses/>.

class Number:
    
    def __init__(self, value):
        self.base10_value = value

    def __str__(self):
        return str(self.base10_value)
    
    def set(self, base, number_string):
        if base > 10 or base < 2:
            raise ValueError("base should be comprised between 2 and 10")
        accum = 0
        exp = len(number_string) - 1
        for i in number_string:
            try:
                digit = int(i)
            except ValueError:
                raise
            if digit >= base:
                raise ValueError("all digits should be smaller than base")
            accum += digit * base**exp
            exp -= 1
        self.base10_value = accum

    def get(self, base):
        if base > 10 or base < 2:
            raise ValueError("base should be comprised between 2 and 10")
        result = ""
        digits = 1
        while base**digits <= self.base10_value:
            digits += 1
        remainder = self.base10_value
        for i in range(digits-1, -1, -1):
            digit = remainder // base**i
            remainder = remainder % base**i
            result += str(digit)
        return result
