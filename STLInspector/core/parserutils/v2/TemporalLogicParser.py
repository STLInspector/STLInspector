# Generated from TemporalLogic.g4 by ANTLR 4.5.2
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\17&\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write(u"\3\2\5\2\20\n\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\2\3\2\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3")
        buf.write(u"\2\3\2\4\2\4\2\2)\2\17\3\2\2\2\4\"\3\2\2\2\6\7\b\2\1")
        buf.write(u"\2\7\b\7\t\2\2\b\20\5\2\2\7\t\20\7\7\2\2\n\20\7\b\2\2")
        buf.write(u"\13\f\7\f\2\2\f\r\5\2\2\2\r\16\7\r\2\2\16\20\3\2\2\2")
        buf.write(u"\17\6\3\2\2\2\17\t\3\2\2\2\17\n\3\2\2\2\17\13\3\2\2\2")
        buf.write(u"\20\37\3\2\2\2\21\22\f\6\2\2\22\23\7\n\2\2\23\36\5\2")
        buf.write(u"\2\7\24\25\f\5\2\2\25\26\7\13\2\2\26\36\5\2\2\6\27\30")
        buf.write(u"\f\4\2\2\30\31\7\3\2\2\31\32\7\4\2\2\32\33\7\16\2\2\33")
        buf.write(u"\34\7\5\2\2\34\36\5\2\2\5\35\21\3\2\2\2\35\24\3\2\2\2")
        buf.write(u"\35\27\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2")
        buf.write(u" \3\3\2\2\2!\37\3\2\2\2\"#\5\2\2\2#$\7\2\2\3$\5\3\2\2")
        buf.write(u"\2\5\17\35\37")
        return buf.getvalue()


class TemporalLogicParser ( Parser ):

    grammarFileName = "TemporalLogic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'U'", u"'['", u"']'", u"<INVALID>", 
                     u"'true'", u"'false'", u"'!'", u"'&'", u"'|'", u"'('", 
                     u"')'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"TOKEN_OPERATOR", u"TOKEN_TRUE", u"TOKEN_FALSE", 
                      u"TOKEN_NOT", u"TOKEN_AND", u"TOKEN_OR", u"TOKEN_LB", 
                      u"TOKEN_RB", u"TOKEN_DIGIT", u"TOKEN_WS" ]

    RULE_formula = 0
    RULE_start = 1

    ruleNames =  [ u"formula", u"start" ]

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
    TOKEN_DIGIT=12
    TOKEN_WS=13

    def __init__(self, input):
        super(TemporalLogicParser, self).__init__(input)
        self.checkVersion("4.5.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(TemporalLogicParser.FormulaContext, self).__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TemporalLogicParser.RULE_formula

     
        def copyFrom(self, ctx):
            super(TemporalLogicParser.FormulaContext, self).copyFrom(ctx)


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


    class UntilCaseContext(FormulaContext):

        def __init__(self, parser, ctx): # actually a TemporalLogicParser.FormulaContext)
            super(TemporalLogicParser.UntilCaseContext, self).__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def TOKEN_DIGIT(self):
            return self.getToken(TemporalLogicParser.TOKEN_DIGIT, 0)
        def formula(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(TemporalLogicParser.FormulaContext)
            else:
                return self.getTypedRuleContext(TemporalLogicParser.FormulaContext,i)


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



    def formula(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = TemporalLogicParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_formula, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            token = self._input.LA(1)
            if token in [TemporalLogicParser.TOKEN_NOT]:
                localctx = TemporalLogicParser.NotCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 5
                self.match(TemporalLogicParser.TOKEN_NOT)
                self.state = 6
                localctx.child = self.formula(5)

            elif token in [TemporalLogicParser.TOKEN_TRUE]:
                localctx = TemporalLogicParser.TrueCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 7
                self.match(TemporalLogicParser.TOKEN_TRUE)

            elif token in [TemporalLogicParser.TOKEN_FALSE]:
                localctx = TemporalLogicParser.FalseCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(TemporalLogicParser.TOKEN_FALSE)

            elif token in [TemporalLogicParser.TOKEN_LB]:
                localctx = TemporalLogicParser.BracketCaseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                self.match(TemporalLogicParser.TOKEN_LB)
                self.state = 10
                localctx.child = self.formula(0)
                self.state = 11
                self.match(TemporalLogicParser.TOKEN_RB)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 29
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 27
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = TemporalLogicParser.AndCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 15
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 16
                        self.match(TemporalLogicParser.TOKEN_AND)
                        self.state = 17
                        localctx.right = self.formula(5)
                        pass

                    elif la_ == 2:
                        localctx = TemporalLogicParser.OrCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 18
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 19
                        self.match(TemporalLogicParser.TOKEN_OR)
                        self.state = 20
                        localctx.right = self.formula(4)
                        pass

                    elif la_ == 3:
                        localctx = TemporalLogicParser.UntilCaseContext(self, TemporalLogicParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 21
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 22
                        self.match(TemporalLogicParser.T__0)
                        self.state = 23
                        self.match(TemporalLogicParser.T__1)
                        self.state = 24
                        self.match(TemporalLogicParser.TOKEN_DIGIT)
                        self.state = 25
                        self.match(TemporalLogicParser.T__2)
                        self.state = 26
                        localctx.right = self.formula(3)
                        pass

             
                self.state = 31
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            localctx.child = self.formula(0)
            self.state = 33
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
        self._predicates[0] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




