# 🔍 ParseVision — Compiler Design Visualizer

**ParseVision** is a terminal-based Compiler Design project built with Python that helps students understand how arithmetic expressions are tokenized, parsed, and converted into parse trees.

## ✨ Features

- **Lexical Analysis:** Converts arithmetic expressions into tokens.
- **Expression Parsing:** Handles arithmetic operators and operator precedence.
- **Parentheses Support:** Parses expressions containing nested parentheses.
- **Parsing Trace:** Displays parsing operations and stack states.
- **Step-by-Step Mode:** Walks through the parsing process interactively.
- **Grammar Explorer:** Displays grammar production rules.
- **Parse Tree Visualization:** Represents parsed expressions as a tree in the terminal.
- **Unit Testing:** Includes tests for core parsing functionality.

## 🛠️ Technologies Used

- Python 3
- Rich — for formatted terminal output
- Regular Expressions — for lexical analysis
- `unittest` — for testing

## 📁 Project Structure

```text
ParseVision/
├── tests/
│   └── test_parser.py
├── main.py
├── lexer.py
├── parser.py
├── tree.py
├── stack_visualizer.py
├── tree_visualizer.py
├── grammar.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/ParseVision.git
cd ParseVision
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

Ensure `requirements.txt` contains:

```text
rich
```

### 5. Run ParseVision

```bash
python main.py
```

## 🖥️ Usage

After launching the program, choose an option from the interactive menu:

| Option | Function |
|---|---|
| 1 | Parse an expression and display the full trace |
| 2 | Parse an expression step by step |
| 3 | View grammar production rules |
| 0 | Exit the application |

### Example Expression

```text
a + b * c
```

The resulting parse tree will represent multiplication before addition:

```text
+
├── a
└── *
    ├── b
    └── c
```

## 🧪 Run Tests

Execute the unit tests with:

```bash
python -m unittest discover -s tests -v
```

## 🎯 Learning Objectives

- Understand the lexical analysis and syntax analysis stages.
- Learn how operator precedence affects expression parsing.
- Explore grammar production rules.
- Visualize parsing operations and parse trees.
- Practice Python programming, modular design, and unit testing.

## ⚠️ Project Scope

ParseVision is an educational arithmetic expression parser and visualization tool. It is not a complete compiler and does not currently implement a formal LR parsing algorithm.

## 👨‍💻 Author

**Omkar Mukhopadhyay**

## 📄 License

This project is intended for educational and academic purposes. Add a specific open-source license if you want others to reuse or distribute it under defined terms.
