console.log("js loaded");
var js;
var cont = 0;
var tfeel = 0;
var trole = 0;
const FeelRole = (value) => {
  console.log(typeof value);
  console.log(value);
  value = JSON.parse(value);
  console.log(typeof value);
  tfeel += value.feel;
  trole += value.role;
};
const Fetchestractor = (json) => {
  jso = json;
};
const fe = async (url = "http://localhost:8000/question") => {
  try {
    const quest = await fetch(url);
    if (quest.ok) {
      js = await quest.json();

      writeQuestion();
      buildBoton();
    }
  } catch (error) {
    console.log(error);
  }
};
fe();
function writeQuestion() {
  var question = document.getElementById("question");
  question.innerText = js[cont].question;
  let answers = "";
  for (let answer of js[cont].answers) {
    answers += `
          <input type="radio" value='{"feel":${answer.feel}, "role":${answer.role}}' name="ans">${answer.answer}<br>
          `;
  }
  var ans = document.getElementById("answer");
  ans.innerHTML = answers;
}

const buildBoton = () => {
  const boto = document.getElementById("next");
  boto.addEventListener("click", function () {
    try {
      const check = document.querySelector('input[name="ans"]:checked').value;
      console.log(check);
      FeelRole(check);
      cont++;
      console.log(tfeel, trole);
      if (cont == js.length - 1) {
        boto.setAttribute("value", "SIMMIT");
      }
      cont < js.length ? writeQuestion() : result();
    } catch (err) {
      console.log(err);
      alert("Seleccione una Respuesta");
    }
  });
};

const result = () => {
  document.getElementById("question").remove();
  document.getElementById("next").remove();
  var ans = document.getElementById("answer");
  ans.innerHTML = `<h1>Result<h1/><br>
  <p><b>Feel: <b/> ${tfeel}<br>
  <b>Role: <b/>${trole}
  <p/>
  `;
};

const info = () => {};
