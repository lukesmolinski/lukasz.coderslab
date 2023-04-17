import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Reading data from user input")


@tc.test(
    "Script asks for name and surname and displays text",
    params=(
        {"name": "George", "surname": "Orwell"},
        {"name": "Julius", "surname": "Caesar"},
    ),
)
def test_script(invoke, stdin, stdout, history, name, surname, **kwargs):
    stdin.append(name)
    stdin.append(surname)

    invoke()

    tc.assert_print_called(stdout)

    expected = "{} {} is a Python programmer".format(name, surname)

    if not any(expected.lower() in line.lower() for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Required phrase: {} was not found.
                Printed text:
                {}
                """
            ).format(p.b.get(expected), p.b.get("".join(h["text"] for h in history)))
        )


tc.run()
