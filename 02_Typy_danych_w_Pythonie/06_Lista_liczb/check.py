import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("List of numbers")


@tc.test("Variable 'numbers' exists", aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "numbers" not in variables:
        raise CodersLabException(
            dedent(
                """
                Could not find a variable named {}
                """
            ).format(p.b.get("numbers"))
        )


@tc.test("Variable 'numbers' contains numbers from 1 to 8", aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if variables["numbers"] != [1, 2, 3, 4, 5, 6, 7, 8]:
        raise CodersLabException(
            dedent(
                """
                Variable {} contains different data than specified by exercise instructions.
                """
            ).format(p.b.get("numbers"))
        )


@tc.test("Second to last number is printed", aborts=True)
def test_variable(invoke, stdout, **kwargs):
    invoke()

    if not stdout:
        raise CodersLabException(
            dedent(
                """
                No lines were printed.
                Has {} function been used?
                """
            ).format(p.b.get("print"))
        )

    if stdout != ["7\n"]:
        raise CodersLabException(
            dedent(
                """
                The required number (7) was not printed. Printed lines:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
