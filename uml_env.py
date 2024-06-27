# uml_env.py

from groq import Groq  # Assuming this is the correct import path for Groq

# Initialize Groq client
client = Groq(api_key="your_api_key_here")  # Replace with your actual API key

# Define the default templates and conditions for Use Cases, Sequence Diagrams, and Requirements
use_case_template = '''
Macro Use Cases :\n
  actor: [Actor\'s Name]\n  description for action: [Action Description]
'''

use_case_conditions = '''
    - Structure the output into macro use cases.
    - Summarize each macro use case with its associated functionalities.
    - Limit the number of macro use cases to cover the main aspects of the system.
    - Ensure clear and concise descriptions for each macro use case.
    - Avoid technical jargon and use simple language understandable to non-experts.
    - Maintain consistency in formatting and presentation throughout the output.
'''

sequence_diagram_template = '''
    Sequence diagram code :
        @startuml
        -
        -
        -
        @enduml
'''

sequence_diagram_conditions = '''
    - Provide a clear and structured sequence diagram.
    - Define participants and their interactions.
    - Include a sample message flow to illustrate interactions.
    - Avoid technical jargon and use simple language understandable to non-experts.
    - Give me also the plantuml code to generate the diagram
    - GIVE ME PLANTUML IN CODE BLOCK
    - Do not place multiple elements on the same line.
    - Maintain the structure with participants and interactions on separate lines.
    - Start the response with "Here is your sequence diagram : "
    - IMPORTANT:ALWAYS!!Remove the notes from plantuml code
    - ALWAYS:if an interaction is a response to a requestA->B do B-->A
'''

requirements_template = '''
    The "{machine}" shall "{do something}" when "{conditions}" with "{an expected performance}" in "{vehicle phase}"..
'''

requirements_conditions = '''
    - Ensure clear and concise description of each requirement.
    - Define the action, conditions, expected performance, and vehicle phase clearly.
    - Use simple language understandable to non-experts.
    - Give the requirements only in this template
'''

# Function to generate content based on selection
def generate_content(content_type, content_input):
    if content_type == "Use Cases":
        template = use_case_template
        conditions = use_case_conditions
    elif content_type == "Sequence Diagram":
        template = sequence_diagram_template
        conditions = sequence_diagram_conditions
    elif content_type == "Requirements":
        template = requirements_template
        conditions = requirements_conditions
    else:
        return "Invalid content type"

    prompt = f"Use the following template:\n\n{template}\n\nWith these conditions:\n\n{conditions}\n\nContent input:\n\n{content_input}"

    # Generate content using Groq
    response = client.generate(prompt)
    return response