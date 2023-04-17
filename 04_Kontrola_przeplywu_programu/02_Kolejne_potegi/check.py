from ast import walk, For
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Subsequent powers")


@tc.test("Script prints sentences to the screen", aborts=True)
def test_printing(invoke, stdout, **kwargs):
    invoke()

    tc.assert_print_called(stdout)

    for num in range(11):
        phrase = "2 to the power of {} is {}".format(num, 2 ** num)
        if phrase not in "".join(stdout).lower():
            raise CodersLabException("Could not find the phrase {}".format(p.b.get(phrase)))


@tc.test("Solution of the exercises uses a 'for' loop", aborts=True)
def test_for_used(ast, **kwargs):
    for node in walk(ast):
        if isinstance(node, For):
            break

    else:
        raise CodersLabException(
            "Could not find the {} loop in in the code".format(p.b.get("for"))
        )


tc.run()
