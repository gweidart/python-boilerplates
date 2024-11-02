from flask import Flask, render_template
from flask_caching import Cache
import time

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300

cache = Cache(app)

@app.route('/')
@cache.cached(timeout=60)
def index():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)
