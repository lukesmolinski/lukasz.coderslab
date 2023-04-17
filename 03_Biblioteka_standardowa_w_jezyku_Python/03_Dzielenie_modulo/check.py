from ast import walk, Call, Attribute, Constant
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Modulo division")


@tc.test('Variables "a", "b" and "result" exist', aborts=True)
def test_variables(invoke, **kwargs):
    variables = invoke()

    for name in ("a", "b", "result"):
        if name not in variables:
            raise CodersLabException("Variable {} not found".format(p.b.get(name)))

        if not isinstance(variables[name], (int, float)):
            raise CodersLabException(
                dedent(
                    """
                    Expected {} variable to be of {} or {} type.
                    Its current type is {}.
                    """
                ).format(
                    p.b.get(name),
                    p.b.get("int"),
                    p.b.get("float"),
                    p.b.get(type(variables[name]).__name__),
                )
            )


@tc.test('Variable "result" has the correct value')
def test_variables(invoke, **kwargs):
    variables = invoke()

    if variables["a"] % variables["b"] != variables["result"]:
        raise CodersLabException(
            dedent(
                """
                Foe a={} and b={} expected value of {} variable was {}.
                Its current value is {}.
                """
            ).format(
                p.b.get(variables["a"]),
                p.b.get(variables["b"]),
                p.b.get("result"),
                p.b.get(variables["a"] % variables["b"]),
                p.b.get(variables["result"]),
            )
        )


tc.run()
