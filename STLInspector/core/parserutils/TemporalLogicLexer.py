# Generated from TemporalLogic.g4 by ANTLR 4.6
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


from ..temporallogic import *
import re as regex


def parse_ap_tuple(string):
    t = []
    if string is not None:
        t = tuple(string.strip('(').strip(')^T').split(','))
    return None if t == [] else tuple([x.strip(' ') for x in t])


def parse_ap_operator(string):
    o = {
        '==': eq,
        '!=': ne,
        '<': lt,
        '<=': le,
        '>': gt,
        '>=': ge
    }
    return o[string]


def parse_conjunction(l):
    """
    Receives a list of temporal logic formulae and returns a conjunction
    containing all the formulae. For example:
    parse_conjunction([AP("a"), AP("b"), AP("c")]) --> AND(AP("a"), AND(AP("b"), AP("c")))
    """
    if len(l) == 1:
        return l[0]
    else:
        return AND(l[0], parse_conjunction(l[1:]))


def parse_disjunction(l):
    """
    Receives a list of temporal logic formulae and returns a disjunction
    containing all the formulae. For example:
    parse_disjunction([AP("a"), AP("b"), AP("c")]) --> OR(AP("a"), OR(AP("b"), AP("c")))
    """
    if len(l) == 1:
        return l[0]
    else:
        return OR(l[0], parse_disjunction(l[1:]))


def parse_c(string):
    res = regex.search('((^\d+(\.\d+)?)|(^\+\d+(\.\d+)?)|(^\-\d+(\.\d+)?))\ *', string)
    return None if res == None else [res.group()]


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\27\u00c7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6")
        buf.write(u"\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4")
        buf.write(u"\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t")
        buf.write(u"\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27")
        buf.write(u"\4\30\t\30\3\2\3\2\3\3\5\3\65\n\3\3\3\7\38\n\3\f\3\16")
        buf.write(u"\3;\13\3\3\3\3\3\6\3?\n\3\r\3\16\3@\3\3\6\3D\n\3\r\3")
        buf.write(u"\16\3E\5\3H\n\3\3\4\3\4\3\5\3\5\3\5\3\5\7\5P\n\5\f\5")
        buf.write(u"\16\5S\13\5\6\5U\n\5\r\5\16\5V\3\5\3\5\3\5\3\5\3\5\3")
        buf.write(u"\6\3\6\7\6`\n\6\f\6\16\6c\13\6\3\7\3\7\3\7\3\7\7\7i\n")
        buf.write(u"\7\f\7\16\7l\13\7\6\7n\n\7\r\7\16\7o\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\7\7w\n\7\f\7\16\7z\13\7\3\7\3\7\3\7\5\7\177\n\7")
        buf.write(u"\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u008a\n\b\3")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write(u"\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3")
        buf.write(u"\21\3\21\3\21\3\22\3\22\7\22\u00a9\n\22\f\22\16\22\u00ac")
        buf.write(u"\13\22\3\22\3\22\3\22\3\23\3\23\3\23\5\23\u00b4\n\23")
        buf.write(u"\3\24\3\24\3\24\5\24\u00b9\n\24\3\25\3\25\3\26\3\26\3")
        buf.write(u"\27\3\27\3\30\6\30\u00c2\n\30\r\30\16\30\u00c3\3\30\3")
        buf.write(u"\30\2\2\31\3\3\5\2\7\4\t\5\13\2\r\6\17\7\21\b\23\t\25")
        buf.write(u"\n\27\13\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+")
        buf.write(u"\25-\26/\27\3\2\b\4\2--//\n\2BGJOQSUVX\\aacpr|\6\2\62")
        buf.write(u";C\\aac|\4\2>>@@\4\2PPqq\5\2\13\f\17\17\"\"\u00d9\2\3")
        buf.write(u"\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write(u"\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write(u"\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write(u"\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)")
        buf.write(u"\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\3\61\3\2\2")
        buf.write(u"\2\5\64\3\2\2\2\7I\3\2\2\2\tK\3\2\2\2\13]\3\2\2\2\r~")
        buf.write(u"\3\2\2\2\17\u0089\3\2\2\2\21\u008b\3\2\2\2\23\u0090\3")
        buf.write(u"\2\2\2\25\u0096\3\2\2\2\27\u0098\3\2\2\2\31\u009a\3\2")
        buf.write(u"\2\2\33\u009c\3\2\2\2\35\u009e\3\2\2\2\37\u00a0\3\2\2")
        buf.write(u"\2!\u00a3\3\2\2\2#\u00a6\3\2\2\2%\u00b3\3\2\2\2\'\u00b8")
        buf.write(u"\3\2\2\2)\u00ba\3\2\2\2+\u00bc\3\2\2\2-\u00be\3\2\2\2")
        buf.write(u"/\u00c1\3\2\2\2\61\62\7_\2\2\62\4\3\2\2\2\63\65\t\2\2")
        buf.write(u"\2\64\63\3\2\2\2\64\65\3\2\2\2\65G\3\2\2\2\668\4\62;")
        buf.write(u"\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:<\3")
        buf.write(u"\2\2\2;9\3\2\2\2<>\7\60\2\2=?\4\62;\2>=\3\2\2\2?@\3\2")
        buf.write(u"\2\2@>\3\2\2\2@A\3\2\2\2AH\3\2\2\2BD\4\62;\2CB\3\2\2")
        buf.write(u"\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FH\3\2\2\2G9\3\2\2\2")
        buf.write(u"GC\3\2\2\2H\6\3\2\2\2IJ\5\5\3\2J\b\3\2\2\2KT\7*\2\2L")
        buf.write(u"M\5\5\3\2MQ\7.\2\2NP\5/\30\2ON\3\2\2\2PS\3\2\2\2QO\3")
        buf.write(u"\2\2\2QR\3\2\2\2RU\3\2\2\2SQ\3\2\2\2TL\3\2\2\2UV\3\2")
        buf.write(u"\2\2VT\3\2\2\2VW\3\2\2\2WX\3\2\2\2XY\5\5\3\2YZ\7+\2\2")
        buf.write(u"Z[\7`\2\2[\\\7V\2\2\\\n\3\2\2\2]a\t\3\2\2^`\t\4\2\2_")
        buf.write(u"^\3\2\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2b\f\3\2\2\2ca")
        buf.write(u"\3\2\2\2dm\7*\2\2ef\5\13\6\2fj\7.\2\2gi\5/\30\2hg\3\2")
        buf.write(u"\2\2il\3\2\2\2jh\3\2\2\2jk\3\2\2\2kn\3\2\2\2lj\3\2\2")
        buf.write(u"\2me\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2\2\2")
        buf.write(u"qr\5\13\6\2rs\7+\2\2s\177\3\2\2\2tx\5\5\3\2uw\5/\30\2")
        buf.write(u"vu\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2y{\3\2\2\2zx")
        buf.write(u"\3\2\2\2{|\5\13\6\2|\177\3\2\2\2}\177\5\13\6\2~d\3\2")
        buf.write(u"\2\2~t\3\2\2\2~}\3\2\2\2\177\16\3\2\2\2\u0080\u0081\7")
        buf.write(u"?\2\2\u0081\u008a\7?\2\2\u0082\u0083\7#\2\2\u0083\u008a")
        buf.write(u"\7?\2\2\u0084\u0085\7>\2\2\u0085\u008a\7?\2\2\u0086\u0087")
        buf.write(u"\7@\2\2\u0087\u008a\7?\2\2\u0088\u008a\t\5\2\2\u0089")
        buf.write(u"\u0080\3\2\2\2\u0089\u0082\3\2\2\2\u0089\u0084\3\2\2")
        buf.write(u"\2\u0089\u0086\3\2\2\2\u0089\u0088\3\2\2\2\u008a\20\3")
        buf.write(u"\2\2\2\u008b\u008c\7v\2\2\u008c\u008d\7t\2\2\u008d\u008e")
        buf.write(u"\7w\2\2\u008e\u008f\7g\2\2\u008f\22\3\2\2\2\u0090\u0091")
        buf.write(u"\7h\2\2\u0091\u0092\7c\2\2\u0092\u0093\7n\2\2\u0093\u0094")
        buf.write(u"\7u\2\2\u0094\u0095\7g\2\2\u0095\24\3\2\2\2\u0096\u0097")
        buf.write(u"\7*\2\2\u0097\26\3\2\2\2\u0098\u0099\7+\2\2\u0099\30")
        buf.write(u"\3\2\2\2\u009a\u009b\7#\2\2\u009b\32\3\2\2\2\u009c\u009d")
        buf.write(u"\7(\2\2\u009d\34\3\2\2\2\u009e\u009f\7~\2\2\u009f\36")
        buf.write(u"\3\2\2\2\u00a0\u00a1\7/\2\2\u00a1\u00a2\7@\2\2\u00a2")
        buf.write(u" \3\2\2\2\u00a3\u00a4\7]\2\2\u00a4\u00a5\5\5\3\2\u00a5")
        buf.write(u"\"\3\2\2\2\u00a6\u00aa\7.\2\2\u00a7\u00a9\5/\30\2\u00a8")
        buf.write(u"\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa\u00a8\3\2\2")
        buf.write(u"\2\u00aa\u00ab\3\2\2\2\u00ab\u00ad\3\2\2\2\u00ac\u00aa")
        buf.write(u"\3\2\2\2\u00ad\u00ae\5\5\3\2\u00ae\u00af\7_\2\2\u00af")
        buf.write(u"$\3\2\2\2\u00b0\u00b1\7]\2\2\u00b1\u00b4\7_\2\2\u00b2")
        buf.write(u"\u00b4\7I\2\2\u00b3\u00b0\3\2\2\2\u00b3\u00b2\3\2\2\2")
        buf.write(u"\u00b4&\3\2\2\2\u00b5\u00b6\7>\2\2\u00b6\u00b9\7@\2\2")
        buf.write(u"\u00b7\u00b9\7H\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b7\3")
        buf.write(u"\2\2\2\u00b9(\3\2\2\2\u00ba\u00bb\t\6\2\2\u00bb*\3\2")
        buf.write(u"\2\2\u00bc\u00bd\7W\2\2\u00bd,\3\2\2\2\u00be\u00bf\7")
        buf.write(u"T\2\2\u00bf.\3\2\2\2\u00c0\u00c2\t\7\2\2\u00c1\u00c0")
        buf.write(u"\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c3")
        buf.write(u"\u00c4\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c6\b\30\2")
        buf.write(u"\2\u00c6\60\3\2\2\2\24\2\649@EGQVajox~\u0089\u00aa\u00b3")
        buf.write(u"\u00b8\u00c3\3\b\2\2")
        return buf.getvalue()


class TemporalLogicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    ANTLR_B = 2
    ANTLR_C = 3
    ANTLR_VARIABLE = 4
    ANTLR_OPERATOR = 5
    ANTLR_TRUE = 6
    ANTLR_FALSE = 7
    ANTLR_LBR = 8
    ANTLR_RBR = 9
    ANTLR_NOT = 10
    ANTLR_AND = 11
    ANTLR_OR = 12
    ANTLR_IMPLIES = 13
    ANTLR_LIMIT_1 = 14
    ANTLR_LIMIT_2 = 15
    ANTLR_GLOBALLY = 16
    ANTLR_FINALLY = 17
    ANTLR_NEXT = 18
    ANTLR_UNTIL = 19
    ANTLR_RELEASE = 20
    ANTLR_WS = 21

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"']'", u"'true'", u"'false'", u"'('", u"')'", u"'!'", u"'&'", 
            u"'|'", u"'->'", u"'U'", u"'R'" ]

    symbolicNames = [ u"<INVALID>",
            u"ANTLR_B", u"ANTLR_C", u"ANTLR_VARIABLE", u"ANTLR_OPERATOR", 
            u"ANTLR_TRUE", u"ANTLR_FALSE", u"ANTLR_LBR", u"ANTLR_RBR", u"ANTLR_NOT", 
            u"ANTLR_AND", u"ANTLR_OR", u"ANTLR_IMPLIES", u"ANTLR_LIMIT_1", 
            u"ANTLR_LIMIT_2", u"ANTLR_GLOBALLY", u"ANTLR_FINALLY", u"ANTLR_NEXT", 
            u"ANTLR_UNTIL", u"ANTLR_RELEASE", u"ANTLR_WS" ]

    ruleNames = [ u"T__0", u"F_NUM", u"ANTLR_B", u"ANTLR_C", u"F_VAR", u"ANTLR_VARIABLE", 
                  u"ANTLR_OPERATOR", u"ANTLR_TRUE", u"ANTLR_FALSE", u"ANTLR_LBR", 
                  u"ANTLR_RBR", u"ANTLR_NOT", u"ANTLR_AND", u"ANTLR_OR", 
                  u"ANTLR_IMPLIES", u"ANTLR_LIMIT_1", u"ANTLR_LIMIT_2", 
                  u"ANTLR_GLOBALLY", u"ANTLR_FINALLY", u"ANTLR_NEXT", u"ANTLR_UNTIL", 
                  u"ANTLR_RELEASE", u"ANTLR_WS" ]

    grammarFileName = u"TemporalLogic.g4"

    def __init__(self, input=None):
        super(TemporalLogicLexer, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


