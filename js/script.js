document.addEventListener("DOMContentLoaded", function () {
  if (window.location.pathname.endsWith("grades.html")) {
    let data = JSON.parse(localStorage.getItem("gradesData"));
    if (data) {
      displayGrades(data);
    }
  } else {
    document.querySelector("form").addEventListener("submit", function (event) {
      event.preventDefault();
      let matricula = document.getElementById("register").value;
      fetch("http://127.0.0.1:5000/matricula", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: matricula,
      })
        .then((response) => response.json())
        .then((data) => {
          localStorage.setItem("gradesData", JSON.stringify(data));
          window.location.href = "./grades.html";
        });
    });
  }
});

function displayGrades(data) {
  let rows = document.querySelectorAll("table tr");
  for (let i = 1; i <= data.length; i++) {
    rows[i].children[0].textContent = data[i - 1].materia;
    rows[i].children[1].textContent = data[i - 1].nota;
  }
  let sum = 0;
  console.log(data);
  for (let grade of data) {
    sum += parseFloat(grade.nota);
  }
  let avg = sum / data.length;
  document.querySelector(".footer").textContent =
    "Média Final: " + avg.toFixed(2);
  let statusElement = document.querySelector("h1");
  statusElement.textContent = avg >= 7 ? "Aprovado(a)" : "Reprovado(a)";
}
