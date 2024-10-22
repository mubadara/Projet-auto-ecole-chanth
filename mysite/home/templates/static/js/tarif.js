document.addEventListener('DOMContentLoaded', function () {
  // Retrieve the tariff data from the script tags
  const tariffData = JSON.parse(document.getElementById('tariff-data').textContent);

  // Tariff Section: Populate the tariffs section dynamically
  const tariffsList = document.getElementById('tariffs-list');
  tariffData.forEach(tariff => {
    const tariffDiv = document.createElement('div');
    tariffDiv.classList.add('tariff-item');
        
    // Create elements for name, price, and description
    const nameEl = document.createElement('h3');
    nameEl.textContent = tariff.name;

    const priceEl = document.createElement('p');
    priceEl.textContent = `Prix: €${tariff.price}`;

    const descEl = document.createElement('p');
    descEl.textContent = tariff.description;

    // Append to the tariff div
    tariffDiv.appendChild(nameEl);
    tariffDiv.appendChild(priceEl);
    tariffDiv.appendChild(descEl);

    // Append the tariff div to the list
    tariffsList.appendChild(tariffDiv);
  })
});
