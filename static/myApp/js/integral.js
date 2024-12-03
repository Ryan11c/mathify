document.getElementById("integralType").addEventListener("change", function () {
    const integralType = this.value;
    const definiteInputs = document.getElementById("definiteInputs");
    if (integralType === "definite") {
        definiteInputs.style.display = "block";
    } else {
        definiteInputs.style.display = "none";
    }
});

document.getElementById("calculate").addEventListener("click", function () {
    const functionInput = document.getElementById("functionInput").value;
    const integralType = document.getElementById("integralType").value;

    if (!functionInput) {
        alert("Please enter a valid function.");
        return;
    }

    let result;
    if (integralType === "indefinite") {
        result = computeIndefiniteIntegral(functionInput);
    } else {
        const lowerLimit = parseFloat(document.getElementById("lowerLimit").value);
        const upperLimit = parseFloat(document.getElementById("upperLimit").value);

        if (isNaN(lowerLimit) || isNaN(upperLimit)) {
            alert("Please specify valid integration limits.");
            return;
        }

        result = computeDefiniteIntegral(functionInput, lowerLimit, upperLimit);
    }

    displayResult(result);
});

function computeIndefiniteIntegral(func) {
    try {
        //Use Algebrite for symbolic integration
        if (typeof Algebrite === "undefined") {
            throw new Error("Algebrite library is not loaded. Indefinite integration requires symbolic processing.");
        }
        const integral = Algebrite.integral(func).toString();
        return `Indefinite Integral: ${integral}`;
    } catch (error) {
        return `Error computing indefinite integral: ${error.message}`;
    }
}

function computeDefiniteIntegral(func, a, b) {
    try {
        const compiledFunction = math.compile(func);
        const integrate = (x) => compiledFunction.evaluate({ x });

        //Numerical integration
        const resolution = 10000;
        let sum = 0;
        const dx = (b - a) / resolution;

        for (let i = 0; i < resolution; i++) {
            const x = a + i * dx;
            sum += integrate(x) * dx;
        }

        return `Definite Integral from ${a} to ${b}: ${sum.toFixed(6)}`;
    } catch (error) {
        return `Error computing definite integral: ${error.message}`;
    }
}

function displayResult(result) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = `<h2>Result:</h2><p>${result}</p>`;
}