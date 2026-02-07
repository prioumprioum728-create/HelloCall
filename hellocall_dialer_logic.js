let currentNumber = '';

function press(digit) {
    currentNumber += digit;
    document.getElementById('number').innerText = currentNumber;
}

function backspace() {
    currentNumber = currentNumber.slice(0, -1);
    document.getElementById('number').innerText = currentNumber;
}

function callNumber() {
    if (currentNumber.length > 0) {
        alert('Calling: ' + currentNumber);
        currentNumber = '';
        document.getElementById('number').innerText = '';
    } else {
        alert('Please enter a number first.');
    }
}
