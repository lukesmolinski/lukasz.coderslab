import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Adding elements to the list")


@tc.test("The list has three elements")
def test_length(invoke, **kwargs):
    variables = invoke()

    if "animals" not in variables:
        raise CodersLabException(
            dedent(
                """
                Could not find a variable named {}
                """
            ).format(p.b.get("animals"))
        )

    if type(variables["animals"]) != list:
        raise CodersLabException(
            dedent(
                """
                Variable {} is not a list
                """
            ).format(p.b.get("animals"))
        )

    if len(variables["animals"]) != 3:
        raise CodersLabException(
            dedent(
                """
                Variable {} does not have 3 elements. It has {}!
                """
            ).format(p.b.get("animals"), p.b.get(len(variables["animals"])))
        )


tc.run()
