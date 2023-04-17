import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Comparing numbers")


@tc.test("Numbers are saved in variables a and b", aborts=True)
def test_a_b(invoke, stdin, **kwargs):
    stdin.append("123456")
    stdin.append("345678")

    variables = invoke()

    if "a" not in variables:
        raise CodersLabException("Could not find variable {}".format(p.b.get("a")))

    if "b" not in variables:
        raise CodersLabException("Could not find variable {}".format(p.b.get("b")))

    if str(variables["a"]).split('.')[0] != "123456":
        raise CodersLabException(
            "Numeric keyboard input was not saved "
            "in the {} variable.".format(p.b.get("a"))
        )

    if str(variables["b"]).split('.')[0] != "345678":
        raise CodersLabException(
            "Numeric keyboard input was not saved "
            "in the {} variable.".format(p.b.get("b"))
        )


@tc.test(
    "Numbers {a} and {b} are compared correctly",
    params=[
        {"a": "123", "b": "456", "greater": "b"},
        {"a": "456", "b": "123", "greater": "a"},
    ],
    aborts=True,
)
def test_comparison_lex(invoke, stdin, stdout, a, b, greater, history, **kwargs):
    stdin.append(a)
    stdin.append(b)

    invoke()

    tc.assert_print_called(stdout)

    if "{} is greater!".format(greater) not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Could not find the phrase {} in the printed text.

                Printed lines:
                {}
                """
            ).format(
                p.b.get("{} is greater!".format(greater)),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


@tc.test(
    "Numbers {a} and {b} are compared correctly",
    params=[
        {"a": "123", "b": "56", "greater": "a", "smaller": "b"},
        {"a": "99", "b": "789", "greater": "b", "smaller": "a"},
    ],
    aborts=True,
)
def test_comparison_as_number(
    invoke, stdin, stdout, a, b, greater, smaller, history, **kwargs
):
    stdin.append(a)
    stdin.append(b)

    invoke()

    wrong = "{} is greater!".format(smaller)

    if wrong in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Incorrect result ({}) found in the printed text:
                Likely reason is that the input data was compared as strings,
                not as numbers.
                "{}" looks like greater than "{}" because 
                "{}" is behind "{}" in "computer alphabet".

                To compare them as numbers use the {} function.

                Example:
                >>> a = "12"
                >>> b = "34"
                >>> a + b
                "1234"
                >>> float(a) + float(b)
                46

                """
            ).format(
                p.b.get(wrong),
                p.b.get(min(a, b)),
                p.b.get(max(a, b)),
                p.b.get(str(max(a, b))[0]),
                p.b.get(str(min(a, b))[0]),
                p.b.get("float"),
            )
        )

    correct = "{} is greater!".format(greater)


tc.run()
