# Generated from TemporalLogic.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\17L\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\5\3\5\5\5-\n\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write(u"\3\f\3\f\3\r\3\r\3\16\6\16G\n\16\r\16\16\16H\3\16\3\16")
        buf.write(u"\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write(u"\27\r\31\16\33\17\3\2\5\4\2>>@@\3\2\62;\5\2\13\f\17\17")
        buf.write(u"\"\"P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write(u"\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write(u"\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write(u"\33\3\2\2\2\3\35\3\2\2\2\5\37\3\2\2\2\7!\3\2\2\2\t,\3")
        buf.write(u"\2\2\2\13.\3\2\2\2\r\63\3\2\2\2\179\3\2\2\2\21;\3\2\2")
        buf.write(u"\2\23=\3\2\2\2\25?\3\2\2\2\27A\3\2\2\2\31C\3\2\2\2\33")
        buf.write(u"F\3\2\2\2\35\36\7W\2\2\36\4\3\2\2\2\37 \7]\2\2 \6\3\2")
        buf.write(u"\2\2!\"\7_\2\2\"\b\3\2\2\2#$\7?\2\2$-\7?\2\2%&\7#\2\2")
        buf.write(u"&-\7?\2\2\'(\7>\2\2(-\7?\2\2)*\7@\2\2*-\7?\2\2+-\t\2")
        buf.write(u"\2\2,#\3\2\2\2,%\3\2\2\2,\'\3\2\2\2,)\3\2\2\2,+\3\2\2")
        buf.write(u"\2-\n\3\2\2\2./\7v\2\2/\60\7t\2\2\60\61\7w\2\2\61\62")
        buf.write(u"\7g\2\2\62\f\3\2\2\2\63\64\7h\2\2\64\65\7c\2\2\65\66")
        buf.write(u"\7n\2\2\66\67\7u\2\2\678\7g\2\28\16\3\2\2\29:\7#\2\2")
        buf.write(u":\20\3\2\2\2;<\7(\2\2<\22\3\2\2\2=>\7~\2\2>\24\3\2\2")
        buf.write(u"\2?@\7*\2\2@\26\3\2\2\2AB\7+\2\2B\30\3\2\2\2CD\t\3\2")
        buf.write(u"\2D\32\3\2\2\2EG\t\4\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2")
        buf.write(u"\2HI\3\2\2\2IJ\3\2\2\2JK\b\16\2\2K\34\3\2\2\2\5\2,H\3")
        buf.write(u"\b\2\2")
        return buf.getvalue()


class TemporalLogicLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    TOKEN_OPERATOR = 4
    TOKEN_TRUE = 5
    TOKEN_FALSE = 6
    TOKEN_NOT = 7
    TOKEN_AND = 8
    TOKEN_OR = 9
    TOKEN_LB = 10
    TOKEN_RB = 11
    TOKEN_DIGIT = 12
    TOKEN_WS = 13

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'U'", u"'['", u"']'", u"'true'", u"'false'", u"'!'", u"'&'", 
            u"'|'", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>",
            u"TOKEN_OPERATOR", u"TOKEN_TRUE", u"TOKEN_FALSE", u"TOKEN_NOT", 
            u"TOKEN_AND", u"TOKEN_OR", u"TOKEN_LB", u"TOKEN_RB", u"TOKEN_DIGIT", 
            u"TOKEN_WS" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"TOKEN_OPERATOR", u"TOKEN_TRUE", 
                  u"TOKEN_FALSE", u"TOKEN_NOT", u"TOKEN_AND", u"TOKEN_OR", 
                  u"TOKEN_LB", u"TOKEN_RB", u"TOKEN_DIGIT", u"TOKEN_WS" ]

    grammarFileName = u"TemporalLogic.g4"

    def __init__(self, input=None):
        super(TemporalLogicLexer, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


