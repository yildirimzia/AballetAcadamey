import '../scss/base.scss';
import $ from "jquery";
import anime from 'animejs/lib/anime.es.js';

const sayHello = ()=> {
  setInterval(() => {
    console.log('nasilsin ziya')
  }, 8000);
}

sayHello();