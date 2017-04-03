/**
 * Creates a real-valued chart
 * @function realChart
 * @param {HTMLElement} dom The HTMLElement it should live in
 * @param {string} name The y-label of the chart
 * @param {number} step The step between points in time
 * @param {number[]} signal The y-values for points in time and in between
 * @returns 
 */
var realChart = function (dom, name, step, signal) {
    var chartSignal = [];
    for (var i in signal) {
        chartSignal.push({
            'x': step * i / 2,
            'y': signal[i]
        })
    }

    dom.parent().height(180);

    return new Chart(dom, {
        type: 'line',
        data: {
            datasets: [{
                label: name,
                cubicInterpolationMode: 'monotone',
                fill: false,
                backgroundColor: "rgba(153,255,51,0.4)",
                borderColor: "rgba(153,255,51,1)",
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

                    }
                }]
            },
            maintainAspectRatio: false,
            responsive: true
        }
    });
}
