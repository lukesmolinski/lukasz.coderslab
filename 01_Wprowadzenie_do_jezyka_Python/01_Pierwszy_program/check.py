import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("First program")


@tc.test("Print function was used", aborts=True)
def test_print(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)


@tc.test("The text starts with the correct phrase", aborts=True)
def test_print_value(invoke, stdout, **kwargs):
    invoke()

    if not any("My name is" in line for line in stdout):
        raise CodersLabException(
            dedent(
                """
                Could not find the expected phrase {} in the text output to the screen
                Output text is:
                {}
                """
            ).format(
                p.b.get("My name is"),
                p.b.get("".join(stdout)),
            )
        )


tc.run()
