function showConversionSteps() {
    const input = document.getElementById('decimalForTutorial');
    const stepsContainer = document.getElementById('conversionSteps');
    const errorContainer = document.getElementById('errorTutorial');
    stepsContainer.innerHTML = ''; 
    errorContainer.textContent = ''; 

    let number = parseInt(input.value);
    if (input.value === '' || isNaN(number)) {
        return;
    }

    if (number < 0 || number > 256) {
        errorContainer.textContent = 'Please enter a number between 0 and 256.';
        return;
    }

    let steps = [];
    while (number > 0) {
        const remainder = number % 2;
        steps.unshift(`${number} ÷ 2 = ${Math.floor(number / 2)} remainder ${remainder}`);
        number = Math.floor(number / 2);
    }

    steps.forEach((step) => {
        const stepElement = document.createElement('div');
        stepElement.className = 'step';
        stepElement.innerHTML = `<span class="arrow"></span>${step}`;
        stepsContainer.appendChild(stepElement);
    });
}

function convertToBinary() {
    const decimalInput = document.getElementById('decimalInput');
    const binaryOutput = document.getElementById('binaryOutput');
    const errorContainer = document.getElementById('errorInteractive');
    errorContainer.textContent = ''; 

    let number = parseInt(decimalInput.value);
    if (decimalInput.value === '' || isNaN(number)) {
        binaryOutput.textContent = '0000 0000';
        return;
    }

    if (number < 0 || number > 2048) {
        errorContainer.textContent = 'Please enter a number between 0 and 2048.';
        return;
    }

    let binary = number.toString(2).padStart(12, '0'); // Ensure 12 bits for clear visualization
    binaryOutput.textContent = formatBinary(binary); // Format and display binary
}

function formatBinary(binaryString) {
    return binaryString.slice(0, 4) + ' ' + binaryString.slice(4, 8) + ' ' + binaryString.slice(8, 12); // Split into 3 groups of 4 bits
}

function checkAnswer() {
    const binary = document.getElementById('randomBinary').textContent.replace(/ /g, '');
    const userInput = document.getElementById('userInput');
    const decimal = parseInt(binary, 2);
    const result = document.getElementById('result');
    const streak = document.getElementById('streak');
    let currentStreak = parseInt(streak.textContent.split(': ')[1]);

    if (parseInt(userInput.value) === decimal) {
        result.textContent = 'Correct!';
        result.className = 'result';
        currentStreak++;
    } else {
        result.textContent = `Incorrect, the correct number is ${decimal}`;
        result.className = 'result incorrect';
        currentStreak = 0;
    }

    streak.textContent = `Streak: ${currentStreak}`;
    generateRandomBinary(); // Generate a new binary number each time an answer is checked
    userInput.value = ''; // Clear the input field after checking the answer
}

function generateRandomBinary() {
    const randomBinary = Math.floor(Math.random() * 256).toString(2).padStart(8, '0');
    document.getElementById('randomBinary').textContent = formatBinary(randomBinary); // Format into 2 groups of 4 bits
    document.getElementById('userInput').value = ''; // Clear the user input field when generating a new number
}

window.onload = generateRandomBinary;