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

let index = 0;
const imagens = document.querySelectorAll('.carousel img');

function trocarImagem() {
    imagens[index].classList.remove('active');

    index++;
    if (index >= imagens.length) {
        index = 0;
    }

    imagens[index].classList.add('active');
}

// troca automática a cada 3 segundos
setInterval(trocarImagem, 3000);


chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  // ✅ If async, return true AND call sendResponse eventually
  someAsyncOperation().then(result => {
    sendResponse({ data: result });
  });
  return true; // keeps channel open
});