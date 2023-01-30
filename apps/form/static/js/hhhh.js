var jso = {};
const Fetchestractor = (json) => {
  jso = json;
};
const fe = async (url = "http://localhost:8000/question") => {
  try {
    const quest = await fetch(url);
    if (quest.status == 200) {
      let js = await quest.json();
      Fetchestractor(js);
    }
  } catch (error) {
    console.log(error);
  }
};
fe();
var cont = 0;

function writeQuestion() {
  var question = document.getElementById("question");
  question.innerText = jso[cont].question;
  console.log(jso[cont].question);
  let answers = "";
  for (let answer of jso[cont].answers) {
    answers += `
          <input type="radio" value="{'feel':${answer.feel},'role':${answer.role}}" name="ans">${answer.answer}<br>
          `;
  }
  var ans = document.getElementById("answer");
  ans.innerHTML = answers;
}
var start = document.getElementById("answer");
start.innerHTML = ` `;
let boto = document.getElementById("next");
boto.addEventListener("click", function () {
  console.log(jso);
  //   try {
  //     let check = document.querySelector('input[name="ans"]:checked').value;
  //     console.log(check);
  //     cont++;
  //     writeQuestion();
  //   } catch {
  //     alert("none selected");
  //   }
});
//writeQuestion();

const info = () => {};
