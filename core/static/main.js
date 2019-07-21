(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){let c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);let a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}let p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){let n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(let u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

},{}]},{},[1]);
const markLiked = document.querySelectorAll('.mark-liked')
let count = 0;
let display = document.querySelectorAll(".count-liked");

console.log(count)
for (let button of markLiked) {
    console.log(count)
    button.addEventListener('click', function(event){
        event.preventDefault();
        console.log(count);
        count++;
        console.log(count);
        display.innerText = count;
        console.log(count);
    });
}