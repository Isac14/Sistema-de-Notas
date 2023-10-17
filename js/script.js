document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Interrompe o envio padrão do formulário

    const matricula = document.getElementById("register").value;

    fetch("/matricula", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        matricula: matricula,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          alert("Erro ao buscar notas: " + data.error);
        } else {
          // Atualizar página de notas
          window.location.href = "./grades.html";

          // Aqui, você pode armazenar as notas em local storage ou em algum outro lugar
          // para que possam ser acessadas quando a página grades.html for carregada
          localStorage.setItem("notas", JSON.stringify(data));
        }
      })
      .catch((error) => {
        alert("Erro ao buscar notas: " + error.message);
      });
  });
});

// Se estivermos na página de notas, vamos atualizar o conteúdo da tabela
if (window.location.pathname.endsWith("grades.html")) {
  const notas = JSON.parse(localStorage.getItem("notas") || "[]");

  // Atualizar a tabela com as notas
  const table = document.querySelector("table");
  const nome = document.querySelector(".title");

  if (notas.length > 0) {
    nome.textContent = notas[0].nome; // Nome do aluno (assumindo que o nome também é retornado pelo backend)

    notas.forEach((nota, index) => {
      table.rows[index + 1].cells[0].textContent = nota.materia;
      table.rows[index + 1].cells[1].textContent = nota.nota;
    });
  }
}
