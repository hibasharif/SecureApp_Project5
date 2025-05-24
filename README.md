
````markdown
# 🔐 Secure Data Encryption System (Streamlit App)

A simple yet powerful Streamlit web app that allows users to securely **encrypt**, **store**, and **retrieve** sensitive text data using **Fernet symmetric encryption** and **SHA-256 hashed passkeys**.

---

## 🚀 Live Demo

🌐 Try it here: [https://secure-data-app.streamlit.app](https://secureappproject5-gblbyrxlxrpp4ycasjqgvk.streamlit.app/)



---

## 📦 Features

- 🔒 Encrypt sensitive data with Fernet encryption
- 🔐 Protect encrypted data with a secure passkey
- 🔓 Retrieve and decrypt data using the correct passkey
- 🚫 Lock access after 3 failed attempts
- 🔑 Master login page to reauthorize access

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/secure-encryption-app.git
cd secure-encryption-app
````

### 2. Install dependencies

Make sure you have Python 3.9+ installed. Then run:

```bash
pip install streamlit cryptography
```

---

## ▶️ Usage

```bash
streamlit run secure_app.py
```

Navigate to the provided local URL (usually `http://localhost:8501`) to interact with the app.

---

## 📷 Screenshots

### 🏠 Home Page

![Home Page](screenshots/home.png)

### 📂 Store Data

![Store Page](screenshots/store.png)

### 🔍 Retrieve Data

![Retrieve Page](screenshots/retrieve.png)

---

## 🔐 Master Login

To reauthorize access after multiple failed decryption attempts, go to the **Login** tab and use the master password:

```
admin123
```

*(For demo purposes only. In production, use environment variables or secure storage.)*

---

## 📁 Project Structure

```
secure-encryption-app/
│
├── secure_app.py        # Main Streamlit app
├── README.md            # Project documentation
└── requirements.txt     # Optional: dependencies list
```

---

## 🧠 Concepts Used

* Streamlit Web App Interface
* Symmetric Encryption with `cryptography.fernet`
* Secure passkey hashing using `hashlib.sha256`
* Session state for in-memory secure storage

---

## 📜 License

MIT License. Use freely and responsibly.

---

## 👩‍💻 Author

**Hiba Sharif** – Software Engineering Student at Jinnah University for Women
📫 [Connect on LinkedIn](https://www.linkedin.com) *(Insert your real profile link)*

````

---

### Optional: `requirements.txt`

You can include this file for easy installation:

```txt
streamlit
cryptography
````

---

