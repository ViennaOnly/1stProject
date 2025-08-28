from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# "База данных" в памяти (список словарей)
notes = [
    {"id": 1, "text": "Первая заметка"},
    {"id": 2, "text": "Вторая заметка"}
]

@app.route('/')
def index():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():
    new_text = request.form['note_text']
    new_id = len(notes) + 1
    notes.append({"id": new_id, "text": new_text})
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note['id'] != note_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:note_id>', methods=['GET', 'POST'])
def edit_note(note_id):
    note = next((note for note in notes if note['id'] == note_id), None)
    if request.method == 'POST':
        note['text'] = request.form['note_text']
        return redirect(url_for('index'))
    return render_template('edit.html', note=note)

if __name__ == '__main__':
    app.run(debug=True)
