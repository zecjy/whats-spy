var chart = AmCharts.makeChart( "chartdiv", {
  "type": "gantt",
  "theme": "light",
  "marginRight": 70,
  "period": "DD",
  "dataDateFormat": "YYYY-MM-DD",
  "columnWidth": 0.5,
  "valueAxis": {
    "type": "date"
  },
  "brightnessStep": 7,
  "graph": {
    "fillAlphas": 1,
    "lineAlpha": 1,
    "lineColor": "#fff",
    "fillAlphas": 0.85,
    "balloonText": "<b>[[task]]</b>:<br />[[open]] -- [[value]]"
  },
  "rotate": true,
  "categoryField": "category",
  "segmentsField": "segments",
  "colorField": "color",
  "startDateField": "start",
  "endDateField": "end",
  "dataProvider": [ {
    "category": "Module #1",
    "segments": [ {
      "start": new Date(1511049961000),
      "end": new Date(1511053644000),
      "color": "#b9783f",
      "task": "Gathering requirements"
    }, {
      "start": "2016-01-16",
      "end": "2016-01-27",
      "task": "Producing specifications"
    }, {
      "start": "2016-02-05",
      "end": "2016-04-18",
      "task": "Development"
    }, {
      "start": "2016-04-18",
      "end": "2016-04-30",
      "task": "Testing and QA"
    } ]
  }, {
    "category": "Module #2",
    "segments": [ {
      "start": "2016-01-08",
      "end": "2016-01-10",
      "color": "#cc4748",
      "task": "Gathering requirements"
    }, {
      "start": "2016-01-12",
      "end": "2016-01-15",
      "task": "Producing specifications"
    }, {
      "start": "2016-01-16",
      "end": "2016-02-05",
      "task": "Development"
    }, {
      "start": "2016-02-10",
      "end": "2016-02-18",
      "task": "Testing and QA"
    } ]
  }, {
    "category": "Module #3",
    "segments": [ {
      "start": "2016-01-02",
      "end": "2016-01-08",
      "color": "#cd82ad",
      "task": "Gathering requirements"
    }, {
      "start": "2016-01-08",
      "end": "2016-01-16",
      "task": "Producing specifications"
    }, {
      "start": "2016-01-19",
      "end": "2016-03-01",
      "task": "Development"
    }, {
      "start": "2016-03-12",
      "end": "2016-04-05",
      "task": "Testing and QA"
    } ]
  }, {
    "category": "Module #4",
    "segments": [ {
      "start": "2016-01-01",
      "end": "2016-01-19",
      "color": "#2f4074",
      "task": "Gathering requirements"
    }, {
      "start": "2016-01-19",
      "end": "2016-02-03",
      "task": "Producing specifications"
    }, {
      "start": "2016-03-20",
      "end": "2016-04-25",
      "task": "Development"
    }, {
      "start": "2016-04-27",
      "end": "2016-05-15",
      "task": "Testing and QA"
    } ]
  }, {
    "category": "Module #5",
    "segments": [ {
      "start": "2016-01-01",
      "end": "2016-01-12",
      "color": "#448e4d",
      "task": "Gathering requirements"
    }, {
      "start": "2016-01-12",
      "end": "2016-01-19",
      "task": "Producing specifications"
    }, {
      "start": "2016-01-19",
      "end": "2016-03-01",
      "task": "Development"
    }, {
      "start": "2016-03-08",
      "end": "2016-03-30",
      "task": "Testing and QA"
    } ]
  } ],
  "valueScrollbar": {
    "autoGridCount": true
  },
  "chartCursor": {
    "cursorColor": "#55bb76",
    "valueBalloonsEnabled": false,
    "cursorAlpha": 0,
    "valueLineAlpha": 0.5,
    "valueLineBalloonEnabled": true,
    "valueLineEnabled": true,
    "zoomable": false,
    "valueZoomable": true
  },
  "export": {
    "enabled": true
  }
} );