$(function(){
	$('.tm').on("click",function(){
		 $(".c_marks").slideToggle("slow");
	});

	$('.tm').on("click",function(){
	var g = 0; 
	var	a = parseFloat($('.m1').html())
	var	b = parseFloat($('.m2').html())
	var	c = parseFloat($('.m3').html())
	var	d = parseFloat($('.m4').html())
	var	e = parseFloat($('.m5').val())
	 g = parseFloat($('.m6').val())
	var f = a+b+c+d+e
	alert(f)
	$('.total_marks').val(f)

	});
});