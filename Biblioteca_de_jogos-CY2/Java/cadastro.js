let usu = document.querySelector(".usuario01");
let sen = document.querySelector(".senha01");
let dat = document.querySelector(".data01");
let mail = document.querySelector(".email01");
let usus = [];
<<<<<<< HEAD
let botaoCadastrar = document.querySelector("#botaoCadastrar");
let mensagem = document.querySelector("#mensagem");
=======
let mensagem = document.querySelector("#mensagem");
let botaoCadastrar = document.querySelector("#botaoCadastrar");

>>>>>>> 081ecbeae54b56af81644450b008de457d98f0a5
const USU = (
    nomeExterno,
    senhaExterna,
    dataExterna,
    emailExterno
) => ({ nome: nomeExterno, senha: senhaExterna, data: dataExterna, email: emailExterno });

// function CadastrarUsuario(){
//     let usuario = USU(usu.value, sen.value, dat.value, email.value);
//     usus.push(usuario);

//     localStorage.setItem("usuarios_registrados", JSON.stringify(usus));

//     window.location.href = "home.html"
// };
const formatoCampoSenha = {
    {
<<<<<<< HEAD
    mensagem: "A senha deve conter pelo menos uma letra maiuscula",
        regra = /[A-Z]/
};
{
    mensagem: "A senha deve conter pelo menos uma letra minuscula",
        regra = /[a-z]/
};
{
    mensagem: "A senha deve conter pelo menos um numero",
        regra = /[0-9]/
};
{
    mensagem: "A senha NÃO deve conter pelo menos um caractere especial",
        regra = /[ @#$%&* ]/
    // /[-_%$#@!.,;/=¨'"\|~^[]{}()*&ªº₢§¬£¢°/?<>:]/
};
}
function ValidarSenha(senhaUsuario) {

    let validacao = true;
    for (let i = 0; i < formatoCampoSenha.length; i++) {
        if (ValidarRegraDeSenha(senhaUsuario, formatoCampoSenha[i].regra) == false) {
            mensagem.innerHTML += formatoCampoSenha[i].mensagem;
            validacao = false;
        }
    }
    return validacao;
    //     let senhaVerificada = sen.value;
    //     let letrasMa = /[A-Z]/;
    //     let letrasMi = /[a-z]/;
    //     let numeros = /[0-9]/;
    //     //     let caracterEsp = /[-_%$#@!.,;/=¨'"\|~^[]{}()*&ªº₢§¬£¢°/?]/;
    //     let caractereEsp = /[ @#$%&* ]/;

    //     if (letrasMa.test(senhaVerificada)
    //         || letrasMi.test(senhaVerificada)
    //         || numeros.test(senhaVerificada)
    //         || caractereEsp.test(senhaVerificada) == false) {
    //         console.log("OK!")
    //     }
    //     else {
    //         console.log("Não OK")
    //     }
}
function ValidarRegraDeSenha(senhaUsuario, regra) {

    if (regra.test(senhaUsuario)) {
        return true;
    }
    else {
        return false;
    }

}


botaoCadastrar.addEventListener("click", function (event) {

    event.preventDefault();

    let usuario = Usuario(nome.value, senha.value, data.value, email.value);

    if (ValidarSenha(senha.value) == true) {
        usuarios.push(usuario);
        localStorage.setItem("usuarios_registrados", JSON.stringify(usuarios));
        window.location.href = "paginaDeSucesso.html";
=======
        mensagem: "A senha deve conter pelo menos uma letra maiuscula",
        regra: /[A-Z]/
    }
    {
        mensagem: "A senha deve conter pelo menos uma letra minuscula",
        regra: /[a-z]/
    }
    {
        mensagem: "A senha deve conter pelo menos um numero",
        regra: /[0-9]/
    }
    {
        mensagem: "A senha NAO deve conter pelo menos um caractere especial",
        regra: /[@#$%&*]/
    }
}
function ValidarSenha(senhaUsuario) {
    // let senhaVerificada = sen.value;
    // let letrasMa = /[A-Z]/;
    // let letrasMi = /[a-z]/;
    // let numeros = /[0-9]/;
    // //     let caracterEsp = /[-_%$#@!.,;/=¨'"\|~^[]{}()*&ªº₢§¬£¢°/?]/;
    // let caractereEsp = /[ @#$%&* ]/;

    // if (letrasMa.test(senhaVerificada)
    //     || letrasMi.test(senhaVerificada)
    //     || numeros.test(senhaVerificada)
    //     || caractereEsp.test(senhaVerificada) == false) {
    //     console.log("OK!")
    // }
    // else {
    //     console.log("Não OK")
    // }
    let validacao = true;
    for (let i=0; i < formatoCampoSenha.lenght; i++) {
        if (ValidarRegraDeSenha(senhaUsuario, formatoCampoSenha[i].regra))==false{
            mensage.innerHTML += formatoCampoSenha[i].mensagem;
            validacao = false;
        }
    }
    return validacao;
    }
    function ValidarRegraDeSenha(senhaUsuario, regra) {
        if(regra.test(senhaUsuario)){
            return true;
        }
        else {
            return false;
        }
>>>>>>> 081ecbeae54b56af81644450b008de457d98f0a5
    }
    else {
        alert("Preencha todos os campos corretamente!")
    }

})
function AcessarPaginaInicial(){
  window.location.href = "home.html"
}

mail.addEventListener("click", function (event) {
    event.preventDefault();

    let usuario = USU(usu.value, sen.value, dat.value, email.value);
    if (ValidarSenha(senha.value)){
    usus.push(usuario);
    localStorage.setItem("usuarios_registrados", JSON.stringify(usus));
    window.location.href = "home.html"
<<<<<<< HEAD
});

for (let i = 0; i < usuarios.length; i++) {
    const div = document.createElement("div");

    div.innerHTML = `
  <p> ${usuarios[i].usu} </p>
  <p> ${usuarios[i].dat} </p>
  <p> ${usuarios[i].email} </p>
  <p> ${usuarios[i].sen} </p>

  <button onclick="EditarUsuario(${i})"> Editar </button>
  `;
    USUS.appendChild(div);
};

function EditarUsuario(idUsuario) {
    const div = document.createElement("div");
    div.innerHTML = `
  <form>
    <div class="div_formulário">

      <label for= "nomeEditar"> Nome: </label>
      <input id="nomeEditar" type="text" name="nome" value="${usuarios.usu}">
      <br>

      <label for= "dataEditar"> Data de Nascimento: </label>
      <input id="dataEditar" type="date" name="data" value="${usuarios.dat}">
      <br>

      <label for= "emailEditar"> E-mail: </label>
      <input id="emailEditar" type="email" name="email" value="${usuarios.email}">
      <br>

      <label for= "senhaEditar"> Senha: </label>
      <input id="senhaEditar" type="password" name="senha" value="${usuarios.sen}">
      <br>

      <button id="botaoSalvarEditar" type="button">
        Salvar Alterações
      </button>
    </div>
  </form>`;

    const botaoSalvarEditar = document.getElementById("botaoSalvarEditar");

    botaoSalvarEditar.addEventListener("click", function () {
        const nome = document.getElementById("nomeEditar");
        const data = document.getElementById("dataEditar");
        const email = document.getElementById("emailEditar");
        const senha = document.getElementById("senhaEditar");

        usuarios[idUsuario] = {
            nome: nome.value,
            data: data.value,
            email: email.value,
            senha: senha.value
        };

    });
=======
    }
    else {
        alert("Preencha todos os campos corretamente!")
    }
});
function AcessarPaginaInicial() {
    window.location.href = "home.html"
>>>>>>> 081ecbeae54b56af81644450b008de457d98f0a5
}