$(function(){

	$('.s_case').on("click",function(){
		$('.c_marks').style.display = "block";
	});

	

	$('.tm').on("click",function(){
	var	a = parseFloat($('.m1').html())
	var	b = parseFloat($('.m2').html())
	var	c = parseFloat($('.m3').val())
	var	d = parseFloat($('.m4').val())

	var g = parseFloat($('.m6').val())

	if(isNaN(g)){
		g = 0;
	}

	var f = a+b+c+d+g
	alert(f)
	$('.total_marks').val(f)

	});
});