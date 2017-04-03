/**
 * Project view model
 * @constructor
 * @param {any} project The project model
 * @param {any} alertView The alert view model
 */
function ProjectView(project, alertView) {
	this._project = project;
	this._dom = false;
	this._alertView = alertView;
	this._renderResults = false;

	// load templates
	this._templates = {
		site: Handlebars.compile($('#project-page-template').html()),
		loadMsg: Handlebars.compile($('#message-loading').html()),
		testResults: Handlebars.compile($('#project-test-results').html()),
		testEntry: Handlebars.compile($('#project-test-entry').html()),
		testRow: Handlebars.compile($('#project-test-row').html())
	};

	/**
	 * @function save
	 * saves the project on the server
	 * @return jqXHR object
	 */
	this.save = _ => {
		this._project.save()
			.done(_ => {
				if (!this._alertView) return;
				this._alertView.show('success', 'Project ' + this._project.getTitle() + ' was successfully saved.');
			})
			.fail(_ => {
				if (!this._alertView) return;
				this._alertView.show('danger', 'An error occurred saving project ' + this._project.getTitle());
			});
	}

	/**
	 * @function startVisualInspection
	 * starts the visualInspection for the given user
	 * @param username
	 */
	this.startVisualInspection = (username) => {
		// check if a stl candidate is not available
		candidate = this._project.getData().stlCandidate;
		if (typeof (candidate) !== 'string' || candidate.length === 0) {
			if (!this._alertView) return;
			this._alertView.show('danger', 'Visual inspection for project ' + this._project.getTitle() + ' not possible due to missing STL candidate.');
			return;
		}

		this.hideOverview(true);
		this._signalView.show('evaluate', username);
	}

	/**
	 * @function showSignal
	 * opens the signal page for the given id
	 * @param id
	 */
	this.showSignal = (id) => {
		this.hideOverview(true);
		this._signalView.show('show', id);
	}

	/**
	 * @function hideOverview
	 * hides or shows the project overview
	 * @param hide boolean parameter, selects hide or show
	 */
	this.hideOverview = (hide) => {
		if (hide) {
			this._dom.find('.project-overview').hide();
		} else {
			this._dom.find('.project-overview').show();
		}
	}

	/**
	 * @function changeStlCandidate
	 * changes stl candidate to candidate
	 * if candidate string is not given, open dialog
	 * @param candidate string or event (no string = candidate not given)
	 */
	this.changeStlCandidate = (candidate) => {
		if (typeof (candidate) !== 'string') {
			this._stlCandidateDialog.find('form .project-form-stlcandidate').val(
				(this._project && this._project.getData() && this._project.getData().stlCandidate)
				|| ""
			);
			this._stlCandidateDialog.dialog("open");
		} else {
			// loading message
			this.renderLoading({ 'stlCandidate': true });

			// trigger parsing on server
			this._project.setStlCandidate(candidate)
				.done(this.load)
				.fail(_ => {
					// old value should be visualized again
					this.render();

					if (!this._alertView) return;
					this._alertView.show('danger', 'Parsing ' + candidate + ' not possible.');
				});
		}
	}

	/**
	 * @function changeTextRequirement
	 * changes the text requirement
	 * if textRequirement string is not given, open dialog
	 * @param textRequirement string or event (no string = textRequirement not given)
	 */
	this.changeTextRequirement = (textRequirement) => {
		if (typeof (textRequirement) !== 'string') {
			this._textRequirementDialog.find('form .project-form-textrequirement').val(
				(this._project && this._project.getData() && this._project.getData().textRequirement)
				|| ""
			);
			this._textRequirementDialog.dialog("open");
		} else {
			// loading message
			this.renderLoading({ 'textRequirement': true });

			// trigger parsing on server
			this._project.setTextRequirement(textRequirement)
				.done(this.load)
				.fail(_ => {
					// old value should be visualized again
					this.render();

					if (!this._alertView) return;
					this._alertView.show('danger', 'TextRequirement could not be set.');
				});
		}
	}

	/**
	 * @function changeTextNotes
	 * changes the text notes
	 * if textNotes string is not given, open dialog
	 * @param textNotes string or event (no string = textNotes not given)
	 */
	this.changeTextNotes = (textNotes) => {
		if (typeof (textNotes) !== 'string') {
			this._textNotesDialog.find('form .project-form-textnotes').val(
				(this._project && this._project.getData() && this._project.getData().textNotes)
				|| ""
			);
			this._textNotesDialog.dialog("open");
		} else {
			// loading message
			this.renderLoading({ 'textNotes': true });

			// trigger parsing on server
			this._project.setTextNotes(textNotes)
				.done(this.load)
				.fail(_ => {
					// old value should be visualized again
					this.render();

					if (!this._alertView) return;
					this._alertView.show('danger', 'TextNotes could not be set.');
				});
		}
	}
	/**
	 * @function render
	 * set the view to loading everywhere
	 * @param if set as object, only the true entries are set to loading
	 * @return domNode to append somewhere
	 */
	this.renderLoading = select => {
		this.setProgress(100, 'progress-bar-info', 'Loading...');
		if (!select || select.textRequirement) {
			this._dom.find('.textRequirement').html(this._templates.loadMsg());
		}
		if (!select || select.stlCandidate) {
			this._dom.find('.stlCandidate').html(this._templates.loadMsg());
		}
		if (!select || select.textNotes) {
			this._dom.find('.textNotes').html(this._templates.loadMsg());
		}
		if (!select || select.testResults) {
			this._dom.find('.testResults').html(this._templates.loadMsg());
		}
	}

	/**
	 * @function renderEntry
	 * generates the dom of a test result entry
	 * @param accepted true (yes), false (no), or null (unknown)
	 * @param conflict true if a conflict happend
	 */
	this.renderEntry = (accepted, conflict) => {
		var iconClasses;

		if (this._renderResults) {
			if (accepted === true) {
				iconClasses = 'glyphicon-ok-sign icon-success';
			} else if (accepted === false) {
				iconClasses = 'glyphicon-remove-sign icon-danger';
			} else {
				iconClasses = 'glyphicon-question-sign icon-warning';
			}
		} else {
			if (accepted === true || accepted === false) {
				iconClasses = 'glyphicon-eye-close';
			} else {
				iconClasses = 'glyphicon-question-sign';
			}
			conflict = false;
		}

		return this._templates.testEntry({
			'conflictClass': conflict ? 'bg-danger' : '',
			'iconClasses': iconClasses
		});
	}

	/**
	 * @function render
	 * renders the project view
	 * @return domNode to append somewhere
	 */
	this.render = _ => {
		// initialize dom if not happend
		if (this._dom === false) {
			this._dom = $(this._templates.site({
				id: this._project.getId(),
				title: this._project.getTitle()
			}));

			this._dom.find('.btn-action-save').click(this.save);

			// initialize dialogs
			this._stlCandidateDialog = this._dom.find(".project-dialog-stlcandidate").dialog({
				resizable: false,
				height: "auto",
				autoOpen: false,
				modal: true,
				width: 400,
				'buttons': {
					Save: _ => {
						this.changeStlCandidate(
							this._stlCandidateDialog.find('form .project-form-stlcandidate').val()
						);
						this._stlCandidateDialog.dialog("close");
					},
					Cancel: _ => {
						this._stlCandidateDialog.dialog("close");
					}
				}
			});
			this._dom.find('.btn-action-change-stlcandidate').click(this.changeStlCandidate);

			this._textRequirementDialog = this._dom.find(".project-dialog-textrequirement").dialog({
				resizable: false,
				height: "auto",
				autoOpen: false,
				modal: true,
				width: 400,
				'buttons': {
					Save: _ => {
						this.changeTextRequirement(
							this._textRequirementDialog.find('form .project-form-textrequirement').val()
						);
						this._textRequirementDialog.dialog("close");
					},
					Cancel: _ => {
						this._textRequirementDialog.dialog("close");
					}
				}
			});
			this._dom.find('.btn-action-change-textrequirement').click(this.changeTextRequirement);

			this._textNotesDialog = this._dom.find(".project-dialog-textnotes").dialog({
				resizable: false,
				height: "auto",
				autoOpen: false,
				modal: true,
				width: 400,
				'buttons': {
					Save: _ => {
						this.changeTextNotes(
							this._textNotesDialog.find('form .project-form-textnotes').val()
						);
						this._textNotesDialog.dialog("close");
					},
					Cancel: _ => {
						this._textNotesDialog.dialog("close");
					}
				}
			});
			this._dom.find('.btn-action-change-textnotes').click(this.changeTextNotes);
		}

		// render data if available
		var data = this._project && this._project.getData();
		if (data) {
			var addPre = html => {
				return '<pre>' + html + '</pre>';
			};

			this._dom.find('.textRequirement').html(addPre(data.textRequirement));
			this._dom.find('.stlCandidate').html(addPre(data.stlCandidate));
			this._dom.find('.textNotes').html(addPre(data.textNotes));
			this.setProgress(
				data.coverage,
				data.conflict ? 'progress-bar-danger' : undefined,
				data.conflict ? 'conflict' : undefined
			);
			this._dom.find('.testResults').children().remove();
			this._dom.find('.testResults').html(this._templates.testResults({
				showResultsButtonText: this._renderResults ? 'Hide results' : 'Show results'
			}));
			this._dom.find('.newVisualInspection button').click(_ => {
				this.startVisualInspection(this._dom.find('#visual-inspection-name').val().replace(/\W/g, '_'));
			});

			//render tests
			var dom = this._dom.find('.row-test th:last-child');
			for (var i = 0; i < data.testCount; ++i) {
				dom.before('<th><button class="btn btn-default">' + (i + 1) + '</button></th>');
				this._dom.find('.row-test th button').eq(-2).click((i => {
					return (_ => this.showSignal(i));
				})(i));
			}
			// toggle show results button
			dom.find('button').click(_ => {
				this._renderResults = !this._renderResults;
				this.render();
			});

			/*
			 * if candidateSat is false, rowSat contains the candidateSat
			 */
			var useSatResults = (length, rowSat, dom, candidateSat, candidateConflicts) => {
				for (var i = 0; i < length; ++i) {
					var conflict = false;

					if (rowSat.length > i
						&& rowSat[i] !== '?'
						&& candidateSat
						&& candidateSat.length > i) {
						conflict = rowSat[i] !== candidateSat[i];
						candidateConflicts[i] = candidateConflicts[i] | conflict;
					}

					dom.before(this.renderEntry(
						i < rowSat.length
							? rowSat[i]
							: null,
						candidateSat ? conflict : candidateConflicts[i]));
				}

				return candidateConflicts;
			}

			var candidateSat = data.sat.candidate;
			var candidateConflicts = [];
			// initially no conflicts
			for (var i = 0; i < data.testCount; ++i) {
				candidateConflicts.push(false)
			}

			// render visual inspection results
			// header
			var dom = this._dom.find('.visualInspection td:last-child');
			for (var i = 0; i < data.testCount; ++i) {
				dom.before('<td></td>');
			}
			// footer
			var dom = this._dom.find('.newVisualInspection td:last-child');
			for (var i = 0; i < data.testCount; ++i) {
				dom.before('<td></td>');
			}
			// rows
			for (p in data.sat.visualInspection) {
				inspectSat = data.sat.visualInspection[p];
				this._dom.find('.newVisualInspection').before(
					this._templates.testRow({
						'id': 'visualInspection-' + p,
						'name': p
					})
				);

				var dom = this._dom.find('.visualInspection-' + p + ' td:last-child');
				candidateConflicts = useSatResults(
					data.testCount,
					inspectSat,
					dom,
					candidateSat,
					candidateConflicts);

				// do unevaluated tests exist?
				if (data.testCount != inspectSat.length || data.coverage < 100) {
					// continue button action
					dom.find('button').click((p => {
						return _ => this.startVisualInspection(p);
					})(p));
				} else {
					dom.find('button').hide();
				}
			}

			// render current candidate entries
			var dom = this._dom.find('.row-candidate td:last-child');
			useSatResults(
				data.testCount,
				candidateSat,
				dom,
				false,
				candidateConflicts);

			//// render old candidates
			//var dom = this._dom.find('.oldStlCandidates td:last-child');
			//for (var i=0; i<data.testCount; ++i) {
			//	dom.before('<td></td>');
			//}
		}

		return this._dom;
	}

	/**
	 * @function setProgress
	 * renders the progress
	 * @param progress number between 0 and 100 or string
	 */
	this.setProgress = (progress, progressClass, progressText) => {
		var progressSize;

		progressClass = progressClass
			|| (progress < 100 ? 'progress-bar-warning' : 'progress-bar-success');
		progressText = progressText || progress.toFixed(1) + '%';
		progressSize = progress.toFixed(1) + '%';

		this._dom.find('.project-overview .progress-bar')
			.width(progressSize)
			.removeClass('progress-bar-info progress-bar-warning progress-bar-success progress-bar-danger')
			.addClass(progressClass)
			.html(progressText);
	}

	/**
	 * @function load
	 * (re)loads the data from the server
	 */
	this.load = _ => {
		this.renderLoading();

		this._project.load()
			.done(this.render)
			.fail(_ => {
				if (!this._alertView) return;
				this._alertView.show('danger', 'Project data of ' + this._project.getTitle() + ' could not be loaded.');
			});
	}

	/**
	 * @function remove
	 * removes the dom node
	 */
	this.remove = _ => {
		this._dom.remove();
		// tell the server to free the project
		this._project.close();
	}

	// trigger initialization
	this.render();
	this.load();
	this._signalView = new SignalView(
		this._project,
		_ => {
			this.load();
			this.hideOverview(false);
		},
		this._alertView
	);
	this._dom.append(this._signalView.render());
	this._signalView.hide();
}
