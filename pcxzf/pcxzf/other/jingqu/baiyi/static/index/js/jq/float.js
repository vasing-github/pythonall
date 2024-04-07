$(function(){
	var timer=null;/*定时器*/
	var _left=0;/*默认left距离*/
	var _top=20;/*默认top距离*/
	var top_folg=false;/*控制高度-锁*/
	var left_folg=true;/*控制宽度-锁*/
	var win_width=$(window).width()-$(".floatimg").width();/*获取并计算浏览器初始宽度*/
	var win_height=$(window).height()-$(".floatimg").height();/*获取并计算浏览器初始高度*/
	$("#liulan").html(win_height+"px");
	$("#sumwid").html(win_width+"px");;
	action();/*执行走动*/
	$(".floatimg").mouseover(function(){
		clearInterval(timer);
		$(this).find(".c_adver").css({"background":"url('images/no.gif')","bakcground-repeat":"no-repeat"});
		$(this).find(".txt").text("放开我!!!");

	}).mouseout(function(){
		action();
		$(this).find(".txt").text("杜绝广告");
		$(this).find(".c_adver").css({"background":"url('images/back.gif')","bakcground-repeat":"no-repeat"});
	});

	$(window).resize(function(){
		conobj=$(".floatimg");
		win_width=$(window).width()-conobj.width();
		win_height=$(window).height()-conobj.height();
		$("#liulan").html(win_height+"px");
		$("#sumwid").html(win_width+"px");;
	});

	function action(){
		timer=setInterval(function(){
			if(!top_folg){
				_top++;
				if(_top>=win_height){top_folg=true;};
			}else{
				_top--;
				if(_top<=0){top_folg=false;};
			};
			if(left_folg){
				 _left++;
				if(_left>=win_width){left_folg=false;};
			}else{
				_left--;
				if(_left<=0){left_folg=true;};
			};
            $("#textone").html(_top+"px");
			$("#timewid").html(_left+"px");
			$(".floatimg").animate({
				left:_left,
				top:_top
			},3);
		},15);
	};

	$(".floatimg .c_adver").dblclick(function(){
		$(this).parents(".floatimg").slideUp(500,function(){
			$(this).remove();
			clearInterval(timer);
		});
	});
	$(".floatclose").click(function(){//点击版权信息
		$('.floatimg').css({display:'none'});
	});
	$('.botgg-close').on('click',function(){//广告关闭按钮
		$('.bot-ggbox').css({'right':"-300px"})
	})
	var state;/*拖动锁*/
	$(".c_header").mousedown(function(event){
	state=false;
	var x=event.clientX;
	var y=event.clientY;
	var obj=$(this).parents(".floatimg");
	var c_left=obj.offset().left;
	var c_top=obj.offset().top;
			$(document).mousemove(function(e){
				if(!state){
					  var x1=e.clientX;
					  var y1=e.clientY;
					  var action_left=x1-x+c_left;
					  var action_top=y1-y+c_top;
					  if(action_left<=0){action_left=0;};
					  if(action_top<=0){action_top=0;}
					  if(action_left>=win_width){action_left=win_width;};
					  if(action_top>=win_height){action_top=win_height;};
					  obj.css({top:action_top,left:action_left});
					  _left=action_left;
					  _top=action_top;
					  $("#text").html(_top+"px");
					  $("#dywid").html(_left+"px");
					};
			}).mouseup(function(){
				state=true;
			});
	});
});