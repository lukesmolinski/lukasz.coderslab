from ast import walk, AugAssign, Add, Sub
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Incrementation and decrementation")


@tc.test("Text is printed to the screen", aborts=True)
def test_variables(invoke, stdout, **kwargs):
    variables = invoke()

    tc.assert_print_called(stdout)

    for expected in ("145", "146"):
        if not any(expected in line for line in stdout):
            raise CodersLabException(
                "Could not find the number: {} in the printed text".format(
                    p.b.get(expected)
                )
            )

    if "counter" not in variables:
        raise CodersLabException(
            "Could not find the variable: {}".format(p.b.get("counter"))
        )

    if variables["counter"] != 145:
        raise CodersLabException(
            dedent(
                """
                The final value of {} variable should be {}.
                Its current value is {}.
                """
            ).format(
                p.b.get("counter"),
                p.b.get("145"),
                p.b.get(variables["counter"]),
            )
        )


@tc.test(
    "Operator {op} has been used",
    params=(
        {"op": "+=", "cls": Add},
        {"op": "-=", "cls": Sub},
    ),
)
def test_variables(ast, op, cls, **kwargs):
    for node in walk(ast):
        if isinstance(node, AugAssign) and isinstance(node.op, cls):
            return

    raise CodersLabException(
        dedent(
            """
            Operator {} was not found in the code.
            """
        ).format(
            p.b.get(op),
        )
    )


tc.run()
