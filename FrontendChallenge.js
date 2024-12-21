// Get the element with the ID "root" where the button will be inserted
const rootApp = document.getElementById("root");

// Set the inner HTML of the root element to contain a button with the ID "toggleButton" and the text "ON"
rootApp.innerHTML = '<button id="toggleButton">ON</button>';

// Get the button element by its ID "toggleButton"
const toggleButton = document.getElementById("toggleButton");

// Add an event listener to the button, which listens for a "click" event
toggleButton.addEventListener("click", () => {
  // Change the button's text content: if it's "ON", change to "OFF", otherwise change to "ON"
  toggleButton.textContent = toggleButton.textContent === "ON" ? "OFF" : "ON";
});
