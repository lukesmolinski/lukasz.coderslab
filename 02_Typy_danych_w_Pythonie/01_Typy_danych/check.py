import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Data types")


@tc.test(
    "A variable with data of type {name} exists",
    params=(
        {"name": "int", "type_": int},
        {"name": "float", "type_": float},
        {"name": "bool", "type_": bool},
        {"name": "str", "type_": str},
    ),
)
def test_variables(invoke, name, type_, **kwargs):
    variables = invoke()

    types = {type(value) for value in variables.values()}

    if type_ not in types:
        raise CodersLabException(
            """
            Could not find a variable with value of type {}
            """.format(
                p.b.get(name)
            )
        )


@tc.test("Printing names and values", points=5)
def test_printing(invoke, stdout, **kwargs):
    variables = invoke()

    tc.assert_print_called(stdout)

    relevant_lines = [line for line in stdout if line.startswith("Variable")]
    if not relevant_lines:
        raise CodersLabException(
            """
            Could not find a line that starts with "Variable"
            in the lines:
            {}
            """.format(
                p.b.get("".join(stdout))
            )
        )

    mentioned_variables = []
    for line in relevant_lines:
        try:
            mentioned_variables.append(line.split()[1])
        except IndexError:
            raise CodersLabException(
                dedent(
                    """
                    Reading which variable the line:
                    {}
                    refers to was not possible.
                    """
                ).format(p.b.get(line))
            )

    for name in mentioned_variables:
        if not any(
            line.split()[:4] == ["Variable", name, "has", "value"]
            for line in relevant_lines
        ):
            raise CodersLabException(
                dedent(
                    """
                    In the printed lines:
                    {}
                    Could not find a line that starts with:
                    {}
                    """
                ).format(
                    p.b.get("".join(stdout)),
                    p.b.get("Variable {} has value".format(name)),
                )
            )
    if len(mentioned_variables) != 4:
        raise CodersLabException(
            """
            Expected to print four variables, found {}: {}
            """.format(
                len(mentioned_variables), ", ".join(mentioned_variables)
            )
        )

    for name in mentioned_variables:
        if name not in variables:
            raise CodersLabException(
                dedent(
                    """
                    Printed a value of variable {} that could not be found in the code... typo?
                    """
                ).format(p.b.get(name))
            )

        real_value = variables[name]
        relevant_line = next(
            line
            for line in relevant_lines
            if line.split()[:4] == ["Variable", name, "has", "value"]
        )

        if not relevant_line.strip().endswith(str(real_value).strip()):
            raise CodersLabException(
                dedent(
                    """
                    Variable {} has value:
                    {}
                    but the print says it's:
                    {}
                    """
                ).format(
                    p.b.get(name),
                    p.b.yellow.get(real_value),
                    p.b.yellow.get("".join(relevant_line.split(maxsplit=4)[4:])),
                )
            )


tc.run()
