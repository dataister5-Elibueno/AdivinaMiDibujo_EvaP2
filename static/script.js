const canvas = document.getElementById("drawCanvas");
const ctx = canvas.getContext("2d");
let dibujando = false;


let intentos = 0;
let aciertos = 0;
let errores = 0;

canvas.addEventListener("mousedown", () => dibujando = true);
canvas.addEventListener("mouseup", () => dibujando = false);
canvas.addEventListener("mousemove", dibujar);

function dibujar(e) {
  if (!dibujando) return;
  ctx.fillStyle = "white";
  ctx.beginPath();
  ctx.arc(e.offsetX, e.offsetY, 5, 0, Math.PI * 2);
  ctx.fill();
}

// cambiar entre pantallas
function mostrarPantalla(id) {
  document.querySelectorAll('.pantalla').forEach(p => p.style.display = 'none');
  document.getElementById(id).style.display = 'block';
}

document.getElementById("clearBtn").addEventListener("click", () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  document.getElementById("resultado").innerHTML = "";
});

// enviar predicción
document.getElementById("predictBtn").addEventListener("click", async () => {
  const imageData = canvas.toDataURL("image/png");

  const response = await fetch("/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ image: imageData })
  });

  const predictions = await response.json();
  let output = "";
  predictions.forEach(p => {
    output += `Clase ${p.label} → ${(p.confidence * 100).toFixed(2)}%<br>`;
  });

  const mejorPrediccion = predictions[0].label;
  
  const esCorrecto =  predictions[0].confidence > 0.5;

  intentos++;
  if (esCorrecto) aciertos++;
  else errores++;

  document.getElementById("stats").innerHTML =
    `Intentos: ${intentos} | Aciertos: ${aciertos} | Errores: ${errores}`;

  mostrarPantalla("predicciones");
  document.getElementById("resultado").innerHTML = output;
});

document.getElementById("finalBtn").addEventListener("click", () => {
  const porcentaje = intentos ? (aciertos / intentos * 100).toFixed(2) : 0;

const resumenHTML = `
    <strong>Intentos:</strong> ${intentos}<br>
    <strong>Aciertos:</strong> ${aciertos}<br>
    <strong>Errores:</strong> ${errores}<br>
    <strong>Precisión:</strong> ${porcentaje}%<br>
  `;
document.getElementById("resumenDatos").innerHTML = resumenHTML;
  mostrarPantalla("final");
});
document.getElementById("volverInicioBtn").addEventListener("click", () => {
  mostrarPantalla("inicio");
});