from math import log, ceil, floor


class PalindromicNumbers:

    def __init__(self):
        self.domain = [1, 20]

    def check_all_in_domain(self):
        for i in range(self.domain[0], self.domain[1] + 1):
            print(str(i) + ',' + str(self.check_lowest_palindromic_base(i)))

    def check_lowest_palindromic_base(self, number):
        base = 2
        # Edge cases not covered correctly by algorithm
        if number == 1:
            return 2
        if number == 2:
            return 3
        # Algorithm as explained in readme.md
        while base < number - 1:
            temp_number = number
            number_digits = ceil(log(number, base) + 1e-10)
            for i in range(0, floor(number_digits / 2)):
                first_digit = floor(temp_number / base**(number_digits - i - 1))
                temp_number -= base**(number_digits - i - 1) * first_digit
                last_digit = int((temp_number % base**(i + 1)) / base**i)
                temp_number -= last_digit * base**i
                if first_digit != last_digit:
                    base += 1
                    break
                if i == floor(number_digits / 2) - 1:
                    return base
        return number - 1

    def run_unit_tests(self):
        test_cases = [
            {'type': 'edge case',
             'number': 1,
             'answer': 2},
            {'type': 'edge case',
             'number': 2,
             'answer': 3},
            {'type': 'binary palindromic prime',
             'number': 443,
             'answer': 2},
            {'type': 'first triply palindromic prime (in base 1)',
             'number': 10000500001,
             'answer': 10}
        ]
        for test in test_cases:
            print('testing for ' + test['type'])
            print(self.check_lowest_palindromic_base(test['number']) == test['answer'])


pn = PalindromicNumbers()
pn.check_all_in_domain()
pn.run_unit_tests()
