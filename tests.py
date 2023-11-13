# CS362
# A2: TDD Hands On
# by Kongkom Hiranpradit ONID ID: hiranprk
# 12 November 2023

import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    """ Rule 1: Must be between 8 and 20 characters (inclusive) """
    """ Rule 2: Must contain at least one lowercase letter (standard English alphabet) """
    """ Rule 3: Must contain at least one uppercase letter (standard English alphabet) """
    """ Rule 4: Must contain at least one digit """
    """ Rule 5: Must contain at least one symbol """

    def test1(self):
        """too short: 7 characters """
        input = 'aldjfld'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        """1 symbol, 1 digit, 1 upper, 1 lower"""
        input = '$1Asdfgh'
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        """1 symbol, 1 digit, 1 upper, 1 lower but too long"""
        input = '$(#*asdf-1DFJSDF39;k)'
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        """no lowercase, correct length"""
        input = "$1ASDFGHJ"
        expected = False
        self.assertEqual(check_pwd(input), expected)



if __name__ == '__main__':
    unittest.main()
