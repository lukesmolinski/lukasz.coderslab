from ast import walk, Call, Attribute, Constant
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Joining elements of a list")


@tc.test("Variable 'letters' exists and has expected value", aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "letters" not in variables:
        raise CodersLabException("Variable {} was not found".format(p.b.get("letters")))

    if variables["letters"] != ["a", "b", "c", "d", "e"]:
        raise CodersLabException(
            dedent(
                """
                Expected the variable {} to have the value {}.
                Its current value is {}.
                """
            ).format(
                p.b.get("letters"),
                p.b.get(["a", "b", "c", "d", "e"]),
                p.b.get(variables["letters"]),
            )
        )


@tc.test("'join' method has been used")
def test_variable(ast, **kwargs):
    for node in walk(ast):
        if (
            isinstance(node, Call)
            and isinstance(node.func, Attribute)
            and node.func.attr == "join"
        ):
            return

    raise CodersLabException(
        dedent(
            """
            Could not find the {} method used as required in this exercise. 
            Example:
            {}
            {}
            """
        ).format(
            p.b.get("join"),
            p.b.get('>>> print(" && ".join(["A", "B", "CDE"]))'),
            p.b.get("A && B && CDE"),
        )
    )


@tc.test("Text appears on the screen")
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    if not any("a b c d e" in line for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Expected phrase: {} did not appear on the screen.
                Printed text:
                {}
                """
            ).format(
                p.b.get("a b c d e"),
                p.b.get("".join(stdout)),
            )
        )


tc.run()
