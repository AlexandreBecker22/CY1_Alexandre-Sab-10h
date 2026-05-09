let IP01 = document.getElementById("IP01")
let lista_de_música = document.querySelector(".lista_de_música")
let musicas = new Array();


function Cadastrar_Jogo() {
    nova_musica = IP01.value;
    musicas.push(nova_musica);
    console.log(nova_musica);


    lista_de_música.innerHTML = "";
    for (let i = 0; i < musicas.length; i ++){
        lista_de_música.innerHTML += "" + musicas[i];
    }

}

function Remover_Elementos () {
    musicas = [];
    lista_de_música.innerHTML = "";
}