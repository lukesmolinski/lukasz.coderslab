import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Boolean values")


@tc.test(
    "There is a variable {name}",
    aborts=True,
    params=(
        {"name": "foo", "value": True},
        {"name": "bar", "value": False},
        {"name": "check", "value": False},
    ),
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
                Variable {} has a different value that expected
                """
            ).format(p.b.get(name))
        )


@tc.test("The text appears on the screen")
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

    if "Variable check has value False\n" not in stdout:
        raise CodersLabException(
            dedent(
                """
                Could not find the expected text. 
                Printed lines:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
