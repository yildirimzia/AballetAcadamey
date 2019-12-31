import $ from 'jquery';
import './slider';
import '../scss/base.scss';



const backToTop = () => {
  let lastScrollTop = 0;
  const backToTop =  $('.js-back-to-top');
  $(window).scroll(()=> {
    let scTop = $(window).scrollTop();

    if (scTop < lastScrollTop && scTop > $('.header').outerHeight()){
      backToTop.addClass('active');
    } else {
      backToTop.removeClass('active');
    }
    lastScrollTop = scTop;
  });

  $(document).on('click', '.js-back-to-top',() => {
    $('html, body').animate({ scrollTop: 0 }, 400);
  });
}
backToTop();




$(document).on('click','.js-hamburger-menu',function() {
  $('.js-mobile-menu').toggleClass('menu-open')
});