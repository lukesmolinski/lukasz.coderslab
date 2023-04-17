import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("Defining a list of numbers")


@tc.test("Numbers are printed")
def test_print(invoke, stdout, **kwargs):
    invoke()

    for i in range(1, 9):
        try:
            next(l for l in stdout if "number: {}".format(i) in l.lower())
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Could not find the required phrase {} in the text printed by the script:
                    {}
                    """
                ).format(p.b.get("number: {}".format(i)), p.b.get("".join(stdout)))
            )

    try:
        next(l for l in stdout if "number: 0" in l.lower())
    except:
        pass
    else:
        raise CodersLabException(
            dedent(
                """
                Script printed a phrase ({}) that should not appear!
                """
            ).format(
                p.b.get("number: 0"),
            )
        )

    try:
        next(l for l in stdout if "number: 9" in l.lower())
    except:
        pass
    else:
        raise CodersLabException(
            dedent(
                """
                Script printed a phrase ({}) that should not appear!
                """
            ).format(
                p.b.get("number: 9"),
            )
        )


tc.run()
