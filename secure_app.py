import streamlit as st
import hashlib
from cryptography.fernet import Fernet, InvalidToken

# Store encryption key in session so it's consistent during app use
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()

cipher = Fernet(st.session_state.fernet_key)

# In-memory storage (shared across reruns using session state)
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}  # Format: {encrypted_text: {"encrypted_text":..., "passkey": hashed}}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "authorized" not in st.session_state:
    st.session_state.authorized = True


# Hashing function using SHA-256
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()


# Encrypt text
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()


# Decrypt text
def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)

    if encrypted_text in st.session_state.stored_data:
        entry = st.session_state.stored_data[encrypted_text]
        if entry["passkey"] == hashed:
            try:
                decrypted = cipher.decrypt(encrypted_text.encode()).decode()
                st.session_state.failed_attempts = 0
                return decrypted
            except InvalidToken:
                pass  # Handle decryption error

    st.session_state.failed_attempts += 1
    return None


# Main Streamlit UI
st.title("🛡️ Secure Data Encryption System")

# Navigation Menu
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigate", menu)

# Home Page
if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("This tool lets you securely **store** and **retrieve** sensitive data using encryption and passkeys.")

# Store Data Page
elif choice == "Store Data":
    st.subheader("📂 Store Data")
    user_data = st.text_area("Enter the data you want to store:")
    passkey = st.text_input("Enter a secure passkey:", type="password")

    if st.button("Encrypt and Save"):
        if user_data and passkey:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(user_data)
            st.session_state.stored_data[encrypted] = {
                "encrypted_text": encrypted,
                "passkey": hashed
            }
            st.success("✅ Data encrypted and stored securely!")
            st.code(encrypted, language="text")
        else:
            st.error("⚠️ Please provide both data and a passkey.")

# Retrieve Data Page
elif choice == "Retrieve Data":
    if not st.session_state.authorized:
        st.warning("🔒 You must login again due to too many failed attempts.")
        st.rerun()

    st.subheader("🔍 Retrieve Data")
    encrypted_input = st.text_area("Paste the encrypted data:")
    input_passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_input and input_passkey:
            result = decrypt_data(encrypted_input, input_passkey)
            if result:
                st.success("✅ Data decrypted successfully!")
                st.code(result, language="text")
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts left: {attempts_left}")

                if st.session_state.failed_attempts >= 3:
                    st.warning("🚫 Too many failed attempts. You must reauthorize.")
                    st.session_state.authorized = False
                    st.rerun()
        else:
            st.error("⚠️ Please fill in all fields.")

# Login Page
elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter master password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Simple demo password
            st.session_state.failed_attempts = 0
            st.session_state.authorized = True
            st.success("✅ Login successful! You can now access the Retrieve page.")
            st.rerun()
        else:
            st.error("❌ Incorrect master password!")
