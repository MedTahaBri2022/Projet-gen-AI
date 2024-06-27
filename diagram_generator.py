import base64
import streamlit as st
import plantuml

# Function to generate and display the PlantUML diagram
def generate_diagram(plantuml_code):
    try:
        diagram_bytes = plantuml.PlantUML(url='http://www.plantuml.com/plantuml/img/').processes(plantuml_code)
        st.session_state.diagram_bytes = diagram_bytes  # Store in session state
        return diagram_bytes
    except Exception as e:
        st.error(f"Error generating diagram: {e}")
        return None
