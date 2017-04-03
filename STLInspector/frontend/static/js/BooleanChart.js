
// new boolean chart type
Chart.elements.PointSegmentLine = Chart.elements.Line.extend({
    // this function implements only the used options,
    // such as: no loop, etc.
    draw: function () {
        var me = this;
        var vm = me._view;
        var fillPoint = vm.scaleBottom;

        var ctx = me._chart.ctx;
        ctx.save();

        var points = me._children.slice();

        function drawSequence() {
            for (index = 1; index < points.length; index++) {
                if (index % 2 === 1) { // index points to an interval
                    ctx.lineTo(
                        (2 * points[index - 1]._view.x + points[index]._view.x) / 3.0,
                        points[index]._view.y
                    );
                    ctx.lineTo(points[index]._view.x, points[index]._view.y);
                } else { // index points to a point
                    ctx.lineTo(
                        (points[index - 1]._view.x + 2 * points[index]._view.x) / 3.0,
                        points[index - 1]._view.y
                    );
                    ctx.lineTo(points[index]._view.x, points[index]._view.y);
                }
            }
        }

        // fill line
        if (points.length && vm.fill) {
            ctx.beginPath();

            ctx.moveTo(points[0]._view.x, fillPoint);
            ctx.lineTo(points[0]._view.x, points[0]._view.y);
            drawSequence();
            ctx.lineTo(points[points.length - 1]._view.x, fillPoint);

            ctx.fillStyle = vm.backgroundColor || Chart.defaults.global.defaultColor;
            ctx.closePath();
            ctx.fill();
        }

        // draw line
        var globalOptionLineElements = Chart.defaults.global.elements.line;
        ctx.lineCap = vm.borderCapStyle || globalOptionLineElements.borderCapStyle;

        ctx.lineDashOffset = vm.borderDashOffset || globalOptionLineElements.borderDashOffset;
        ctx.lineJoin = vm.borderJoinStyle || globalOptionLineElements.borderJoinStyle;
        ctx.lineWidth = vm.borderWidth || globalOptionLineElements.borderWidth;
        ctx.strokeStyle = vm.borderColor || Chart.defaults.global.defaultColor;

        ctx.beginPath();
        ctx.moveTo(points[0]._view.x, points[0]._view.y);
        drawSequence();
        ctx.stroke();
        ctx.restore();

    }
});

Chart.defaults.pointSegmentBoolean = Chart.defaults.line;
Chart.controllers.pointSegmentBoolean = Chart.controllers.line.extend({
    datasetElementType: Chart.elements.PointSegmentLine,
    dataElementType: Chart.elements.Point,
});


/**
 * Creates a Boolean chart
 * @function booleanChart
 * @param {HTMLElement} dom The HTMLElement it should live in
 * @param {string} name The y-label of the chart
 * @param {number} step The step between points in time
 * @param {number[]} signal The y-values for points in time and in between
 * @returns 
 */
var booleanChart = function (dom, name, step, signal) {
    var chartSignal = [];
    for (var i in signal) {
        chartSignal.push({
            'x': step * i / 2,
            'y': signal[i]
        })
    }

    dom.parent().height(90);

    return new Chart(dom, {
        type: 'pointSegmentBoolean',
        data: {
            yLabels: ["false", "true"],
            datasets: [{
                label: name,
                steppedLine: true,
                backgroundColor: "rgba(255,153,0,0.4)",
                borderColor: "rgba(255,153,0,1)",
                data: chartSignal
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom',
                    ticks: {
                        suggestedMin: 0,
                        stepSize: step

                    }
                }],
                yAxes: [{
                    type: 'linear',
                    position: 'left',
                    afterFit: function (obj) {
                        var diff = 50 - obj.width
                        obj.width = 50;
                        obj.right += diff;

                    },
                    ticks: {
                        min: 0,
                        max: 1,
                        stepSize: 1,
                        callback: function (value, index, values) {
                            switch (value) {
                                case 0.0: return 'false';
                                case 1.0: return 'true';
                                default: return '';
                            }
                        }
                    }
                }]
            },
            maintainAspectRatio: false,
            responsive: true
        }
    });
}
