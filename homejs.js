console.log('linked sucessfully')
// js for timer 

let daysE1 = document.getElementById('days')
let hoursE1 = document.getElementById('hours')
let munitsE1 = document.getElementById('munits')
let secondsE1 = document.getElementById('seconds')

function countdownTimer() {
    const countdownDate = new Date('02/14/2024').getTime()

    // convert to millioseconds
    const seconds = 1000
    const munite = seconds * 60
    const hour = munite * 60
    const day = hour * 24
    // calculate every second
    const interval = setInterval(()=>{

        // get current date
        const now = new Date().getTime()
        const distance = countdownDate - now
    
        daysE1.innerText = formatenumber(Math.floor(distance/day))
        hoursE1.innerText = formatenumber(Math.floor((distance % day)/hour))
        munitsE1.innerText = formatenumber(Math.floor((distance % hour)/munite))
        secondsE1.innerText = formatenumber(Math.floor((distance % munite)/seconds))
        // when time get over
        if (distance <0){
            document.getElementById('countdown').style.display ="none"
            clearInterval(interval)
            document.getElementById('countdownend').innerText="offer is ended wait few days for new offers "
        }

    },1000);
}
// number formatter function 
function formatenumber(number) {
    if (number< 10){
        return '0'+ number
    }
    return number
}

// run timer
countdownTimer()



// 
//              founders button 
// 


function toggelHide(){
    let foundersbtn = document.getElementById('foundersbtn')
    let information = document.getElementById('information')
    
    if (information.style.display != 'none'){
        information.style.display = 'none';
        foundersbtn.innerHTML ="Show information"
    }
    else{
        information.style.display = 'block'
        foundersbtn.innerHTML ="Hide information"
    }
    
}








// function exitFromLogin(){
//     let loginpopupwindow = document.getElementById('loginwindow')
//     let cross = document.getElementById('cross')
//     if (loginpopupwindow.style.display !='none'){
//         loginpopupwindow.style.display ='none';
//         // loginpopupwindow.style.position ='Hidden';

//     }
//     else{
//         loginpopupwindow.style.display = 'block'
//     }
// }


//                      login popup window
// 

const loginpopupwindow = document.getElementById('loginwindow')
const close = document.getElementById('cross')

window.addEventListener('load',function(){
    showPopup();
})
function showPopup(){
    const timeLimit = 5
    let i = 0
    const timer = setInterval(function(){
        i++;
        if(i==timeLimit){
            clearInterval(timer)
            loginpopupwindow.style.display = 'block'
        }
        console.log(i)
    },1000)
    
}


close.addEventListener('click',function(){
    loginpopupwindow.style.display ='none'
})