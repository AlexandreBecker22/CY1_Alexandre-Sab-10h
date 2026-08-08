let IP01 = document.getElementById("IP01");

// document → busca no HTML
// .getElementById(" ID ") → elemento com o ID x
// .querySelector("# ID") → elemento com o ID x
// .querySelector(". CLASS") → elemento com o CLASS x 

let IP02 = document.querySelector(".IP02")
let IP03 = document.querySelector(".IP03")
let link = document.querySelector("#link")
let IMG01 = document.querySelector("#IMG01")
let AUD01 = document.querySelector(".audio001")
let lista_de_música = document.querySelector(".lista_de_música");
let musicas = [];
let audio01 = document.querySelector("audio001")


function Pegar_img() {
    const urlIMG = URL.createObjectURL(IMG01.files[0]);
    return urlIMG;
}
function Pegar_audio() {
    const urlAUD01 = URL.createObjectURL(AUD01.files[0]);
    return urlAUD01;
}

function Cadastrar_Jogo() {
    const urlImagem = Pegar_img();
    const urlaudio = Pegar_audio();
    const nova_musica = musica(IP01.value, IP02.value, IP03.value, link.value,  urlImagem, urlaudio );
    musicas.push(nova_musica);


    // lista_de_música.innerHTML = "";
    // for (let i = 0; i < musicas.length; i ++){
    //     lista_de_música.innerHTML += "" + musicas[i];
    // }

    for (let i = 0; i < musicas.length; i++) {
        
        const div = document.createElement("div")
        div.classList.add("div01");
        div.innerHTML = `
        <img class="div01-C" id="imgIMG01"src= "${musicas[i].IMG01}">
        <h1 class="h3h401" class="div01-C" id= "H3-01"> ${musicas[i].IP01}  </h1>
        <h4 class="h3h401" class="div01-C id= "H4-01"> ${musicas[i].IP02}  </h4>
        <h4 class="h3h401" class="div01-C id= "H4-02"> ${musicas[i].IP03}  </h4>
        <a class="h3h401" class="div01-C id="alink01" href="${musicas[i].link}"> Link da música </a>
        <audio src= "${musicas[i].AUD01}" controls>
        <br>
        <button class="B02" onclick="Remover_Elementos(${i})">Remover Música</button>
        `
        lista_de_música.appendChild(div);

    }

}

function Remover_Elementos(posicao_Array) {

    musicas.splice(posicao_Array, 1);
    lista_de_música.innerHTML="";

    

  for (let i = 0; i < musicas.length; i++) {
        const div = document.createElement("div");
        div.classList.add("div");
        div.innerHTML = `
        <img class="div01-C" id="imgIMG01"src= "${musicas[i].IMG01}">
        <h1 class="h3h401" class="div01-C" id= "H3-01"> ${musicas[i].IP01}  </h1>
        <h4 class="h3h401" class="div01-C id= "H4-01"> ${musicas[i].IP02}  </h4>
        <h4 class="h3h401" class="div01-C id= "H4-02"> ${musicas[i].IP03}  </h4>
        <a class="h3h401" class="div01-C id="alink01" href="${musicas[i].link}"> Link da música </a>
        <br>
        
        <button class="B02" onclick="Remover_Elementos(${i})">Remover Música</button>
        `
        lista_de_música.appendChild(div);

    }

}

const musica = (IP01, IP02, IP03, link, IMG01, AUD01) => ({
    IP01,
    IP02,
    IP03, 
    link, 
    IMG01,
    AUD01

})

