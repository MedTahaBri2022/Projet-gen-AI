''' import streamlit as st
import hashlib

# Simulated user database
users_db = {
    "test_user": hashlib.sha256("test_password".encode()).hexdigest()
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in users_db and users_db[username] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.sidebar.success(f"Welcome {username}")
        else:
            st.sidebar.error("Invalid username or password")

def create_account():
    st.sidebar.title("Create Account")
    username = st.sidebar.text_input("New Username")
    password = st.sidebar.text_input("New Password", type="password")
    if st.sidebar.button("Create Account"):
        if username in users_db:
            st.sidebar.error("Username already exists")
        else:
            users_db[username] = hash_password(password)
            st.sidebar.success("Account created successfully")

def logout():
    st.session_state.logged_in = False
    st.sidebar.success("Logged out successfully") '''

import streamlit as st
import hashlib

# Simulated user database
users_db = {
    "test_user": hashlib.sha256("test_password".encode()).hexdigest()
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    st.sidebar.title("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Login"):
        if username in users_db and users_db[username] == hash_password(password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.sidebar.success(f"Welcome {username}")
        else:
            st.sidebar.error("Invalid username or password")

def create_account():
    st.sidebar.title("Create Account")
    username = st.sidebar.text_input("New Username")
    password = st.sidebar.text_input("New Password", type="password")
    if st.sidebar.button("Create Account"):
        if username in users_db:
            st.sidebar.error("Username already exists")
        else:
            users_db[username] = hash_password(password)
            st.sidebar.success("Account created successfully")

def logout():
    st.session_state.logged_in = False
    st.sidebar.success("Logged out successfully")