<html>
<head>
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-109904572-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    //gtag('js', new Date());
    
    //gtag('config', 'UA-109904572-1');
    </script>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script>
        var ids = "<?echo $_GET['id'];?>";
        var key = "<?echo $_GET['key'];?>";
    </script>
    <script type="text/javascript" src="js/chart.js?v=<?echo filemtime('js/chart.js');?>"></script>
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="shortcut icon" type="image/x-icon" href="img/favicon.ico?v=1">
    <title>Whats-Spy.online</title>
</head>
<body>
<div class="global_wrapper">
    <b>Status: <?include 'scripts/status.php';?></b><br>
    <div id="chart_div"></div>
</div>
</body>
</html>