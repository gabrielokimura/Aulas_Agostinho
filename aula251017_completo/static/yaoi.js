const texto = document.getElementById("conteudo")
let conteudo =""



fetch("/api")
.then(response=>response.json())
    .then(dados=>{
        // 1. Pega a string de consulta da URL atual (ex: "?page=3&limit=10")
const urlParams = new URLSearchParams(window.location.search);

// 2. Busca o valor de 'page' (retorna uma string ou null se não existir)
let pageString = urlParams.get('page');

// 3. Converte para inteiro e aplica o padrão '1'
let page;

if (pageString === null) {
    // Se 'page' não estiver na URL, usa o padrão 1
    page = 1;
} else {
    // Tenta converter para inteiro, e se a conversão falhar (NaN), usa o padrão 1
    const parsedPage = parseInt(pageString);
    if (isNaN(parsedPage) || parsedPage < 1) {
        page = 1; // Padrão se o valor for inválido ou negativo
    } else {
        page = parsedPage;
    }}
    const PERPAGE = 5
    let start = (page - 1) * PERPAGE
    let end = start + PERPAGE
    let total_page = Math.ceil( dados.length / PERPAGE)
    let produtos_da_pagina = dados.slice(start,end)
    conteudo+="<ul>"
    for (let produto of produtos_da_pagina){
        conteudo+=`<a href="/produto/${produto.id}"> <li> ${produto.nome} </li></a>`
    }
    conteudo+="</ul>"

    conteudo+="<nav>"

    conteudo += "<ul class='pagination'>"
    for (let page_num = 1; page_num<= total_page; page_num++){
        if(page === page_num){
            conteudo += `<li class ="page-item active>"`
            conteudo+="</li>"}
            else{
                conteudo+='<li class ="page-item>"'
                conteudo+="</li>"
            }
        conteudo+= `<a class="page-link" href="?page=${page_num}">${page_num}</a>`
        
    }
    conteudo+="</ul>"
    conteudo+="</nav>"


    texto.innerHTML =conteudo

 
    })