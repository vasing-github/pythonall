//移动端判定
function goPAGE() {
      var is_iPd = navigator.userAgent.match(/(iPad|iPod|iPhone)/i) != null;
      var is_mobi = navigator.userAgent.toLowerCase().match(/(ipod|iphone|android|coolpad|mmp|smartphone|midp|wap|xoom|symbian|j2me|blackberry|win ce)/i) != null;
      if(is_mobi && window.location.search.indexOf("mv=fp")<0){
        window.location.href="http://wap.pcbygz.com";
      }
}
goPAGE();
//移动端判定结束
jQuery(document).ready(function() {
		var counter = 0;
		if (window.history && window.history.pushState) {
			$(window).on('popstate', function () {
				window.history.pushState('forward', null, '#');
				window.history.forward(1);
				
			});
		}
		window.history.pushState('forward', null, '#'); //在IE中必须得有这两行
		window.history.forward(1);
	});
$(function(){
	$('.topbox').addClass('active');
	$('.allrightbox').addClass('active');
	//	点击展开搜索框
	$('.kssearch').click(function() {
		$('.kssearch-form').toggleClass('active');
		$('.kssearch').toggleClass('active');
		$('.toplang').removeClass('active');
		$('.riglag').removeClass('active');
	});
	$('.riglag').click(function() {
		$('.riglag').toggleClass('active');
		$('.toplang').toggleClass('active');
		$('.kssearch-form').removeClass('active');
		$('.kssearch').removeClass('active');
	});
	//点击展开微信二维码
	$('.all-btn-wxx').on('click',function(){
		$('.wx-zsbox').css({'left':"0"})
	})
	//点击关闭微信二维码
	$(".wx-close").click(function(){
		$('.wx-zsbox').css({'left':"100%"})
	});
	//返回顶部
	$('.backtop').on('click',function(){
		$("html,body").animate({scrollTop:0},300)
	})
});

$(window).scroll(function(){
	if($(window).width()>1366){
		var Nhh = '78px'
		var Uhh = '65px'
	}
	if($(window).width()<=1366){
		var Nhh = '70px'
		var Uhh = '60px'
	}
   	if($(window).scrollTop()>=$('.topbox').height()*0.5){
		$('.topbox').removeClass('active');
		$('.backtop').addClass('active');

		
	}
   	if($(window).scrollTop()<$('.topbox').height()*0.5){
		$('.topbox').addClass('active');
		$('.backtop').removeClass('active');
	}
   	
})