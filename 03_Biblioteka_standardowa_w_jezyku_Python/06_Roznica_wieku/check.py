import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Age difference")


@tc.test(
    "Variable '{name}' exists and has the value {value} of type int",
    params=(
        {"name": "father", "value": 1974},
        {"name": "child", "value": 2007},
    ),
    aborts=True,
)
def test_variables(invoke, name, value, **kwargs):
    variables = invoke()

    if name not in variables:
        raise CodersLabException("Could not find the variable {}".format(p.b.get(name)))

    if variables[name] != value:
        raise CodersLabException(
            "Incorrect value of {} variable".format(p.b.get(name))
        )


@tc.test("Expected text is printed", aborts=True)
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    if not any("Father is 33 years older" in l for l in stdout):
        raise CodersLabException("Could not find the expected text")


tc.run()
