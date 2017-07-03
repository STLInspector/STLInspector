# Generated from TemporalLogic.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\31`\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\5\2\13\n\2\3\2\3")
        buf.write(u"\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\5\3)\n\3\3\3\3\3\3\3\7\3.\n\3\f\3\16\3\61\13\3\3\3")
        buf.write(u"\3\3\5\3\65\n\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3=\n\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write(u"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3X\n\3")
        buf.write(u"\f\3\16\3[\13\3\3\4\3\4\3\4\3\4\2\3\4\5\2\4\6\2\3\3\2")
        buf.write(u"\17\20m\2\n\3\2\2\2\4<\3\2\2\2\6\\\3\2\2\2\b\t\7\22\2")
        buf.write(u"\2\t\13\7\16\2\2\n\b\3\2\2\2\n\13\3\2\2\2\13\f\3\2\2")
        buf.write(u"\2\f\r\7\30\2\2\r\3\3\2\2\2\16\17\b\3\1\2\17\20\7\t\2")
        buf.write(u"\2\20=\5\4\3\f\21\22\7\23\2\2\22\23\7\3\2\2\23\24\7\22")
        buf.write(u"\2\2\24\25\7\4\2\2\25\26\7\22\2\2\26\27\7\5\2\2\27=\5")
        buf.write(u"\4\3\b\30\31\7\24\2\2\31\32\7\3\2\2\32\33\7\22\2\2\33")
        buf.write(u"\34\7\4\2\2\34\35\7\22\2\2\35\36\7\5\2\2\36=\5\4\3\7")
        buf.write(u"\37 \7\25\2\2 !\7\3\2\2!\"\7\22\2\2\"#\7\5\2\2#=\5\4")
        buf.write(u"\3\6$=\7\7\2\2%=\7\b\2\2&=\7\30\2\2\')\t\2\2\2(\'\3\2")
        buf.write(u"\2\2()\3\2\2\2)*\3\2\2\2*/\5\2\2\2+,\t\2\2\2,.\5\2\2")
        buf.write(u"\2-+\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\62")
        buf.write(u"\3\2\2\2\61/\3\2\2\2\62\64\7\6\2\2\63\65\t\2\2\2\64\63")
        buf.write(u"\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\7\22\2\2\67")
        buf.write(u"=\3\2\2\289\7\f\2\29:\5\4\3\2:;\7\r\2\2;=\3\2\2\2<\16")
        buf.write(u"\3\2\2\2<\21\3\2\2\2<\30\3\2\2\2<\37\3\2\2\2<$\3\2\2")
        buf.write(u"\2<%\3\2\2\2<&\3\2\2\2<(\3\2\2\2<8\3\2\2\2=Y\3\2\2\2")
        buf.write(u">?\f\13\2\2?@\7\n\2\2@X\5\4\3\fAB\f\n\2\2BC\7\13\2\2")
        buf.write(u"CX\5\4\3\13DE\f\t\2\2EF\7\21\2\2FX\5\4\3\nGH\f\5\2\2")
        buf.write(u"HI\7\26\2\2IJ\7\3\2\2JK\7\22\2\2KL\7\4\2\2LM\7\22\2\2")
        buf.write(u"MN\7\5\2\2NX\5\4\3\6OP\f\4\2\2PQ\7\27\2\2QR\7\3\2\2R")
        buf.write(u"S\7\22\2\2ST\7\4\2\2TU\7\22\2\2UV\7\5\2\2VX\5\4\3\5W")
        buf.write(u">\3\2\2\2WA\3\2\2\2WD\3\2\2\2WG\3\2\2\2WO\3\2\2\2X[\3")
        buf.write(u"\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\5\3\2\2\2[Y\3\2\2\2\\]\5")
        buf.write(u"\4\3\2]^\7\2\2\3^\7\3\2\2\2\t\n(/\64<WY")
        return buf.getvalue()


class TemporalLogicParser ( Parser ):

    grammarFileName = "TemporalLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'['", u"','", u"']'", u"<INVALID>", 
                     u"'true'", u"'false'", u"'!'", u"'&'", u"'|'", u"'('", 
                     u"')'", u"'*'", u"'+'", u"'-'", u"'->'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'U'", u"'R'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"TOKEN_OPERATOR", u"TOKEN_TRUE", u"TOKEN_FALSE", 
                      u"TOKEN_NOT", u"TOKEN_AND", u"TOKEN_OR", u"TOKEN_LB", 
                      u"TOKEN_RB", u"TOKEN_MULT", u"TOKEN_ADD", u"TOKEN_SUB", 
                      u"TOKEN_IMPLIES", u"TOKEN_POSNUMBER", u"TOKEN_GLOBALLY", 
                      u"TOKEN_FINALLY", u"TOKEN_NEXT", u"TOKEN_UNTIL", u"TOKEN_RELEASE", 
                      u"TOKEN_VARIABLE", u"TOKEN_WS" ]

    RULE_pos_scaled_variable = 0
    RULE_formula = 1
    RULE_start = 2

    ruleNames =  [ u"pos_scaled_variable", u"formula", u"start" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    TOKEN_OPERATOR=4
    TOKEN_TRUE=5
    TOKEN_FALSE=6
    TOKEN_NOT=7
    TOKEN_AND=8
    TOKEN_OR=9
    TOKEN_LB=10
    TOKEN_RB=11
    TOKEN_MULT=12
    TOKEN_ADD=13
    TOKEN_SUB=14
    TOKEN_IMPLIES=15
    TOKEN_POSNUMBER=16
    TOKEN_GLOBALLY=17
    TOKEN_FINALLY=18
    TOKEN_NEXT=19
    TOKEN_UNTIL=20
    TOKEN_RELEASE=21
    TOKEN_VARIABLE=22
    TOKEN_WS=23

    def __init__(self, input):
        super(TemporalLogicParser, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class Pos_scaled_variableContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.Pos_scaled_variableContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_VARIABLE(self):
            return self.getToken(TemporalLogicParser.TOKEN_VARIABLE, 0)

        def TOKEN_POSNUMBER(self):
            return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, 0)

        def TOKEN_MULT(self):
            return self.getToken(TemporalLogicParser.TOKEN_MULT, 0)

        def getRuleIndex(self):
            return TemporalLogicParser.RULE_pos_scaled_variable

        def enterRule(self, listener):
            if hasattr(listener, "enterPos_scaled_variable"):
                listener.enterPos_scaled_variable(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPos_scaled_variable"):
                listener.exitPos_scaled_variable(self)




    def pos_scaled_variable(self):

        localctx = TemporalLogicParser.Pos_scaled_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_pos_scaled_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            _la = self._input.LA(1)
            if _la==TemporalLogicParser.TOKEN_POSNUMBER:
                self.state = 6
                self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                self.state = 7
                self.match(TemporalLogicParser.TOKEN_MULT)


            self.state = 10
            self.match(TemporalLogicParser.TOKEN_VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.FormulaContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_formula

     
        def copyFrom(self, ctx):
            super(TemporalLogicParser.FormulaContext, self).copyFrom(ctx)


    class ImpliesCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.ImpliesCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_IMPLIES(self):
            return self.getToken(TemporalLogicParser.TOKEN_IMPLIES, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterImpliesCase"):
                listener.enterImpliesCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitImpliesCase"):
                listener.exitImpliesCase(self)


    class TrueCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.TrueCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TOKEN_TRUE(self):
            return self.getToken(TemporalLogicParser.TOKEN_TRUE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterTrueCase"):
                listener.enterTrueCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitTrueCase"):
                listener.exitTrueCase(self)


    class BooleanVarCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.BooleanVarCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TOKEN_VARIABLE(self):
            return self.getToken(TemporalLogicParser.TOKEN_VARIABLE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterBooleanVarCase"):
                listener.enterBooleanVarCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBooleanVarCase"):
                listener.exitBooleanVarCase(self)


    class FinallyCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.FinallyCaseContext, self).__init__(parser)
            self.leftlimit = None # Token
            self.rightlimit = None # Token
            self.child = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_FINALLY(self):
            return self.getToken(TemporalLogicParser.TOKEN_FINALLY, 0)
        def TOKEN_POSNUMBER(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_POSNUMBER)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, i)
        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterFinallyCase"):
                listener.enterFinallyCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFinallyCase"):
                listener.exitFinallyCase(self)


    class UntilCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.UntilCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.leftlimit = None # Token
            self.rightlimit = None # Token
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_UNTIL(self):
            return self.getToken(TemporalLogicParser.TOKEN_UNTIL, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)

        def TOKEN_POSNUMBER(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_POSNUMBER)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, i)

        def enterRule(self, listener):
            if hasattr(listener, "enterUntilCase"):
                listener.enterUntilCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitUntilCase"):
                listener.exitUntilCase(self)


    class FalseCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.FalseCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def TOKEN_FALSE(self):
            return self.getToken(TemporalLogicParser.TOKEN_FALSE, 0)

        def enterRule(self, listener):
            if hasattr(listener, "enterFalseCase"):
                listener.enterFalseCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFalseCase"):
                listener.exitFalseCase(self)


    class OrCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.OrCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_OR(self):
            return self.getToken(TemporalLogicParser.TOKEN_OR, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterOrCase"):
                listener.enterOrCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitOrCase"):
                listener.exitOrCase(self)


    class AndCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.AndCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_AND(self):
            return self.getToken(TemporalLogicParser.TOKEN_AND, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)


        def enterRule(self, listener):
            if hasattr(listener, "enterAndCase"):
                listener.enterAndCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAndCase"):
                listener.exitAndCase(self)


    class APCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.APCaseContext, self).__init__(parser)
            self.copyFrom(ctx)

        def pos_scaled_variable(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.Pos_scaled_variableContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.Pos_scaled_variableContext,i)

        def TOKEN_OPERATOR(self):
            return self.getToken(TemporalLogicParser.TOKEN_OPERATOR, 0)
        def TOKEN_POSNUMBER(self):
            return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, 0)
        def TOKEN_ADD(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_ADD)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_ADD, i)
        def TOKEN_SUB(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_SUB)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_SUB, i)

        def enterRule(self, listener):
            if hasattr(listener, "enterAPCase"):
                listener.enterAPCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitAPCase"):
                listener.exitAPCase(self)


    class ReleaseCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.ReleaseCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.leftlimit = None # Token
            self.rightlimit = None # Token
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_RELEASE(self):
            return self.getToken(TemporalLogicParser.TOKEN_RELEASE, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)

        def TOKEN_POSNUMBER(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_POSNUMBER)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, i)

        def enterRule(self, listener):
            if hasattr(listener, "enterReleaseCase"):
                listener.enterReleaseCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitReleaseCase"):
                listener.exitReleaseCase(self)


    class NotCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.NotCaseContext, self).__init__(parser)
            self.child = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_NOT(self):
            return self.getToken(TemporalLogicParser.TOKEN_NOT, 0)
        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNotCase"):
                listener.enterNotCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNotCase"):
                listener.exitNotCase(self)


    class GloballyCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.GloballyCaseContext, self).__init__(parser)
            self.leftlimit = None # Token
            self.rightlimit = None # Token
            self.child = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_GLOBALLY(self):
            return self.getToken(TemporalLogicParser.TOKEN_GLOBALLY, 0)
        def TOKEN_POSNUMBER(self, i=None):
            if i is None:
                return self.getTokens(TemporalLogicParser.TOKEN_POSNUMBER)
            else:
                return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, i)
        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterGloballyCase"):
                listener.enterGloballyCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitGloballyCase"):
                listener.exitGloballyCase(self)


    class NextCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.NextCaseContext, self).__init__(parser)
            self.offset = None # Token
            self.child = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_NEXT(self):
            return self.getToken(TemporalLogicParser.TOKEN_NEXT, 0)
        def TOKEN_POSNUMBER(self):
            return self.getToken(TemporalLogicParser.TOKEN_POSNUMBER, 0)
        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterNextCase"):
                listener.enterNextCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNextCase"):
                listener.exitNextCase(self)


    class BracketCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.BracketCaseContext, self).__init__(parser)
            self.child = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_LB(self):
            return self.getToken(TemporalLogicParser.TOKEN_LB, 0)
        def TOKEN_RB(self):
            return self.getToken(TemporalLogicParser.TOKEN_RB, 0)
        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


        def enterRule(self, listener):
            if hasattr(listener, "enterBracketCase"):
                listener.enterBracketCase(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitBracketCase"):
                listener.exitBracketCase(self)



    def formula(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TemporalLogicParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = TemporalLogicParser.NotCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 13
                self.match(TemporalLogicParser.TOKEN_NOT)
                self.state = 14
                localctx.child = self.formula(10)
                pass

            elif la_ == 2:
                localctx = TemporalLogicParser.GloballyCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 15
                self.match(TemporalLogicParser.TOKEN_GLOBALLY)
                self.state = 16
                self.match(TemporalLogicParser.T__0)
                self.state = 17
                localctx.leftlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                self.state = 18
                self.match(TemporalLogicParser.T__1)
                self.state = 19
                localctx.rightlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                self.state = 20
                self.match(TemporalLogicParser.T__2)
                self.state = 21
                localctx.child = self.formula(6)
                pass

            elif la_ == 3:
                localctx = TemporalLogicParser.FinallyCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 22
                self.match(TemporalLogicParser.TOKEN_FINALLY)
                self.state = 23
                self.match(TemporalLogicParser.T__0)
                self.state = 24
                localctx.leftlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                self.state = 25
                self.match(TemporalLogicParser.T__1)
                self.state = 26
                localctx.rightlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                self.state = 27
                self.match(TemporalLogicParser.T__2)
                self.state = 28
                localctx.child = self.formula(5)
                pass

            elif la_ == 4:
                localctx = TemporalLogicParser.NextCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(TemporalLogicParser.TOKEN_NEXT)
                self.state = 30
                self.match(TemporalLogicParser.T__0)
                self.state = 31
                localctx.offset = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                self.state = 32
                self.match(TemporalLogicParser.T__2)
                self.state = 33
                localctx.child = self.formula(4)
                pass

            elif la_ == 5:
                localctx = TemporalLogicParser.TrueCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(TemporalLogicParser.TOKEN_TRUE)
                pass

            elif la_ == 6:
                localctx = TemporalLogicParser.FalseCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(TemporalLogicParser.TOKEN_FALSE)
                pass

            elif la_ == 7:
                localctx = TemporalLogicParser.BooleanVarCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(TemporalLogicParser.TOKEN_VARIABLE)
                pass

            elif la_ == 8:
                localctx = TemporalLogicParser.APCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                _la = self._input.LA(1)
                if _la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB:
                    self.state = 37
                    _la = self._input.LA(1)
                    if not(_la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()


                self.state = 40
                self.pos_scaled_variable()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB:
                    self.state = 41
                    _la = self._input.LA(1)
                    if not(_la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()
                    self.state = 42
                    self.pos_scaled_variable()
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 48
                self.match(TemporalLogicParser.TOKEN_OPERATOR)
                self.state = 50
                _la = self._input.LA(1)
                if _la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB:
                    self.state = 49
                    _la = self._input.LA(1)
                    if not(_la==TemporalLogicParser.TOKEN_ADD or _la==TemporalLogicParser.TOKEN_SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()


                self.state = 52
                self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                pass

            elif la_ == 9:
                localctx = TemporalLogicParser.BracketCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 54
                self.match(TemporalLogicParser.TOKEN_LB)
                self.state = 55
                localctx.child = self.formula(0)
                self.state = 56
                self.match(TemporalLogicParser.TOKEN_RB)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 85
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = TemporalLogicParser.AndCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 60
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 61
                        self.match(TemporalLogicParser.TOKEN_AND)
                        self.state = 62
                        localctx.right = self.formula(10)
                        pass

                    elif la_ == 2:
                        localctx = TemporalLogicParser.OrCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 63
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 64
                        self.match(TemporalLogicParser.TOKEN_OR)
                        self.state = 65
                        localctx.right = self.formula(9)
                        pass

                    elif la_ == 3:
                        localctx = TemporalLogicParser.ImpliesCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 66
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 67
                        self.match(TemporalLogicParser.TOKEN_IMPLIES)
                        self.state = 68
                        localctx.right = self.formula(8)
                        pass

                    elif la_ == 4:
                        localctx = TemporalLogicParser.UntilCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 69
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 70
                        self.match(TemporalLogicParser.TOKEN_UNTIL)
                        self.state = 71
                        self.match(TemporalLogicParser.T__0)
                        self.state = 72
                        localctx.leftlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                        self.state = 73
                        self.match(TemporalLogicParser.T__1)
                        self.state = 74
                        localctx.rightlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                        self.state = 75
                        self.match(TemporalLogicParser.T__2)
                        self.state = 76
                        localctx.right = self.formula(4)
                        pass

                    elif la_ == 5:
                        localctx = TemporalLogicParser.ReleaseCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 77
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 78
                        self.match(TemporalLogicParser.TOKEN_RELEASE)
                        self.state = 79
                        self.match(TemporalLogicParser.T__0)
                        self.state = 80
                        localctx.leftlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                        self.state = 81
                        self.match(TemporalLogicParser.T__1)
                        self.state = 82
                        localctx.rightlimit = self.match(TemporalLogicParser.TOKEN_POSNUMBER)
                        self.state = 83
                        self.match(TemporalLogicParser.T__2)
                        self.state = 84
                        localctx.right = self.formula(3)
                        pass

             
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
            self.child = None # FormulaContext

        def EOF(self):
            return self.getToken(TemporalLogicParser.EOF, 0)

        def formula(self):
            return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,0)


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
        self.enterRule(localctx, 4, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            localctx.child = self.formula(0)
            self.state = 91
            self.match(TemporalLogicParser.EOF)
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
        self._predicates[1] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




