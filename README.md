The documentation and all frontend components will be added shortly.

----------------------------------------------------------------------------------------------

[STLInspector](http://github.com/STLInspector/STLInspector) is a tool for systematic validation of Signal Temporal Logic (STL) specifications against informal textual requirements. Its goal is to identify typical faults that occur in the process of formalizing requirements by mutating a candidate specification. [STLInspector](http://github.com/STLInspector/STLInspector) computes a series of representative signals that enables a requirements engineer to validate a candidate specification against all its mutated variants, thus achieving full mutation coverage. By visual inspection of the signals via a web-based GUI, an engineer can obtain high confidence in the correctness of the formalization - even if she is not familiar with STL. [STLInspector](http://github.com/STLInspector/STLInspector) makes the assessment of formal specifications accessible to a wide range of developers in industry, hence contributes to leveraging the use of formal specifications and computer-aided verification in industrial practice.

# Installation

[STLInspector](http://github.com/STLInspector/STLInspector) depends on [Python 2](http://www.python.org), [ANTLR v4](http://github.com/antlr/antlr4), the theorem prover [Z3](http://github.com/Z3Prover/z3) with Python bindings and the Python packages [Flask](http://flask.pocoo.org/) and [Flask-Assets](https://flask-assets.readthedocs.io/en/latest/).
Additionally, the GUI depends on [Bootstrap](http://getbootstrap.com/), [jQuery](https://jquery.com/), [jQuery UI](https://jqueryui.com/), [Chart.js](http://www.chartjs.org/), and [handlebars](http://handlebarsjs.com/).
The dependencies can be installed as follows:

Install the Python 2 >= 2.7.9 using your package manager or download it from
http://www.python.org/downloads. This also provides the Python package manager pip. Clone the [STLInspector](http://github.com/STLInspector/STLInspector) repository,
change into its root directory and install all Python packages listed in [requirements.txt](https://github.com/STLInspector/STLInspector/blob/master/LICENSE) using pip:
```bash
git clone http://github.com/STLInspector/STLInspector STLInspector
cd STLInspector
sudo pip install -r requirements.txt
```
Now [ANTLR v4](http://github.com/antlr/antlr4), [Flask](http://flask.pocoo.org/) and [Flask-Assets](https://flask-assets.readthedocs.io/en/latest/) should be installed. For installation of Z3 follow the directions under https://github.com/Z3Prover/z3. Do not forget to use the ``--python`` command line flag with ``mk_make.py`` to enable building the Python bindings.

You do not need to install the javascript frameworks, the GUI of STLInspector relies on. However, this comes with the restriction that you can used the GUI with an internet connection only. Due to safety reasons, network access to the GUI is forbidden and the GUI is only available via localhost.

# Tutorial

This is a tutorial that demonstrates how to use [STLInspector](http://github.com/STLInspector/STLInspector). It shows the standard workflow of the program with an example requirement. For a deeper understanding consider reading the [documentation](http://github.com/STLInspector/STLInspector/doc).

1. Start the server by executing `python start.py` in the
   [STLInspector](http://github.com/STLInspector/STLInspector) folder.
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
Congratulations, you validated the STL candidate against the textual
requirement!

# Documentation

Further information can be found in the [documentation](http://github.com/STLInspector/STLInspector/doc) that details the use of the web-based GUI, the parser and the mutation operators.

# Contributing

We greatly appreciate fixes and new features for [STLInspector](http://github.com/STLInspector/STLInspector). All contributions to this project should be sent as pull requests on github.

# Licence
[STLInspector](http://github.com/STLInspector/STLInspector) is released under the [Apache Licence 2.0](https://github.com/STLInspector/STLInspector/blob/master/LICENSE).
