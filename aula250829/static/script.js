const botao = document.getElementById("carregar")
const divConteudo = document.getElementById("conteudo")



botao.addEventListener("click", ()=> {
    fetch("/api/aluno")
    .then(response=>response.json())
    .then(dados=>{
        let tabelahtml="<table border='1'>"
    })})
  