# 🔐 Even-Numbered Solutions to *Understanding Cryptography*

This project contains full, well-documented LaTeX solutions to the **even-numbered problems** from the renowned cryptography textbook [*Understanding Cryptography*](https://www.springer.com/gp/book/9783642041006) by Christof Paar and Jan Pelzl.

While the official solution manual covers only odd-numbered exercises, this repository tackles the even-numbered ones — chapter by chapter — with detailed writeups and Python implementations where relevant.

---

## 📘 Motivation

> “While trying to recall a bit of cryptography for interview prep, I rewatched Prof. Christof Paar’s lectures on YouTube. Discovering the official handbook only solves odd-numbered problems, I found it intriguing — as if the authors left space for readers to complete the other half.  
> 
> So I decided to take on this challenge myself, chapter by chapter, and publish my solutions — with working Python examples where appropriate.”

— Mustapha EL BOUAZAOUI

---

## 📁 Project Structure

```
understanding-cryptography-even-solutions/
├── chapter-01/
│   ├── chapter-01.tex             # LaTeX write-up for Chapter 1
│   ├── 1.1.py                 
│   └── 1.2.py                 
│
├── main.tex                       # Main file combining all chapters
├── main.pdf                       # Compiled PDF of solutions
├── README.md
└── LICENSE
```

---

## 📖 Chapters Covered

| Chapter | Title                                | Status     |
|---------|--------------------------------------|------------|
| 1       | Introduction to Cryptography         | ✅ Complete |
| 2       | Stream Cipher                        | 🚧 In Progress |
| 3+      | ...                                   | 🔜 Coming soon |

> ✍️ Solutions are written chapter-by-chapter, not exercise-by-exercise, to enhance learning and documentation quality.

---

## 🐍 Python Code Examples

In addition to theory, several problems are backed by real Python code:

- [chapter-01/1.1.py](chapter-01/1.1.py)
- [chapter-01/1.2.py](chapter-01/1.2.py) 

Future chapters may include Vigenère cipher cracking, modular arithmetic, and RSA toy implementations.

---

## 🧠 Skills Covered

- Classical and modern cipher mechanics
- Number theory and modular arithmetic
- Frequency analysis and cipher attacks
- Cryptographic protocols and key exchange
- Practical crypto scripting in Python

---

## 🛠️ Build Instructions

To compile the LaTeX file locally:

```bash
pdflatex main.tex
```

Or use [Overleaf](https://www.overleaf.com) to edit and compile online.

---

## 📜 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.

Please credit this work if you reuse solutions or code.

---

## 🙌 Contributions

If you are also solving this book and want to collaborate:

- Fork the repo
- Add your writeups or improvements
- Open a pull request 🚀

---

## 📫 Contact

**Author**: Mustapha EL BOUAZAOUI  
📧 [mustaphaelbouazaoui@gmail.com](mailto:mustaphaelbouazaoui@gmail.com)
🌐 [LinkedIn](https://www.linkedin.com/in/elbouazaouimustapha/)