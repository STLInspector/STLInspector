# STLInspector

Systematic validation of Signal Temporal Logic (STL) specifications against informal textual requirements.

----------------------------------------------------------------------------------------------

The goal of [STLInspector](http://github.com/STLInspector/STLInspector) is to identify typical faults that occur in the process of formalizing requirements by mutating a candidate specification. [STLInspector](http://github.com/STLInspector/STLInspector) computes a series of representative signals that enables a requirements engineer to validate a candidate specification against all its mutated variants, thus achieving full mutation coverage. By visual inspection of the signals via a web-based GUI, an engineer can obtain high confidence in the correctness of the formalization - even if she is not familiar with STL. [STLInspector](http://github.com/STLInspector/STLInspector) makes the assessment of formal specifications accessible to a wide range of developers, hence contributes to leveraging the use of formal specifications and computer-aided verification in practice.

## Installation

[STLInspector](http://github.com/STLInspector/STLInspector) depends on [Python 2](http://www.python.org), [ANTLR v4](http://github.com/antlr/antlr4), the theorem prover [Z3](http://github.com/Z3Prover/z3) with Python bindings and the Python packages [Flask](http://flask.pocoo.org/) and [Flask-Assets](https://flask-assets.readthedocs.io/en/latest/).
Additionally, the GUI depends on [Bootstrap](http://getbootstrap.com/), [jQuery](https://jquery.com/), [jQuery UI](https://jqueryui.com/), [Chart.js](http://www.chartjs.org/), and [handlebars](http://handlebarsjs.com/).

Install the Python 2 >= 2.7.9 using your package manager or download it from
http://www.python.org/downloads. This also provides the Python package manager pip. [STLInspector](http://github.com/STLInspector/STLInspector) is provided as an [python package](https://pypi.python.org/pypi/STLInspector) and can be installed using pip:
```bash
pip install STLInspector
```

Note that the required javascript frameworks are not installed locally, but loaded over an internet connection. This comes with the restriction that you can used the GUI with an internet connection only. Due to safety reasons, network access to the GUI is forbidden and the GUI is only available via localhost.

## Tutorial

This is a tutorial that demonstrates how to use [STLInspector](http://github.com/STLInspector/STLInspector). It shows the standard workflow of the program with an example requirement. For a deeper understanding consider reading the [documentation](https://github.com/STLInspector/STLInspector/tree/master/STLInspector/doc).

1. Start the server by executing `stlinspector .`.
2. Open a browser and go to [http://localhost:5000](http://localhost:5000).
3. Press the *new requirements project* button, input the title *tutorial
   requirements project* and press the *add* button. The project overview opens.
4. In the *textual requirements* block press the *edit* button and input:

    > The velocity should be higher than 5km/h from second 1 to second 3.

5. In the *current STL candidate* block press the *edit* button and input:

    > F[1,3] velocity > 5                                                       

6. Under *visual inspection results* replace *Name* with *Test User* and press
*new visual inspection*.
7. The textual requirement and a test signal is shown. Evaluate the textual
requirement on the test signal and press the *yes* or *no* button. Do this until
no test signals are shown any more. Then press *go back to project overview*.
8. To see the evaluation results, press the *show results* button. Since in our
example the STL candidate is wrong, some of your evaluation results should
differ from the STL candidate results.
9. Change the STL candidate to:

    > G[1,3] velocity > 5                                                       

10. Redo the visual inspection on the new STL candidate.
11. You should not get conflicting evaluation results for the STL candidate now.
12. Press the save button and the project is saved to `tutorial_requirements_project.stlinspector` in the current directory.
Congratulations, you validated the STL candidate against the textual
requirement!

## Documentation

Further information can be found in the [documentation](https://github.com/STLInspector/STLInspector/tree/master/STLInspector/doc) that details the use of the web-based GUI, the parser and the mutation operators. The GUI provides a html version of the documentation.

## Contributing

We greatly appreciate fixes and new features for [STLInspector](http://github.com/STLInspector/STLInspector). All contributions to this project should be sent as pull requests on github. [STLInspector](http://github.com/STLInspector/STLInspector) uses *semantic versioning* as described in [packaging.python.org](https://packaging.python.org/distributing/#choosing-a-versioning-scheme).

## Licence
[STLInspector](http://github.com/STLInspector/STLInspector) is released under the [Apache Licence 2.0](https://github.com/STLInspector/STLInspector/blob/master/LICENSE).
