google.charts.load('current', {'packages':['timeline']});
google.charts.setOnLoadCallback(getData);


function getData() {
    if(ids != "") {
        $.get( "scripts/dbHelper.php?type=1&id="+ ids + "&key=" + key, function() {}).done(function(data) {
            data = JSON.parse(data);
            drawChart( data );
        });
    }
}

function drawChart(data_in) {
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Name');
    data.addColumn('date', 'Online time');
    data.addColumn('date', 'Offline time');

    data_in.forEach(function(point) {
        data.addRows([
            [point[0], new Date(point[1]), new Date(point[2])]
        ]);
    });

    var options = {
        height: 700,
        timeline: {
            groupByRowLabel: true
        }
    };

    var chart = new google.visualization.Timeline(document.getElementById('chart_div'));

    chart.draw(data, options);
}
