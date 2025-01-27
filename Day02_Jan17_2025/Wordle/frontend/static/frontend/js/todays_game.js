const maxRows = 5; // Total number of guesses
const maxLength = 5; // Length of the word
let currentRow = 0; // Tracks the current guess row
let guesses = Array(maxRows).fill(""); // Array to store guesses for each row

// Add a letter to the current guess
function addLetter(letter) {
  if (currentRow < maxRows && guesses[currentRow].length < maxLength) {
    guesses[currentRow] += letter;
    updateGuessRow();
  }
}

// Handle special keys (backspace or submit)
function handleSpecialKey(key) {
  if (key === "⬅") {
    guesses[currentRow] = guesses[currentRow].slice(0, -1); // Remove the last letter
    updateGuessRow();
  } else if (key === "✅") {
    submitGuess(); // Submit the current guess
  } else {
    addLetter(key); // Add letter if it's not a special key
  }
}

// Function to disable keyboard interaction
function disableKeyboard() {
  const keys = document.querySelectorAll(".key"); // Assuming your keyboard keys have a class 'key'
  keys.forEach((key) => {
    key.style.pointerEvents = "none"; // Disable mouse clicks
    key.style.opacity = "0.5"; // Optional: Dim the keys visually
  });
}

// Update the current row with letters
function updateGuessRow() {
  const guessRow = document.querySelector(
    `.word-tiles-${currentRow + 1}`
  );
  const tiles = guessRow.children;

  for (let i = 0; i < maxLength; i++) {
    const letter = guesses[currentRow][i] || ""; // Get the letter or empty string
    tiles[i].textContent = letter.toUpperCase();
  }
}

// Submit the guess to the backend for validation
async function submitGuess() {
  const currentGuess = guesses[currentRow].toUpperCase();

  if (currentGuess.length !== maxLength) {
    alert("Incomplete guess! Fill all the tiles before submitting.");
    return;
  }

  try {
    // Send the guess to the backend
    const response = await fetch("{% url 'validate_guess' %}", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": "{{ csrf_token }}",
      },
      body: JSON.stringify({ guess: currentGuess }),
    });

    const data = await response.json();

    if (data.status === "error") {
      alert(data.message);
      return;
    }

    const result = data.result; // Array: ["correct", "present", "absent", ...]
    const guessRow = document.querySelector(
      `.word-tiles-${currentRow + 1}`
    );
    const tiles = guessRow.children;

    // Update tile classes based on the backend result
    for (let i = 0; i < result.length; i++) {
      tiles[i].classList.remove("absent", "present", "correct");
      tiles[i].classList.add(result[i]);
    }

    if (data.status === "success") {
      alert(data.message);
      disableKeyboard();
      return;
    }

    if (data.status === "game_over") {
      alert(data.message);
      disableKeyboard();
      return;
    }

    // Move to the next row
    currentRow++;
  } catch (error) {
    console.error("Error submitting guess:", error);
    alert("An error occurred. Please try again.");
  }
}

// Initialize rows when the page loads
function initializeRows() {
  for (let row = 1; row <= maxRows; row++) {
    const rowDiv = document.querySelector(`.word-tiles-${row}`);
    for (let col = 0; col < maxLength; col++) {
      const tile = document.createElement("h1");
      tile.classList.add("guess-tile");
      rowDiv.appendChild(tile);
    }
  }
}

document.addEventListener("DOMContentLoaded", initializeRows);