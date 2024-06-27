import streamlit as st
import base64
from plantuml import PlantUML, PlantUMLHTTPError
from io import BytesIO
from groq import Groq

# Initialize GROQ client with your API key
client = Groq(api_key="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")

# Function to interact with GROQ and generate responses
def generate_groq_response(user_message):
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": "Translate text to plantuml code for sequence diagram"},
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""

        return response.strip()

    except Exception as e:
        st.error(f"Error generating GROQ response: {str(e)}")
        return ""

# Function to generate and display the PlantUML diagram
def generate_diagram(plantuml_code):
    try:
        plantuml_bytes = PlantUML(url='http://www.plantuml.com/plantuml/img/').processes(plantuml_code)
        diagram_bytes = BytesIO(plantuml_bytes)
        return diagram_bytes

    except PlantUMLHTTPError as e:
        st.error(f"PlantUML HTTP Error: {e.response.status_code} - {e.response.reason}")
    except Exception as e:
        st.error(f"Error generating diagram: {str(e)}")
    return None

# Function to simulate user login (replace with your actual authentication logic)
def login(username, password):
    # Replace with actual authentication logic (e.g., check against a database)
    if username == "admin" and password == "password":
        return True
    else:
        return False

# Main function to run the Streamlit app
def main():
    # Login state management
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Set page configuration
    st.set_page_config(
        page_title="PlantUML Generator",
        page_icon=":pencil2:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # CSS for styling
    st.markdown(
        """
        <style>
        .st-bm {
            padding: 10px;
        }
        .st-bp {
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Login page
    if not st.session_state["logged_in"]:
        st.title("Login")

        # Login form
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login_button = st.button("Login")

        if login_button:
            if login(username, password):
                st.session_state["logged_in"] = True
            else:
                st.error("Invalid username or password")

    else:
        # After login: Main content area
        st.title("Generate PlantUML Diagrams")

        # Text area for entering PlantUML code
        plantuml_code = st.text_area("Enter your PlantUML code:", height=400)

        # Button to generate diagram
        if st.button("Generate Diagram"):
            if plantuml_code.strip():
                diagram_bytes = generate_diagram(plantuml_code)
                if diagram_bytes:
                    st.image(diagram_bytes, caption="Generated Diagram", use_column_width=True)
                    
                    # Download link for diagram
                    diagram_bytes.seek(0)
                    b64 = base64.b64encode(diagram_bytes.read()).decode()
                    href = f'<a href="data:file/png;base64,{b64}" download="diagram.png">Download Diagram as PNG</a>'
                    st.markdown(href, unsafe_allow_html=True)
            else:
                st.warning("Please enter some PlantUML code before generating the diagram.")

        # Text area for entering user message
        user_message = st.text_area("Enter your message to translate to PlantUML code:", height=200)
        if st.button("Translate to PlantUML"):
            if user_message.strip():
                with st.spinner("Processing..."):
                    groq_response = generate_groq_response(user_message)
                st.write("GROQ Response:")
                st.code(groq_response, language="plaintext")
            else:
                st.warning("Please enter a message.")

if __name__ == "__main__":
    main()