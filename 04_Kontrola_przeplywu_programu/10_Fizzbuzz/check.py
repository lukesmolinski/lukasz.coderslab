import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), "..", "..")))


from testrunner import CodersLabTestSuite, CodersLabException, p, dedent


tc = CodersLabTestSuite("FizzBuzz")


@tc.test("Expected numbers are printed")
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = [str(n) for n in range(1, 101) if n % 3 and n % 5]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Could not find expected line: {} 
                    Printed lines:
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


@tc.test("'Fizz' is printed in all the right places")
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = ["Fizz" if n % 3 == 0 else str(n) for n in range(1, 101) if n % 5]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Could not find expected line: {} 
                    Printed lines:
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


@tc.test("'Buzz' is printed in all the right places")
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = ["Buzz" if n % 5 == 0 else str(n) for n in range(1, 101) if n % 3]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Could not find expected line: {} 
                    Printed lines:                    
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


@tc.test("'FizzBuzz' is printed in all the right places")
def test_numbers(invoke, stdout, **kwargs):
    invoke()

    expected = [
        "FizzBuzz" if n % 5 == n % 3 == 0 else str(n)
        for n in range(1, 101)
        if n % 5 == n % 3 == 0 or n % 5 and n % 3
    ]

    it = iter(stdout)

    for e in expected:
        try:
            while e not in next(it):
                pass
        except StopIteration:
            raise CodersLabException(
                dedent(
                    """
                    Could not find expected line: {} 
                    Printed lines:                    
                    {}
                    """
                ).format(
                    p.b.get(e),
                    p.b.get("".join(stdout)),
                )
            )


tc.run()
