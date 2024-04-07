//景点滚动样式
$(function() {
	//背景自动播放
	var bgmusic = document.getElementById('voice');
    bgmusic.play();
    if(bgmusic.paused){
	 	$('#bgmusic').removeClass('active');
		$('.bgmusico').removeClass('iconyinle');
		$('.bgmusico').addClass('iconjingyin');
	   
	}else{
	    $('#bgmusic').addClass('active')
    	$('.bgmusico').addClass('iconyinle');
		$('.bgmusico').removeClass('iconjingyin');
	}
	//音乐播放
    $('#bgmusic').on('click',function(){
		if(bgmusic.paused){
		    bgmusic.play();
		    $('#bgmusic').addClass('active')
	    	$('.bgmusico').addClass('iconyinle');
			$('.bgmusico').removeClass('iconjingyin');
		}else{
		    bgmusic.pause()
		    $('#bgmusic').removeClass('active');
			$('.bgmusico').removeClass('iconyinle');
			$('.bgmusico').addClass('iconjingyin');
		}
	})
   
   /*首页景点滚动轮播图*/
    var IndjdSlide = new Swiper ('.solution-swiper', {
        wrapperClass: 'solution-wrapper',
		slideClass: 'solution-slide',
		slidesPerView: 'auto',
		loop: true,
		autoplay: {
            delay: 3000,//切换时间
        },
    });
	IndjdSlide.el.onmouseleave = function(){
	    IndjdSlide.autoplay.start();
	},
	IndjdSlide.el.onmouseover = function(){ 
	    IndjdSlide.autoplay.stop();
	}
   
	$('.jdmenu li').click(function(){
    	$(".jdmenu li").removeClass("active");
		$(this).addClass("active");     
    	$('.jdnrbox').removeClass("on").eq($(this).index()).addClass("on");
	});
	//点击视频播放按钮
	$('.spbbbg').on('click',function(){
		$('#spplay').attr('src','1230.mp4')
		$('.sp-playbox').css({'left':"0"})
		$('body').css({'overflow':'hidden'})
	})
	//点击视频关闭按钮
	$(".sp-close").click(function(){
		$('.video-spbox').find('#spplay').attr('src','');
		$('.sp-playbox').css({'left':"100%"})
		$('body').css({'overflow':'auto'})
	});
	//内容视频播放
	$('.videobtn').on('click',function(){
		$('#spplay').attr('src',$(this).find('a').attr('art'))
		$('.sp-playbox').css({'left':"0"})
		
		//清空音乐及恢复样式
    	$('#audiox').attr('src','');
    	$('.jjaudio').removeClass('active');
	    $('.jjbfico').addClass('iconlaba');
	    $('.jjbfico').removeClass('iconjingyin');
	})
	//栏目点击load事件
	$('.lmtcx').on('click',function(){
		var links = $(this).attr('links')
		$('body').css({'overflow':'hidden'})
		$('.lmtcbox').addClass('disstyle');
		$('.lmtcbox .tcbg').addClass('disstyle');
		setTimeout(function(){$('.lmtcbox .tcbg2').addClass('hei')},300);
		setTimeout(function(){$('.lmtcbox .tcbg2').addClass('width')},900);
		
		setTimeout(function(){$('.lmtcbox .TCnrbox').addClass('hei')},300);
		setTimeout(function(){$('.lmtcbox .TCnrbox').addClass('width')},900);
		setTimeout(function(){$('.lmtcbox .TCnrbox').addClass('bor')},1200);
		setTimeout(function(){$('.lmtcbox .loadbox').addClass('disstyle')},1200);
		setTimeout(function(){$('.lmtcbox .closebtn').addClass('disstyle')},1200);
		$('.loadbox').load(links);
		console.log(links)
	});
	
	//内容点击load事件
	$('.nrtcx').on('click',function(){
		var links = $(this).attr('links')
		$('body').css({'overflow':'hidden'})
		$('.lmtcbox').addClass('disstyle');
		$('.lmtcbox .tcbg').addClass('disstyle');
		setTimeout(function(){$('.lmtcbox .tcbg2').addClass('hei')},300);
		setTimeout(function(){$('.lmtcbox .tcbg2').addClass('width')},900);
		
		setTimeout(function(){$('.lmtcbox .TCnrbox').addClass('hei')},300);
		setTimeout(function(){$('.lmtcbox .TCnrbox').addClass('width')},900);
		setTimeout(function(){$('.lmtcbox .TCnrbox').addClass('bor')},1200);
		setTimeout(function(){$('.lmtcbox .loadbox').addClass('disstyle')},1200);
		setTimeout(function(){$('.lmtcbox .closebtn').addClass('disstyle')},1200);
		$('.loadbox').load(links);
	});
	
	
	//内容弹窗
	$('.tcbtn').on('click',function(){
		var txt = $(this).attr('txt');
		var art = $(this).attr('art');
		$("<iframe id='nrtc_iframes' frameborder='0'></iframe>").prependTo('.nrtc-nrbox');
   		$('.nrtc-nrbox #nrtc_iframes').attr("src", art);
		$('.nrtc-nrbox .tc-top .title').text(txt);
		setTimeout(function(){
			$('.nr-tc').addClass('active');
			$('.nrtc-nrbox').addClass('active');
		},100);
		//清空音乐及恢复样式
    	$('#audiox').attr('src','');
    	$('.jjaudio').removeClass('active');
	    $('.jjbfico').addClass('iconlaba');
	    $('.jjbfico').removeClass('iconjingyin');
	})
	$('.nrtc-back').on('click',function(){
		$('#nrtc_iframes').attr('src','');;
		$('.nr-tc').removeClass('active');
		$('.nrtc-nrbox').removeClass('active');
		$('.nrtc-nrbox .tc-top .title').text('');
		setTimeout(function(){
			 $('#nrtc_iframes').remove();//清空父元素下iframes
		},400);
	})
	
	//音乐播放
	var audio1 = document.getElementById('audio1');
	$('.jjaudio1').on('click',function(){
		var music = $('#audio1').attr('src');
		var musicNow = $(this).find('a').attr('art');
		if( music == "" || music !== musicNow){
		    $('#audio1').attr('src',$(this).find('a').attr('art'));
		}
		$('.jjaudio1').removeClass('active');
	    $('.jjbfico1').addClass('iconlaba');
	    $('.jjbfico1').removeClass('iconjingyin');
	    
	    console.log(1)
		if(audio1.paused){
		    audio1.play();
		    $(this).addClass('active');
	    	$(this).find('.jjbfico1').removeClass('iconlaba');
	    	$(this).find('.jjbfico1').addClass('iconjingyin');
		}else{
		    audio1.pause()
		    $(this).removeClass('active');
	    	$(this).find('.jjbfico1').addClass('iconlaba');
	    	$(this).find('.jjbfico1').removeClass('iconjingyin');
		}
		audio1.loop = false;
	    audio1.addEventListener('ended', function () {  
	    	$('.jjaudio1').removeClass('active');
	    	$('.jjbfico1').addClass('iconlaba');
	    	$('.jjbfico1').removeClass('iconjingyin');
	    }, false);
	});
	
	
	
	//首页banner
	function autoPlay(){
		this.init();
	}
	autoPlay.prototype={
		time:null,
		index:0,
		len:$('.wraper-list').length,
		init:function(){//初始化
			var _this = this;
			this.play()
			
			$('.wraper-list').on('swiperight',function(){
				 _this.index--;
				if(_this.index<0){
					_this.index=_this.len-1;
				}
				_this.shows(_this.index)
			})
			//左点击
			$('.wraper-prev').on('click',function(){
				_this.index--;
				if(_this.index<0){
					_this.index=_this.len-1;
				}
				_this.shows(_this.index)
			})
			//左滑动
			$('.wraper-list').on('swipeleft',function(){
				_this.index++;
				if(_this.index>=_this.len){
					_this.index=0;
				}
				_this.shows(_this.index)
			})
			//右点击
			$('.wraper-next').on('click',function(){
				_this.index++;
				if(_this.index>=_this.len){
					_this.index=0;
				}
				_this.shows(_this.index)
			})
			$('.wraper-dir').on('mouseover',function(){
				clearInterval(_this.time)
			})
			$('.wraper-dir').on('mouseout',function(){
				_this.play()
			})
		},
		shows:function(num){//轮播图显示
			$('.wraper-list').eq(num).fadeIn(1000).siblings('.wraper-list').fadeOut(1000);
			$('.wraper-nownum').text('0'+(num+1));
			$('.wraper-destxt').eq(num).delay(1000).fadeIn('slow').siblings('.wraper-destxt').fadeOut('slow');
		},
		play:function(){//轮播
			var _this = this;
			this.time = setInterval(function(){
				_this.index++;
				if(_this.index>=_this.len){
					_this.index=0;
				}
				_this.shows(_this.index);
			},7000)
		},
		
	}
	new autoPlay()
})


//滚动条加载样式
$(window).scroll(function(){
	var windowTop = $(window).scrollTop();
    $('.homebanner .wraper').css('transform', "translate(0px," + (windowTop) / 2 + "px)");
    //$('.homebanner').css({'top':$(window).scrollTop()/1.7+'px'})
	//$('.homebanner .wraper').css({'top':$(window).scrollTop()/1.7+'px'})
	
	var Oh = $('.homebanner').height();
	//console.log(Oh);
 	var Ah = $('.ind-about').height();
 	//console.log(Ah);
 	var Bh = $('.ind_news').height();
 	//console.log(Bh);
 	var Ch = $('.ind-senic').height();
 	//console.log(Ch);
 	var Dh = $('.ind-chwl').height();
 	//console.log(Dh);
 	var Eh = $('.ind-ser').height();
 	//console.log(Eh);
	
	if($(window).scrollTop()>=Ah*0.25){
		$('.ind-about .v-title').addClass('active');
		$('.ind-about .vpic').addClass('active');
		$('.ind-about .vtit').addClass('active');
		$('.ind-about .vinfo').addClass('active');
		$('.ind-about .bmorebox').addClass('active');
	}
	if($(window).scrollTop()<Ah*0.25){
		$('.ind-about .v-title').removeClass('active');
		$('.ind-about .vpic').removeClass('active');
		$('.ind-about .vtit').removeClass('active');
		$('.ind-about .vinfo').removeClass('active');
		$('.ind-about .bmorebox').removeClass('active');
	}
	if($(window).scrollTop()>Ah*0.75+Oh){
		$('.ind-about .v-title').removeClass('active');
		$('.ind-about .vpic').removeClass('active');
		$('.ind-about .vtit').removeClass('active');
		$('.ind-about .vinfo').removeClass('active');
		$('.ind-about .bmorebox').removeClass('active');
	}

	if($(window).scrollTop()>=Ah+Bh*0.25){
		$('.ind_news .cenbox .b-titbox').addClass('active');
		$('.tjnewsbox .leftbox').addClass('active');
		$('.tjnewsbox .rightbox').addClass('active');
		$('.ind_news .bmorebox .bmore').addClass('active');
	}
	if($(window).scrollTop()<Ah+Bh*0.25){
		$('.ind_news .cenbox .b-titbox').removeClass('active');
		$('.tjnewsbox .leftbox').removeClass('active');
		$('.tjnewsbox .rightbox').removeClass('active');
		$('.ind_news .bmorebox .bmore').removeClass('active');
	}
	if($(window).scrollTop()>Ah+Bh*0.75+Oh){
		$('.ind_news .cenbox .b-titbox').removeClass('active');
		$('.tjnewsbox .leftbox').removeClass('active');
		$('.tjnewsbox .rightbox').removeClass('active');
		$('.ind_news .bmorebox .bmore').removeClass('active');
	}
	
	if($(window).scrollTop()>=Ah+Bh+Ch*0.25){
		$('.ind-senic .cenbox .b-titbox').addClass('active');
		$('.ind-senic .cenbox .info').addClass('active');
		$('.ind-senic .cenbox .btnbox').addClass('active');
		$('.ind-senic .cenbox .jdboxs').addClass('active');
	}
	if($(window).scrollTop()<Ah+Bh+Ch*0.25){
		$('.ind-senic .cenbox .b-titbox').removeClass('active');
		$('.ind-senic .cenbox .info').removeClass('active');
		$('.ind-senic .cenbox .btnbox').removeClass('active');
		$('.ind-senic .cenbox .jdboxs').removeClass('active');
	}
	if($(window).scrollTop()>Ah+Bh+Ch*0.75+Oh){
		$('.ind-senic .cenbox .b-titbox').removeClass('active');
		$('.ind-senic .cenbox .info').removeClass('active');
		$('.ind-senic .cenbox .btnbox').removeClass('active');
		$('.ind-senic .cenbox .jdboxs').removeClass('active');
	}
	
	if($(window).scrollTop()>=Ah+Bh+Ch+Dh*0.25){
		$('.ind-chwl .cenbox .nrbg').addClass('active');
		$('.ind-chwl .cenbox .b-titbox').addClass('active');
		$('.ind-chwl .cenbox .info').addClass('active');
		$('.ind-chwl .cenbox .line').addClass('active');
		$('.ind-chwl .con-plays').addClass('active');
	}
	if($(window).scrollTop()<Ah+Bh+Ch+Dh*0.25){
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .con-plays').removeClass('active');
	}
	if($(window).scrollTop()>Ah+Bh+Ch+Dh+Oh+Oh*0.75){
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .cenbox .nrbg').removeClass('active');
		$('.ind-chwl .con-plays').removeClass('active');
	}
	
	if($(window).scrollTop()>= Ah + Bh + Ch + Dh + Eh*0.25){
		$('.ind-ser .cenbox .b-titbox').addClass('active');
		$('.ind-ser .cenbox .line').addClass('active');
		$('.ind-ser .cenbox .lytq').addClass('active');
		$('.ind-ser .cenbox .con-mation').addClass('active');
		$('.ind-ser .cenbox .otherbox').addClass('active');
	}
 	if($(window).scrollTop()< Ah + Bh + Ch + Dh + Eh*0.25){
		$('.ind-ser .cenbox .b-titbox').removeClass('active');
		$('.ind-ser .cenbox .line').removeClass('active');
		$('.ind-ser .cenbox .lytq').removeClass('active');
		$('.ind-ser .cenbox .con-mation').removeClass('active');
		$('.ind-ser .cenbox .otherbox').removeClass('active');
	}
	
})