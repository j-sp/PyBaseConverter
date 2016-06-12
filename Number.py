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

"""A Number class one can get and set using different bases.

This module implements class Number, a place holder for a number
one can set and get using different bases.
"""

class Number:
    """A class for holding a number one can get and set using different bases.

    Public methods:
    __init__: initialize with a value in base 10.
    __str__ : provide string representation for number in base 10.
    set     : set the number using a number string and a given base.
    get     : get the number in a given base.
    """
    def __init__(self, value):
        """ Initialize number with a value in base 10."""
        self.base10_value = value

    def __str__(self):
        """ Return string representation of number in base 10."""
        return str(self.base10_value)
    
    def set(self, base, number_string):
        """Set value of number using a number string in a given base.
        
        Args:
          base: a number between 2 and 10 included.
          number_string: a string representing the number in the given base.

        Exceptions raised:
          ValueError if the base is not comprised between 2 and 10.
          ValueError if one of the characters in the string does not correspond
          to an integer (0-9).
          ValueError if at least one of the digits is not smaller than the base.
        """
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
        """Get number in a given base.

        Args:
          base: a number specifying the base.

        Returns:
          A string containing the representation of the number in the given base.

        Exceptions raised:
          ValueError if the base is not comprised between 2 and 10 included.
        """
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
