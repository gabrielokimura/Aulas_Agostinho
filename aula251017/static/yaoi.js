const conteudo = document.getElementById("conteudo")



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
    let total_page = math.ceil( data.length() / PERPAGE)
    let produtos_da_pagina = dados.slice(start,end)
    conteudo+="<ul>"
    for (let produto of dados){
        conteudo+=` <li> ${produto.nome} </li>`
    }
    conteudo+="</ul> class='pagination'>"
    conteudo += "<ul>"
    for (let page_num = 1; page_num<= total_page+1 ){

        conteudo += `<li class ='page-item' ${if(page === page_num){
            active 
        }}>`

    }
    


    })