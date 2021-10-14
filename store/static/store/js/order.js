function getToken() {
  if (document.cookie && document.cookie !== "") {
    const name = "csrftoken";
    const cookies = document.cookie.split(";");
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.substring(0, name.length + 1) === `${name}=`) {
        return decodeURIComponent(cookie.substring(name.length + 1));
      }
    }
  }
}

const amount = document.getElementById("amount").value;
const form = document.getElementById("shipping-form");
const container = document.getElementById("paypal-container");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  if (amount > 0) {
    form.style.visibility = "hidden";
    container.removeAttribute("hidden");

    fetch("/order/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getToken(),
      },
      body: JSON.stringify({
        name: form.name.value,
        address: form.address.value,
        city: form.city.value,
        country: form.country.value,
        zipcode: form.zipcode.value,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        document.cookie = "cart={};domain=;path=/";
      });
  } else {
    const child = form.removeChild(form.lastElementChild);
    const div = document.createElement("div");
    div.classList.add("alert", "alert-danger");
    div.textContent = "Your cart is empty !";

    if (!child.className.includes("alert")) {
      form.appendChild(child);
    }
    form.appendChild(div);
  }
});
