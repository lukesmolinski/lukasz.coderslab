import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Sum of numbers")


@tc.test(
    "Displays correct sum for n = {n}",
    params=[
        {"n": "2"},
        {"n": "3"},
        {"n": "5"},
        {"n": "7"},
        {"n": "100"},
        {"n": "567"},
    ],
    aborts=True,
)
def test_print(invoke, stdin, n, stdout, history, **kwargs):
    stdin.append(n)

    invoke()

    tc.assert_print_called(stdout)

    expected = str(sum(range(int(n) + 1)))

    if expected not in "".join(stdout):
        raise CodersLabException(
            dedent(
                """
                Could not find the expected result. Expected number {}. 
                Printed lines:
                {}
                """
            ).format(
                p.b.get(expected),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


tc.run()
