
# 🎓 Aptech Exam CLI Runner

A simple command-line quiz app that lets you practice past Aptech exam papers by loading `.htm` files. It extracts the questions, options, and correct answers automatically and lets you take the test with real-time scoring.

![Screenshot (34)](https://github.com/user-attachments/assets/7f674f1c-de78-449f-976b-b1c830891e06)

---

## ✨ Features

- ✅ Load `.htm` files exported from Aptech
- ✅ Automatically detect questions, options, and correct answers
- ✅ Clean CLI interface for taking the test
- ✅ Final score summary at the end
- ✅ One-command setup with `start.sh`

---

## 📦 Requirements

- Python 3.x installed  
- Internet access only needed once (to install dependencies)

---

## 🚀 Getting Started

### 1. Clone this repo

```bash
git clone https://github.com/Mahmudumar/Aptech-exam-practice.git

````

### 2. Start the exam system

```bash
./start.sh
```

> The script installs required libraries and starts the CLI quiz app.

---

## 📁 How to Use

1. Place your `.htm` file (e.g., `1.htm`) in this folder.
2. Run the app (`./start.sh`).
3. When prompted, type the filename like: ```1.htm```

4. Answer each question (type `1`, `2`, `3`, or `4`).
5. Get your final score!

---

## 🔧 Manual Setup (Alternative)

If `start.sh` doesn’t work, you can install manually:

```bash
pip install -r requirements.txt
python3 exam_test.py
```

---

## 👨‍💻 Created by

**Umar Mahmud**: Built to help students prepare smarter and faster.

---

## 🙌 Contributions

Feel free to fork this repo or suggest improvements via pull request or issue.
