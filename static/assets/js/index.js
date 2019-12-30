import $ from 'jquery';
import './slider';
import '../scss/base.scss';



$(document).on('click','.js-hamburger-menu',function() {
  $('.js-mobile-menu').toggleClass('menu-open')
})