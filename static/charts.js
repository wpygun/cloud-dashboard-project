
// palette for the pie charts
const palette = ['#145eff', '#4fa2fe', '#bedaff', '#c4ddff', '#89919e'];

// default layout settings for all charts
const defaultLayout = {
    paper_bgcolor: 'rgba(0,0,0,0)', // makes background transparent for bar and line charts
    plot_bgcolor: 'rgba(0,0,0,0)',  // makes background transparent for pie charts
    height: 350,
    margin: { t: 20, b: 40, l: 30, r: 10 },
    font: {
        family: 'Inter, sans-serif',
        color: '#eefaf7'
    },
    // changes grid lines color from white to darker
    xaxis: { gridcolor: '#1f2937' },
    yaxis: { gridcolor: '#1f2937' }
};

// loop through the data object
for (const key in chartsData) {

    const data = chartsData[key];
    let trace;

    if (data.type === 'pie') {
        trace = {
            labels: data.labels,
            values: data.values,
            type: 'pie',
            hole: 0.45,
            marker: { colors: palette }
        };
    }
    else if (data.type === 'bar') {
        trace = {
            x: data.labels,
            y: data.values,
            type: 'bar',
            marker: { color: '#145eff'}
        };
    }
    else if (data.type === 'line') {
        trace = {
            x: data.labels,
            y: data.values,
            type: 'scatter',
            mode: 'lines+markers',
            line: {
                shape: 'spline',
                width: 3,
                color: '#145eff'
            }
        };
        if (key === 'chf') {
            trace.line.color = '#4fa2fe';
        }
    }

    // plot the specific chart
    Plotly.newPlot(data.divId, [trace], defaultLayout, {
        responsive: true,
        displayModeBar: false
    });
}