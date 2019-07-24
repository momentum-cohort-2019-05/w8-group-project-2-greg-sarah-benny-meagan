const buttonsSpansCont = document.querySelectorAll('.button-span-container')
const markLikedButtons = document.querySelectorAll('.mark-liked')
// let display = document.querySelectorAll(".count-liked");
// let currentNumberLiked = display.dataset['num'];
// const markAnswerCorrect = document.querySelectorAll('#markAnswerCorrect')
// let answerPk = display.dataset['pk'];
// const replyForm = document.querySelector('#reply-form')
// const csrftoken = Cookies.get('csrftoken')

// replyForm.addEventListener('submit', function(event){
//     event.preventDefault();
//         fetch('question/<int:pk>/')
//             credentials: 'include',
//             method: 'POST',
//             headers: {
//                 'X-CSRFToken': csrftoken
//             },
//             body: JSON.stringify({ 'body': answerInput.value })
//             })
//         .then(response => response.json())
//         .then(function (data) {
//         console.log('data', data);
//         })
// });


// console.log(count)
// for (let button of markLikedButtons) {
//     button.addEventListener('click', function(){
//         let newTotal = parseInt(display.innerText) + 1;
//         display.innerHTML = newTotal;
//     });
// }

for (let e of buttonsSpansCont) {
    const button = e.querySelector('.mark-liked');
    const span = e.querySelector('.count-liked');

    button.addEventListener('click', function(){
        let newTotal = parseInt(span.innerText) + 1;
        span.innerHTML = newTotal;
    });
}

// for (let button of markAnswerCorrect) {
//     button.addEventListener('click', function(event){
//         console.log(event)
//     fetch('markanswercorrect/'( answerPk )) 
//         .then(response => response.json())
//         .then(function (data) {
//             console.log('data', data);

//         })

//     });
// }

for (let button of markLikedButtons) {
    button.addEventListener('click', function(){
        fetch('/liked/' + button.dataset.pk + '/')
            .then(response => response.json())
            .then(function (data) {
                console.log('data', data);
            })
    });
}