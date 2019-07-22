import { EAGAIN } from "constants";

(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

},{}]},{},[1]);


function answerQuestion(jquery???) {

    for (let form of document.querySelectorAll('.answer-question-form')) {
        form.addEventListener('submit', function (event) {
          event.preventDefault()

        const questionPK = jquery???.data(questionPK)

        fetch(requests.answerQuestion(questionPK))
            .then(res => res.json())
            .then(function(data) {
        console.log('data', data)
        })
    } 
}

function postQuestionAnswer(questionPK) {
    const csrftoken = Cookies.get('csrftoken')
    return new Request(??????? {
        credentials: 'include',
        method: 'POST',
        headers: {
            'X-CSFRToken': csrftoken
        },
        body: JSON.stringify()
    })

}


// const answerQuestion = document.querySelectorAll(".answer-question"); 

// document.addEventListener('submit', function (event) {
//     fetch( 'some url ?????' )
//         .then (function (response) {
//         return response.json ()
//     })
//         .then (function (data))  
//         console.log (data)
//         populateAnswerForm (data)
//         // submitAnswerButton.querySelectorAll('input')
//         // return (answer.body)
// })

 












