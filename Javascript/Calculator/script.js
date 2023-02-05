let RunningTotal = 0;
let Buffer = "0";
let PreviousOperator;

const screen = document.querySelector('.screen')

function ButtonClick(value){
    if(isNaN(value)){
        HandleSymbol(value);
    }else{
        HandleNumber(value);
    }
    screen.innerText = Buffer;
}

function HandleNumber(value){
    if(Buffer === "0"){
        Buffer = value;
    }else{
        Buffer += value;
    }
}

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

function init(){
    document.querySelector('.calc-buttons').
    addEventListener('click', function(event){
        ButtonClick(event.target.innerText);
    })
}

init(); 