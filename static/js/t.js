$(function(){
	$('.tm').on("click",function(){
	var	a = parseFloat($('.m1').html())
	alert("a")
	alert(a)
	var	b = parseFloat($('.m2').html())
	alert(b)
	var	c = parseFloat($('.m3').html())
	alert(c)
	var	d = parseFloat($('.m4').html())
	alert(d)
	var	e = parseFloat($('.m5').val())
	alert(e)
	var f = a+b+c+d+e
	$('.total_marks').val(f)

	});
});
