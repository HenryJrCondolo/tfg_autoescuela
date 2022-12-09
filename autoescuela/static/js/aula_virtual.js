var random = 0;
var examenSelect = null;
const selecionarExamen = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/examen/");
    const data = await res.json();
    random = Math.floor(Math.random() * data.length);
    if (data) {
      examenSelect = data[random];
      return examenSelect;
    } else {
      return console.log(error);
    }
  } catch (error) {
    console.log(error);
  }
};

const obtenerPreguntas = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/pregunta/");
    const data = await res.json();
    if (data) {
      const preguntasJson = data;
      const examenSelect = await selecionarExamen();

      let preguntas = [];

      preguntasJson.forEach((pregunta) => {
        examenSelect.preguntas.forEach((e) => {
          if (e == pregunta.id_Pregunta) {
            preguntas.push(pregunta);
            const respuestas = [
              pregunta.respuesta_Falsa_1,
              pregunta.respuesta_Falsa_2,
              pregunta.respuesta_Correcta,
            ];
            respuestasCorrectas.push(pregunta.respuesta_Correcta);
            respuestasOrdenadas.push(
              respuestas.sort(() => Math.random() - 0.5)
            );
          }
        });
      });
      return preguntas;
    } else {
      return console.log(error);
    }
  } catch (error) {
    console.log(error);
  }
};
var respuestasOrdenadas = [];
var respuestasCorrectas = [];
var preguntasObtenidas = false;
var preguntas;
const mostrarPregunta = async (id) => {
  if (!preguntasObtenidas) {
    preguntas = await obtenerPreguntas();
    preguntasObtenidas = true;
  }
  const pregunta = preguntas[id];
  try {
    question_count.innerHTML = `Pregunta ${id + 1} de ${preguntas.length}`;
    if (pregunta.imagen_pregunta != null) {
      imgPregunta.setAttribute("src", pregunta.imagen_pregunta);
    } else {
      imgPregunta.setAttribute(
        "src",
        "/static/icono/iconoAutoescuela-removebg-preview.png"
      );
    }
    question.innerHTML = pregunta.pregunta;
    op1.innerHTML = respuestasOrdenadas[id][0];
    op2.innerHTML = respuestasOrdenadas[id][1];
    op3.innerHTML = respuestasOrdenadas[id][2];
  } catch (error) {
    console.log(error);
  }
};
var checkMarcado = [];
function verificarRadioButtom() {
  if (document.getElementById("flexRadioDefault1").checked) {
    document.getElementById("flexRadioDefault1").checked = false;
    checkMarcado[id] = [true, respuestasOrdenadas[id][0], "op1"];
    return true;
  } else if (document.getElementById("flexRadioDefault2").checked) {
    document.getElementById("flexRadioDefault2").checked = false;
    checkMarcado[id] = [true, respuestasOrdenadas[id][1], "op2"];
    return true;
  } else if (document.getElementById("flexRadioDefault3").checked) {
    document.getElementById("flexRadioDefault3").checked = false;
    checkMarcado[id] = [true, respuestasOrdenadas[id][2], "op3"];
    return true;
  } else {
    alert("Seleccione una respuesta");
    return false;
  }
}

var totalPreguntasCorrectas = 0;
function verificarRespuesta() {
  let respuestasFalladas = [];
  respuestasCorrectas.forEach((respuestaCorrecta, index) => {
    if (respuestaCorrecta == checkMarcado[index][1]) {
      totalPreguntasCorrectas++;
      console.log(respuestaCorrecta);
    } else {
      respuestasFalladas.push(checkMarcado[index][1]);
    }
  });
  return respuestasFalladas;
}

var id = 0;

const cargaInicial = async () => {
  await mostrarPregunta(id);
  await enumPreguntas();
};

window.addEventListener("load", async () => {
  await cargaInicial();
});

fin.addEventListener("click", () => {
  comprobarExamen();
});

const next = document.getElementsByClassName("next")[0];
next.addEventListener("click", () => {
  if (verificarRadioButtom()) {
    // Verificar la respuesta del usuario
    if (checkMarcado[id][0] == true && id < preguntas.length - 1) {
      ++id;
      mostrarPregunta(id);
    } else if (comprobarPreguntasContestadas()) {
      alert("No hay más preguntas");
      cambiarVisibilidadBotones();
    }
  } else {
    alert("Compruebe que todas las preguntas esten contestadas");
  }
});



const cambiarVisibilidadBotones = async () => {
  var end = document.getElementsByClassName("end");
  Array.from(end).forEach((x) => {
    if (x.style.display == "none") {
      x.style.display = "block";
      next.style.display = "none";
    }
  });
};

const comprobarPreguntasContestadas = () => {
  let contador = 0;
  checkMarcado.forEach((e) => {
    if (e[0] == true) {
      contador++;
    }
  });
  if (contador == preguntas.length) {
    return true;
  } else {
    return false;
  }
};

const obtenerUsuario = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/usuariologged/");
    const data = await res.json();
    if (data) {
      let usuario = data[0];
      let id_usuario = usuario.dni;
      return id_usuario
    } else {
      return alert("No hay usuario logeado");
    }
  } catch (error) {
    console.log(error);
  }
};

const enumPreguntas = async () => {
  try {
    let totalColumnas = preguntas.length / 2;

    for (let i = 1; i <= totalColumnas; i++) {
      row1.innerHTML += `<a class="col " id="colPreguntas"> <button class="btn btn-primary"  id="btn${i}">${i}</button> </a>`;
    }
    for (let e = totalColumnas + 1; e <= preguntas.length; e++) {
      row2.innerHTML += `<a class="col " id="colPreguntas"> <button class="btn btn-primary"  id="btn${e}">${e}</button> </a>`;
    }
    for (let a = 0; a < preguntas.length; a++) {
      let btn = document.getElementById(`btn${a + 1}`);
      btn.addEventListener("click", () => {
        id = a;
        mostrarPregunta(id);
        try {
          if (checkMarcado[id][2] == "op1") {
            document.getElementById("flexRadioDefault1").checked = true;
          } else if (checkMarcado[id][2] == "op2") {
            document.getElementById("flexRadioDefault2").checked = true;
          } else if (checkMarcado[id][2] == "op3") {
            document.getElementById("flexRadioDefault3").checked = true;
          }
        } catch (error) {
          document.getElementById("flexRadioDefault1").checked = false;
          document.getElementById("flexRadioDefault2").checked = false;
          document.getElementById("flexRadioDefault3").checked = false;
        }
      });
    }
  } catch (error) {
    console.log(error);
  }
};

const comprobarExamen = async () => {
  try {
    let aprobado = false;
    let usuario = await obtenerUsuario();
    let respuestasFalladas = verificarRespuesta();
    let respuestasUser = [];
    checkMarcado.forEach((check) => {
      respuestasUser.push(check[1]);
    });
    if (respuestasFalladas.length <= 3) {
      aprobado = true;
    }
    let examenRealizado = examenSelect;

    let examen = {
      usuario: usuario,
      respuestas_Usuario: respuestasUser,
      id_respuestas_falladas: respuestasFalladas,
      aprobado: aprobado,
      examen: examenRealizado,
    };

    console.log(examen);
  } catch (error) {
    console.log(error);
  }
}
