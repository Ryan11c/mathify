function calculateDerivative() {
    const functionInput = document.getElementById("function").value.trim();
    const variableInput = document.getElementById("variable").value.trim();
    const resultElement = document.getElementById("result");
    const stepsElement = document.getElementById("steps");
  
    if (!functionInput || !variableInput) {
      resultElement.textContent =
        "Please provide both a function and a variable.";
      stepsElement.textContent = "";
      return;
    }
  
    try {
      // Parse and differentiate the function
      const node = math.parse(functionInput);
      const derivative = math.derivative(node, variableInput);
  
      resultElement.textContent = derivative.toString();
  
      // Generate steps for differentiation
      const steps = generateSteps(node, variableInput);
      stepsElement.textContent = steps.join("\n");
    } catch (error) {
      resultElement.textContent = `An error occurred: ${error.message}`;
      stepsElement.textContent = "";
    }
  }
  
  function generateSteps(node, variable) {
    const steps = [];
    const expression = node.toString();
  
    steps.push(`Original expression: ${expression}\n`);
  
    if (expression.includes("+")) {
      steps.push("Apply the Sum Rule - Differentiate each term separately.\n");
    }
    if (expression.includes("*")) {
      steps.push("Apply the Product Rule - d(uv) = u'v + uv'.\n");
    }
    if (expression.includes("/")) {
      steps.push("Apply the Quotient Rule - d(u/v) = (u'v - uv') / v^2.\n");
    }
    if (expression.includes("sin") || expression.includes("cos")) {
      steps.push("Apply the Trigonometric Derivatives.\n");
    }
    if (expression.match(/\^/)) {
      steps.push("Apply the Power Rule - d(x^n) = n*x^(n-1).\n");
    }
  
    // Simulate intermediate steps (example for power rule)
    node.traverse((child) => {
      if (child.type === "OperatorNode" && child.op === "^") {
        const base = child.args[0].toString();
        const exponent = child.args[1].toString();
        steps.push(
          `Applying Power Rule on ${base}^${exponent}: ${exponent} * ${base}^(${exponent} - 1)\n`
        );
      }
    });
  
    steps.push("Final step: Combine all differentiated parts.");
  
    return steps;
  }