
# 🏦 AI Banking Chatbot

An AI-powered Banking Assistant built using **TinyLlama**, **Flask**, and **Ollama**. The chatbot answers banking and finance-related questions through a simple web interface while restricting conversations to banking topics only.

---

## 📖 Overview

The AI Banking Chatbot is a lightweight domain-specific chatbot that uses the TinyLlama Small Language Model (SLM) to provide quick and accurate responses to banking-related queries. The chatbot runs locally using Ollama, ensuring privacy and eliminating dependency on cloud APIs.

---

## ✨ Features

- 🏦 Banking-focused AI assistant
- 💬 Answers banking and finance questions
- 🦙 Powered by TinyLlama SLM
- ⚡ Local inference using Ollama
- 🌐 Flask web application
- 🔒 Restricts responses to banking topics
- 💻 Easy-to-use web interface

---

## 🛠️ Tech Stack

- Python
- Flask
- TinyLlama
- Ollama
- HTML
- CSS
- Requests

---

## 📂 Project Structure

```
Bank-Bot/
│
├── tinyllama/
│   ├── model.py
│   └── templates/
│       └── index.html
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com//Bank-Bot.git
```

### Navigate to the Project

```bash
cd Bank-Bot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🦙 Install TinyLlama

Pull the TinyLlama model using Ollama.

```bash
ollama pull tinyllama
```

Start the Ollama server.

```bash
ollama serve
```

---

## ▶️ Run the Application

```bash
python model.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 💻 Supported Topics

The chatbot answers questions related to:

- Bank Accounts
- Savings Account
- Current Account
- Debit Cards
- Credit Cards
- UPI
- IMPS
- NEFT
- RTGS
- Loans
- Fixed Deposits
- Interest Rates
- Digital Banking
- Mobile Banking
- Internet Banking
- Banking Security

---

## 🚫 Limitations

- Answers only banking and finance-related questions.
- Does not perform real banking transactions.
- Never requests sensitive information such as:
  - Passwords
  - ATM PIN
  - OTP
  - CVV
  - Account Passwords

---

## 📸 Screenshot

```
images/img.png
```

---

## 🚀 Future Improvements

- Chat history
- User authentication
- Voice assistant
- Multi-language support
- RAG with banking documents
- PDF-based banking policy assistant
- Banking FAQs database

---

## 📋 Requirements

```
Python 3.10+
Flask
Requests
Ollama
TinyLlama
```

---

## 👨‍💻 Author

**Abdul**

GitHub: https://github.com/Hakkeem7

LinkedIn: https://www.linkedin.com/in/kabdul-hakkeem/

---
## ⭐ Acknowledgements

- TinyLlama
- Ollama
- Flask
- Python Community
