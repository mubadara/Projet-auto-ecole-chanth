document.addEventListener("DOMContentLoaded", function () {
    const tarifContainer = document.getElementById("tarif-container");
  
  if (!Array.isArray(tarifs) || tarifs.length === 0) {
    tarifList.innerHTML = "<li>No tarifs available.</li>";
    return;
  }

    tarifContainer.innerHTML = ""; // Clear existing content

    tarifs.forEach((tarif) => {
      const nameElement = document.createElement("h3");
      nameElement.textContent = tarif.name;

      const descriptionElement = document.createElement("p");
      descriptionElement.textContent = tarif.description;

      const priceElement = document.createElement("p");
      priceElement.textContent = `Price: $${tarif.price}`;

      tarifElement.appendChild(nameElement);
      tarifElement.appendChild(descriptionElement);
      tarifElement.appendChild(priceElement);

      tarifContainer.appendChild(tarifElement);
    });
  });