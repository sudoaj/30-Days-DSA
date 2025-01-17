


# TODO - January 17, 2025

## Django Project: Wordle Game

### Models
- **Updated `DailyWord` model**:
  - Added fields for `word`, `date`, and `is_active`.
  - Ensured the word is a unique 5-letter string and associated with a unique date.

- **Updated `Player` model**:
  - Changed the `username` field to a `OneToOneField` linked to the `User` model.

- **Created `Guess` model**:
  - Tracks individual guesses, linking them to `Player` and `DailyWord`.

---

### Views
- **Combined Views**:
  - Merged `home`, `todays_game`, and `submit_guess` into a single view (`todays_game`).
  - Unified logic for game initialization, guess submission, and result handling.

- **Error Handling**:
  - Added checks for:
    - Missing daily words.
    - Players without associated `Player` instances.
    - Invalid guesses (e.g., non-5-letter words).

---

### Templates
- **`home.html`**:
  - Created a welcoming page with a "Play Now" button.

- **`todays_game.html`**:
  - Built a unified template to:
    - Display the game interface.
    - Show previous guesses and remaining attempts.
    - Handle dynamic error messages.

---

### Scripts
- **Bash Scripts**:
  - **`create_daily_word.sh`**:
    - Generates a random 5-letter word and saves it as the `DailyWord` for today.
  - **`create_players_from_users.sh`**:
    - Automatically creates `Player` instances for all existing `User` accounts.
  - **`run_server_and_open.sh`**:
    - Starts the Django server and opens the project in Safari.

---

### URLs
- Updated `urls.py`:
  - Consolidated routing to support the unified `todays_game` view.
  - Ensured all links and reverse routing worked seamlessly with the new view structure.

---

### Debugging & Fixes
- Fixed `NoReverseMatch` error:
  - Corrected mismatched view names and URL patterns for `todays_game`.
- Resolved `FieldError`:
  - Updated queries to use `request.user.player` instead of `request.user`.
- Enhanced Error Messages:
  - Added user-friendly error feedback for missing words, unregistered players, and invalid guesses.

---

### Next Steps
- Add more styling to templates for better user experience.
- Implement a leaderboard to track player performance.
- Add unit tests for views and models.
- Optimize the game logic for performance and scalability.