/**
 * Sends and loads data from the server
 * @function serverRequest
 * @param {string} module
 * @param {string} action
 * @param {any} data Json serializable data
 * @returns 
 */
function serverRequest(module, action, data) {
    return $.ajax({
        type: "post",
        url: "/api/" + module + "/" + action,
        data: data,
        dataType: "json"
    });
}
