// Wordle Game Core Logic
class WordleGame {
  constructor() {
    // Game Configuration
    this.maxRows = 5;
    this.maxLength = 5;
    
    // Game State
    this.currentRow = 0;
    this.guesses = Array(this.maxRows).fill("");
    this.keyboardEnabled = true;
    this.gameOver = false;

    // DOM Elements
    this.messageBox = null;
    this.initializeDOM();
  }

  // Initialize Game DOM Elements
  initializeDOM() {
    this.createMessageBox();
    this.initializeRows();
    this.setupEventListeners();
  }

  // Create Message Display Box
  createMessageBox() {
    this.messageBox = document.createElement("div");
    this.messageBox.id = "message-box";
    this.messageBox.className = "message";
    document.body.insertBefore(this.messageBox, document.body.firstChild);
  }

  // Display Game Messages
  displayMessage(message, type = "info") {
    if (!this.messageBox) this.createMessageBox();
    this.messageBox.textContent = message;
    this.messageBox.className = `message ${type}`;
    
    // Auto-clear message after 3 seconds
    setTimeout(() => {
      this.messageBox.textContent = "";
      this.messageBox.className = "message";
    }, 3000);
  }

  // Initialize Game Rows
  initializeRows() {
    for (let row = 1; row <= this.maxRows; row++) {
      const rowDiv = document.querySelector(`.word-tiles-${row}`);
      if (!rowDiv) {
        console.error(`Row .word-tiles-${row} not found`);
        continue;
      }
      rowDiv.innerHTML = '';
      for (let col = 0; col < this.maxLength; col++) {
        const tile = document.createElement("h1");
        tile.classList.add("guess-tile");
        rowDiv.appendChild(tile);
      }
    }
  }

  updateGuessRow() {
    // Select the current row based on `currentRow`
    const guessRow = document.querySelector(`.word-tiles-${this.currentRow + 1}`);
    
    // Check if the row exists
    if (!guessRow) {
      console.error(`Row .word-tiles-${this.currentRow + 1} not found`);
      return;
    }
  
    // Get the tiles in the current row
    const tiles = guessRow.children;
  
    // Loop through the tiles and update their content
    for (let i = 0; i < this.maxLength; i++) {
      const letter = this.guesses[this.currentRow][i] || ""; // Use empty string for missing letters
      tiles[i].textContent = letter.toUpperCase(); // Set the letter (uppercase)
    }
  }
  // Event Listeners
  setupEventListeners() {
    document.addEventListener('keydown', (event) => {
      if (!this.keyboardEnabled || this.gameOver) return;
      const key = event.key.toUpperCase();
      if (/^[A-Z]$/.test(key)) this.addLetter(key);
      else if (key === 'BACKSPACE') this.removeLetter();
      else if (key === 'ENTER') this.submitGuess();
    });
  }

  // Add Letter
  addLetter(letter) {
    if (this.guesses[this.currentRow].length < this.maxLength) {
      this.guesses[this.currentRow] += letter;
      this.updateGuessRow();
    }
  }

  // Remove Letter
  removeLetter() {
    if (this.guesses[this.currentRow].length > 0) {
      this.guesses[this.currentRow] = this.guesses[this.currentRow].slice(0, -1);
      this.updateGuessRow();
    }
  }

  // Submit Guess
  async submitGuess() {
    const currentGuess = this.guesses[this.currentRow].toUpperCase();
    if (currentGuess.length !== this.maxLength) {
      this.displayMessage("Incomplete guess! Fill all the tiles.", "error");
      return;
    }

    try {
      const response = await fetch(validateGuessUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify({ guess: currentGuess }),
      });

      const data = await response.json();
      if (data.status === "error") {
        this.displayMessage(data.message, "error");
      } else if (data.status === "success") {
        this.handleGameWin(data.message);
      } else if (data.status === "game_over") {
        this.handleGameLoss(data.message);
      } else {
        this.updateRowResult(data.result);
        this.advanceToNextRow();
      }
    } catch (error) {
      console.error("Guess submission error:", error);
      this.displayMessage("Network error. Please try again.", "error");
    }
  }

  // Update Row Result
  updateRowResult(result) {
    const guessRow = document.querySelector(`.word-tiles-${this.currentRow + 1}`);
    if (guessRow) {
      const tiles = guessRow.children;
      result.forEach((status, index) => {
        tiles[index].classList.remove("absent", "present", "correct");
        tiles[index].classList.add(status);
      });
    }
  }

  // Advance to Next Row
  advanceToNextRow() {
    if (this.currentRow < this.maxRows - 1) {
      this.currentRow++;
    } else {
      this.handleGameLoss("No more attempts left!");
    }
  }

  // Handle Game Win
  handleGameWin(message) {
    this.displayMessage(message, "success");
    this.endGame();
  }

  // Handle Game Loss
  handleGameLoss(message) {
    this.displayMessage(message, "error");
    this.endGame();
  }

  // End Game
  endGame() {
    this.gameOver = true;
    this.disableKeyboard();
  }

  // Disable Keyboard
  disableKeyboard() {
    this.keyboardEnabled = false;
  }
}

// Initialize Wordle Game
document.addEventListener("DOMContentLoaded", () => {
  window.wordleGame = new WordleGame();
});

