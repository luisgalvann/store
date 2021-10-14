function getCookie(name) {
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (const cookie of cookies) {
      const cookiePair = cookie.split("=");
      if (name == cookiePair[0].trim()) {
        return decodeURIComponent(cookiePair[1]);
      }
    }
  }
  return null
}

function updateCookie(productId, action) {
  if (action == "add") {
    if (!cart[productId]) {
      cart[productId] = { quantity: 1 };
    }
    else {
      cart[productId]["quantity"]++;
    }
  } else if (action == "remove") {
    cart[productId]["quantity"]--;
    if (cart[productId]["quantity"] <= 0) {
      delete cart[productId];
    }
  }
  document.cookie = `cart=${JSON.stringify(cart)};domain=;path=/`;
  location.reload(); // recargamos la página
}

let cart = JSON.parse(getCookie("cart"));
const updateBtns = document.getElementsByClassName("update-btn");

if (!cart) {
  cart = {};
  document.cookie = `cart=${JSON.stringify(cart)};domain=;path=/`;
}

for (const btn of updateBtns) {
  btn.addEventListener("click", () => {
    const productId = btn.dataset.product;
    const action = btn.dataset.action;
    updateCookie(productId, action);
  });
}
