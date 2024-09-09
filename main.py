from flask import Flask, render_template, request
from services.openai_service import ask_openai

# Initialize the Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    user_question = None

    if request.method == 'POST':
        # Get the question from the form
        user_question = request.form.get('question')

        # Call the OpenAI service to get the response
        response_text = ask_openai(user_question)

        # Render the page with the question and response
        return render_template('index.html', question=user_question, response=response_text)

    # On GET request, simply load the page without any response
    return render_template('index.html', question='', response='')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
