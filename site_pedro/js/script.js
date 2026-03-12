function abrirMenu() {
    var menu = document.getElementById("menu");
    var botao = document.querySelector(".menu-toggle");

    // só funciona no mobile
    if (window.innerWidth > 768) return;

    if (menu.style.display === "flex" || menu.style.display === "block") {
        menu.style.display = "none";
        botao.innerHTML = "☰";
    } else {
        menu.style.display = "flex"; // ou "block", mas "flex" mantém alinhamento vertical
        botao.innerHTML = "✖";
    }
}