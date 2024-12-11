let matrix = [];
let rows = 0;
let columns = 0;

function initializeMatrix() {
  rows = parseInt(document.getElementById("rows").value);
  columns = parseInt(document.getElementById("columns").value);

  const matrixInput = document.getElementById("matrix-input");
  matrixInput.innerHTML = "";

  matrix = Array.from({ length: rows }, () => Array(columns).fill(0));

  for (let i = 0; i < rows; i++) {
    const rowDiv = document.createElement("div");
    rowDiv.style.display = "flex";
    for (let j = 0; j < columns; j++) {
      const input = document.createElement("input");
      input.type = "number";
      input.style.width = "50px";
      input.onchange = (e) => (matrix[i][j] = parseInt(e.target.value));
      rowDiv.appendChild(input);
    }
    matrixInput.appendChild(rowDiv);
  }
}

function printMatrix(matrix, elementId) {
  const output = matrix.map((row) => `[ ${row.join(" ")} ]`).join("\n");
  document.getElementById(elementId).textContent = output;
}

function performRowReduction() {
  printMatrix(matrix, "original-matrix");

  for (let i = 0; i < rows; i++) {
    if (matrix[i][i] === 0) {
      for (let j = i + 1; j < rows; j++) {
        if (matrix[j][i] !== 0) {
          [matrix[i], matrix[j]] = [matrix[j], matrix[i]];
          break;
        }
      }
    }

    const pivot = matrix[i][i];
    for (let k = 0; k < columns; k++) {
      matrix[i][k] /= pivot;
    }

    for (let j = 0; j < rows; j++) {
      if (j !== i) {
        const factor = matrix[j][i];
        for (let k = 0; k < columns; k++) {
          matrix[j][k] -= factor * matrix[i][k];
        }
      }
    }
  }

  printMatrix(matrix, "reduced-matrix");
}