<?php
$para = "urbanvision777@gmail.com";
$assunto = "Mensagem do Formulário de Contato";
$nome = $_POST['nome'];
$email = $_POST['email'];
$mensagem = $_POST['mensagem'];

$corpo = "Nome: $nome\nEmail: $email\nMensagem:\n$mensagem";
$cabecalho = "From: $email";

if(mail($para, $assunto, $corpo, $cabecalho)){
    echo "Mensagem enviada com sucesso!";
} else {
    echo "Erro ao enviar mensagem.";
}
?>