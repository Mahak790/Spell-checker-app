from flask import Flask, request, render_template
from model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Spell check from form
@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text = spell_checker_module.correct_spell(text)
        return render_template('index.html', corrected_text=corrected_text)

# Spell check from uploaded file
@app.route('/grammar', methods=['POST', 'GET'])
def grammar():
    if request.method == 'POST':
        file = request.files['file']
        readable_file = file.read().decode('utf-8', errors='ignore')
        corrected_file_text = spell_checker_module.correct_spell(readable_file)
        return render_template('index.html', corrected_file_text=corrected_file_text)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
