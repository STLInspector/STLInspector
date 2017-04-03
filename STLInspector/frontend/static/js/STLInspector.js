// the following code is executed when the DOM is ready and initializes STLInspector
$(function () {

	var alertView = new AlertView($('#message-list'));
	var projects = new Projects();
	var projectsView = new ProjectsView($("#tabs"), $('#overview-page'), projects, alertView);

});
