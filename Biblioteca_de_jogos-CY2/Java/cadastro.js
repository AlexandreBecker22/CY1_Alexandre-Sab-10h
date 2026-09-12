let usu = document.querySelector(".usuario01");
let sen = document.querySelector(".senha01");
let dat = document.querySelector(".data01");
let mail = document.querySelector(".email01");
let usus = [];

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
        mensagem: "A senha NÃO deve conter pelo menos um caractere especial",
        regra: /[-_%$#@!.,;/=¨'"\|~^[]{}()*&ªº₢§¬£¢°/?<>:]/
    }
}
function ValidarSenha() {
    let senhaVerificada = sen.value;
    let letrasMa = /[A-Z]/;
    let letrasMi = /[a-z]/;
    let numeros = /[0-9]/;
    //     let caracterEsp = /[-_%$#@!.,;/=¨'"\|~^[]{}()*&ªº₢§¬£¢°/?]/;
    let caractereEsp = /[ @#$%&* ]/;

    if (letrasMa.test(senhaVerificada)
        || letrasMi.test(senhaVerificada)
        || numeros.test(senhaVerificada)
        || caractereEsp.test(senhaVerificada) == false) {
        console.log("OK!")
    }
    else {
        console.log("Não OK")
    }
    }

mail.addEventListener("click", function (event) {
    event.preventDefault();

    let usuario = USU(usu.value, sen.value, dat.value, email.value);
    usus.push(usuario);

    localStorage.setItem("usuarios_registrados", JSON.stringify(usus));

    window.location.href = "home.html"
});