import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Math operations")


@tc.test(
    "There is a variable {name} with a proper value",
    params=(
        {"name": "a1", "value": 25},
        {"name": "a2", "value": 10},
        {"name": "sum_value", "value": 35},
        {"name": "quotus", "value": 2.5},
        {"name": "int_part", "value": 2},
    ),
    aborts=False,
)
def test_variables(invoke, name, value, **kwargs):
    variables = invoke()
    if name not in variables:
        raise CodersLabException(
            dedent(
                """
                Could not find a variable named {}
                """
            ).format(p.b.get(name))
        )

    if variables[name] != value:
        raise CodersLabException(
            dedent(
                """
                Variable {} has a different value than expected
                """
            ).format(p.b.get(name))
        )


@tc.test("Printing the value on the screen")
def test_print(invoke, stdout, **kwargs):
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

    if stdout != ["25\n", "10\n", "35\n", "2.5\n", "2\n"]:
        raise CodersLabException(
            dedent(
                """
                Expected lines were not printed on the screen. 
                Printed lines:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
