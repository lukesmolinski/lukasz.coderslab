import os
import sys
import datetime


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("User's age")


@tc.test(
    "Script asks for name and year and stores them in variables",
    params=(
        {"name": "Camilla", "year": "1980"},
        {"name": "Martin", "year": "1999"},
        {"name": "Hedwig", "year": "1975"},
        {"name": "Richard", "year": "2002"},
    ),
    aborts=True,
)
def test_print(invoke, stdin, name, year, **kwargs):
    stdin.append(name)
    stdin.append(year)

    variables = invoke()

    for name, value in (("name", name), ("year", year)):
        if name not in variables:
            raise CodersLabException("Could not find the variable {}".format(p.b.get(name)))
        if str(variables[name]) != value:
            raise CodersLabException(
                "Incorrect value of {} variable".format(p.b.get(name))
            )


@tc.test(
    "Script correctly calculates the age and saves it in 'age' variable",
    params=(
        {"name": "Camilla", "year": "1980"},
        {"name": "Martin", "year": "1999"},
        {"name": "Hedwig", "year": "1975"},
        {"name": "Richard", "year": "2002"},
    ),
    aborts=True,
)
def test_print(invoke, stdin, name, year, **kwargs):
    stdin.append(name)
    stdin.append(year)

    variables = invoke()

    if "age" not in variables:
        raise CodersLabException("Could not find the variable {}".format(p.b.get("age")))
    if int(variables["age"]) != datetime.date.today().year - int(year):
        raise CodersLabException(
            "Variable {} has incorrect value".format(p.b.get("age"))
        )


@tc.test(
    "Script displays correct text",
    params=(
        {"name": "Camilla", "year": "1980"},
        {"name": "Martin", "year": "1999"},
        {"name": "Hedwig", "year": "1975"},
        {"name": "Richard", "year": "2002"},
    ),
    aborts=True,
)
def test_print(invoke, stdin, stdout, history, name, year, **kwargs):
    stdin.append(name)
    stdin.append(year)

    variables = invoke()

    age = datetime.date.today().year - int(year)

    expected = "User: {} is {} years old".format(name, age)

    if expected not in "".join(stdout):
        raise CodersLabException(
            dedent(
                """
                Could not find the expected phrase {}.
                Printed text:
                {}
                """
            ).format(p.b.get(expected), p.b.get("".join(h["text"] for h in history)))
        )


tc.run()
