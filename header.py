<html>
<head>
<?php
   setcookie("name", "Jya Bhadoria", time()+3600, "/","", 0);
   setcookie("age", "36", time()+3600, "/", "",  0);
?>
<meta name="description" content="" />
<meta name="keywords" content="" />
<title>OBM</title>
<link href='../images/logo.jpg' rel='icon'/>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<link rel="stylesheet" type="text/css" href="../css/style.css" />
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
<script type="text/javascript" src="../js/jquery.dropotron-1.0.js"></script>
<script type="text/javascript" src="../js/jquery.slidertron-1.1.js"></script>
<script type="text/javascript">
	$(function() {
		$('#menu > ul').dropotron({
			mode: 'fade',
			globalOffsetY: 11,
			offsetY: -15
		});
		$('#slider').slidertron({
			viewerSelector: '.viewer',
			indicatorSelector: '.indicator span',
			reelSelector: '.reel',
			slidesSelector: '.slide',
			speed: 'slow',
			advanceDelay: 4000
		});
	});
</script>
</head>
<body style="background-color:#003366 ;">
<div id="wrapper" >
	<div id="header" style="background-color:#996699;">
		<div id="logo">
                    <h1><a href="#"><font color='white'>Book-market</font></a></h1>
		</div>
		<div id="slogan">
			<h2><font color='white'>Buy & Sell Books....</font></h2>
		</div>
	</div>
