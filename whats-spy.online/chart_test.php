<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://www.amcharts.com/lib/3/amcharts.js"></script>
        <script src="https://www.amcharts.com/lib/3/serial.js"></script>
        <script src="https://www.amcharts.com/lib/3/gantt.js"></script>
        <script src="https://www.amcharts.com/lib/3/plugins/export/export.min.js"></script>
        <link rel="stylesheet" href="https://www.amcharts.com/lib/3/plugins/export/export.css" type="text/css" media="all" />
        <script src="https://www.amcharts.com/lib/3/themes/light.js"></script>
        <title>Test chart</title>
        <script>
            var ids = "<?echo $_GET['id'];?>";
            var key = "<?echo $_GET['key'];?>";
        </script>
        <style>
            #chartdiv {
                width: 100%;
                height: 500px;
            }
        </style>
        <script>
        $.get( "scripts/dbHelper.php?type=2&id="+ ids + "&key=" + key, function() {}).done(function(data) {
            data = JSON.parse(data);
            data.forEach(function(points) {
                points.segments.forEach(function(point) {
                    point.start = new Date(point.start);
                    point.end = new Date(point.end);
                });
            });
            createChart( data );
            console.log(data);
        });

        function createChart(data) {
            var chart = AmCharts.makeChart( "chartdiv", {
            "type": "gantt",
            "theme": "light",
            "marginRight": 70,
            //"period": "DD",
            //"dataDateFormat": "YYYY-MM-DD",
            "columnWidth": 0.5,
            "valueAxis": {
                "type": "date"
            },
            //"brightnessStep": 7,
            "graph": {
                "fillAlphas": 1,
                "lineAlpha": 1,
                "lineColor": "#fff",
                "balloonText": "<b>[[name]]</b>:<br />[[start]] -- [[end]]"
            },
            "balloonDateFormat": "HH-MM-SS",
            "rotate": true,
            "categoryField": "category",
            "segmentsField": "segments",
            "colorField": "color",
            "startDateField": "start",
            "endDateField": "end",
            "dataProvider": data,
            "valueScrollbar": {
                "autoGridCount": true
            },
            "chartCursor": {
                "cursorColor": "#55bb76",
                "valueBalloonsEnabled": false,
                "cursorAlpha": 0,
                "valueLineAlpha": 0.5,
                "valueLineBalloonEnabled": false,
                "valueLineEnabled": false,
                "zoomable": false,
                "valueZoomable": true
            },
            "export": {
                "enabled": false
            }
            } );
        }
        </script>
    </head>
    <body>
        <div id="chartdiv"></div>
    </body>
</html>
