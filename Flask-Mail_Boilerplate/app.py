from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Replace with actual mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-password'  # Replace with your password

mail = Mail(app)

@app.route('/send_mail', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        body = request.form['body']
        msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[recipient])
        msg.body = body
        mail.send(msg)
        flash('Email sent successfully!', 'success')
        return redirect(url_for('send_mail'))
    return render_template('email.html')

if __name__ == '__main__':
    app.run(debug=True)
