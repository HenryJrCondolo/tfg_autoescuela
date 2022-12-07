const listarExamen = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/examen/");
    const data = await res.json();
    if (data) {
      const examenes = data;
      let examenesHTML = ``;
      examenes.forEach((examen) => {
        examenesHTML += `<option value="${examen.id_Examen}">${examen.nombre_Examen}</option>`;
      });
      slcexamen.innerHTML = examenesHTML;
      return examenes;
    } else {
      return console.log(error);
    }
  } catch (error) {
    return console.log(error);
  }
};

const selecionarExamen = async (id_Examen) => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/examen/");
    const data = await res.json();

    if (data) {
      const examenes = data;
      const examenSelect = examenes.find(
        (examen) => examen.id_Examen == id_Examen
      );
      return examenSelect;
    } else {
      return console.log(error);
    }
  } catch (error) {
    console.log(error);
  }
};

const listarPregunta = async (examen) => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/pregunta/");
    const data = await res.json();
    if (data) {
      const preguntasJson = data;
      let preguntasHTML = ``;
      examen.then((examenSelect) => {
        console.log(examenSelect);
        preguntasJson.forEach((pregunta) => {
          examenSelect.preguntas.forEach((e) => {
            if (e == pregunta.id_Pregunta) {
              preguntasHTML += `<option value="${pregunta.id_Pregunta}">${pregunta.pregunta}</option>`;
            }
          });
        });
        slcpregunta.innerHTML = preguntasHTML;
      });
    } else {
      console.log(error);
    }
  } catch (error) {
    console.log(error);
  }
};

const cargaInicial = async () => {
  await listarExamen();
  slcexamen.addEventListener("change", (event) => {
    let examen = selecionarExamen(event.target.value);
    listarPregunta(examen);
  });
};

window.addEventListener("load", async () => {
  await cargaInicial();
});
