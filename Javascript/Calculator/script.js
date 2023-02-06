let RunningTotal = 0;
let Buffer = "0";
let PreviousOperator;

// Get the screen element from the DOM
const screen = document.querySelector('.screen')


// A function that gets called when a button is clicked
function ButtonClick(value){
    if(isNaN(value)){
        HandleSymbol(value);
    }else{
        HandleNumber(value);
    }
    screen.innerText = Buffer;
}

// A function that handles the input of numbers
function HandleNumber(value){
    if(Buffer === "0"){
        Buffer = value;
    }else{
        Buffer += value;
    }
}

// A function that handles the input of symbols
function HandleSymbol(value){
    switch (value) {
        case 'C':
            Buffer = "0";
            RunningTotal = 0;
            PreviousOperator = null;
            break;
        case '←':
            if (Buffer.length === 1) {
                Buffer = "0";
            } else {
                Buffer = Buffer.substring(0, Buffer.length - 1);
            }
            break;
        case '=':
            if (PreviousOperator === null) {
                return;
            }
            FlushOperation(parseInt(Buffer));
            PreviousOperator = null;
            Buffer = "" + RunningTotal;
            RunningTotal = 0;
            break;
        case '+':
        case '-':
        case '×':
        case '÷':
            HandleMath(value);
            break;
    }
}

// A function to handle the input of symbols
function HandleMath(value){
    const intBuffer = parseInt(Buffer);
    if (RunningTotal === 0) {
        RunningTotal = intBuffer;
    } else {
        FlushOperation(intBuffer);
    }
    PreviousOperator = value;
    Buffer = "0";
}

// A function to perform the calculation based on the previous operator
function FlushOperation(intBuffer){
    if (PreviousOperator === '+') {
        RunningTotal += intBuffer;
    } else if (PreviousOperator === '-') {
        RunningTotal -= intBuffer;
    } else if (PreviousOperator === '×') {
        RunningTotal *= intBuffer;
    } else {
        RunningTotal /= intBuffer;
    }
}

// A function to initialize the calculator
function init(){
    document.querySelector('.calc-buttons').
    addEventListener('click', function(event){
        ButtonClick(event.target.innerText);
    })
}

init(); 
