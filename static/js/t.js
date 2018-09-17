$(function(){
	$('.tm').on("click",function(){
	var	a = parseFloat($('.m1').html())
	var	b = parseFloat($('.m2').html())
	var	c = parseFloat($('.m3').html())
	var	d = parseFloat($('.m4').html())
	var	e = parseFloat($('.m5').val())

	var f = a+b+c+d+e
	alert(f)
	$('.total_marks').val(f)

	});
});