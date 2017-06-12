''' parses an input to a temporal logic formula '''

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from TemporalLogicLexer import TemporalLogicLexer
from TemporalLogicParser import TemporalLogicParser
from TemporalLogicVisitor import TemporalLogicVisitor

# nice explanation:
# https://blog.logentries.com/2015/06/how-to-implement-antlr4-autocomplete/

class ParseException(Exception):

    def __init__(self, msg, line, column):
        super(ParseException, self).__init__(msg)
        self.input_line = line
        self.input_column = column

class AntlrErrorListener(ErrorListener):

    def __init__(self):
        super(AntlrErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseException(msg, line, column)


def main():
    input = InputStream('  (!  true |false&true|false)')
    #input = InputStream('rue)') # todo: Throw lexer error here
    #input = InputStream('  (!  true |false&true|false')
    lexer = TemporalLogicLexer(input)
    stream = CommonTokenStream(lexer)
    #stream.fill(); print([token.text for token in stream.tokens])
    try:
        parser = TemporalLogicParser(stream)
        # hack, no listener setter function available
        parser._listeners = [AntlrErrorListener()]
        tree = parser.start()
        visitor = TemporalLogicVisitor()
        formula = visitor.visit(tree)
        print formula
    except ParseException as e:
        print 'parse error at line {} column {}: {}'.format(e.input_line, e.input_column, e)

 
if __name__ == '__main__':
    main()
