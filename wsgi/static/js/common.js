$(document).ready(function() {

	//FancyBox
	//Documentation: http://fancybox.net/howto
    $(".fancybox").fancybox();

	//Carousel
	//Documentation: http://owlgraphic.com/owlcarousel/
	$("#owl-demo").owlCarousel({
      autoPlay: 3000, 
      items : 4,
      itemsDesktop : [1199,3],
      itemsDesktopSmall : [979,3]
  });
    
    var owl = $("#owl-demo");
	owl.owlCarousel({
		items : 4,
		autoHeight : true
	});
	owl.on("mousewheel", ".owl-wrapper", function (e) {
		if (e.deltaY > 0) {
			owl.trigger("owl.prev");
		} else {
			owl.trigger("owl.next");
		}
		e.preventDefault();
	});
	$(".next_button").click(function() {
		owl.trigger("owl.next");
	});
	$(".prev_button").click(function() {
		owl.trigger("owl.prev");
	});

});



