import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("List of numbers")


@tc.test("Variable 'characters' still exists", aborts=True)
def test_variable(invoke, **kwargs):
    variables = invoke()

    if "characters" not in variables:
        raise CodersLabException(
            dedent(
                """
                Could not find a variable named {}
                """
            ).format(p.b.get("characters"))
        )


@tc.test(
    "{which} character is printed",
    params=(
        {"which": "First", "character": "Harry"},
        {"which": "Last", "character": "Hermione"},
    ),
    aborts=False,
)
def test_variable(invoke, stdout, character, **kwargs):
    invoke()

    if not stdout:
        raise CodersLabException(
            dedent(
                """
                Script printed no text.
                Has {} function been used?
                """
            ).format(p.b.get("print"))
        )

    if character + "\n" not in stdout:
        raise CodersLabException(
            dedent(
                """
                The required person was not printed. Printed lines:
                {}
                """
            ).format(p.b.get("".join(stdout)))
        )


tc.run()
