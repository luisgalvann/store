paypal
  .Buttons({
    createOrder: function (data, actions) {
      return actions.order.create({
        purchase_units: [{ amount: { value: "0.01" } }], // coste TOTAL
      });
    },

    onApprove: function (data, actions) {
      return actions.order.capture().then(function (orderData) {
        var transaction = orderData.purchase_units[0].payments.captures[0];
        alert("Transacción completada"); // acciones una vez está la TRANSACCIÓN COMPLETADA
      });
    },
  })
  .render("#paypal-button-container");

// acciones sugeridas en la documentación para transacción completada
// console.log("Capture result", orderData, JSON.stringify(orderData, null, 2));
// alert( "Transaction " + transaction.status + ": " + transaction.id);
// element.innerHTML = '<h3>Thank you for your payment!</h3>';
// Or go to another URL:  actions.redirect('thank_you.html');

// para redireccionar con javascript
// window.location.href = "{% url 'store' %}";
