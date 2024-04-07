// 地图显示
$('.san-maps-btn').on('click',function(){
  $('#maps').attr('src',$(this).find('a').attr('href'));
  $('.mask').fadeIn('fast');
  $('.san-maps').delay(500).fadeIn('fast');
  $('#dowebok').fullpage.setAllowScrolling(false);
})
$('.right-maps-btn').on('click',function(){
  var url = $(this).attr('url');
  $('#maps').attr('src',url);
  $('.mask').fadeIn('fast');
  $('.san-maps').delay(500).fadeIn('fast');
})
$('.mask').on('click',function(){
	$('#maps').attr('src','');
  $('.mask').delay(500).fadeOut('fast');
  $('.san-maps').fadeOut('fast');
  $('#dowebok').fullpage.setAllowScrolling(true);
})
$('.san-close').on('click',function(){
	$('#maps').attr('src','');
  $('.mask').delay(500).fadeOut('fast');
  $('.san-maps').fadeOut('fast');
  $('#dowebok').fullpage.setAllowScrolling(true);
})
// 附近选择
$('.ilist-btns>a').on('click',function(){
  var index = $(this).index();
  $(this).addClass('active').siblings('a').removeClass('active');
  $('.ilist-icontent').fadeIn('fast');
  $('.back').addClass('active');
  $('.ilist-lines').fadeOut('fast');
  $('.ilist-inews').eq(index).delay(500).fadeIn('fast').siblings('.ilist-inews').fadeOut('fast')
})
// 查询路线
  $('.ilist-fund').on('click',function(){
    $('.lines-news').eq(0).addClass('active');
    $('.ilist-box').fadeOut(100);
    $('.iback').addClass('active');
    $('.ilist-lines-btns').fadeIn();
    $('.ilist-lines-btns>a').on('click',function(){
      var index = $(this).index();
      $(this).addClass('active').siblings('a').removeClass('active');
      $('.lines-news').eq(index).addClass('active').siblings('.lines-news').removeClass('active')
    })
  })

// 关闭
$('.san-iclose').on('click',function(){
  $('.san-info').toggleClass('active');
  $('.san-iframes').toggleClass('active');
  $('#dowebok').fullpage.setAllowScrolling(true);
})
$('.back').on('click',function(){
  $('.no-shows').fadeOut('fast');
  $('.ilist-lines').delay(500).fadeIn('fast');
  $('.ilist-inews').fadeOut('fast');
  $(this).removeClass('active');
	$('#dowebok').fullpage.setAllowScrolling(true);
})
$('.iback').on('click',function(){
  $('.ilist-lines-btns').fadeOut();
  $('.ilist-box').fadeIn();
  $('.lines-news').removeClass('active')
})

$('body').delegate('#close','click',function(){//弹层关闭
  $('.mask').delay(200).fadeOut('fast');
  $('.san-maps').fadeOut('fast');
  console.log($('.mask'))
})
