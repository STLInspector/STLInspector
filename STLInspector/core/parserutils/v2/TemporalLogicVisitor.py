# Generated from TemporalLogic.g4 by ANTLR 4.5.2
from antlr4 import *
from STLInspector.core.temporallogic import *

# This class defines a complete generic visitor for a parse tree produced by TemporalLogicParser.
# todo: I assume the visitor pattern was not used correctly

class TemporalLogicVisitor(ParseTreeVisitor):

    def visit(self, ctx):
        # hack, visti* attributes are not called otherwise
        classname = ctx.__class__.__name__
        if not classname.endswith('Context'):
            return super(TemporalLogicVisitor, self).visit(ctx)
        fct = 'visit' + classname[:-len('Context')]
        if not hasattr(self, fct):
            return super(TemporalLogicVisitor, self).visit(ctx)
        return getattr(self, fct)(ctx)


    # Visit a parse tree produced by TemporalLogicParser#NotCase.
    def visitNotCase(self, ctx):
        return NOT(self.visit(ctx.child))


    # Visit a parse tree produced by TemporalLogicParser#TrueCase.
    def visitTrueCase(self, ctx):
        return ap_true


    # Visit a parse tree produced by TemporalLogicParser#UntilCase.
    def visitUntilCase(self, ctx):
        print "U"
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TemporalLogicParser#FalseCase.
    def visitFalseCase(self, ctx):
        return ap_false


    # Visit a parse tree produced by TemporalLogicParser#OrCase.
    def visitOrCase(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return OR(left, right)


    # Visit a parse tree produced by TemporalLogicParser#AndCase.
    def visitAndCase(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return AND(left, right)


    # Visit a parse tree produced by TemporalLogicParser#ParensCase.
    def visitBracketCase(self, ctx):
        return self.visit(ctx.child)


    # Visit a parse tree produced by TemporalLogicParser#start.
    def visitStart(self, ctx):
        return self.visit(ctx.child)

