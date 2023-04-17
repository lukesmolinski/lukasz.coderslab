import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Quadratic equation")


@tc.test(
    "Numbers {a}, {b} and {c} are saved as a, b, c variables",
    params=[
        {"a": "12345", "b": "23456", "c": "34567"},
        {"a": "33443", "b": "44554", "c": "55665"},
        {"a": "-5", "b": "-10", "c": "-15"},
    ],
    aborts=True,
)
def test_a_b_c(invoke, stdin, a, b, c, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    for name, value in [("a", a), ("b", b), ("c", c)]:
        if name not in variables:
            raise CodersLabException("Could not find variable {}".format(p.b.get(name)))

        if str(variables[name]) not in (value, value + ".0"):
            raise CodersLabException(
                ("Variable {} has different value than the keyboard input").format(
                    p.b.get(name)
                )
            )

        if type(variables[name]) == int:
            raise CodersLabException(
                dedent(
                    """
                    Variable {} has a value of type {}. Better than {}, 
                    but what about numbers like 5.25?
                    """
                ).format(
                    p.b.get(name),
                    p.b.get("int"),
                    p.b.get("str"),
                )
            )

        if type(variables[name]) == str:
            raise CodersLabException(
                dedent(
                    """
                    Variable {} has a value of type {}.
                    Exercise requires the {} variable to have 
                    the value cast in the type that enables
                    performing mathematical operations on it. 
                    """
                ).format(
                    p.b.get(name),
                    p.b.get("str"),
                    p.b.get(name),
                )
            )

        if type(variables[name]) != float:
            raise CodersLabException(
                dedent(
                    """
                    Variable {} has a value of type {}.
                    Exercise requires the {} variable to have 
                    the value cast in the type that enables
                    performing mathematical operations on it.
                    """
                ).format(
                    p.b.get(name),
                    p.b.get(type(variables[name]).__name__),
                    p.b.get(name),
                )
            )


@tc.test(
    "Calculating delta for params {a}, {b} and {c}",
    params=[
        {"a": "2", "b": "6", "c": "3", "delta": 12.0},
        {"a": "2", "b": "5", "c": "3", "delta": 1.0},
        {"a": "1", "b": "8", "c": "16", "delta": 0.0},
        {"a": "2", "b": "4", "c": "3", "delta": -8.0},
    ],
    aborts=True,
)
def test_delta(invoke, stdin, a, b, c, delta, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    if "delta" not in variables:
        raise CodersLabException("Could not find variable {}".format(p.b.get("delta")))

    if variables["delta"] != delta:
        raise CodersLabException(
            dedent(
                """
                Incorrect value of variable {}.
                Script returned value: {},
                expected: {}.
                """
            ).format(
                p.b.get("delta"),
                p.b.get(variables["delta"]),
                p.b.get(delta),
            )
        )


@tc.test(
    "Calculating x_1 and x_2 for params {a}, {b} and {c}",
    params=[
        {"a": "5", "b": "9", "c": "4", "delta": 1, "x1": -1.0, "x2": -0.8},
        {"a": "2", "b": "-7", "c": "6", "delta": 1, "x1": 1.5, "x2": 2},
        {"a": "9", "b": "6", "c": "1", "delta": 0, "x1": -1/3, "x2": -1/3},
    ],
    aborts=True,
)
def test_x1_x2(invoke, stdin, stdout, a, b, c, delta, x1, x2, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    for name, value in (("x_1", x1), ("x_2", x2)):
        if name not in variables:
            raise CodersLabException("Could not find the variable {}".format(p.b.get(name)))

        if variables[name] != value:
            raise CodersLabException(
                dedent(
                    """
                    Incorrect value of variable {}.
                    Script returned value: {},
                    expected: {}.
                    """
                ).format(
                    p.b.get(name),
                    p.b.get(variables[name]),
                    p.b.get(value),
                )
            )


@tc.test(
    "Displaying results for params {a}, {b} and {c} (positive delta)",
    params=[
        {"a": "5", "b": "9", "c": "4", "delta": 1, "x1": -1.0, "x2": -0.8},
        {"a": "2", "b": "-7", "c": "6", "delta": 1, "x1": 1.5, "x2": 2},
    ],
    aborts=True,
)
def test_print_x1_x2(invoke, stdin, stdout, history, a, b, c, delta, x1, x2, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    tc.assert_print_called(stdout)

    for name, value in (("x_1", x1), ("x_2", x2)):
        if "{} = {}".format(name, value) not in "".join(stdout).lower():
            raise CodersLabException(
                dedent(
                    """
                    Could not find the expected result in the text
                    Expected: {}
                    Printed lines:
                    {}
                    """
                ).format(
                    p.b.get("{} = {}".format(name, value)),
                    p.b.get("".join(h.get("text", "") for h in history)),
                )
            )


@tc.test(
    "Displaying results for params {a}, {b} and {c} (delta=0)",
    params=[
        {"a": "9", "b": "6", "c": "1", "x": -1/3},
        {"a": "4", "b": "-4", "c": "1", "x": 0.5},
    ],
    aborts=True,
)
def test_print_x12(invoke, stdin, stdout, history, a, b, c, x, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    tc.assert_print_called(stdout)

    if "x_1 = x_2 = {}".format(x) not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Could not find the expected result in the text
                Expected: {}
                Printed lines:
                {}
                """
            ).format(
                p.b.get("x_1 = x_2 = {}".format(x)),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


@tc.test(
    "Displaying results for params {a}, {b} and {c} (negative delta)",
    params=[
        {"a": "9", "b": "6", "c": "2"},
        {"a": "4", "b": "-4", "c": "2"},
    ],
    aborts=True,
)
def test_no_solution(invoke, stdin, stdout, history, a, b, c, **kwargs):
    stdin.append(a)
    stdin.append(b)
    stdin.append(c)

    variables = invoke()

    tc.assert_print_called(stdout)

    if "no solution" not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Could not find the expected result in the text
                Expected: {}
                Printed lines:
                {}
                """
            ).format(
                p.b.get("no solution"),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


tc.run()
