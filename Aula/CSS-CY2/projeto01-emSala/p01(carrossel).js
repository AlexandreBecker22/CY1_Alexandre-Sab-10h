let setaD = document.querySelector(".setaD")
let setaE = document.querySelector(".setaE")
let img01 = document.querySelector(".imgcarrossel01")
let ulc01 = document.querySelector(".ulcarrossel01")
let indice = 0
// let trilho_de_imagens =
// document.querySelector(".ulcarrossel01");

let lenght = ulc01.children.length;


function anterior() {
    if (indice === 0) { indice = 0 }
    else { indice = indice - 1 }

    atualizar_carrossel();
}
function posterior() {
    if (indice === lenght - 1) { indice = 0 }
    else { indice = indice + 1 }

    atualizar_carrossel();
}
function atualizar_carrossel() {
    const deslocamento = indice * 105;
    ulc01.style.transform = `translateX(-${deslocamento}%)`;
}


function Menuu() {
    const div = document.createElement("div");
    div.classList.add("Menu");
    div.innerHTML = `
        < ul class="ul01" >
                <li><a href="./../projeto01-emSala/p01.html">Home</a></li>
                <li><a href="./../cadastro/cadastro.html">Cadastro de músicas</a></li>
                <li><a href="">Fale conosco(inoperante)</a></li>
            </ul >
        `
        
}