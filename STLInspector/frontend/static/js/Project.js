/**
 * Model of a project
 * @constructor
 * @param {any} req The data of the project, such as id and title
 */
function Project(req) {
    this._id = req.id;
    this._title = req.title || "Project";
    this._data = null;
    this._saveState = true;
    this._saveHandler = null;

    /**
     * @function getId
     * @return project id
     */
    this.getId = _ => {
        return this._id;
    }

    /**
     * @function getTitle
     * @return project title
     */
    this.getTitle = _ => {
        return this._title;
    }

    /**
     * @function getData
     * @return project data such as stlCandidate, textRequirement, etc.
     */
    this.getData = _ => {
        return this._data;
    }

    /**
     * @function setSaveStateHandler
     * sets a handler which is called which is called
     * after a change with the new save state
     * @param callback
     */
    this.setSaveStateHandler = (handler) => {
        this._saveHandler = handler;
    }

    /**
     * @function getSaveState
     * @return saveState of the project
     */
    this.getSaveState = _ => {
        return this._saveState;
    }

    /**
     * @function setUnsaved
     * should be called if the project contains unsaved data
     */
    this.setUnsaved = _ => {
        this._saveState = false;
        if (typeof (this._saveHandler) === 'function') {
            this._saveHandler(this._saveState);
        }
    }

    /**
     * @function save
     * saves the project on the server
     * @return jqXHR object
     */
    this.save = _ => {
        return serverRequest(
            'project',
            'save',
            {
                'id': this._id
            })
            .done(_ => {
                if (this._saveState === false
                    && typeof (this._saveHandler) === 'function') {
                    this._saveHandler(true);
                }
                this._saveState = true;
            });
    }

    /**
     * @function close
     * closes the project on the server
     * @return jqXHR object
     */
    this.close = _ => {
        return serverRequest(
            'project',
            'close',
            {
                'id': this._id
            }
        )
    }

    /**
     * @function setStlCandidate
     * tries to parse the stl candidate on the server and fails if it is not possible
     * @param stlCandidate string
     * @return jqHXR object
     */
    this.setStlCandidate = (candidate) => {
        return serverRequest(
            'project',
            'change',
            {
                'id': this.getId(),
                'stlCandidate': candidate
            })
            .done(_ => this.setUnsaved());
    }

    /**
     * @function setTextRequirement
     * saves the textRequirement on the server
     * @param textRequirement string
     * @return jqHXR object
     */
    this.setTextRequirement = (textRequirement) => {
        return serverRequest(
            'project',
            'change',
            {
                'id': this.getId(),
                'textRequirement': textRequirement
            })
            .done(_ => this.setUnsaved());
    }

    /**
     * @function setTextNotes
     * saves the textNotes on the server
     * @param textNotes string
     * @return jqHXR object
     */
    this.setTextNotes = (textNotes) => {
        return serverRequest(
            'project',
            'change',
            {
                'id': this.getId(),
                'textNotes': textNotes
            })
            .done(_ => this.setUnsaved());
    }

    /**
     * @function load
     * loads the project data from the server
     * @return jqXHR object
     */
    this.load = _ => {
        return serverRequest(
            'project',
            'load',
            {
                'id': this._id
            })
            .done(data => {
                this._data = data;
            })
            .fail(_ => {
                this._data = null;
            })
    }
}
