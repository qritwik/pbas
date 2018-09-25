$(function(){
	//o_t


	$('.o_t').on("click",function(){

	var o_t_avg = 0;
	var o_t1_favg = 0;
	var o_t2_favg = 0;
	var o_t3_favg = 0;

	var c=0 ;

	var o_tr_avg = 0;

	var	d=0;



	var o_t1_f1 = parseFloat($('.o_t1_f1').val());
	var o_t1_f2 = parseFloat($('.o_t1_f2').val());

	o_t1_favg = Math.round((o_t1_f1+o_t1_f2)/2);
	if(o_t1_favg<=100){
		$('.o_t1_favg').val(o_t1_favg);
		o_t_avg = o_t_avg + o_t1_favg;
		c++;
	}


    var o_t2_f1 = parseFloat($('.o_t2_f1').val());
	var o_t2_f2 = parseFloat($('.o_t2_f2').val());
	o_t2_favg = Math.round((o_t2_f1+o_t2_f2)/2);
	if(o_t2_favg<=100){
		$('.o_t2_favg').val(o_t2_favg);
		o_t_avg = o_t_avg + o_t2_favg;
		c++;
	}


	var o_t3_f1 = parseFloat($('.o_t3_f1').val());
	var o_t3_f2 = parseFloat($('.o_t3_f2').val());
	o_t3_favg = Math.round((o_t3_f1+o_t3_f2)/2);
	if(o_t3_favg<=100){
		$('.o_t3_favg').val(o_t3_favg);
		o_t_avg = o_t_avg + o_t3_favg;
		c++;
	}


	var o_t1_stu_app = parseFloat($('.o_t1_stu_app').val());
	var o_t1_stu_pass = parseFloat($('.o_t1_stu_pass').val());
	if(o_t1_stu_pass<=o_t1_stu_app){
		var o_t1 = Math.round((o_t1_stu_pass/o_t1_stu_app)*100);
		$('.o_t1_stu_perpass').val(o_t1);
		o_tr_avg = o_tr_avg + o_t1;
		d++;
	}


	var o_t2_stu_app = parseFloat($('.o_t2_stu_app').val());
	var o_t2_stu_pass = parseFloat($('.o_t2_stu_pass').val());
	if(o_t2_stu_pass<=o_t2_stu_app){
		var o_t2 = Math.round((o_t2_stu_pass/o_t2_stu_app)*100);
		$('.o_t2_stu_perpass').val(o_t2);
		o_tr_avg = o_tr_avg + o_t2;
		d++;
	}

	var o_t3_stu_app = parseFloat($('.o_t3_stu_app').val());
	var o_t3_stu_pass = parseFloat($('.o_t3_stu_pass').val());
	if(o_t3_stu_pass<=o_t3_stu_app){
		o_t3 = Math.round((o_t3_stu_pass/o_t3_stu_app)*100);
		$('.o_t3_stu_perpass').val(o_t3);
		o_tr_avg = o_tr_avg + o_t3 ;
		d++;
	}


	o_t_avg = Math.round((o_t_avg)/c);
	if(isNaN(o_t_avg)){
		$('.o_t_f_avg').val(0);
	}
	else{
		$('.o_t_f_avg').val(o_t_avg);
	}

	o_tr_avg = Math.round((o_tr_avg)/d);
	o_tr_avg =Math.round(o_tr_avg * 100)/100;
	if(isNaN(o_tr_avg)){
		$('.o_t_r_avg').val(0);
	}
	else{
		$('.o_t_r_avg').val(o_tr_avg);
	}

 });

//o_l
$('.o_l').on("click",function(){

	var o_l_avg = 0;
	var o_l1_favg = 0;
	var o_l2_favg = 0;
	var o_l3_favg = 0;
	var o_l4_favg = 0;
	var o_l5_favg = 0;


	var c=0 ;

	var o_lr_avg = 0;
	var d=0 ;



	var o_l1_f1 = parseFloat($('.o_l1_f1').val());
	var o_l1_f2 = parseFloat($('.o_l1_f2').val());
	o_l1_favg = Math.round((o_l1_f1+o_l1_f2)/2);
	if(o_l1_favg<=100){
		$('.o_l1_favg').val(o_l1_favg);
		o_l_avg = o_l_avg + o_l1_favg;
		c++;
	}


    var o_l2_f1 = parseFloat($('.o_l2_f1').val());
	var o_l2_f2 = parseFloat($('.o_l2_f2').val());
	o_l2_favg = Math.round((o_l2_f1+o_l2_f2)/2);
	if(o_l2_favg<=100){
		$('.o_l2_favg').val(o_l2_favg);
		o_l_avg = o_l_avg + o_l2_favg;
		c++;
	}


	var o_l3_f1 = parseFloat($('.o_l3_f1').val());
	var o_l3_f2 = parseFloat($('.o_l3_f2').val());
	o_l3_favg = Math.round((o_l3_f1+o_l3_f2)/2);
	if(o_l3_favg<=100){
		$('.o_l3_favg').val(o_l3_favg);
		o_l_avg = o_l_avg + o_l3_favg;
		c++;
	}

	var o_l4_f1 = parseFloat($('.o_l4_f1').val());
	var o_l4_f2 = parseFloat($('.o_l4_f2').val());
	o_l4_favg = Math.round((o_l4_f1+o_l4_f2)/2);
	if(o_l4_favg<=100){
		$('.o_l4_favg').val(o_l4_favg);
		o_l_avg = o_l_avg + o_l4_favg;
		c++;
	}

	var o_l5_f1 = parseFloat($('.o_l5_f1').val());
	var o_l5_f2 = parseFloat($('.o_l5_f2').val());
	o_l5_favg = Math.round((o_l5_f1+o_l5_f2)/2);
	if(o_l5_favg<=100){
		$('.o_l5_favg').val(o_l5_favg);
		o_l_avg = o_l_avg + o_l5_favg;
		c++;
	}

	var o_l1_stu_app = parseFloat($('.o_l1_stu_app').val());
	var o_l1_stu_pass = parseFloat($('.o_l1_stu_pass').val());
	if(o_l1_stu_pass<=o_l1_stu_app){
		var o_l1 = Math.round((o_l1_stu_pass/o_l1_stu_app)*100);
		$('.o_l1_stu_perpass').val(o_l1);
		o_lr_avg = o_lr_avg + o_l1;
		d++;
	}


	var o_l2_stu_app = parseFloat($('.o_l2_stu_app').val());
	var o_l2_stu_pass = parseFloat($('.o_l2_stu_pass').val());
	if(o_l2_stu_pass<=o_l2_stu_app){
		var o_l2 = Math.round((o_l2_stu_pass/o_l2_stu_app)*100);
		$('.o_l2_stu_perpass').val(o_l2);
		o_lr_avg = o_lr_avg + o_l2;
		d++;
	}

	var o_l3_stu_app = parseFloat($('.o_l3_stu_app').val());
	var o_l3_stu_pass = parseFloat($('.o_l3_stu_pass').val());
	if(o_l3_stu_pass<=o_l3_stu_app){
		var o_l3 = Math.round((o_l3_stu_pass/o_l3_stu_app)*100);
		$('.o_l3_stu_perpass').val(o_l3);
		o_lr_avg = o_lr_avg + o_l3;
		d++;
	}

	var o_l4_stu_app = parseFloat($('.o_l4_stu_app').val());
	var o_l4_stu_pass = parseFloat($('.o_l4_stu_pass').val());
	if(o_l4_stu_pass<=o_l4_stu_app){
		var o_l4 = Math.round((o_l4_stu_pass/o_l4_stu_app)*100);
		$('.o_l4_stu_perpass').val(o_l4);
		o_lr_avg = o_lr_avg + o_l4;
		d++;
	}

	var o_l5_stu_app = parseFloat($('.o_l5_stu_app').val());
	var o_l5_stu_pass = parseFloat($('.o_l5_stu_pass').val());
	var o_l5 = Math.round((o_l5_stu_pass/o_l5_stu_app)*100);
	if(o_l5_stu_pass<=o_l5_stu_app){
		$('.o_l5_stu_perpass').val(o_l5);
		o_lr_avg = o_lr_avg + o_l5;
		d++;
	}

	o_l_avg = Math.round((o_l_avg)/c);
	if(isNaN(o_l_avg)){
		$('.o_l_f_avg').val(0);
	}
	else{
		$('.o_l_f_avg').val(o_l_avg);
	}


	o_lr_avg = Math.round((o_lr_avg)/d);
	o_lr_avg =Math.round(o_lr_avg * 100)/100;

	if(isNaN(o_lr_avg)){
	$('.o_l_r_avg').val(0);

	}
	else{
	$('.o_l_r_avg').val(o_lr_avg);

	}


 });


	//e_t


	$('.e_t').on("click",function(){


	var e_t_avg = 0;
	var e_t1_favg = 0;
	var e_t2_favg = 0;
	var e_t3_favg = 0;

	var c=0 ;

	var e_tr_avg = 0;
	var	d=0;


	var e_t1_f1 = parseFloat($('.e_t1_f1').val());
	var e_t1_f2 = parseFloat($('.e_t1_f2').val());
	e_t1_favg = Math.round((e_t1_f1+e_t1_f2)/2);
	if(e_t1_favg<=100){
		$('.e_t1_favg').val(e_t1_favg);
		e_t_avg = e_t_avg + e_t1_favg;
		c++;
	}


    var e_t2_f1 = parseFloat($('.e_t2_f1').val());
	var e_t2_f2 = parseFloat($('.e_t2_f2').val());
	e_t2_favg = Math.round((e_t2_f1+e_t2_f2)/2);
	if(e_t2_favg<=100){
		$('.e_t2_favg').val(e_t2_favg);
		e_t_avg = e_t_avg + e_t2_favg;
		c++;
	}


	var e_t3_f1 = parseFloat($('.e_t3_f1').val());
	var e_t3_f2 = parseFloat($('.e_t3_f2').val());
	e_t3_favg = Math.round((e_t3_f1+e_t3_f2)/2);
	if(e_t3_favg<=100){
		$('.e_t3_favg').val(e_t3_favg);
		e_t_avg = e_t_avg + e_t3_favg;
		c++;
	}


	var e_t1_stu_app = parseFloat($('.e_t1_stu_app').val());
	var e_t1_stu_pass = parseFloat($('.e_t1_stu_pass').val());
	if(e_t1_stu_pass<=e_t1_stu_app){
		var e_t1 = Math.round((e_t1_stu_pass/e_t1_stu_app)*100);
		$('.e_t1_stu_perpass').val(e_t1);
		e_tr_avg = e_tr_avg + e_t1;
		d++;
	}


	var e_t2_stu_app = parseFloat($('.e_t2_stu_app').val());
	var e_t2_stu_pass = parseFloat($('.e_t2_stu_pass').val());
	if(e_t2_stu_pass<=e_t2_stu_app){
		var e_t2 = Math.round((e_t2_stu_pass/e_t2_stu_app)*100);
		$('.e_t2_stu_perpass').val(e_t2);
		e_tr_avg = e_tr_avg + e_t2;
		d++;
	}

	var e_t3_stu_app = parseFloat($('.e_t3_stu_app').val());
	var e_t3_stu_pass = parseFloat($('.e_t3_stu_pass').val());
	if(e_t3_stu_pass<=e_t3_stu_app){
		var e_t3 = Math.round((e_t3_stu_pass/e_t3_stu_app)*100);
		$('.e_t3_stu_perpass').val(e_t3);
		e_tr_avg = e_tr_avg + e_t3;
		d++;
	}

	e_t_avg = Math.round((e_t_avg)/c);

	if(isNaN(e_t_avg)){
	$('.e_t_f_avg').val(0);

	}
	else{
	$('.e_t_f_avg').val(e_t_avg);

	}

	e_tr_avg =Math.round((e_tr_avg)/d);
	e_tr_avg =Math.round(e_tr_avg * 100)/100;

	if(isNaN(e_tr_avg)){
	$('.e_t_r_avg').val(0);

	}
	else{
	$('.e_t_r_avg').val(e_tr_avg);

	}


 });

//e_l
$('.e_l').on("click",function(){

	var e_l_avg = 0;
	var e_l1_favg = 0;
	var e_l2_favg = 0;
	var e_l3_favg = 0;
	var e_l4_favg = 0;
	var e_l5_favg = 0;


	var c=0 ;

	var e_lr_avg = 0;
	var	d=0;

	var e_l1_f1 = parseFloat($('.e_l1_f1').val());
	var e_l1_f2 = parseFloat($('.e_l1_f2').val());
	 e_l1_favg = Math.round((e_l1_f1+e_l1_f2)/2);
	if(e_l1_favg<=100){
		$('.e_l1_favg').val(e_l1_favg);
		e_l_avg = e_l_avg + e_l1_favg;
		c++;
	}


    var e_l2_f1 = parseFloat($('.e_l2_f1').val());
	var e_l2_f2 = parseFloat($('.e_l2_f2').val());
	e_l2_favg = Math.round((e_l2_f1+e_l2_f2)/2);
	if(e_l2_favg<=100){
		$('.e_l2_favg').val(e_l2_favg);
		e_l_avg = e_l_avg + e_l2_favg;
		c++;
	}


	var e_l3_f1 = parseFloat($('.e_l3_f1').val());
	var e_l3_f2 = parseFloat($('.e_l3_f2').val());
	e_l3_favg = Math.round((e_l3_f1+e_l3_f2)/2);
	if(e_l3_favg<=100){
		$('.e_l3_favg').val(e_l3_favg);
		e_l_avg = e_l_avg + e_l3_favg;
		c++;
	}

	var e_l4_f1 = parseFloat($('.e_l4_f1').val());
	var e_l4_f2 = parseFloat($('.e_l4_f2').val());
	e_l4_favg = Math.round((e_l4_f1+e_l4_f2)/2);
	if(e_l4_favg<=100){
		$('.e_l4_favg').val(e_l4_favg);
		e_l_avg = e_l_avg + e_l4_favg;
		c++;
	}

	var e_l5_f1 = parseFloat($('.e_l5_f1').val());
	var e_l5_f2 = parseFloat($('.e_l5_f2').val());
	e_l5_favg = Math.round((e_l5_f1+e_l5_f2)/2);
	if(e_l5_favg<=100){
		$('.e_l5_favg').val(e_l5_favg);
		e_l_avg = e_l_avg + e_l5_favg;
		c++;
	}

	var e_l1_stu_app = parseFloat($('.e_l1_stu_app').val());
	var e_l1_stu_pass = parseFloat($('.e_l1_stu_pass').val());
	if(e_l1_stu_pass<=e_l1_stu_app){
		var e_l1 = Math.round((e_l1_stu_pass/e_l1_stu_app)*100);
		$('.e_l1_stu_perpass').val(e_l1);
		e_lr_avg = e_lr_avg + e_l1;
		d++;
	}


	var e_l2_stu_app = parseFloat($('.e_l2_stu_app').val());
	var e_l2_stu_pass = parseFloat($('.e_l2_stu_pass').val());
	if(e_l2_stu_pass<=e_l2_stu_app){
		var e_l2 = Math.round((e_l2_stu_pass/e_l2_stu_app)*100);
		$('.e_l2_stu_perpass').val(e_l2);
		e_lr_avg = e_lr_avg + e_l2;
		d++;
	}

	var e_l3_stu_app = parseFloat($('.e_l3_stu_app').val());
	var e_l3_stu_pass = parseFloat($('.e_l3_stu_pass').val());
	if(e_l3_stu_pass<=e_l3_stu_app){
		var e_l3 = Math.round((e_l3_stu_pass/e_l3_stu_app)*100);
		$('.e_l3_stu_perpass').val(e_l3);
		e_lr_avg = e_lr_avg + e_l3;
		d++;
	}

	var e_l4_stu_app = parseFloat($('.e_l4_stu_app').val());
	var e_l4_stu_pass = parseFloat($('.e_l4_stu_pass').val());
	if(e_l4_stu_pass<=e_l4_stu_app){
		var e_l4 = Math.round((e_l4_stu_pass/e_l4_stu_app)*100);
		$('.e_l4_stu_perpass').val(e_l4);
		e_lr_avg = e_lr_avg + e_l4;
		d++;
	}

	var e_l5_stu_app = parseFloat($('.e_l5_stu_app').val());
	var e_l5_stu_pass = parseFloat($('.e_l5_stu_pass').val());
	if(e_l5_stu_pass<=e_l5_stu_app){
		var e_l5 = Math.round((e_l5_stu_pass/e_l5_stu_app)*100);
		$('.e_l5_stu_perpass').val(e_l5);
		e_lr_avg = e_lr_avg + e_l5;
		d++;
	}

	e_l_avg = Math.round((e_l_avg)/c);

	if(isNaN(e_l_avg)){
	$('.e_l_f_avg').val(0);
	}
	else{
	$('.e_l_f_avg').val(e_l_avg);

	}

	e_lr_avg = Math.round((e_lr_avg)/d);
	e_lr_avg =Math.round(e_lr_avg * 100)/100;

	if(isNaN(e_lr_avg)){
	$('.e_l_r_avg').val(0);
	}
	else{
	$('.e_l_r_avg').val(e_lr_avg);

	}


 });


//

$('.e_p').on("click",function(){

	var p_avg = 0;
	var c=0;

	var p1_f1 = parseFloat($('.p1_f1').val());
	var p1_f2 = parseFloat($('.p1_f2').val());
	var p1_favg = Math.round((p1_f1+p1_f2)/2);
	if(p1_favg<=100){
		$('.p1_favg').val(p1_favg);
		p_avg = p_avg + p1_favg;
		c++;
	}

	var p2_f1 = parseFloat($('.p2_f1').val());
	var p2_f2 = parseFloat($('.p2_f2').val());
	var p2_favg = Math.round((p2_f1+p2_f2)/2);
	if(p2_favg<=100){
		$('.p2_favg').val(p2_favg);
		p_avg = p_avg + p2_favg;
		c++;
	}

	var p3_f1 = parseFloat($('.p3_f1').val());
	var p3_f2 = parseFloat($('.p3_f2').val());
	var p3_favg = Math.round((p3_f1+p3_f2)/2);
	if(p3_favg<=100){
		$('.p3_favg').val(p3_favg);
		p_avg = p_avg + p3_favg;
		c++;
	}

	var p4_f1 = parseFloat($('.p4_f1').val());
	var p4_f2 = parseFloat($('.p4_f2').val());
	var p4_favg = Math.round((p4_f1+p4_f2)/2);
	if(p4_favg<=100){
		$('.p4_favg').val(p4_favg);
		p_avg = p_avg + p4_favg;
		c++;
	}

	var p5_f1 = parseFloat($('.p5_f1').val());
	var p5_f2 = parseFloat($('.p5_f2').val());
	var p5_favg = Math.round((p5_f1+p5_f2)/2);
	if(p5_favg<=100){
		$('.p5_favg').val(p5_favg);
		p_avg = p_avg + p5_favg;
		c++;
	}

	var p6_f1 = parseFloat($('.p6_f1').val());
	var p6_f2 = parseFloat($('.p6_f2').val());
	var p6_favg = Math.round((p6_f1+p6_f2)/2);
	if(p6_favg<=100){
		$('.p6_favg').val(p6_favg);
		p_avg = p_avg + p6_favg;
		c++;
	}

	var p7_f1 = parseFloat($('.p7_f1').val());
	var p7_f2 = parseFloat($('.p7_f2').val());
	var p7_favg = Math.round((p7_f1+p7_f2)/2);
	if(p7_favg<=100){
		$('.p7_favg').val(p7_favg);
		p_avg = p_avg + p7_favg;
		c++;
	}

	var p8_f1 = parseFloat($('.p8_f1').val());
	var p8_f2 = parseFloat($('.p8_f2').val());
	var p8_favg = Math.round((p8_f1+p8_f2)/2);
	if(p8_favg<=100){
		$('.p8_favg').val(p8_favg);
		p_avg = p_avg + p8_favg;
		c++;
	}

	var p9_f1 = parseFloat($('.p9_f1').val());
	var p9_f2 = parseFloat($('.p9_f2').val());
	var p9_favg = Math.round((p9_f1+p9_f2)/2);
	if(p9_favg<=100){
		$('.p9_favg').val(p9_favg);
		p_avg = p_avg + p9_favg;
		c++;
	}

	var p10_f1 = parseFloat($('.p10_f1').val());
	var p10_f2 = parseFloat($('.p10_f2').val());
	var p10_favg = Math.round((p10_f1+p10_f2)/2);
	if(p10_favg<=100){
		$('.p10_favg').val(p10_favg);
		p_avg = p_avg + p10_favg;
		c++;
	}

	p_avg = Math.round(p_avg/c);
	if(isNaN(p_avg)){
	$('.p_f_avg').val(0);
	}
	else{
	$('.p_f_avg').val(p_avg);

	}
 });

//out of 40

$('.f_calc').on("click",function(){

	var c = 5;
	var d = 4;


	var o_t_avg = parseFloat($('.o_t_f_avg').val());
	var o_l_avg = parseFloat($('.o_l_f_avg').val());
	var e_t_avg = parseFloat($('.e_t_f_avg').val());
	var e_l_avg = parseFloat($('.e_l_f_avg').val());
	var p_avg = parseFloat($('.p_avg').val());

	var o_tr_avg = parseFloat($('.o_t_r_avg').val());
	var o_lr_avg = parseFloat($('.o_l_r_avg').val());
	var e_tr_avg = parseFloat($('.e_t_r_avg').val());
	var e_lr_avg = parseFloat($('.e_l_r_avg').val());


	if(isNaN(o_t_avg)){
		o_t_avg  = 0;
		c--;
	}
	if(isNaN(o_l_avg)){
		o_l_avg = 0;
		c--;
	}
	if(isNaN(e_t_avg)){
		e_t_avg  = 0;
		c--;
	}
	if(isNaN(e_l_avg)){
		e_l_avg  = 0;
		c--;
	}
	if(isNaN(p_avg)){
		p_avg  = 0;
		c--;
	}

	if(isNaN(o_tr_avg)){
		o_tr_avg  = 0;
		d--;
	}

	if(isNaN(o_lr_avg)){

		o_lr_avg  = 0;
		d--;
	}
	if(isNaN(e_tr_avg)){
		e_tr_avg  = 0;

		d--;
	}
	if(isNaN(e_lr_avg)){
		e_lr_avg  = 0;
		d--;
	}


	var a = (o_t_avg + o_l_avg + e_t_avg + e_l_avg + p_avg)/c;
	var b = (o_tr_avg + o_lr_avg + e_tr_avg + e_lr_avg)/d;

	console.log(a);

	console.log(b);

	var f_marks = 0;

	if(a<59.5){
		f_marks = 0;
	}
	else if(a>59.5 && a<=69.5)
		f_marks = 5;

	else if(a>69.5 && a<=79.5)
		f_marks = 10;

	else if(a>79.5 && a<=89.5)
		f_marks = 15;

	else if(a>89.5)
		f_marks = 20;


	if(b<59.5){
		f_marks = f_marks + 0;
	}
	else if(b>59.5 && b<=69.5)
		f_marks = f_marks + 5;

	else if(b>69.5 && b<=79.5)
		f_marks = f_marks + 10;

	else if(b>79.5 && b<=89.5)
		f_marks = f_marks+ 15;

	else if(b>89.5)
		f_marks = f_marks+20;


	$('.e_o_f_r_final').val(f_marks);
 });



//r&d

$('.rd').on("click",function(){
	a=0;
	b=0;
	c=0;
	d=0;
	e=0;
	f=0;

	var w_s_d = parseFloat($('.w_s_d').val());
	var w_n_d = parseFloat($('.w_n_d').val());
	var w_i_d = parseFloat($('.w_i_d').val());

	if(isNaN(w_s_d)){
		w_s_d = 0;
	}

	if(isNaN(w_n_d)){
		w_n_d = 0;
	}

	if(isNaN(w_i_d)){
		w_i_d = 0;
	}


	a = (w_s_d * 0.5) + (w_n_d * 1) + (w_i_d * 1) ;

	//max 5
	if(a>=5){
		$('.w_m').val(5);
		a = 5;
	}
	else{
		$('.w_m').val(a);
	}


	var p_s_d = parseFloat($('.p_s_d').val());
	var p_n_d = parseFloat($('.p_n_d').val());
	var p_i_d = parseFloat($('.p_i_d').val());

	if(isNaN(p_s_d)){
		p_s_d = 0;
	}

	if(isNaN(p_n_d)){
		p_n_d = 0;
	}

	if(isNaN(p_i_d)){
		p_i_d = 0;
	}

	b = (p_s_d * 2) + (p_n_d * 4) + (p_i_d * 5) ;

	//max 5
	if(b>=5){
		$('.p_m').val(5);
		b= 5;
	}
	else{
		$('.p_m').val(b);
	}


	//max 10
	var onl_course_c = parseFloat($('.onl_course_c').val())

	if(isNaN(onl_course_c)){
		onl_course_c = 0;
	}

	var c = onl_course_c*5;

	if(c>=10){
		c = 10;
	}
	$('.onl_course_m').val(c);

	///
	///
	var m=0;

	if($('.s_c_name').val()){
		var s_c_m = parseFloat($('.s_c_name').val());
		s_c_m = s_c_m*5
		$('.s_c_m').val(s_c_m)
		m = m+s_c_m
	}


	if($('.f_c_name').val()){
		var f_c_m = parseFloat($('.f_c_name').val());
		f_c_m = f_c_m*3
		$('.f_c_m').val(f_c_m)
		m = m+f_c_m
	}


	if($('.o_c_name').val()){
		var o_c_m = parseFloat($('.o_c_name').val());
		o_c_m = o_c_m*2
		$('.o_c_m').val(o_c_m)
		m = m+o_c_m
	}

	if(m>8){
		m= 8
	}

////
	n= 0

	if($('.s_j_name').val()){
		var s_j_m = parseFloat($('.s_j_name').val());
		s_j_m=s_j_m*10
		$('.s_j_m').val(s_j_m)
		n = n+s_j_m
	}


	if($('.f_j_name').val()){
		var f_j_m = parseFloat($('.f_j_name').val());
		f_j_m=f_j_m*6
		$('.f_j_m').val(f_j_m)
		n = n+f_j_m
	}


	if($('.o_j_name').val()){
		var o_j_m = parseFloat($('.o_j_name').val());
		o_j_m=o_j_m*4
		$('.o_j_m').val(o_j_m)
		n = n+o_j_m
	}

	if(n>12){
		n = 12
	}






	var book_i = parseFloat($('.book_i').val());
	var book_n = parseFloat($('.book_n').val());
	var book_ci = parseFloat($('.book_ci').val());
	var book_cn = parseFloat($('.book_cn').val());
	var book_ai = parseFloat($('.book_ai').val());
	var book_nm = parseFloat($('.book_nm').val());

	if(isNaN(book_i)){
		book_i = 0;
	}

	if(isNaN(book_n)){
		book_n = 0;
	}

	if(isNaN(book_ci)){
		book_ci = 0;
	}

	if(isNaN(book_cn)){
		book_cn = 0;
	}

	if(isNaN(book_ai)){
		book_ai = 0;
	}

	if(isNaN(book_nm)){
		book_nm = 0;
	}





	d = (book_i * 10) + (book_n * 8) + (book_ci * 6) + (book_cn * 4) + (book_ai * 10) + (book_nm * 6) ;

	//max 10
	if(d>=10){
		$('.book_m').val(10);
		d = 10;
	}
	else{
		$('.book_m').val(d);
	}

	var if_s = 0;
	var if_f = 0;
	var if_c = 0;
	var ef_s = 0;
	var ef_f = 0;
	var ef_c = 0;
	var eef_s = 0;
	var eef_f = 0;
	var eef_c = 0;
	var cw_2 = 0;
	var cw_2_5 = 0;
	var cw_5 = 0;

	if($('.if_s').val()){
		if_s = 5;

	}

	if($('.if_f').val()){
		if_f = 3;
	}

	if($('.if_c').val()){
		if_c = 2;
	}

	if($('.ef_s').val()){
		ef_s = 5;
	}

	if($('.ef_f').val()){
		ef_f = 3;
	}

	if($('.ef_c').val()){
		ef_c = 2;
	}

	if($('.eef_s').val()){
		eef_s = 10;
	}

	if($('.eef_f').val()){
		eef_f = 6;
	}

	if($('.eef_c').val()){
		eef_c = 4;
	}

	if($('.cw_2').val()){
		cw_2 = 5;
	}

	if($('.cw_2_5').val()){
		cw_2_5 = 8;
	}

	if($('.cw_5').val()){
		cw_5 = 10;
	}

	e = if_s + if_f +if_c + ef_s +ef_f +ef_c + eef_s + eef_f + eef_c + cw_2 + cw_2_5 + cw_5 ;

	//max 5
	if(e>=5){
		$('.rp_marks').val(5);
		e =5;
	}
	else{
		$('.rp_marks').val(e);
	}

	 f = a+b+c+d+e+m+n;

	//out of 35

	if(f>=35){
		$('.rd_tot_marks').val(35);
		f = 35;
	}
	else{
		$('.rd_tot_marks').val(f);
	}
 });
 $('.p12').on("click",function(){
	var a = parseFloat($('.m3').val())

	if(a > 5){

 		$('.m3').val(5);
 	}
 var b = parseFloat($('.m4').val())

 	if(b>15){
 		$('.m4').val(15);
 	}
 });

 $('.ipr_type').change(function(){
 	if ($(this).val() == 8){
 		$('.ipr_status').attr('disabled',true)
 		$('.ipr_status').val(8)
 		$('.ipr_info').attr('disabled',true)
 		$('.ipr_info').val("None")
 	}
 	else{
 		$('.ipr_status').attr('disabled',false)
 		$('.ipr_info').attr('disabled',false)
 	}

 });

});
