"""An interpreter for the Scheme Calculator Language

An interpreter for a calculator language that uses prefix-order call syntax.
Operator expressions must be operator symbols.  Operand expressions are
separated by spaces.

Examples:
    scalc> (* 1 2 3)
    6
    scalc> (+)
    0
    scalc> (+ 2 (/ 4 8))
    2.5
    scalc> (+ 2 2) (* 3 3)
    4
    9
    scalc> (+ 1
         (- 23)
         (* 4 2.5))
    -12
    scalc> )
    SyntaxError: unexpected token: )
    scalc> 2.3.4
    ValueError: invalid numeral: 2.3.4
    scalc> +
    TypeError: + is not a number or call expression
    scalc> (/ 5)
    TypeError: / requires exactly 2 arguments
    scalc> (/ 1 0)
    ZeroDivisionError: division by zero
"""

from ucb import main
from operator import add, sub, mul, truediv, floordiv
from scheme_reader import Link, nil, scheme_read, buffer_input
from typing import Union
from collections.abc import Callable


# Eval & Apply

env = {} # The global environment

def calc_eval(exp: Union[int, float, str, Link]) -> Union[int, float, str]:
    """Evaluate a Calculator expression.

    >>> calc_eval(10)  # numbers are self-evaluating
    10
    >>> calc_eval(25.7437)
    25.7437
    >>> calc_eval(as_scheme_list('+', 2, as_scheme_list('*', 4, 6)))  # (+ 2 (* 4 6))
    26
    >>> calc_eval(as_scheme_list('+', 2, as_scheme_list('/', 40, 5)))  # (+ 2 (/ 40 5))
    10
    >>> calc_eval(as_scheme_list('define', 'x', 3))  # (define x 3)
    'x'
    >>> calc_eval('x')  # symbols are also expressions
    3
    >>> calc_eval(as_scheme_list('+', 'x', 2))  # you can use variables in expressions, ex: (+ x 2)
    5
    >>> calc_eval(as_scheme_list('*', 'x', as_scheme_list('+', 2, 'x')))  # (* x (+ 2 x))
    15
    >>> calc_eval('y')
    Traceback (most recent call last):
        ...
    NameError: Undefined variable 'y'
    """
    if type(exp) in (int, float):
        return simplify(exp)
    if type(exp) is str:
        "*** YOUR CODE HERE (replace this entire block, including the return statement) ***"
        return nil
    elif isinstance(exp, Link):
        if exp.first == "define":
            return do_define_form(exp.rest)
        arguments = exp.rest.map(calc_eval)
        return simplify(calc_apply(exp.first, arguments))
    else:
        raise TypeError(exp + ' is not a primitive or call expression')

def do_define_form(vals: Link) -> str:
    """
    Defines (or redefines) a variable in the global environment,
    and returns that symbol as a Python string.

    >>> do_define_form(as_scheme_list('x', 5))
    'x'
    >>> env['x']
    5
    >>> do_define_form(as_scheme_list('x', 10))
    'x'
    >>> env['x']
    10
    >>> do_define_form(as_scheme_list('y', 2))
    'y'
    >>> env['y']
    2
    """
    "*** YOUR CODE HERE (replace this entire block, including the return statement) ***"
    return nil

def calc_apply(operator: str, args: Link) -> Union[int, float]:
    """Apply the named operator to a list of args.

    Basic arithmetic doctests:

    >>> calc_apply('+', as_scheme_list(1, 2, 3))
    6
    >>> calc_apply('-', as_scheme_list(10, 1, 2, 3))
    4
    >>> calc_apply('+', nil)
    0
    >>> calc_apply('*', nil)
    1
    >>> calc_apply('/', as_scheme_list(5))
    0.2
    >>> calc_apply('-', as_scheme_list(2))
    -2
    >>> calc_apply('*', as_scheme_list(1, 2, 3, 4, 5))
    120
    >>> calc_apply('/', as_scheme_list(40, 5))
    8.0

    Quotient doctests:

    >>> calc_apply('quotient', as_scheme_list(40, 5))
    8
    >>> calc_apply('quotient', as_scheme_list(10, 3))
    3

    Raising exceptions doctests:

    >>> calc_apply('-', nil)
    Traceback (most recent call last):
        ...
    TypeError: '-' operator requires at least 1 argument
    >>> calc_apply('/', nil)
    Traceback (most recent call last):
        ...
    TypeError: '/' operator requires at least 1 argument
    >>> calc_apply('quotient', as_scheme_list(40))
    Traceback (most recent call last):
        ...
    TypeError: 'quotient' operator requires exactly 2 arguments
    >>> calc_apply('quotient', nil)
    Traceback (most recent call last):
        ...
    TypeError: 'quotient' operator requires exactly 2 arguments
    >>> calc_apply('**', nil)
    Traceback (most recent call last):
        ...
    TypeError: '**' is an unknown operator
    """
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')
    if operator == '+':
        "*** YOUR CODE HERE (replace this entire block, including the return statement) ***"
        return 0
    elif operator == '-':
        "*** YOUR CODE HERE (replace this entire block, including the return statement) ***"
        return 0
    elif operator == '*':
        "*** YOUR CODE HERE (replace this entire block, including the return statement) ***"
        return 0
    elif operator == '/':
        "*** YOUR CODE HERE (replace this entire block, including the return statement) ***"
        return 0

def simplify(value: Union[int, float, str]) -> Union[int, float, str]:
    """Return an int if value is an integer, or value otherwise.

    >>> simplify(8.0)
    8
    >>> simplify(2.3)
    2.3
    >>> simplify('+')
    '+'
    >>> simplify('f')
    'f'
    """
    if isinstance(value, float) and int(value) == value:
        return int(value)
    return value

def reduce(fn: Callable, scheme_list: Link, start):
    """Reduce a recursive list of Links using fn and a start value.

    >>> reduce(add, as_scheme_list(1, 2, 3), 0)
    6
    >>> reduce(sub, as_scheme_list(20, 5), 30)
    5
    """
    if scheme_list is nil:
        return start
    return reduce(fn, scheme_list.rest, fn(start, scheme_list.first))

def as_scheme_list(*args) -> Link:
    """Return a recursive list of Links that contains the elements of args.

    >>> as_scheme_list(1, 2, 3)
    Link(1, Link(2, Link(3, nil)))
    >>> as_scheme_list(4)
    Link(4, nil)
    """
    if len(args) == 0:
        return nil
    return Link(args[0], as_scheme_list(*args[1:]))

@main
def read_eval_print_loop():
    """Run a read-eval-print loop for Calculator."""
    while _________:
        try:
            src = buffer_input('scalc')
            while src.more_on_line:
                expression = _________(src)
                print(_________(expression))
        except (SyntaxError, TypeError, ValueError, ZeroDivisionError, NameError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Exiting Scheme Calculator...')
            return
