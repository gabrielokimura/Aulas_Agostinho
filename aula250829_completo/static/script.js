const botao = document.getElementById("carregar")
const divConteudo = document.getElementById("conteudo")



botao.addEventListener("click", ()=> {
    fetch("/api/aluno")
    .then(response=>response.json())
    .then(dados=>{
        let tabelahtml="<table border='1'>"
        tabelahtml+="<tr><th>Aluno</th><th>Nota</th></tr>"
        for (const aluno of dados){
            tabelahtml+="<tr><td>${aluno.nome}</td><td>${aluno.nota}</td></tr>"
        }
        tabelahtml+="</table>"

        divConteudo.innerHTML=tabelahtml


    })})
  