''' parses an input to a temporal logic formula '''

from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from TemporalLogicLexer import TemporalLogicLexer
from TemporalLogicParser import TemporalLogicParser
from TemporalLogicVisitor import TemporalLogicVisitor, ParseException

# nice explanation:
# https://blog.logentries.com/2015/06/how-to-implement-antlr4-autocomplete/

class AntlrErrorListener(ErrorListener):

    def __init__(self):
        super(AntlrErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseException(msg, line, column)


def main():
    #input = InputStream('  (!  true |false&true|false)')
    #input = InputStream('rue)') # todo: Throw lexer error here
    #input = InputStream('  (!  true |false&true|false')
    #input = InputStream('<>[0,1] a R[0,1] (a | 35*abc - tdc <= 31.5) & b & abc -> Ga -> GU')
    input = InputStream('! F[0, 1] a U[0,42] -b+1*c < 7')
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
