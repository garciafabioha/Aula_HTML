const products = [
  {
    id: 1,
    title: "Smartphone Samsung Galaxy S21",
    price: 799.99,
    discount: 15,
    image: "https://i.zst.com.br/thumbs/12/c/2f/-940175893.jpg",
  },
  {
    id: 2,
    title: "Notebook Dell Inspiron 15",
    price: 1199.99,
    discount: 10,
    image:
      "https://http2.mlstatic.com/D_NQ_NP_956166-MLA79426872420_092024-O.webp",
  },
  {
    id: 3,
    title: "Fone de Ouvido Bluetooth JBL",
    price: 199.99,
    discount: 20,
    image: "https://m.media-amazon.com/images/I/51olNZRjn+L.jpg",
  },
  {
    id: 4,
    title: "Smart TV LG 55 polegadas",
    price: 1499.99,
    discount: 25,
    image:
      "https://fujiokadistribuidor.vteximg.com.br/arquivos/ids/168929-292-292/43900-TV-LED-UHD-55-LG-55UM7470-THQAI--1-.png",
  },
  {
    id: 5,
    title: "Console PlayStation 5",
    price: 499.99,
    discount: 5,
    image: "https://m.media-amazon.com/images/I/51+qnZm7V7L.jpg",
  },
  {
    id: 6,
    title: "Câmera Digital Canon EOS Rebel T7",
    price: 599.99,
    discount: 30,
    image:
      "https://www.detonashop.com.br/media/mf_webp/png/media/catalog/product/cache/041e82462066eef1ae3402cf9c4986f8/t/7/t7_50mm.webp",
  },
  {
    id: 7,
    title: "Smartwatch Apple Watch Series 6",
    price: 399.99,
    discount: 12,
    image:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTquL0fiDP7lgzrcarir4TQVbfSpxmGSt6AqQ&s",
  },
  {
    id: 8,
    title: "Tablet Samsung Galaxy Tab S7",
    price: 699.99,
    discount: 10,
    image:
      "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_lgz1Fks4IXd0XhZMknOzGcY6bgvPs7yMew&s",
  },
  {
    id: 9,
    title: "hone 17 pro max 256gb",
    price: 13949.1,
    discount: 10,
    image:
      "https://images7.kabum.com.br/produtos/fotos/925357/iphone-17-pro-max-apple-256gb-48mp-tela-6-9-super-retina-xdr-azul-intenso_1757698084_gg.jpg",
  },
];

const productsGrid = document.getElementById("productsGrid");
const searchInput = document.getElementById("searchInput");
const searchBtn = document.getElementById("searchBtn");

function formatPrice(price) {
  return price.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

function createProductCard(product) {
  const discountedPrice = product.price * (1 - product.discount / 100);
  return `
    <div class="product-card">
      <img src="${product.image}" alt="${product.title}" class="product-image">
      <h3 class="product-title">${product.title}</h3>
      <div class="product-price">Preço Original: ${formatPrice(product.price)}</div>
      <div class="product-discount">Desconto: ${product.discount}%</div>
      <div class="product-discount">Preço com Desconto: ${formatPrice(discountedPrice)}</div>
    </div>
  `;
}

function renderProduct(products) {
  const grid = document.getElementById("productsGrid");
  grid.innerHTML = products.map(createProductCard).join("");
}

//Pesquisar Produtos
function searchProducts() {
  const searchTerm = (
    document.getElementById("searchInput").value || ""
  ).toLowerCase();

  const searchInput = document
    .getElementById("searchInput")
    .value.toLowerCase();
  const filteredProducts = products.filter((product) =>
    product.title.toLowerCase().includes(searchInput),
  );

  renderProduct(filteredProducts);
}

document.addEventListener("DOMContentLoaded", () => {
  renderProduct(products);

  document
    .getElementById("searchBtn")
    .addEventListener("click", searchProducts);
});
