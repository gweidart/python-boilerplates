from flask import Flask, render_template, redirect, url_for, flash
from forms import SimpleForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash(f'Form submitted successfully with name: {form.name.data}')
        return redirect(url_for('index'))
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
