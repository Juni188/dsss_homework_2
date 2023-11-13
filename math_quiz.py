import random

def generate_random_interger(min_value, max_value):
    """
    Generate a random integer between min_value and max_value (inclusive).
    """
    return random.randint(min_value, max_value)


def generate_random_operator():
    """
    Generate a random arithmetic operator: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def perform_operation(number1, number2, operator):
    """
    Perform the arithmetic operation specified by the operator on number1 and number2.
    Returns a tuple containing the problem expression and the correct answer.
    """
    problem_expression = f"{number1} {operator} {number2}"
    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return problem_expression, answer

def math_quiz():
    score = 0
    total_questions = 3
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    for _ in range(total_questions):
        number1 = generate_random_interger(1, 10)
        number2 = generate_random_interger(1, 5)
        operator = generate_random_operator()

        problem, answer = perform_operation(number1, number2, operator)

        print(f"\nQuestion: {problem}")
        user_answer = input("Your answer: ")

        try:
            user_answer=int(user_answer)
        except ValueError:
            print("Invalid input.Please enter a valid integer.")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()

