$(document).ready(() => {
    $('#id_cep').mask('99999-999');

    let formClear = () => {
        // Limpa valores do formulário de cep.
        $("#id_rua").val("");
        $("#id_bairro").val("");
        $("#id_cidade").val("");
        $("#id_uf").val("");
    }
    $("#id_cep").blur(() => {
        //Nova variável "cep" somente com dígitos.
        let zipCode = $('#id_cep').val().replace(/\D/g, '');
        //Verifica se campo cep possui valor informado.
        if (zipCode != "") {
            //Expressão regular para validar o CEP.
            let validCep = /^[0-9]{8}$/;
            //Valida o formato do CEP.
            if (validCep.test(zipCode)) {
                //Preenche os campos com "..." enquanto consulta webservice.
                $("#id_rua").val("...");
                $("#id_bairro").val("...");
                $("#id_cidade").val("...");
                $("#id_estado").val("...");
                $("#id_uf").val("...");
                //Consulta o webservice viacep.com.br/
                $.getJSON(`https://viacep.com.br/ws/${zipCode}/json/?callback=?`, data => {
                    if (!("erro" in data)) {
                        //Atualiza os campos com os valores da consulta.
                        $("#id_rua").val(data.logradouro);
                        $("#id_bairro").val(data.bairro);
                        $("#id_cidade").val(data.localidade);
                        $("#id_uf").val(data.uf);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        formClear();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                formClear();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            formClear();
        }
    });
});
i=1
$('.btn-sm').click(function(){
    i++
    $campo = $('#imagem'+i)
    $campo.removeAttr('hidden')
});
