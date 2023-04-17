import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Comparing variables")


@tc.test(
    'Variable "{name}" exists',
    params=(
        {"name": "a"},
        {"name": "b"},
        {"name": "result"},
    ),
    aborts=True,
)
def test_variables(invoke, name, **kwargs):
    variables = invoke()

    if name not in variables:
        raise CodersLabException("Could not find the variable {}".format(p.b.get(name)))


@tc.test("Variable 'result' has the result of comparison using >", aborts=True)
def test_result(invoke, **kwargs):
    variables = invoke()

    if variables["result"] != (variables["a"] > variables["b"]):
        raise CodersLabException(
            "Incorrect value of {} variable".format(p.b.get("result"))
        )


tc.run()
