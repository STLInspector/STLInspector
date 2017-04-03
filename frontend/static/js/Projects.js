/**
 * Model of the project list
 * @constructor
 */
function Projects() {
    this._projects = [];
    this._status = 'loading'; // loading, error, or loaded
    
    /**
     * @function list
     * @return array of projects
     */
    this.list = _ => {
        return this._projects;
    }

    /**
     * @function status
     * @return string status loading, error, or loaded
     */
    this.status = _ => {
        return this._status;
    }

    /**
     * @function load
     * loads the list from the server
     * @return jqXHR jquery object
     **/
    this.load = _ => {
        this._status = 'loading';

        // request handler
        var doneHandler = (projects) => {
            projects.sort(function (a, b) {
                return a.title > b.title;
            });
            this._projects = projects;
            this._status = 'loaded';
        };

        var failHandler = _ => {
            this._projects = [];
            this._status = 'error';
        };

        // request list from server
        var request = serverRequest('projects', 'list')
            .done(doneHandler)
            .fail(failHandler);

        return request;
    }

    /**
     * @function delete
     * deletes a project from the server
     * @return jqXHR jquery object
     */
    this.delete = (id) => {
        return serverRequest(
            'projects',
            'delete',
            {
                'id': id
            }
        );
    }

    /**
     * @function create
     * creates a project with the given title
     * @param title
     * @return jqXHR jquery object, which calls done
     *		with an object similar to ones in the load list
     */
    this.create = (title) => {
        return serverRequest(
            'projects',
            'create',
            {
                'title': title
            }
        );
    }
}
