/**
 * View model of the projects list
 * @constructor
 * @param {any} tabs 
 * @param {HTMLElement} dom The element it should live in
 * @param {any} projects The projects model
 * @param {any} alertView The alert view model
 */
function ProjectsView(tabs, dom, projects, alertView) {
    this._dom = dom;
    this._projects = projects;
    this._alertView = alertView;
    this._openProjects = {};

    // load templates
    this._templates = {
        loading: Handlebars.compile($('#req-list-loading').html()),
        error: Handlebars.compile($('#req-list-error').html()),
        empty: Handlebars.compile($('#req-list-empty').html()),
        entry: Handlebars.compile($('#req-list-entry').html()),
        tabNavEntry: Handlebars.compile($('#tab-nav-entry').html())
    };

    /**
     * @function setStatus
     * set the status in the view to error, loading, or loaded
     * if set to loaded, all entries are removed from the dom
     */
    this.setStatus = (status) => {
        if (status === 'loading') {
            this._dom.find('.req-list li').remove();
            this._dom.find('.req-list').html(this._templates.loading());
        } else if (status === 'error') {
            this._dom.find('.req-list li').remove();
            this._dom.find('.req-list').html(this._templates.error());
        } else if (status === 'loaded') {
            this._dom.find('.req-list li').remove();
        }
    }

    /**
     * @function open
     * opens the project in a new tab
     * or switches to the right tab if already opened
     * @param req projects object
     */
    this.open = (req) => {
        if (!(req.id in this._openProjects)) {
            // open new tab
            var tabDom = $(this._templates.tabNavEntry(req));
            this._tabs.find(".ui-tabs-nav").append(tabDom);
            tabDom.find('.ui-icon-close').click(_ => {
                this.close(req.id);
            });

            // initialize project and view
            var project = new Project(req);
            var projectView = new ProjectView(project, this._alertView);
            this._openProjects[req.id] = projectView;
            this._tabs.append(projectView.render());

            // saveState handler which renders the state
            var handler = (state) => {
                tabDom.find('.glyphicon')
                    .removeClass('glyphicon-floppy-saved glyphicon-floppy-disk icon-warning icon-danger')
                    .addClass(state ? 'glyphicon-floppy-saved icon-warning' : 'glyphicon-floppy-disk icon-danger')
            };
            handler(true);
            project.setSaveStateHandler(handler);

            this._tabs.tabs("refresh");
        }

        // focus tab
        var index = this._tabs.find('a[href="#project-' + req.id + '"]').parent().index();
        this._tabs.tabs("option", "active", index - 1);
    };

    /**
     * @function close
     * closes a tab
     * @param project id
     */
    this.close = (id) => {
        if (!(id in this._openProjects)) {
            return;
        }

        var closeProject = _ => {
            this._openProjects[id].remove();
            delete this._openProjects[id];

            // remove tab
            this._tabs.find('a[href="#project-' + id + '"]').parent().remove();

            // reload the list (project is possibly not saved and should therefore not show up)
            this.loadList();

            // jump to first page
            this._tabs.tabs(
                'option',
                'active',
                0);
        }

        // check if project contains unsaved data
        // if not, just close the project
        if (this._openProjects[id]._project.getSaveState()) {
            closeProject();
            return;
        }

        // show confirmation dialog
        // set correct handler
        this._saveBeforeCloseDialog.dialog(
            'option',
            'buttons',
            {
                'Save and Close': _ => {
                    this.setStatus('loading');
                    this._openProjects[id]._project.save()
                        .done(_ => {
                            closeProject();
                        })
                        .fail(_ => {
                            if (!this._alertView) return;
                            this._alertView.show(
                                'danger',
                                'Project ' + req.title + ' could not be deleted.');
                            this.loadList();
                        })
                        .always(_ => {
                            this._saveBeforeCloseDialog.dialog("close");
                        });
                },
                Close: _ => {
                    closeProject();
                    this._saveBeforeCloseDialog.dialog("close");
                },
                Cancel: _ => {
                    this._saveBeforeCloseDialog.dialog("close");
                }
            }
        );

        // set correct title
        this._saveBeforeCloseDialog.dialog(
            'option',
            'title',
            this._openProjects[id]._project.getTitle()
        );

        this._saveBeforeCloseDialog.dialog("open");
    }

    /**
     * @function delete
     * delete a project by id and reloads the list
     * @param req project object
     * @param confirmed if not set, the confirmation dialog is shown
     * 		if set to true the project is deleted
     */
    this.delete = (req, confirmed) => {
        if (confirmed !== true) {
            // set correct handler
            this._deleteDialog.dialog(
                'option',
                'buttons',
                {
                    Delete: _ => {
                        this.delete(req, true);
                        this._deleteDialog.dialog("close");
                    },
                    Cancel: _ => {
                        this._deleteDialog.dialog("close");
                    }
                }
            );

            // set correct title
            this._deleteDialog.dialog(
                'option',
                'title',
                'Delete ' + req.title
            );

            this._deleteDialog.dialog("open");

            return
        }

        this._projects.delete(req.id)
            .done(_ => {
                if (!this._alertView) return;
                this._alertView.show('success', 'Project ' + req.title + ' was successfully deleted');
            })
            .fail(_ => {
                if (!this._alertView) return;
                this._alertView.show('danger', 'An error occurred deleting project ' + req.title);
            })
            .always(this.loadList);
    };

    /**
     * @function _loadHandler
     * should be called after loading the projects list
     * updates the view
     */
    this._loadHandler = _ => {

        var status = this._projects.status();
        this.setStatus(status);

        // if nothing is loaded, return
        if (status !== 'loaded') {
            return;
        }

        var list = this._projects.list();

        // check if projects list is empty
        if (list.length === 0) {
            this._dom.find('.req-list').html(this._templates.empty());
            return;
        }

        var dom = this._dom.find('.req-list');

        // insert projects in the list
        $.each(list, (index, req) => {
            var coverageClass, coverageText;

            // coverage is number between 0 and 100
            if (req.conflict) {
                coverageClass = 'label-danger';
                coverageText = 'conflict';
            } else if (req.error) {
                coverageClass = 'label-danger';
                coverageText = req.error;
            } else {
                coverageClass = req.coverage < 100
                    ? 'label-warning'
                    : 'label-success';
                coverageText = req.coverage.toFixed(0) + '% coverage';
            }

            // render entry
            dom.append(
                this._templates.entry({
                    id: req.id,
                    title: req.title,
                    coverageText: coverageText,
                    coverageClass: coverageClass
                })
            );

            // append click handler
            dom.find('#' + req.id + ' .btn-action-open').click(this.open.bind(this, req));
            dom.find('#' + req.id + ' .btn-action-delete').click(this.delete.bind(this, req));
        });
    }

    /**
     * @function loadList
     * loads the projects list and displays it
     */
    this.loadList = _ => {
        // set page to loading
        this.setStatus('loading');

        // request list from server
        projects.load()
            .always(this._loadHandler);
    }

    /**
     * @function newProject
     * handler for clicking the new project button
     */
    this._newProject = _ => {
        this._newDialog.dialog("open");
    }

    /**
     * @function createProject
     * creates the new project
     */
    this._createProject = (title) => {
        this._projects.create(title)
            .done(req => {
                this.open(req);
                this.loadList();
            })
            .fail(_ => {
                if (!this._alertView) return;
                this._alertView.show('danger', 'An error occurred creating project ' + title);
            });
    }

    // initialize new project dialog and form
    var submitAction = _ => {
        this._createProject(
            this._newDialog.find('form #project-new-title').val()
        );
        this._newDialog.dialog("close");
    }
    this._newDialog = this._dom.find("#project-new-dialog").dialog({
        autoOpen: false,
        modal: true,
        buttons: {
            Add: submitAction,
            Cancel: _ => {
                this._newDialog.dialog("close");
            }
        },
        close: _ => {
            this._newDialog.find("form")[0].reset();
        }
    });
    this._newDialog.find( "form" ).on( "submit", event => {
        event.preventDefault();
        submitAction();
    });
 

    // initialize delete project dialog
    this._deleteDialog = this._dom.find("#project-delete-dialog").dialog({
        resizable: false,
        height: "auto",
        width: 400,
        autoOpen: false,
        modal: true
    });

    // initialize project save before close dialog
    this._saveBeforeCloseDialog = this._dom.find("#project-savebeforeclose-dialog").dialog({
        resizable: false,
        height: "auto",
        width: 400,
        autoOpen: false,
        modal: true
    });

    // activate tabs
    this._tabs = tabs.tabs({
        beforeActivate: (event, ui) => {
            // reload event, such that on list tab activate
            // the renewed data is shown
            if ($(ui.newTab[0]).index() == 0) {
                this.loadList();
            }
        }
    });

    // new project button click
    this._dom.find('.btn-action-new').click(this._newProject);

    // refresh button click
    this._dom.find('.btn-action-refresh').click(this.loadList);

    // load list initially
    this.loadList();
}
