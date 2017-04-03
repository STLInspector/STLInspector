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
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\27\u00f7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\3\2\3\2\3\2\3\2\5\2!\n\2\3\3\3\3\7\3%\n")
        buf.write(u"\3\f\3\16\3(\13\3\3\3\3\3\7\3,\n\3\f\3\16\3/\13\3\3\3")
        buf.write(u"\3\3\3\3\3\3\7\3\65\n\3\f\3\16\38\13\3\3\3\3\3\7\3<\n")
        buf.write(u"\3\f\3\16\3?\13\3\3\3\3\3\7\3C\n\3\f\3\16\3F\13\3\3\3")
        buf.write(u"\3\3\5\3J\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4T\n")
        buf.write(u"\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write(u"\5b\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6m\n\6")
        buf.write(u"\f\6\16\6p\13\6\3\6\3\6\5\6t\n\6\3\7\3\7\3\7\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\3\7\7\7\177\n\7\f\7\16\7\u0082\13\7\3\7")
        buf.write(u"\3\7\5\7\u0086\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write(u"\b\7\b\u0091\n\b\f\b\16\b\u0094\13\b\3\t\3\t\3\t\3\t")
        buf.write(u"\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a3\n\t\3")
        buf.write(u"\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write(u"\n\u00b2\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\5\13\u00c1\n\13\3\f\3\f\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write(u"\3\f\7\f\u00d4\n\f\f\f\16\f\u00d7\13\f\3\r\3\r\3\r\3")
        buf.write(u"\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write(u"\r\7\r\u00ea\n\r\f\r\16\r\u00ed\13\r\3\16\3\16\3\16\3")
        buf.write(u"\16\3\16\3\16\5\16\u00f5\n\16\3\16\2\5\16\26\30\17\2")
        buf.write(u"\4\6\b\n\f\16\20\22\24\26\30\32\2\2\u0104\2 \3\2\2\2")
        buf.write(u"\4I\3\2\2\2\6S\3\2\2\2\ba\3\2\2\2\ns\3\2\2\2\f\u0085")
        buf.write(u"\3\2\2\2\16\u0087\3\2\2\2\20\u00a2\3\2\2\2\22\u00b1\3")
        buf.write(u"\2\2\2\24\u00c0\3\2\2\2\26\u00c2\3\2\2\2\30\u00d8\3\2")
        buf.write(u"\2\2\32\u00f4\3\2\2\2\34\35\7\b\2\2\35!\b\2\1\2\36\37")
        buf.write(u"\7\t\2\2\37!\b\2\1\2 \34\3\2\2\2 \36\3\2\2\2!\3\3\2\2")
        buf.write(u"\2\"&\7\6\2\2#%\7\27\2\2$#\3\2\2\2%(\3\2\2\2&$\3\2\2")
        buf.write(u"\2&\'\3\2\2\2\')\3\2\2\2(&\3\2\2\2)-\7\7\2\2*,\7\27\2")
        buf.write(u"\2+*\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2")
        buf.write(u"\2/-\3\2\2\2\60\61\7\4\2\2\61J\b\3\1\2\62\66\7\5\2\2")
        buf.write(u"\63\65\7\27\2\2\64\63\3\2\2\2\658\3\2\2\2\66\64\3\2\2")
        buf.write(u"\2\66\67\3\2\2\2\679\3\2\2\28\66\3\2\2\29=\7\6\2\2:<")
        buf.write(u"\7\27\2\2;:\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3")
        buf.write(u"\2\2\2?=\3\2\2\2@D\7\7\2\2AC\7\27\2\2BA\3\2\2\2CF\3\2")
        buf.write(u"\2\2DB\3\2\2\2DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GH\7\4\2")
        buf.write(u"\2HJ\b\3\1\2I\"\3\2\2\2I\62\3\2\2\2J\5\3\2\2\2KL\7\6")
        buf.write(u"\2\2LT\b\4\1\2MN\5\4\3\2NO\b\4\1\2OT\3\2\2\2PQ\5\2\2")
        buf.write(u"\2QR\b\4\1\2RT\3\2\2\2SK\3\2\2\2SM\3\2\2\2SP\3\2\2\2")
        buf.write(u"T\7\3\2\2\2UV\7\f\2\2VW\5\b\5\2WX\b\5\1\2Xb\3\2\2\2Y")
        buf.write(u"Z\5\6\4\2Z[\b\5\1\2[b\3\2\2\2\\]\7\n\2\2]^\5\30\r\2^")
        buf.write(u"_\7\13\2\2_`\b\5\1\2`b\3\2\2\2aU\3\2\2\2aY\3\2\2\2a\\")
        buf.write(u"\3\2\2\2b\t\3\2\2\2cd\5\b\5\2de\b\6\1\2et\3\2\2\2fg\5")
        buf.write(u"\b\5\2gn\b\6\1\2hi\7\r\2\2ij\5\b\5\2jk\b\6\1\2km\3\2")
        buf.write(u"\2\2lh\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2oq\3\2\2")
        buf.write(u"\2pn\3\2\2\2qr\b\6\1\2rt\3\2\2\2sc\3\2\2\2sf\3\2\2\2")
        buf.write(u"t\13\3\2\2\2uv\5\n\6\2vw\b\7\1\2w\u0086\3\2\2\2xy\5\b")
        buf.write(u"\5\2y\u0080\b\7\1\2z{\7\16\2\2{|\5\b\5\2|}\b\7\1\2}\177")
        buf.write(u"\3\2\2\2~z\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080")
        buf.write(u"\u0081\3\2\2\2\u0081\u0083\3\2\2\2\u0082\u0080\3\2\2")
        buf.write(u"\2\u0083\u0084\b\7\1\2\u0084\u0086\3\2\2\2\u0085u\3\2")
        buf.write(u"\2\2\u0085x\3\2\2\2\u0086\r\3\2\2\2\u0087\u0088\b\b\1")
        buf.write(u"\2\u0088\u0089\5\f\7\2\u0089\u008a\b\b\1\2\u008a\u0092")
        buf.write(u"\3\2\2\2\u008b\u008c\f\3\2\2\u008c\u008d\7\17\2\2\u008d")
        buf.write(u"\u008e\5\16\b\4\u008e\u008f\b\b\1\2\u008f\u0091\3\2\2")
        buf.write(u"\2\u0090\u008b\3\2\2\2\u0091\u0094\3\2\2\2\u0092\u0090")
        buf.write(u"\3\2\2\2\u0092\u0093\3\2\2\2\u0093\17\3\2\2\2\u0094\u0092")
        buf.write(u"\3\2\2\2\u0095\u0096\5\16\b\2\u0096\u0097\b\t\1\2\u0097")
        buf.write(u"\u00a3\3\2\2\2\u0098\u0099\7\22\2\2\u0099\u009a\7\20")
        buf.write(u"\2\2\u009a\u009b\7\21\2\2\u009b\u009c\5\b\5\2\u009c\u009d")
        buf.write(u"\b\t\1\2\u009d\u00a3\3\2\2\2\u009e\u009f\7\22\2\2\u009f")
        buf.write(u"\u00a0\5\b\5\2\u00a0\u00a1\b\t\1\2\u00a1\u00a3\3\2\2")
        buf.write(u"\2\u00a2\u0095\3\2\2\2\u00a2\u0098\3\2\2\2\u00a2\u009e")
        buf.write(u"\3\2\2\2\u00a3\21\3\2\2\2\u00a4\u00a5\5\20\t\2\u00a5")
        buf.write(u"\u00a6\b\n\1\2\u00a6\u00b2\3\2\2\2\u00a7\u00a8\7\23\2")
        buf.write(u"\2\u00a8\u00a9\7\20\2\2\u00a9\u00aa\7\21\2\2\u00aa\u00ab")
        buf.write(u"\5\b\5\2\u00ab\u00ac\b\n\1\2\u00ac\u00b2\3\2\2\2\u00ad")
        buf.write(u"\u00ae\7\23\2\2\u00ae\u00af\5\b\5\2\u00af\u00b0\b\n\1")
        buf.write(u"\2\u00b0\u00b2\3\2\2\2\u00b1\u00a4\3\2\2\2\u00b1\u00a7")
        buf.write(u"\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b2\23\3\2\2\2\u00b3\u00b4")
        buf.write(u"\5\22\n\2\u00b4\u00b5\b\13\1\2\u00b5\u00c1\3\2\2\2\u00b6")
        buf.write(u"\u00b7\7\24\2\2\u00b7\u00b8\7\20\2\2\u00b8\u00b9\7\3")
        buf.write(u"\2\2\u00b9\u00ba\5\b\5\2\u00ba\u00bb\b\13\1\2\u00bb\u00c1")
        buf.write(u"\3\2\2\2\u00bc\u00bd\7\24\2\2\u00bd\u00be\5\b\5\2\u00be")
        buf.write(u"\u00bf\b\13\1\2\u00bf\u00c1\3\2\2\2\u00c0\u00b3\3\2\2")
        buf.write(u"\2\u00c0\u00b6\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c1\25\3")
        buf.write(u"\2\2\2\u00c2\u00c3\b\f\1\2\u00c3\u00c4\5\24\13\2\u00c4")
        buf.write(u"\u00c5\b\f\1\2\u00c5\u00d5\3\2\2\2\u00c6\u00c7\f\4\2")
        buf.write(u"\2\u00c7\u00c8\7\25\2\2\u00c8\u00c9\7\20\2\2\u00c9\u00ca")
        buf.write(u"\7\21\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00cc\5\26\f\5\u00cc")
        buf.write(u"\u00cd\b\f\1\2\u00cd\u00d4\3\2\2\2\u00ce\u00cf\f\3\2")
        buf.write(u"\2\u00cf\u00d0\7\25\2\2\u00d0\u00d1\5\26\f\4\u00d1\u00d2")
        buf.write(u"\b\f\1\2\u00d2\u00d4\3\2\2\2\u00d3\u00c6\3\2\2\2\u00d3")
        buf.write(u"\u00ce\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2")
        buf.write(u"\2\u00d5\u00d6\3\2\2\2\u00d6\27\3\2\2\2\u00d7\u00d5\3")
        buf.write(u"\2\2\2\u00d8\u00d9\b\r\1\2\u00d9\u00da\5\26\f\2\u00da")
        buf.write(u"\u00db\b\r\1\2\u00db\u00eb\3\2\2\2\u00dc\u00dd\f\4\2")
        buf.write(u"\2\u00dd\u00de\7\26\2\2\u00de\u00df\7\20\2\2\u00df\u00e0")
        buf.write(u"\7\21\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\5\30\r\5\u00e2")
        buf.write(u"\u00e3\b\r\1\2\u00e3\u00ea\3\2\2\2\u00e4\u00e5\f\3\2")
        buf.write(u"\2\u00e5\u00e6\7\26\2\2\u00e6\u00e7\5\26\f\2\u00e7\u00e8")
        buf.write(u"\b\r\1\2\u00e8\u00ea\3\2\2\2\u00e9\u00dc\3\2\2\2\u00e9")
        buf.write(u"\u00e4\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2")
        buf.write(u"\2\u00eb\u00ec\3\2\2\2\u00ec\31\3\2\2\2\u00ed\u00eb\3")
        buf.write(u"\2\2\2\u00ee\u00ef\7\2\2\3\u00ef\u00f5\b\16\1\2\u00f0")
        buf.write(u"\u00f1\5\30\r\2\u00f1\u00f2\7\2\2\3\u00f2\u00f3\b\16")
        buf.write(u"\1\2\u00f3\u00f5\3\2\2\2\u00f4\u00ee\3\2\2\2\u00f4\u00f0")
        buf.write(u"\3\2\2\2\u00f5\33\3\2\2\2\30 &-\66=DISans\u0080\u0085")
        buf.write(u"\u0092\u00a2\u00b1\u00c0\u00d3\u00d5\u00e9\u00eb\u00f4")
        return buf.getvalue()


class TemporalLogicParser ( Parser ):

    grammarFileName = "TemporalLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"']'", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"'true'", u"'false'", u"'('", u"')'", 
                     u"'!'", u"'&'", u"'|'", u"'->'", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'U'", u"'R'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"ANTLR_B", u"ANTLR_C", 
                      u"ANTLR_VARIABLE", u"ANTLR_OPERATOR", u"ANTLR_TRUE", 
                      u"ANTLR_FALSE", u"ANTLR_LBR", u"ANTLR_RBR", u"ANTLR_NOT", 
                      u"ANTLR_AND", u"ANTLR_OR", u"ANTLR_IMPLIES", u"ANTLR_LIMIT_1", 
                      u"ANTLR_LIMIT_2", u"ANTLR_GLOBALLY", u"ANTLR_FINALLY", 
                      u"ANTLR_NEXT", u"ANTLR_UNTIL", u"ANTLR_RELEASE", u"ANTLR_WS" ]

    RULE_constant = 0
    RULE_ap = 1
    RULE_simp = 2
    RULE_literal = 3
    RULE_conjunction = 4
    RULE_disjunction = 5
    RULE_implication = 6
    RULE_globally = 7
    RULE_myfinally = 8
    RULE_mynext = 9
    RULE_until = 10
    RULE_release = 11
    RULE_start = 12

    ruleNames =  [ u"constant", u"ap", u"simp", u"literal", u"conjunction", 
                   u"disjunction", u"implication", u"globally", u"myfinally", 
                   u"mynext", u"until", u"release", u"start" ]

    EOF = Token.EOF
    T__0=1
    ANTLR_B=2
    ANTLR_C=3
    ANTLR_VARIABLE=4
    ANTLR_OPERATOR=5
    ANTLR_TRUE=6
    ANTLR_FALSE=7
    ANTLR_LBR=8
    ANTLR_RBR=9
    ANTLR_NOT=10
    ANTLR_AND=11
    ANTLR_OR=12
    ANTLR_IMPLIES=13
    ANTLR_LIMIT_1=14
    ANTLR_LIMIT_2=15
    ANTLR_GLOBALLY=16
    ANTLR_FINALLY=17
    ANTLR_NEXT=18
    ANTLR_UNTIL=19
    ANTLR_RELEASE=20
    ANTLR_WS=21

    def __init__(self, input):
        super(TemporalLogicParser, self).__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.ConstantContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None

        def ANTLR_TRUE(self):
            return self.getToken(TemporalLogicParser.ANTLR_TRUE, 0)

        def ANTLR_FALSE(self):
            return self.getToken(TemporalLogicParser.ANTLR_FALSE, 0)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_constant

        def enterRule(self, listener):
            if hasattr(listener, "enterConstant"):
                listener.enterConstant(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConstant"):
                listener.exitConstant(self)




    def constant(self):

        localctx = TemporalLogicParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_constant)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TemporalLogicParser.ANTLR_TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(TemporalLogicParser.ANTLR_TRUE)
                localctx.c = ap_true
                pass
            elif token in [TemporalLogicParser.ANTLR_FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(TemporalLogicParser.ANTLR_FALSE)
                localctx.c = ap_false
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ApContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.ApContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._ANTLR_VARIABLE = None # Token
            self._ANTLR_OPERATOR = None # Token
            self._ANTLR_B = None # Token
            self._ANTLR_C = None # Token

        def ANTLR_VARIABLE(self):
            return self.getToken(TemporalLogicParser.ANTLR_VARIABLE, 0)

        def ANTLR_OPERATOR(self):
            return self.getToken(TemporalLogicParser.ANTLR_OPERATOR, 0)

        def ANTLR_B(self):
            return self.getToken(TemporalLogicParser.ANTLR_B, 0)

        def ANTLR_WS(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.ANTLR_WS)
            else:
                return self.getToken(TemporalLogicParser.ANTLR_WS, i)

        def ANTLR_C(self):
            return self.getToken(TemporalLogicParser.ANTLR_C, 0)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_ap

        def enterRule(self, listener):
            if hasattr(listener, "enterAp"):
                listener.enterAp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAp"):
                listener.exitAp(self)




    def ap(self):

        localctx = TemporalLogicParser.ApContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ap)
        self._la = 0 # Token type
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TemporalLogicParser.ANTLR_VARIABLE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                localctx._ANTLR_VARIABLE = self.match(TemporalLogicParser.ANTLR_VARIABLE)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TemporalLogicParser.ANTLR_WS:
                    self.state = 33
                    self.match(TemporalLogicParser.ANTLR_WS)
                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 39
                localctx._ANTLR_OPERATOR = self.match(TemporalLogicParser.ANTLR_OPERATOR)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TemporalLogicParser.ANTLR_WS:
                    self.state = 40
                    self.match(TemporalLogicParser.ANTLR_WS)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                localctx._ANTLR_B = self.match(TemporalLogicParser.ANTLR_B)
                localctx.c = AP(None, parse_c((None if localctx._ANTLR_VARIABLE is None else localctx._ANTLR_VARIABLE.text)), parse_ap_operator((None if localctx._ANTLR_OPERATOR is None else localctx._ANTLR_OPERATOR.text)), float((None if localctx._ANTLR_B is None else localctx._ANTLR_B.text)), [regex.sub("((^\d+(\.\d+)?)|(^\+\d+(\.\d+)?)|(^\-\d+(\.\d+)?))\ *", '', (None if localctx._ANTLR_VARIABLE is None else localctx._ANTLR_VARIABLE.text))])
                pass
            elif token in [TemporalLogicParser.ANTLR_C]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                localctx._ANTLR_C = self.match(TemporalLogicParser.ANTLR_C)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TemporalLogicParser.ANTLR_WS:
                    self.state = 49
                    self.match(TemporalLogicParser.ANTLR_WS)
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 55
                localctx._ANTLR_VARIABLE = self.match(TemporalLogicParser.ANTLR_VARIABLE)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TemporalLogicParser.ANTLR_WS:
                    self.state = 56
                    self.match(TemporalLogicParser.ANTLR_WS)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                localctx._ANTLR_OPERATOR = self.match(TemporalLogicParser.ANTLR_OPERATOR)
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TemporalLogicParser.ANTLR_WS:
                    self.state = 63
                    self.match(TemporalLogicParser.ANTLR_WS)
                    self.state = 68
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 69
                localctx._ANTLR_B = self.match(TemporalLogicParser.ANTLR_B)
                localctx.c = AP(None, parse_ap_tuple((None if localctx._ANTLR_C is None else localctx._ANTLR_C.text)), parse_ap_operator((None if localctx._ANTLR_OPERATOR is None else localctx._ANTLR_OPERATOR.text)), float((None if localctx._ANTLR_B is None else localctx._ANTLR_B.text)), parse_ap_tuple((None if localctx._ANTLR_VARIABLE is None else localctx._ANTLR_VARIABLE.text)))
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.SimpContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._ANTLR_VARIABLE = None # Token
            self._ap = None # ApContext
            self._constant = None # ConstantContext

        def ANTLR_VARIABLE(self):
            return self.getToken(TemporalLogicParser.ANTLR_VARIABLE, 0)

        def ap(self):
            return self.getTypedRuleContext(TemporalLogicParser.ApContext,0)


        def constant(self):
            return self.getTypedRuleContext(TemporalLogicParser.ConstantContext,0)


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_simp

        def enterRule(self, listener):
            if hasattr(listener, "enterSimp"):
                listener.enterSimp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitSimp"):
                listener.exitSimp(self)




    def simp(self):

        localctx = TemporalLogicParser.SimpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simp)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                localctx._ANTLR_VARIABLE = self.match(TemporalLogicParser.ANTLR_VARIABLE)
                localctx.c = AP((None if localctx._ANTLR_VARIABLE is None else localctx._ANTLR_VARIABLE.text))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                localctx._ap = self.ap()
                localctx.c = localctx._ap.c
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                localctx._constant = self.constant()
                localctx.c = localctx._constant.c
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.LiteralContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._literal = None # LiteralContext
            self._simp = None # SimpContext
            self._release = None # ReleaseContext

        def ANTLR_NOT(self):
            return self.getToken(TemporalLogicParser.ANTLR_NOT, 0)

        def literal(self):
            return self.getTypedRuleContext(TemporalLogicParser.LiteralContext,0)


        def simp(self):
            return self.getTypedRuleContext(TemporalLogicParser.SimpContext,0)


        def ANTLR_LBR(self):
            return self.getToken(TemporalLogicParser.ANTLR_LBR, 0)

        def release(self):
            return self.getTypedRuleContext(TemporalLogicParser.ReleaseContext,0)


        def ANTLR_RBR(self):
            return self.getToken(TemporalLogicParser.ANTLR_RBR, 0)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_literal

        def enterRule(self, listener):
            if hasattr(listener, "enterLiteral"):
                listener.enterLiteral(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLiteral"):
                listener.exitLiteral(self)




    def literal(self):

        localctx = TemporalLogicParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TemporalLogicParser.ANTLR_NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(TemporalLogicParser.ANTLR_NOT)
                self.state = 84
                localctx._literal = self.literal()
                localctx.c = NOT(localctx._literal.c)
                pass
            elif token in [TemporalLogicParser.ANTLR_C, TemporalLogicParser.ANTLR_VARIABLE, TemporalLogicParser.ANTLR_TRUE, TemporalLogicParser.ANTLR_FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                localctx._simp = self.simp()
                localctx.c = localctx._simp.c
                pass
            elif token in [TemporalLogicParser.ANTLR_LBR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.match(TemporalLogicParser.ANTLR_LBR)
                self.state = 91
                localctx._release = self.release(0)
                self.state = 92
                self.match(TemporalLogicParser.ANTLR_RBR)
                localctx.c = localctx._release.c
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.ConjunctionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._literal = None # LiteralContext
            self.a = None # LiteralContext
            self.b = None # LiteralContext

        def literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.LiteralContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.LiteralContext,i)


        def ANTLR_AND(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.ANTLR_AND)
            else:
                return self.getToken(TemporalLogicParser.ANTLR_AND, i)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_conjunction

        def enterRule(self, listener):
            if hasattr(listener, "enterConjunction"):
                listener.enterConjunction(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitConjunction"):
                listener.exitConjunction(self)




    def conjunction(self):

        localctx = TemporalLogicParser.ConjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conjunction)
        thelist = list()
        try:
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                localctx._literal = self.literal()
                localctx.c = localctx._literal.c
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 100
                localctx.a = self.literal()
                thelist.append(localctx.a.c);
                self.state = 108
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 102
                        self.match(TemporalLogicParser.ANTLR_AND)
                        self.state = 103
                        localctx.b = self.literal()
                        thelist.append(localctx.b.c) 
                    self.state = 110
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

                localctx.c = parse_conjunction(thelist)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DisjunctionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.DisjunctionContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._conjunction = None # ConjunctionContext
            self.a = None # LiteralContext
            self.b = None # LiteralContext

        def conjunction(self):
            return self.getTypedRuleContext(TemporalLogicParser.ConjunctionContext,0)


        def literal(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.LiteralContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.LiteralContext,i)


        def ANTLR_OR(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.ANTLR_OR)
            else:
                return self.getToken(TemporalLogicParser.ANTLR_OR, i)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_disjunction

        def enterRule(self, listener):
            if hasattr(listener, "enterDisjunction"):
                listener.enterDisjunction(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDisjunction"):
                listener.exitDisjunction(self)




    def disjunction(self):

        localctx = TemporalLogicParser.DisjunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_disjunction)
        thelist = list()
        try:
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 115
                localctx._conjunction = self.conjunction()
                localctx.c = localctx._conjunction.c
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                localctx.a = self.literal()
                thelist.append(localctx.a.c);
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 120
                        self.match(TemporalLogicParser.ANTLR_OR)
                        self.state = 121
                        localctx.b = self.literal()
                        thelist.append(localctx.b.c) 
                    self.state = 128
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

                localctx.c = parse_disjunction(thelist)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImplicationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.ImplicationContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self.a = None # ImplicationContext
            self._disjunction = None # DisjunctionContext
            self.b = None # ImplicationContext

        def disjunction(self):
            return self.getTypedRuleContext(TemporalLogicParser.DisjunctionContext,0)


        def ANTLR_IMPLIES(self):
            return self.getToken(TemporalLogicParser.ANTLR_IMPLIES, 0)

        def implication(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.ImplicationContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.ImplicationContext,i)


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_implication

        def enterRule(self, listener):
            if hasattr(listener, "enterImplication"):
                listener.enterImplication(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitImplication"):
                listener.exitImplication(self)



    def implication(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TemporalLogicParser.ImplicationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_implication, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            localctx._disjunction = self.disjunction()
            localctx.c = localctx._disjunction.c
            self._ctx.stop = self._input.LT(-1)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = TemporalLogicParser.ImplicationContext(self, _parentctx, _parentState)
                    localctx.a = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_implication)
                    self.state = 137
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 138
                    self.match(TemporalLogicParser.ANTLR_IMPLIES)
                    self.state = 139
                    localctx.b = self.implication(2)
                    localctx.c = IMPLIES(localctx.a.c, localctx.b.c) 
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class GloballyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.GloballyContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._implication = None # ImplicationContext
            self._ANTLR_LIMIT_1 = None # Token
            self._ANTLR_LIMIT_2 = None # Token
            self.a = None # LiteralContext

        def implication(self):
            return self.getTypedRuleContext(TemporalLogicParser.ImplicationContext,0)


        def ANTLR_GLOBALLY(self):
            return self.getToken(TemporalLogicParser.ANTLR_GLOBALLY, 0)

        def ANTLR_LIMIT_1(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_1, 0)

        def ANTLR_LIMIT_2(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_2, 0)

        def literal(self):
            return self.getTypedRuleContext(TemporalLogicParser.LiteralContext,0)


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_globally

        def enterRule(self, listener):
            if hasattr(listener, "enterGlobally"):
                listener.enterGlobally(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGlobally"):
                listener.exitGlobally(self)




    def globally(self):

        localctx = TemporalLogicParser.GloballyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_globally)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                localctx._implication = self.implication(0)
                localctx.c = localctx._implication.c
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(TemporalLogicParser.ANTLR_GLOBALLY)
                self.state = 151
                localctx._ANTLR_LIMIT_1 = self.match(TemporalLogicParser.ANTLR_LIMIT_1)
                self.state = 152
                localctx._ANTLR_LIMIT_2 = self.match(TemporalLogicParser.ANTLR_LIMIT_2)
                self.state = 153
                localctx.a = self.literal()
                localctx.c = GLOBALLY(localctx.a.c, int((None if localctx._ANTLR_LIMIT_1 is None else localctx._ANTLR_LIMIT_1.text).strip('[')), int((None if localctx._ANTLR_LIMIT_2 is None else localctx._ANTLR_LIMIT_2.text).strip(',').strip(']')))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(TemporalLogicParser.ANTLR_GLOBALLY)
                self.state = 157
                localctx.a = self.literal()
                localctx.c = GLOBALLY(localctx.a.c)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MyfinallyContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.MyfinallyContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._globally = None # GloballyContext
            self._ANTLR_LIMIT_1 = None # Token
            self._ANTLR_LIMIT_2 = None # Token
            self.a = None # LiteralContext

        def globally(self):
            return self.getTypedRuleContext(TemporalLogicParser.GloballyContext,0)


        def ANTLR_FINALLY(self):
            return self.getToken(TemporalLogicParser.ANTLR_FINALLY, 0)

        def ANTLR_LIMIT_1(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_1, 0)

        def ANTLR_LIMIT_2(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_2, 0)

        def literal(self):
            return self.getTypedRuleContext(TemporalLogicParser.LiteralContext,0)


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_myfinally

        def enterRule(self, listener):
            if hasattr(listener, "enterMyfinally"):
                listener.enterMyfinally(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMyfinally"):
                listener.exitMyfinally(self)




    def myfinally(self):

        localctx = TemporalLogicParser.MyfinallyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_myfinally)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                localctx._globally = self.globally()
                localctx.c = localctx._globally.c
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.match(TemporalLogicParser.ANTLR_FINALLY)
                self.state = 166
                localctx._ANTLR_LIMIT_1 = self.match(TemporalLogicParser.ANTLR_LIMIT_1)
                self.state = 167
                localctx._ANTLR_LIMIT_2 = self.match(TemporalLogicParser.ANTLR_LIMIT_2)
                self.state = 168
                localctx.a = self.literal()
                localctx.c = FINALLY(localctx.a.c, int((None if localctx._ANTLR_LIMIT_1 is None else localctx._ANTLR_LIMIT_1.text).strip('[')), int((None if localctx._ANTLR_LIMIT_2 is None else localctx._ANTLR_LIMIT_2.text).strip(',').strip(']')))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 171
                self.match(TemporalLogicParser.ANTLR_FINALLY)
                self.state = 172
                localctx.a = self.literal()
                localctx.c = FINALLY(localctx.a.c)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MynextContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.MynextContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self._myfinally = None # MyfinallyContext
            self._ANTLR_LIMIT_1 = None # Token
            self.a = None # LiteralContext

        def myfinally(self):
            return self.getTypedRuleContext(TemporalLogicParser.MyfinallyContext,0)


        def ANTLR_NEXT(self):
            return self.getToken(TemporalLogicParser.ANTLR_NEXT, 0)

        def ANTLR_LIMIT_1(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_1, 0)

        def literal(self):
            return self.getTypedRuleContext(TemporalLogicParser.LiteralContext,0)


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_mynext

        def enterRule(self, listener):
            if hasattr(listener, "enterMynext"):
                listener.enterMynext(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMynext"):
                listener.exitMynext(self)




    def mynext(self):

        localctx = TemporalLogicParser.MynextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_mynext)
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                localctx._myfinally = self.myfinally()
                localctx.c = localctx._myfinally.c
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.match(TemporalLogicParser.ANTLR_NEXT)
                self.state = 181
                localctx._ANTLR_LIMIT_1 = self.match(TemporalLogicParser.ANTLR_LIMIT_1)
                self.state = 182
                self.match(TemporalLogicParser.T__0)
                self.state = 183
                localctx.a = self.literal()
                localctx.c = NEXT(localctx.a.c, int((None if localctx._ANTLR_LIMIT_1 is None else localctx._ANTLR_LIMIT_1.text).strip('[')))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
                self.match(TemporalLogicParser.ANTLR_NEXT)
                self.state = 187
                localctx.a = self.literal()
                localctx.c = NEXT(localctx.a.c)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UntilContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.UntilContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self.a = None # UntilContext
            self._mynext = None # MynextContext
            self._ANTLR_LIMIT_1 = None # Token
            self._ANTLR_LIMIT_2 = None # Token
            self.b = None # UntilContext

        def mynext(self):
            return self.getTypedRuleContext(TemporalLogicParser.MynextContext,0)


        def until(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.UntilContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.UntilContext,i)


        def ANTLR_UNTIL(self):
            return self.getToken(TemporalLogicParser.ANTLR_UNTIL, 0)

        def ANTLR_LIMIT_1(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_1, 0)

        def ANTLR_LIMIT_2(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_2, 0)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_until

        def enterRule(self, listener):
            if hasattr(listener, "enterUntil"):
                listener.enterUntil(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUntil"):
                listener.exitUntil(self)



    def until(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TemporalLogicParser.UntilContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_until, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            localctx._mynext = self.mynext()
            localctx.c = localctx._mynext.c
            self._ctx.stop = self._input.LT(-1)
            self.state = 211
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 209
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = TemporalLogicParser.UntilContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_until)
                        self.state = 196
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 197
                        self.match(TemporalLogicParser.ANTLR_UNTIL)
                        self.state = 198
                        localctx._ANTLR_LIMIT_1 = self.match(TemporalLogicParser.ANTLR_LIMIT_1)
                        self.state = 199
                        localctx._ANTLR_LIMIT_2 = self.match(TemporalLogicParser.ANTLR_LIMIT_2)
                        self.state = 201
                        localctx.b = self.until(3)
                        localctx.c = UNTIL(localctx.a.c, localctx.b.c, int((None if localctx._ANTLR_LIMIT_1 is None else localctx._ANTLR_LIMIT_1.text).strip('[')), int((None if localctx._ANTLR_LIMIT_2 is None else localctx._ANTLR_LIMIT_2.text).strip(',').strip(']')))
                        pass

                    elif la_ == 2:
                        localctx = TemporalLogicParser.UntilContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_until)
                        self.state = 204
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                        self.state = 205
                        self.match(TemporalLogicParser.ANTLR_UNTIL)
                        self.state = 206
                        localctx.b = self.until(2)
                        localctx.c = UNTIL(localctx.a.c, localctx.b.c)
                        pass

             
                self.state = 213
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ReleaseContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.ReleaseContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self.a = None # ReleaseContext
            self._until = None # UntilContext
            self._ANTLR_LIMIT_1 = None # Token
            self._ANTLR_LIMIT_2 = None # Token
            self.b = None # ReleaseContext
            self.d = None # UntilContext

        def until(self):
            return self.getTypedRuleContext(TemporalLogicParser.UntilContext,0)


        def release(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.ReleaseContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.ReleaseContext,i)


        def ANTLR_RELEASE(self):
            return self.getToken(TemporalLogicParser.ANTLR_RELEASE, 0)

        def ANTLR_LIMIT_1(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_1, 0)

        def ANTLR_LIMIT_2(self):
            return self.getToken(TemporalLogicParser.ANTLR_LIMIT_2, 0)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_release

        def enterRule(self, listener):
            if hasattr(listener, "enterRelease"):
                listener.enterRelease(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitRelease"):
                listener.exitRelease(self)



    def release(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TemporalLogicParser.ReleaseContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_release, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            localctx._until = self.until(0)
            localctx.c = localctx._until.c
            self._ctx.stop = self._input.LT(-1)
            self.state = 233
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 231
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                    if la_ == 1:
                        localctx = TemporalLogicParser.ReleaseContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_release)
                        self.state = 218
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")

                        self.state = 219
                        self.match(TemporalLogicParser.ANTLR_RELEASE)
                        self.state = 220
                        localctx._ANTLR_LIMIT_1 = self.match(TemporalLogicParser.ANTLR_LIMIT_1)
                        self.state = 221
                        localctx._ANTLR_LIMIT_2 = self.match(TemporalLogicParser.ANTLR_LIMIT_2)
                        self.state = 223
                        localctx.b = self.release(3)
                        localctx.c = RELEASE(localctx.a.c, localctx.b.c, int((None if localctx._ANTLR_LIMIT_1 is None else localctx._ANTLR_LIMIT_1.text).strip('[')), int((None if localctx._ANTLR_LIMIT_2 is None else localctx._ANTLR_LIMIT_2.text).strip(',').strip(']')))
                        pass

                    elif la_ == 2:
                        localctx = TemporalLogicParser.ReleaseContext(self, _parentctx, _parentState)
                        localctx.a = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_release)
                        self.state = 226
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                        self.state = 227
                        self.match(TemporalLogicParser.ANTLR_RELEASE)
                        self.state = 228
                        localctx.d = localctx._until = self.until(0)
                        localctx.c = RELEASE(localctx.a.c, localctx.d.c)
                        pass

             
                self.state = 235
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.StartContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.c = None
            self.a = None # ReleaseContext

        def EOF(self):
            return self.getToken(TemporalLogicParser.EOF, 0)

        def release(self):
            return self.getTypedRuleContext(TemporalLogicParser.ReleaseContext,0)


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_start

        def enterRule(self, listener):
            if hasattr(listener, "enterStart"):
                listener.enterStart(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitStart"):
                listener.exitStart(self)




    def start(self):

        localctx = TemporalLogicParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_start)
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TemporalLogicParser.EOF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.match(TemporalLogicParser.EOF)
                localctx.c = ap_true
                pass
            elif token in [TemporalLogicParser.ANTLR_C, TemporalLogicParser.ANTLR_VARIABLE, TemporalLogicParser.ANTLR_TRUE, TemporalLogicParser.ANTLR_FALSE, TemporalLogicParser.ANTLR_LBR, TemporalLogicParser.ANTLR_NOT, TemporalLogicParser.ANTLR_GLOBALLY, TemporalLogicParser.ANTLR_FINALLY, TemporalLogicParser.ANTLR_NEXT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                localctx.a = self.release(0)
                self.state = 239
                self.match(TemporalLogicParser.EOF)
                localctx.c = localctx.a.c
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.implication_sempred
        self._predicates[10] = self.until_sempred
        self._predicates[11] = self.release_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def implication_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def until_sempred(self, localctx, predIndex):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         

    def release_sempred(self, localctx, predIndex):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




