import math
import operator as op

global global_env


class Symbol(str):
    def __init__(self, sym):
        self = sym


class Number(float):
    def __init__(self, int_or_float):
        self = int_or_float


class Atom:
    def __init__(self, symb_or_num):
        self = symb_or_num


class Exp:
    def __init__(self, atom_or_list):
        self = atom_or_list


class Env(dict):
    def __init__(self, parms={}, args={}, outer=None):
        self.update(zip(parms, args))
        self.outer = outer

    def find(self, var):
        """ Find the innermost Env where var appears"""
        return self if (var in self) else self.outer.find(var)


class Procedure(object):
    """ A user-defined SCI procedure"""

    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env

    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))


def tokenize(chars: str) -> list:
    """ adds a space before and after parentheses, then splits on whitespace"""
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()


def read_from_tokens(tokens: list) -> Exp:
    """" Read an expression from a list of tokens"""
    if len(tokens) == 0:
        raise SyntaxError('Unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise (SyntaxError('Unexpected: ")"'))
    else:
        return atom(token)


def atom(token: str) -> Atom:
    """ Numbers become numbers; every other token is a symbol"""
    try:
        return Number(int(token))
    except ValueError:
        try:
            return Number(float(token))
        except ValueError:
            return Symbol(token)


def parse(program: str) -> Exp:
    """ Read an expression fr oma string"""
    tokens = tokenize(program)
    return read_from_tokens(tokens)


def standard_env() -> Env:
    "An environment with some Scheme standard procedures."
    env = Env()
    env.update(vars(math))  # sin, cos, sqrt, pi, ...
    env.update(
        {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, '>': op.gt, '<': op.lt, '>=': op.ge, '<=': op.le,
         '=': op.eq, 'abs': abs, 'append': op.add, 'apply': lambda proc, args: proc(*args), 'begin': lambda *x: x[-1],
         'car': lambda x: x[0], 'cdr': lambda x: x[1:], 'cons': lambda x, y: [x] + y, 'eq?': op.is_, 'expt': pow,
         'equal?': op.eq, 'length': len, 'list': lambda *x: list(x), 'list?': lambda x: isinstance(x, list), 'map': map,
         'max': max, 'min': min, 'not': op.not_, 'null?': lambda x: x == [], 'number?': lambda x: isinstance(x, Number),
         'print': print, 'procedure?': callable, 'round': round, 'symbol?': lambda x: isinstance(x, Symbol), })
    return env


global_env = standard_env()


def eval(x: Exp, env=global_env) -> Exp:
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):  # variable reference
        return env[x]
    elif isinstance(x, Number):  # constant number
        return x
    elif x[0] == 'if':  # conditional
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif x[0] == 'define':  # definition
        (_, symbol, exp) = x
        env[symbol] = eval(exp, env)
    else:  # procedure call
        proc = eval(x[0], env)
        args = [eval(arg, env) for arg in x[1:]]
        return proc(*args)


def repl(prompt='lis.py> '):
    "A prompt-read-eval-print loop."
    while True:
        val = eval(parse(input(prompt)))
        if val is not None:
            print(schemestr(val))


def schemestr(exp):
    "Convert a Python object back into a Scheme-readable string."
    if isinstance(exp, list):
        return '(' + ' '.join(map(schemestr, exp)) + ')'
    else:
        return str(exp)


if __name__ == '__main__':
    eval(parse("(* begin (define r 10) (* pi ( r r )))"))
    # lines = []
    # with open('C:\\Users\\caleb\\PycharmProjects\\PyFotoSCIop\\World_Creator_old\ATPLIST2.SC', 'r') as f:
    #     line = f.readline()
    #     while line:
    #         if ';' in line:
    #             line = line[:line.index(';')]
    #             if len(line.strip()) > 0:
    #                 lines.append(line)
    #         else:
    #             lines.append(line)
    #         line = f.readline()
    # program = ' '.join(lines)
    # t = parse(program)
    # pass
