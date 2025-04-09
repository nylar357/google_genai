# AI Terminal Assistant (`[Your Script Name]`) 🤖

A simple command-line script to interact with an AI assistant directly from your terminal. Ask questions, generate code, get explanations, and more without leaving your workflow.

## ✨ Features

*   **Direct AI Access:** Send prompts to Google Gamini from your shell.
*   **Inline Queries:** Get quick answers or code snippets.
*   **Streamlined Workflow:** Avoid context switching between your editor/terminal and a web browser.
*   **Customizable:** (Optional: Mention if easily configurable - e.g., model choice, temperature).

## ⚙️  Prerequisites

*   A shell environment (Bash, Zsh, Fish, etc.)
*   `curl` (or `wget`, depending on your script's implementation) to make API requests.
*   `jq` (optional, but recommended) for parsing JSON responses if your script uses it.
*   An API Key from [AI Service Name] ([Link to AI Service Signup if available]).

## 🚀 Installation

1.  **Clone the repository (or download the script):**
    ```bash
    git clone https://github.com/nylar357/google_genai.git
    cd google_genai
    ```
    


## 🔧 Configuration

The script requires your [AI Service Name] API key. Set it as an environment variable:

```bash
export AI_API_KEY="YOUR_API_KEY_HERE"
```

**Tip:** Add this line to your shell configuration file (`~/.bashrc`, `~/.zshrc`, `~/.profile`, or similar) so it's set automatically when you open a new terminal. Remember to source the file (`source ~/.bashrc`) or open a new terminal window after adding it.

*(Alternatively, describe if your script uses a config file or command-line arguments for the key).*

## 💡 Usage

Run the script followed by your prompt in quotes:

```bash
# If added to PATH:
[Your Script Name] "Explain the difference between git merge and git rebase"

# If running directly from its directory:
./[Your Script Name].sh "Write a python function to check if a number is prime"
```

The AI's response will be printed directly to your terminal.

*(Add more examples or mention specific options/flags if your script has them, e.g., multi-line input, file input, etc.)*

---

*This script provides a basic interface. Feel free to fork, modify, and enhance it!*
