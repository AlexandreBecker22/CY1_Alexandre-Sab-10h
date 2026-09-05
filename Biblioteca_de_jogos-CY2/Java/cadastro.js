let usu = document.querySelector(".usuario01");
let sen = document.querySelector(".senha01");
let dat = document.querySelector(".data01");
let usus = [];

const USU = (
    nomeExterno,
    senhaExterna,
    dataExterna,
) => ({nome: nomeExterno, senha: senhaExterna, data: dataExterna});

function CadastrarUsuario(){
    let usuario = USU(usu.value, sen.value, dat.value);
    usus.push(usuario);

    localStorage.setItem("usuarios_registrados", JSON.stringify(usus));

    window.location.href = "home.html"
};