from flask import Flask, redirect, url_for, render_template, flash
from flask_principal import Principal, Permission, RoleNeed, identity_changed, Identity, AnonymousIdentity, identity_loaded
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# Flask-Principal setup
principal = Principal(app)

# Define roles
admin_permission = Permission(RoleNeed('admin'))

# Flask-Login setup
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Dummy user model for demonstration
class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

users = {
    'admin': User('1', 'admin', 'admin'),
    'guest': User('2', 'guest', 'guest')
}

@login_manager.user_loader
def load_user(user_id):
    for user in users.values():
        if user.id == user_id:
            return user
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'role'):
        identity.provides.add(RoleNeed(current_user.role))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/<username>')
def login(username):
    user = users.get(username)
    if user:
        login_user(user)
        identity_changed.send(app, identity=Identity(user.id))
        flash(f'Logged in as {username}', 'success')
        return redirect(url_for('index'))
    flash('User not found', 'danger')
    return redirect(url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    flash('Logged out', 'info')
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return 'Welcome to the admin page!'

if __name__ == '__main__':
    app.run(debug=True)
