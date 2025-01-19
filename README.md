# Voulez-Vous Makan Avec Moi, Ce Soir? a. k. a. makanbot 🍳

# You may test use this bot @canuspicanbot!!

A Telegram bot designed to help coordinate meal timings among friends and display the information in a neat, user-friendly way. With this bot, users can set and share their meal availability, view others’ timings, and easily identify overlaps in schedules.

---

## Features 🚀

### Key Commands
- **`/start`**  
  Starts the bot and provides a friendly introduction.

- **`/help`**  
  Displays a list of commands and their descriptions.

- **`/brekkie`**  
  Allows users to:
  1. View who is available for breakfast at specific timings.
  2. Set their own breakfast availability using a dropdown menu with multiple time slot options.

- **`/makan`**  
  Enables users to select and submit their breakfast times from a dropdown list of 15-minute intervals between 7:00 AM and 10:30 AM. Multiple selections are allowed, and the bot calculates and displays:
  - A summary table showing who can eat at each time slot.
  - The percentage of people available at every time.

### Summary Table
When breakfast times are displayed, the bot generates a well-formatted table showing:
1. **Timings**: 15-minute intervals.
2. **Participants**: Who is eating at each slot.
3. **Percentage**: Percentage of participants available for each slot.

---

## Repository Structure 📂

### Main Files
- **`main.py`**  
  The main bot script containing all the logic and commands for the bot.

- **`requirements.txt`**  
  Contains all Python dependencies for the bot, including the Telegram API library (`python-telegram-bot`).

### Additional Files
- **`.env`**  
  Stores sensitive environment variables like the Telegram bot token. Ensure this file is included in `.gitignore` for security.

---

## Installation and Setup 🛠️

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hanlinnnnn/makanbot.git
   cd makanbot
   ```

2. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

3. **Request for bot credentials**
   Please contact @hanlinnnnn for this.

4. **Run the bot**:
    ```
    cd bot
    python main.py
    ```

## Credits 🙌

### Developer
- **Li Han Lin**
  GitHub handle @hanlinnnnnn
  Passionate about solving everyday coordination challenges through technology.

### Tools and Frameworks
- [Python](https://www.python.org/)  
- [python-telegram-bot](https://python-telegram-bot.readthedocs.io/)  
- [AWS EC2](https://aws.amazon.com/ec2/)  

### Inspiration
This bot was inspired by the need to simplify meal coordination among hostel friends with different schedules.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Feedback 📝

Feel free to open an issue or submit a pull request if you encounter any bugs or have suggestions for improvement!
