$(function() {
	$('.cba').change(function() {
		var one = parseInt($('.abc').val());
		var two = parseInt($('.cba').val());
		$('.poia').html(one+two);
	})
	$('.abc').change(function() {
		var one = parseInt($('.abc').val());
		var two = parseInt($('.cba').val());
		$('.poia').html(one+two);
	})
})