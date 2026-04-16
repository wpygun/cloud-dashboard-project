const palette = ['#145eff', '#89919e', '#4fa2fe', '#374151', '#bedaff'];

function getDynamicLayout(isDarkMode) {
    return {
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        height: 280,
        margin: {t: 10, b: 30, l: 40, r: 10},
        font: {
            family: 'Inter, ui-sans-serif, system-ui, sans-serif',
            color: isDarkMode ? '#9ca3af' : '#6b7280'
        },
        xaxis: {
            gridcolor: isDarkMode ? '#374151' : '#f3f4f6',
            zerolinecolor: isDarkMode ? '#374151' : '#f3f4f6'
        },
        yaxis: {
            gridcolor: isDarkMode ? '#374151' : '#f3f4f6',
            zerolinecolor: isDarkMode ? '#374151' : '#f3f4f6'
        }
    };
}

function renderCharts() {
    const isDarkMode = document.documentElement.classList.contains('dark');
    const layout = getDynamicLayout(isDarkMode);

    for (const key in chartsData) {
        const data = chartsData[key];
        let trace;

        if (data.type === 'pie') {
            const isDarkMode = document.documentElement.classList.contains('dark');
            trace = {
                labels: data.labels,
                values: data.values,
                type: 'pie',
                hole: 0.4,
                marker: {
                    colors: palette,
                    line: {
                        color: isDarkMode ? '#101727' : '#ffffff',
                        width: 3
                    }
                },
                textinfo: 'percent',
                textfont: {color: '#ffffff'}
            };
        } else if (data.type === 'bar') {
            trace = {
                x: data.labels,
                y: data.values,
                type: 'bar',
                marker: {color: '#145eff', borderRadius: 4}
            };
        } else if (data.type === 'line') {
            trace = {
                x: data.labels,
                y: data.values,
                type: 'scatter',
                mode: 'lines+markers',
                line: {
                    shape: 'spline',
                    width: 3,
                    color: key === 'chf' ? '#4fa2fe' : '#145eff'
                },
                marker: {size: 6}
            };
        }

        Plotly.react(data.divId, [trace], layout, {
            responsive: true,
            displayModeBar: false
        });
    }
}

function updateUSDStats() {
    const values = chartsData.usd.values;
    const rateEl = document.getElementById('latest-usd-rate');
    const trendEl = document.getElementById('usd-trend');

    if (values && values.length >= 2) {
        const current = parseFloat(values[values.length - 1]);
        const previous = parseFloat(values[values.length - 2]);

        const diff = current - previous;
        const percentChange = ((diff / previous) * 100).toFixed(2);

        rateEl.textContent = current.toFixed(3);

        if (diff >= 0) {
            trendEl.textContent = `↑ ${percentChange}%`;
            trendEl.className = "text-sm font-medium text-green-500";
        } else {
            trendEl.textContent = `↓ ${Math.abs(percentChange)}%`;
            trendEl.className = "text-sm font-medium text-red-500";
        }
    }
}

renderCharts();
updateUSDStats();

const themeToggleBtn = document.getElementById('theme-toggle');
if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
        setTimeout(renderCharts, 25);
    });
}