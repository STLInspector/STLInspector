from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from parserutils.TemporalLogicLexer import TemporalLogicLexer
from parserutils.TemporalLogicParser import TemporalLogicParser


class AntlrErrorListener(ErrorListener):

    def __init__(self):
        super(AntlrErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception("Syntax Error while parsing with ANTLR.")

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise Exception("Context Sensitivity Error while parsing with ANTLR.")


def parse_from_path(path):
    """ Parses a ((signal) temporal) logic formula from a text file.

    Args:
        path (str) : The path to the file containing the formula to be parsed.

    Returns:
        Clause: Temporal logic formulae that was parsed.
    """
    lexer = TemporalLogicLexer(FileStream(path))
    stream = CommonTokenStream(lexer)
    parser = TemporalLogicParser(stream)
    parser._listeners = [AntlrErrorListener()]
    return parser.start().c


def parse(formula):
    """ Parses a ((signal) temporal) logic formula from a given string.

    Args:
        formula (str) : String of the formula to be parsed.

    Returns:
        Clause: Temporal logic formulae that was parsed.
    """
    lexer = TemporalLogicLexer(InputStream(formula))
    stream = CommonTokenStream(lexer)
    parser = TemporalLogicParser(stream)
    parser._listeners = [AntlrErrorListener()]
    return parser.start().c
