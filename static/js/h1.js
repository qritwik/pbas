$(function(){
	$('.tm').on("click",function(){
	var	a = parseFloat($('.m1').html())
	var	b = parseFloat($('.m2').html())
	var	c = parseFloat($('.m3').val())
	var	d = parseFloat($('.m4').val())

	var f = a+b+c+d
	alert(f)
	$('.total_marks').val(f)

	});
});