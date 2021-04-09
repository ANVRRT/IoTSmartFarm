<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
<link rel="icon" href="images/favicon.ico">
<link rel="shortcut icon" href="images/favicon.ico" />
<link rel="stylesheet" href="css/owl.carousel.css">
<link rel="stylesheet" href="css/style.css">
<script src="js/jquery.js"></script>
<script src="js/jquery-migrate-1.1.1.js"></script>
<script src="js/script.js"></script>
<script src="js/jquery.ui.totop.js"></script>
<script src="js/superfish.js"></script>
<script src="js/sForm.js"></script>
<script src="js/jquery.equalheights.js"></script>

<script src="js/jquery.easing.1.3.js"></script>
<script src="js/owl.carousel.js"></script>
<script>
$(document).ready(function(){
    $().UItoTop({ easingType: 'easeOutQuart' });
    /*carousel*/
    var owl=$("#owl");
    owl.owlCarousel({
        items : 1, //10 items above 1000px browser width
        navigation : true,
        pagination :  false
    });
    var owl=$("#owl1");
    owl.owlCarousel({
        items : 1, //10 items above 1000px browser width
        navigation : true,
        pagination :  false
    });
})
</script>
<title> IoT Smart Farm</title>