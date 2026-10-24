
function CadastrarUsuario() {

    const[nome, setNome] = useState("");
    const[senha, setSenha] = useState("");
    const[email, setEmail] = useState("");
    const[data, setData] = useState("");

    function cadastrarUsuario(event) {
        event.prevenDefault();

        const usuario = {
            nome: nome,
            senha: senha,
            email: email,
            data: data
        }
    }


    return (
        <form>

            <label for="usuario01"><b>Nome de usuário:</b></label>
            <input type="text" placeholder="Preencha com seu usuário" className="senhaeusuario01 usuario01"
                required />
            <br></br>
            <label for="senha01"><b>Senha:</b></label>
            <input type="password" placeholder="Preencha com sua senha" className="senhaeusuario01 senha01"
                required />
            <ol>
                <li>A senha deve ter pelo menos uma letra maiúscula;</li>
                <li>A senha deve ter no minimo uma letra minúscula;</li>
                <li>A senha também deve conter um ou mais números;</li>
                <li>Ela não deve conter nem um caractere especial.</li>
            </ol>
            <br></br>
            <label for="email01"><b>E-mail:</b></label>
            <input type="email" placeholder="Preencha com seu e-mail" className="senhaeusuario01 email01"
                required />
            <br></br>
            <label for="data01"><b>Data de nascimento:</b></label><b>(opcional)</b>
            <input type="date" placeholder="Insira sua data de nascimento" 
                className="senhaeusuario01 data01" />
            <br></br>
        </form>
    );
}