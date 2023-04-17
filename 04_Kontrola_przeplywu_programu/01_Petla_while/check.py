from ast import walk
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("While loop")


@tc.test("Script prints text")
def test_printing(invoke, stdout, **kwargs):
    invoke()

    if "I am a Python programmer".lower() in "".join(stdout).lower():
        return

    tc.assert_print_called(stdout)

    raise CodersLabException(
        "Could not find the required phrase "
        "in the text printed to the screen."
    )


@tc.test("Script prints text 10 times")
def test_printing_10_times(invoke, stdout, **kwargs):
    invoke()

    string = "".join(stdout).lower()
    count = string.count("I am a Python programmer".lower())

    if count != 10:
        raise CodersLabException(
            "The text was printed {} times, expected 10".format(count)
        )


tc.run()
