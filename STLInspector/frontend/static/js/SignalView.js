/**
 * Signal view model
 * @constructor
 * @param {any} project The project model
 * @param {function} closeCallback This function is called when the SignalView was closed
 * @param {any} alertView The alert view model
 */
function SignalView(project, closeCallback, alertView) {
    this._project = project;
    this._alertView = alertView;
    this._charts = [];
    this._closeCallback = closeCallback;
    this._data = null;

    // load templates
    this._templates = {
        page: Handlebars.compile($('#project-signal-template').html()),
        loadMsg: Handlebars.compile($('#message-loading').html()),
        signalCanvas: Handlebars.compile($('#project-signal-canvas').html()),
        errorMessage: Handlebars.compile($('#signal-message').html())
    }

    /**
     * @method render
     * renders the signal page
     * @return domNode to append somewhere
     */
    this.render = _ => {
        var data = this._project.getData();
        var textRequirement = data && data.textRequirement;

        this._dom = $(this._templates.page({
            'id': this._project.getId(),
            'textRequirement': textRequirement
        }));

        this._dom.find('.btn-action-back').click(_ => {
            this.hide();

            if (typeof (this._closeCallback) === 'function') {
                this._closeCallback();
            }
        });

        this._signalsDom = this._dom.find('.test-signals-section');
        this._successDom = this._dom.find('.test-success-section');
        this._evaluationDom = this._dom.find('.test-evaluation-section');

        this._evaluationDom.find('.btn-action-sat').click(_ => this.evaluate(true));
        this._evaluationDom.find('.btn-action-unsat').click(_ => this.evaluate(false));

        return this._dom;
    }

    /**
     * @method _setBackButtonText
     * @param text that should be shown on the button
     */
    this._setBackButtonText = (text) => {
        this._dom.find('h4 button').html(text);
    }

    /**
     * @method _setPageTitle
     * @param text that should be shown as the title
     */
    this._setPageTitle = (text) => {
        this._dom.find('h4 span').html(text);
    }

    /**
     * @method show
     * renders the signal page and a signal
     * type = 'evaluate': result evaluation buttons are shown
     * type = 'show': results from all participants are shown
     * @param type 'evaluate' or 'show'
     * @param parameter username or test number
     * @param preserve if set to true, old error message are kept
     */
    this.show = (type, parameter, preserve) => {
        this._currentType = type === 'evaluate'
            ? type
            : 'show';

        this._parameter = parameter;

        if (!preserve) {
            this._dom.find('.alert').remove();
        }

        this.setProgress(100, 'progress-bar-info', 'Loading...');
        this.removeCharts();
        this._dom.find('.test-signals').html(this._templates.loadMsg());
        this._signalsDom.show();
        this._evaluationDom.hide();
        this._successDom.hide();
        this._setBackButtonText(
            this._currentType === 'evaluate'
                ? 'Cancel'
                : 'Back'
        );
        this._setPageTitle(
            this._currentType === 'evaluate'
                ? this._project.getTitle() + ': Evaluate signal'
                : this._project.getTitle() + ': Show signal number ' + (this._parameter + 1)
        );

        this._dom.show();


        serverRequest('project', 'test', {
            'type': this._currentType,
            'parameter': this._parameter,
            'id': this._project.getId()
        })
            .done(this.renderData)
            .fail(_ => {
                if (!this._alertView) return;
                this._alertView.show('danger', 'An error occurred while loading a test for ' + this._project.getTitle());
            });
    }

    /**
     * @method renderData
     * renders loaded data and set the handlers
     */
    this.renderData = data => {
        this._data = data;

        this.setProgress(
            data.coverage,
            data.conflict ? 'progress-bar-danger' : undefined,
            data.conflict ? 'conflict' : undefined
        );

        if (data.finished === true) {
            // show finished message
            this._signalsDom.hide();
            this._dom.find('.test-evaluation-section').hide();
            this._evaluationDom.hide();
            this._successDom.show();
            this._setBackButtonText('Back');

            return
        }

        this._successDom.hide();

        // remove loading message
        this._dom.find('.test-signals').html('');
        this._signalsDom.show();

        // add signals
        for (var sig in data.signals) {
            var id = 'project-' + this._project.getId() + '-signal-' + sig;

            // create canvas
            this._dom.find('.test-signals').append(
                this._templates.signalCanvas({
                    'id': id
                })
            );

            // check if real or boolean signal
            if (typeof (data.signals[sig][0]) === 'boolean') {
                this._charts.push(booleanChart(this._dom.find('#' + id), sig, data.step, data.signals[sig]));
            } else {
                this._charts.push(realChart(this._dom.find('#' + id), sig, data.step, data.signals[sig]));
            }
        }

        if (this._currentType === 'evaluate') {
            // show yes and no buttons
            this._evaluationDom.show();
        } else {
            this._evaluationDom.hide();
        }
    }

    /**
     * @method evaluate
     * user evaluation of the given test signal
     * @param evaluation true or false
     */
    this.evaluate = (evaluation) => {
        if (this._currentType !== 'evaluate' || !this._data) {
            return;
        }

        // if result wrong, show error message
        if (this._data.kind !== evaluation) {
            this._dom.find('.alert').remove();
            this._dom.find('h4').after(this._templates.errorMessage({
                type: 'danger',
                message: 'Inspection result differed from candidate for test ' + (this._data.testId + 1)
            }));
            this._dom.find('.alert').append('(<a href="#">show</a>)');
            var testId = this._data.testId;
            this._dom.find('.alert a').click(_ => {
                this.show('show', testId);
            });
        }

        serverRequest('project', 'testEvaluation', {
            'id': this._project.getId(),
            'username': this._parameter,
            'testId': this._data.testId,
            'evaluation': evaluation
        })
            .fail(_ => {
                if (!this._alertView) return;
                this._alertView.show('danger', 'Test evaluation could not be saved for ' + this._project.getTitle());
            })
            .always(_ => {
                this._project.setUnsaved();
                this.show(this._currentType, this._parameter, true);
            });
    }

    /**
     * @method hide
     * hides the signal page
     */
    this.hide = _ => {
        this._dom.hide();
    }

    /**
     * @method setProgress
     * renders the progress
     * @param progress number between 0 and 100 or string
     */
    this.setProgress = (progress, progressClass, progressText) => {
        var progressSize;

        progressClass = progressClass
            || (progress < 100 ? 'progress-bar-warning' : 'progress-bar-success');
        progressText = progressText || progress.toFixed(1) + '%';
        progressSize = progress.toFixed(1) + '%';

        this._dom.find('.progress-bar')
            .width(progressSize)
            .removeClass('progress-bar-info progress-bar-warning progress-bar-success progress-bar-danger')
            .addClass(progressClass)
            .html(progressText);
    }

    /**
     * @method removeCharts
     * deletes all chart objects
     */
    this.removeCharts = _ => {
        for (var i in this._charts) {
            this._charts[i].destroy();
            delete this._charts[i];
        }
    }
}
