import os
import requests

from flask import *

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.config['BACKEND'] = 'https://httpbin.org' if os.getenv('BACKEND') is None else os.getenv('BACKEND')

@app.route('/<backend_path1>/', defaults={'backend_path2': ''})
@app.route('/<backend_path1>/<backend_path2>')
def index(backend_path1, backend_path2):
  timeout = None if request.args.get('timeout') is None else int(request.args.get('timeout'))
  backend_url = '{0}/{1}/{2}'.format(app.config['BACKEND'], backend_path1, backend_path2).rstrip('/')
  headers = {"content-type": "application/json"}
  response = requests.get(backend_url, timeout=timeout, headers=headers, params=request.args)

  if request.headers.get("Content-Type") == 'application/json':
    return jsonify(response.json()), response.status_code
  else:
    return render_template("index.html", server=backend_url, req_headers=headers, headers=response.headers, text=response.text, status=response.status_code)

@app.route('/health')
def health():
    return 'OK'

