document.addEventListener('DOMContentLoaded', () => {
  const monedaSelect = document.getElementById('moneda');
  const productos = document.querySelectorAll('.producto-card');
  const tipoCambioApiUrl = '/api/tipo-cambio/';  // debe coincidir con la URL en urls.py

  monedaSelect.addEventListener('change', async () => {
    const moneda = monedaSelect.value;

    if (moneda === 'USD') {
      try {
        const response = await fetch(tipoCambioApiUrl);
        if (!response.ok) throw new Error('Error en la respuesta');
        const data = await response.json();
        const tipoCambio = data.tipo_cambio;

        productos.forEach(card => {
          const precioCLP = parseFloat(card.getAttribute('data-precio'));
          const precioUSD = (precioCLP * tipoCambio).toFixed(2);
          card.querySelector('.precio').textContent = `$ ${precioUSD} USD`;
        });
      } catch (error) {
        console.error('Error al obtener el tipo de cambio:', error);
      }
    } else {
      // Volver a pesos chilenos
      productos.forEach(card => {
        const precioCLP = parseFloat(card.getAttribute('data-precio'));
        card.querySelector('.precio').textContent = `$ ${precioCLP} CLP`;
      });
    }
  });
});
