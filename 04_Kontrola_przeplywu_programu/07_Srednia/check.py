import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Average")


@tc.test(
    "Count of numbers from keyboard input {n} is saved in a variable 'n'",
    params=[
        {"n": "4"},
        {"n": "12"},
        {"n": "60"},
    ],
    aborts=True,
)
def test_n(stdin, stdout, invoke, n, **kwargs):
    stdin.append(n)
    stdin.extend(["123"] * int(n))

    variables = invoke()

    if "n" not in variables:
        raise CodersLabException("Could not find variable {}".format(p.b.get("n")))

    if str(variables["n"]) != n:
        raise CodersLabException(
            dedent(
                """
                Script did not save the numeric keyboard input in variable {}.
                Variable {} has the value of {} instead of expected {}.
                """
            ).format(
                p.b.get("n"),
                p.b.get("n"),
                p.b.get(variables["n"]),
                p.b.get(n),
            )
        )


@tc.test(
    "Script reads {n} numbers from keyboard input and saves them in the 'numbers' list",
    params=[
        {"n": "6", "numbers": ["1", "3", "9", "35", "11", "2"]},
        {"n": "7", "numbers": ["5", "15", "6", "4", "6", "7", "0"]},
        {"n": "8", "numbers": ["3", "6", "4", "6", "7", "8", "-20", "-10"]},
    ],
    aborts=True,
)
def test_n(stdin, stdout, invoke, n, numbers, **kwargs):
    stdin.append(n)
    stdin.extend(numbers)

    variables = invoke()

    if len(stdin) == int(n):
        raise CodersLabException("Script did not read the numbers")

    if stdin:
        raise CodersLabException(
            dedent(
                """
                Script did not read all provided numbers. 
                Expected the script to ask for {} numbers,
                and it only asked for {}.
                """
            ).format(p.b.get(int(n)), p.b.get(int(n) - len(stdin)))
        )

    if "numbers" not in variables:
        raise CodersLabException(
            "Could not find variable {}".format(p.b.get("numbers"))
        )

    if type(variables["numbers"]) != list:
        raise CodersLabException(
            dedent(
                """
                Expected {} to be of type {}, but it is {}
                """
            ).format(
                p.b.get("numbers"),
                p.b.get("list"),
                p.b.get(type(variables["numbers"]).__name__),
            )
        )


@tc.test(
    "Script reads {n} numbers and displays their sum and average",
    params=[
        {"n": "6", "numbers": ["1", "3", "9", "35", "11", "2"]},
        {"n": "7", "numbers": ["5", "15", "6", "4", "6", "7", "0"]},
        {"n": "8", "numbers": ["3", "6", "4", "6", "7", "8", "-20", "-50"]},
    ],
    aborts=True,
)
def test_n(stdin, stdout, invoke, n, numbers, history, **kwargs):
    stdin.append(n)
    stdin.extend(numbers)

    variables = invoke()

    try:
        line = next(line for line in stdout if "sum" in line.lower())
    except StopIteration:
        raise CodersLabException(
            dedent(
                """
                Could not find the word {} in the printed text::
                {}
                """
            ).format(p.b.get("Sum"), p.b.get("".join(h["text"] for h in history)))
        )

    try:
        sum_value = float("".join(c for c in line if c in "0123456789.-"))
    except:
        raise CodersLabException(
            dedent(
            """
            Could not extract sum from line: {}
            """
            ).format(p.b.get(line))
        )

    try:
        line = next(line for line in stdout if "average" in line.lower())
    except StopIteration:
        raise CodersLabException(
            dedent(
                """
                Could not find the word {} in the printed text:
                {}
                """
            ).format(p.b.get("Average"), p.b.get("".join(h["text"] for h in history)))
        )

    try:
        avg_value = float("".join(c for c in line if c in "0123456789.-"))
    except:
        raise CodersLabException(
            dedent(
                """
                Could not extract average from line: {}
                """
            ).format(p.b.get(line))
        )

    expected_sum = sum(map(int, numbers))
    expected_avg = expected_sum / int(n)

    if sum_value != expected_sum:
        raise CodersLabException(
            dedent(
                """
                Scripts calculates the sum of numbers {} as {}.
                Expected result is {}
                """
            ).format(
                p.b.get(", ".join(numbers)),
                p.b.get(sum_value),
                p.b.get(expected_sum),
            )
        )

    if avg_value != expected_avg:
        raise CodersLabException(
            dedent(
                """
                Script calculates the average of numbers {} as {}.
                Expected result is {}
                """
            ).format(
                p.b.get(", ".join(numbers)),
                p.b.get(avg_value),
                p.b.get(expected_avg),
            )
        )

    if expected_avg > expected_sum:
        expected = "average is greater"
    else:
        expected = "sum is greater"

    try:
        next(line for line in stdout if expected in line.lower())
    except:
        raise CodersLabException(
            dedent(
                """
                Could not find the line: {} in the text printed by the script:
                {}
                """
            ).format(
                p.b.get(expected),
                p.b.get("".join(h["text"] for h in history)),
            )
        )


tc.run()
