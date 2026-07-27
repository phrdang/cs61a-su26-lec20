from ucb import main
from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader

# Links and Scheme lists

class Link:
    """A link has two instance attributes: first and rest. Second must be a Link or nil

    >>> s = Link(1, Link(2, nil))
    >>> s
    Link(1, Link(2, nil))
    >>> print(s)
    (1 2)
    >>> len(s)
    2
    >>> s[1]
    2
    >>> print(s.map(lambda x: x + 4))
    (5 6)
    """
    def __init__(self, first, rest):
        assert isinstance(rest, Link) or rest is nil
        self.first = first
        self.rest = rest

    def __repr__(self):
        return "Link({0}, {1})".format(repr(self.first), repr(self.rest))

    def __str__(self):
        s = "(" + str(self.first)
        rest = self.rest
        while isinstance(rest, Link):
            s += " " + str(rest.first)
            rest = rest.rest
        assert rest is nil
        return s + ")"

    def __len__(self):
        n, rest = 1, self.rest
        while isinstance(rest, Link):
            n += 1
            rest = rest.rest
        if rest is not nil:
            raise TypeError("length attempted on improper list")
        return n

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        y = self
        for _ in range(k):
            if y.rest is nil:
                raise IndexError("list index out of bounds")
            y = y.rest
        return y.first

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        return Link(mapped, self.rest.map(fn))

class nil:
    """The empty list"""

    def __repr__(self):
        return "nil"

    def __str__(self):
        return "()"

    def __len__(self):
        return 0

    def __getitem__(self, k):
        if k < 0:
            raise IndexError("negative index into list")
        raise IndexError("list index out of bounds")

    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance

# Scheme list parser, without quotation or dotted lists.

def scheme_read(src):
    """Read the next expression from src, a Buffer of tokens.

    >>> lines = ['(+ 1 ', '(+ 23 4)) (']
    >>> src = Buffer(tokenize_lines(lines))
    >>> print(scheme_read(src))
    (+ 1 (+ 23 4))
    """
    if src.current() is None:
        raise EOFError
    val = src.pop()
    if val == 'nil':
        return nil
    elif type(val) in (float, int):
        return val
    elif val not in DELIMITERS:  # ( ) ' .
        return val
    elif val == "(":
        val = read_tail(src)

        # #Note that this isn't the best idea of what to do.
        # #We have to add this semi-hack because we're modifying the language
        # #in a strange way to get infix notation.
        # if val.rest == nil and val.first != nil:
        #     val = val.first

        # "***YOUR CODE HERE***"
        return val
    else:
        raise SyntaxError("unexpected token: {0}".format(val))

def read_tail(src):
    """Return the remainder of a list in src, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Link(2, Link(3, nil))
    >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
    Link(2, Link(Link(3, Link(4, nil)), nil))
    """
    if src.current() is None:
        raise SyntaxError("unexpected end of file")
    if src.current() == ")":
        src.pop()
        return nil
    first = scheme_read(src)
    rest = read_tail(src)
    return Link(first, rest)


# Interactive loop

def buffer_input(prompt: str):
    return Buffer(tokenize_lines(InputReader(f'{prompt}> ')))

@main
def read_print_loop():
    """Run a read-print loop for Scheme expressions."""
    while True:
        try:
            src = buffer_input('read')
            while src.more_on_line:
                expression = scheme_read(src)
                print(f"str : {expression}")
                print(f"repr: {repr(expression)}")
                print()
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Exiting Scheme Reader...')
            return
