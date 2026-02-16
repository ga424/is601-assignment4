# Calculator Application

A Python-based interactive command-line calculator with support for basic arithmetic operations including addition, subtraction, multiplication, division, and exponentiation. Built using the Factory design pattern for extensible calculation types.

## 🏗️ Architecture

This project follows the C4 model for architecture documentation. View the following diagrams to understand the system structure at different levels:

- **[Context Diagram](docs/c4-context.md)** - System context showing how users interact with the calculator
- **[Container Diagram](docs/c4-container.md)** - High-level containers (REPL, Calculation Engine, Operations)
- **[Component Diagram](docs/c4-component.md)** - Internal component structure and relationships
- **[Code Diagram](docs/c4-code.md)** - Code-level implementation details and class structures
- **[Deployment Diagram](docs/c4-deployment.md)** - Deployment topology and infrastructure

## ✨ Features

- Interactive REPL (Read-Eval-Print Loop) interface
- Support for basic operations: `add`, `subtract`, `multiply`, `divide`, `power`
- Factory pattern for extensible calculation types
- Comprehensive test coverage (99%+)
- Input validation and error handling
- Case-insensitive operation names

## 🎯 Quick Start

```bash
# Clone the repository
git clone git@github.com:ga424/is601-assignment4.git
cd is601-assignment4

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the calculator
python main.py
```

Example usage:
```
>>> add 5 3
5.0 add 3.0 = 8.0
>>> multiply 4 2.5
4.0 multiply 2.5 = 10.0
>>> exit
Goodbye!
```

---

# 📦 Project Setup

---

# 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.  
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

# 🧩 2. Install and Configure Git

## Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).  
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

## Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

## Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

(Press Enter at all prompts.)

2. Start the SSH agent:

```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

# 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

# 🛠️ 4. Install Python 3.10+

## Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).  
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---

## Create and Activate a Virtual Environment

(Optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate.bat  # Windows
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 🐳 5. (Optional) Docker Setup

> Skip if Docker isn't used in this module.

## Install Docker

- [Install Docker Desktop for Mac](https://www.docker.com/products/docker-desktop/)
- [Install Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)

## Build Docker Image

```bash
docker build -t <image-name> .
```

## Run Docker Container

```bash
docker run -it --rm <image-name>
```

---

# 🚀 6. Running the Project

- **Without Docker**:

```bash
python main.py
```

Or run the calculator module directly:

```bash
python -m app.calculator
```

(or update this if the main script is different.)

- **With Docker**:

```bash
docker run -it --rm <image-name>
```

---

# 📝 7. Submission Instructions

After finishing your work:

```bash
git add .
git commit -m "Complete Module X"
git push origin main
```

Then submit the GitHub repository link as instructed.

---

# ✅ 8. Running Tests

Run the full test suite:

```bash
pytest
```

If you see an error about missing `pytest-cov`, install it:

```bash
pip install pytest-cov
```

Or run tests without the coverage config:

```bash
pytest -c /dev/null tests
```

# 🔥 Useful Commands Cheat Sheet

| Action                         | Command                                          |
| ------------------------------- | ------------------------------------------------ |
| Install Homebrew (Mac)          | `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` |
| Install Git                     | `brew install git` or Git for Windows installer |
| Configure Git Global Username  | `git config --global user.name "Your Name"`      |
| Configure Git Global Email     | `git config --global user.email "you@example.com"` |
| Clone Repository                | `git clone <repo-url>`                          |
| Create Virtual Environment     | `python3 -m venv venv`                           |
| Activate Virtual Environment   | `source venv/bin/activate` / `venv\Scripts\activate.bat` |
| Install Python Packages        | `pip install -r requirements.txt`               |
| Build Docker Image              | `docker build -t <image-name> .`                |
| Run Docker Container            | `docker run -it --rm <image-name>`               |
| Push Code to GitHub             | `git add . && git commit -m "message" && git push` |

---

# 📋 Notes

- Install **Homebrew** first on Mac.
- Install and configure **Git** and **SSH** before cloning.
- Use **Python 3.10+** and **virtual environments** for Python projects.
- **Docker** is optional depending on the project.

---

# 📎 Quick Links

- [Homebrew](https://brew.sh/)
- [Git Downloads](https://git-scm.com/downloads)
- [Python Downloads](https://www.python.org/downloads/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [GitHub SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

# 📂 Project Structure

```
assignment4/
├── app/
│   ├── calculation/          # Calculation factory and calculation classes
│   │   └── __init__.py       # Factory pattern implementation
│   ├── calculator/           # REPL interface
│   │   └── __init__.py       # Calculator class and entry point
│   └── operations/           # Core arithmetic operations (legacy)
│       └── __init__.py       # Static operation methods
├── tests/
│   ├── test_calculator.py    # REPL and integration tests
│   └── test_operations.py    # Calculation and operation tests
├── docs/
│   ├── c4-context.md         # System context diagram
│   ├── c4-container.md       # Container-level architecture
│   ├── c4-component.md       # Component-level structure
│   ├── c4-code.md           # Code-level implementation
│   └── c4-deployment.md     # Deployment topology
├── main.py                   # Application entry point
├── requirements.txt          # Python dependencies
└── pytest.ini               # Test configuration
```

## 🔍 Key Components

### Calculation Factory (`app/calculation/`)
- **CalculationFactory**: Factory class for creating calculation instances
- **Calculation**: Abstract base class for all calculation types
- **Concrete Calculations**: AddCalculation, SubtractCalculation, MultiplyCalculation, DivideCalculation, PowerCalculation
- Uses decorator pattern for automatic registration

### Calculator REPL (`app/calculator/`)
- **Calculator**: Main REPL class managing user interaction
- Input parsing and validation
- Error handling and recovery
- Dynamic operation registry from factory

### Operations Module (`app/operations/`)
- Static arithmetic methods (legacy support)
- Used by calculation classes for core arithmetic logic

---

# 📐 Architecture Documentation

Detailed architecture diagrams are available in the `docs/` directory following the C4 model:

| Diagram | Purpose | View |
|---------|---------|------|
| **Context** | System boundaries and external actors | [View](docs/c4-context.md) |
| **Container** | High-level module structure | [View](docs/c4-container.md) |
| **Component** | Internal component relationships | [View](docs/c4-component.md) |
| **Code** | Class structures and methods | [View](docs/c4-code.md) |
| **Deployment** | Infrastructure and deployment topology | [View](docs/c4-deployment.md) |

---

# 🧪 Testing

This project maintains 99%+ code coverage with comprehensive unit and integration tests.

**Run all tests:**
```bash
pytest
```

**Run with coverage report:**
```bash
pytest --cov --cov-report=term-missing
```

**View HTML coverage report:**
```bash
pytest --cov --cov-report=html
open htmlcov/index.html
```

## Test Structure

- `tests/test_calculator.py` - REPL functionality, input parsing, error handling
- `tests/test_operations.py` - Calculation factory, operations, edge cases

---

# 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with tests
4. Ensure tests pass: `pytest`
5. Commit: `git commit -m "Add feature"`
6. Push: `git push origin feature-name`
7. Create a Pull Request

---

# 📄 License

See [LICENSE](LICENSE) file for details.
