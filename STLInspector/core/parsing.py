''' parses an input to a temporal logic formula '''

from antlr4 import CommonTokenStream, InputStream, FileStream
from antlr4.error.ErrorListener import ErrorListener
from parserutils.TemporalLogicLexer import TemporalLogicLexer
from parserutils.TemporalLogicParser import TemporalLogicParser
from parserutils.TemporalLogicVisitor import TemporalLogicVisitor, ParseException


class AntlrErrorListener(ErrorListener):

    def __init__(self):
        super(AntlrErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseException(msg, line, column)


def _parse(stream):
    """ Parses a formula from a stream """
    lexer = TemporalLogicLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = TemporalLogicParser(stream)
    # hack, no listener setter function available
    parser._listeners = [AntlrErrorListener()]
    tree = parser.start()
    visitor = TemporalLogicVisitor()
    formula = visitor.visit(tree)
    return formula


def parse_from_path(path):
    """ Parses a ((signal) temporal) logic formula from a text file.

    Args:
        path (str) : The path to the file containing the formula to be parsed.

    Returns:
        Clause: Temporal logic formulae that was parsed.
    """
    return _parse(FileStream(path))


def parse(formula):
    """ Parses a ((signal) temporal) logic formula from a given string.

    Args:
        formula (str) : String of the formula to be parsed.

    Returns:
        Clause: Temporal logic formulae that was parsed.
    """
    return _parse(InputStream(formula))
