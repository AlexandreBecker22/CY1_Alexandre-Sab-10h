let setaD = document.querySelector(".setaD")
let setaE = document.querySelector(".setaE")
let img01 = document.querySelector(".imgcarrossel01")
let ulc01 = document.querySelector(".ulcarrossel01")
const indice = 0
function anterior(){
  if(indice===0){indice=0}  
  else{indice = indice-1}

  atualizar_carrossel();
}
function posterior(){
    if(indice===ulc01.lenght){indice=0}
    else{indice=indice+1}
}
function atualizar_carrossel(){
    const deslocamento = indice;
    translateX(-[$indice]);
}