import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Comparing names")


@tc.test(
    "Saving name to a variable {name}",
    params=[
        {"name": "first_name", "value": "FirstTestName"},
        {"name": "second_name", "value": "SecondTestName"},
    ],
    aborts=True,
)
def test_variables(invoke, stdin, name, value, **kwargs):
    stdin.append("FirstTestName")
    stdin.append("SecondTestName")

    variables = invoke()

    if name not in variables:
        raise CodersLabException(
            dedent(
                """
                Script did not create variable {}
                """
            ).format(p.b.get(name))
        )

    if variables[name] != value:
        raise CodersLabException(
            dedent(
                """
                Script did not store the keyboard input in the variable {}
                """
            ).format(p.b.get(name))
        )


@tc.test(
    "Names {name1} and {name2}",
    params=[
        {"name1": "Athos", "name2": "Athos", "same": True},
        {"name1": "Porthos", "name2": "Porthos", "same": True},
        {"name1": "Aramis", "name2": "Aramis", "same": True},
        {"name1": "Yarpen", "name2": "Dandelion", "same": False},
        {"name1": "Yarpen", "name2": "Philippa", "same": False},
        {"name1": "Philippa", "name2": "Dandelion", "same": False},
    ],
    aborts=True,
)
def test_same_names(invoke, stdin, stdout, history, name1, name2, same, **kwargs):
    stdin.append(name1)
    stdin.append(name2)

    invoke()

    tc.assert_print_called(stdout)

    if "Enter your name".lower() not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Looks like the script didn't ask for the first name.
                Expected to see {}.

                Script prints:
                {}
                """
            ).format(
                p.b.get("Enter your name"),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )

    if "Enter your middle name".lower() not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Looks like the script didn't ask for the middle name.
                Expected to see {}.

                Script prints:
                {}
                """
            ).format(
                p.b.get("Enter your middle name"),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )

    expected = "Same" if same else "Different"

    if expected.lower() not in "".join(stdout).lower():
        raise CodersLabException(
            dedent(
                """
                Looks like the script didn't show comparison result.
                Expected to see {}.

                Script prints:
                {}
                """
            ).format(
                p.b.get(expected),
                p.b.get("".join(h.get("text", "") for h in history)),
            )
        )


tc.run()
