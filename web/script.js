
function calculate(operation) {
    var num1 = parseFloat(document.getElementById('num1').value);
    var num2 = parseFloat(document.getElementById('num2').value);
    
    var requestBody = {
        num1: num1,
        num2: num2,
        operation: operation
    };
    
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestBody),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = "Ergebnis: " + data.result;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}
