import gradio as gr
from transformers import pipeline

# Load a pre-trained model for conversational purposes.
# You might want to choose a more specialized model if available.
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

def respond_to_query(user_input):
    conversation = chatbot(user_input)
    return conversation[-1]['generated_text']

# Create the Gradio interface
interface = gr.Interface(
    fn=respond_to_query,
    inputs=gr.inputs.Textbox(placeholder="Ask a legal question about Papua New Guinea..."),
    outputs="text",
    title="PNGLawBot",
    description="A chatbot specializing in legal aspects of Papua New Guinea. Ask me anything releated to Legal matters in PNG!",
    theme="default"
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
