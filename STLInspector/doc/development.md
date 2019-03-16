# STLInspector development information

## Install from source

1. Install the required package: `pip install pypandoc`
2. Build the stlinspector package: `python generate_distribution.py`
3. Install the stlinspector package: `python setup.py` or `python setup.py develop`

## Testing

Tests for the core of STLInspector are available. The tests can be executed with `python -m unittest discover` or .

## Versioning

[STLInspector](http://github.com/STLInspector/STLInspector) uses *semantic versioning* as described in [packaging.python.org](https://packaging.python.org/distributing/#choosing-a-versioning-scheme).
To change the version, edit `STLInspector/VERSION` and increase version number according to semantic versioning.

## Changing Grammar

The grammar to parse the formulas uses [Antlr4](https://www.antlr.org).
If you want to change it, reading the book [The Definitive ANTLR 4 Reference](https://pragprog.com/book/tpantlr2/the-definitive-antlr-4-reference) is highly recommended. The runtime is included as a python package, so everything in this section is only needed, if you want to change the Grammar.

### Preparational steps

Install the antlr4 tool, see the [installation guide](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#Installation).
Please be aware that it is required to use the same version of the `antlr4` tool as the `antlr4-python2-runtime` version. Thus, upgrading should be done in parallel.

### Steps to change the grammar

1. Edit `STLInspector/core/parseutils/TemporalLogic.g4`
2. Compile the grammer in the same folder with `antlr4 -Dlanguage=python2 TemporalLogic.g4`. The file `TemporalLogicVisitor.py` contains manual code and should not be overwritten by the compile process.
3. If required, change `TemporalLogicVisitor.py` to parse changed grammar parts so that they are correctly transformed to the temporal logic classes.
