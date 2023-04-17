import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Addition")


@tc.test("Variable add1 of type int exists")
def test_add1(invoke, **kwargs):
    variables = invoke()

    if "add1" not in variables:
        raise CodersLabException(
            dedent(
                """
                Could not find a variable named {}
                """
            ).format(p.b.get("add1"))
        )

    if type(variables["add1"]) != int:
        raise CodersLabException(
            dedent(
                """
                Variable {} does not have a value of type {}.
                """
            ).format(p.b.get("add1"), p.b.get("int"))
        )


@tc.test("Variable add2 of type float exists")
def test_add1(invoke, **kwargs):
    variables = invoke()

    if "add2" not in variables:
        raise CodersLabException(
            dedent(
                """
                Could not find a variable named {}
                """
            ).format(p.b.get("add2"))
        )

    if type(variables["add2"]) != float:
        raise CodersLabException(
            dedent(
                """
                Variable {} does not have a value of type {}.
                """
            ).format(p.b.get("add2"), p.b.get("float"))
        )


@tc.test("There is a variable 'result' with the sum of variables")
def test_result(invoke, **kwargs):
    variables = invoke()

    if "result" not in variables:
        raise CodersLabException(
            dedent(
                """
                Could not find a variable named {}
                """
            ).format(p.b.get("result"))
        )

    if variables["result"] != variables["add1"] + variables["add2"]:
        raise CodersLabException(
            dedent(
                """
                Variable {} has a different value than expected - the value is: {}
                """
            ).format(p.b.get("result"), p.b.get(variables["result"]))
        )


@tc.test("The outcome is displayed on the screen")
def test_print(invoke, stdout, **kwargs):
    variables = invoke()

    if not stdout:
        raise CodersLabException(
            dedent(
                """
                No lines were printed.
                Has {} function been used?
                """
            ).format(p.b.get("print"))
        )

    if str(variables["result"]) + "\n" not in stdout:
        raise CodersLabException(
            dedent(
                """
                Script did not print the expected result.
                Only the result of addition was expected.

                Printed lines:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
