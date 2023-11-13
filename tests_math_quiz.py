import unittest
from math_quiz import generate_random_interger,  generate_random_operator, perform_operation


class TestMathGame(unittest.TestCase):

    def test_generate_random_interger(self):
        # Test if random numbers generated are within the specified range
        min_value = 1
        max_value = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num =generate_random_interger(min_value, max_value)
            self.assertTrue(min_value <= rand_num <= max_value)

    def test_generate_random_operator(self):
        # TODO
        for _ in range(1000):
            rand_operator = generate_random_operator()
            self.assertIn(rand_operator, ['+', '-', '*'])

    def test_perform_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '-', '10 - 3', 7),
                (2, 6, '*', '2 * 6', 12),
                ''' TODO add more test cases here '''
            ]

            for number1, number2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = perform_operation(number1, number2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
