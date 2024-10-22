document.addEventListener("DOMContentLoaded", function () {
  // Get the script tag that holds the JSON data
  const aboutDataElement = document.getElementById("about-data");

  if (aboutDataElement) {
    try {
      // Parse the JSON data
      const aboutData = JSON.parse(aboutDataElement.textContent);

      // Main About Section
      const mainAboutDiv = document.getElementById("main-about");
      if (aboutData.about) {
        const mainAboutContent = document.createElement("p");
        mainAboutContent.textContent = aboutData.about;
        mainAboutDiv.appendChild(mainAboutContent);
      }

      // About Julien Section
      const aboutJulienDiv = document.getElementById("about-julien");
      if (aboutData.about_Julien) {
        const julienContent = document.createElement("p");
        julienContent.textContent = aboutData.about_Julien;
        aboutJulienDiv.appendChild(julienContent);
      }

      // About Chanth Section
      const aboutChanthDiv = document.getElementById("about-chanth");
      if (aboutData.about_Chanth) {
        const chanthContent = document.createElement("p");
        chanthContent.textContent = aboutData.about_Chanth;
        aboutChanthDiv.appendChild(chanthContent);
      }
    } catch (e) {
      console.error("Error parsing JSON data:", e);
    }
  } else {
    console.error("Error: about-data element not found");
  }
});
