const submitButton = document.getElementById('submitButton');
const num1Input = document.getElementById('num1');
const num2Input = document.getElementById('num2');
const resultDiv = document.getElementById('result');

submitButton.addEventListener('click', function() {
  const num1 = parseFloat(num1Input.value);
  const num2 = parseFloat(num2Input.value);

  if (isNaN(num1) || isNaN(num2)) {
    resultDiv.textContent = 'Please enter valid numbers.';
  } else {
    const sum = num1 + num2;
    resultDiv.textContent = 'The sum is: ' + sum;
  }
});
