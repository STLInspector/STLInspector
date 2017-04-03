/**
 * View model of the message bar
 * @constructor
 * @param {HTMLElement} dom The element where the view lives in
 */
function AlertView(dom) {
    this._dom = dom;
    this._template = Handlebars.compile($('#message-list-entry').html());

    /**
     * inserts a message into the dom
     * @function show
     * @param {string} type A bootstrap based alert type: info, warning, success, or danger
     * @param {string} message The message to be shown
     */
    this.show = (type, message) => {
        this._dom.append(this._template({
            type: type,
            message: message
        }));
    }
}
