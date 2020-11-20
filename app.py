import os
import requests

from flask import *

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

app.config['HTTPBIN_ENDPOINT'] = 'https://httpbin.org' if os.getenv('HTTPBIN_ENDPOINT') is None else os.getenv('HTTPBIN_ENDPOINT')

@app.route('/<httpbin_path1>/', defaults={'httpbin_path2': ''})
@app.route('/<httpbin_path1>/<httpbin_path2>')
def index(httpbin_path1, httpbin_path2):
  timeout = None if request.args.get('timeout') is None else int(request.args.get('timeout'))
  httpbin_url = '{0}/{1}/{2}'.format(app.config['HTTPBIN_ENDPOINT'], httpbin_path1, httpbin_path2).rstrip('/')
  headers = {"content-type": "application/json"}
  response = requests.get(httpbin_url, timeout=timeout, headers=headers, params=request.args)

  if request.headers.get("Content-Type") == 'application/json':
    return response.json, response.status_code
  else:
    return render_template("index.html", server=httpbin_url, req_headers=headers, headers=response.headers, text=response.text, status=response.status_code)

@app.route('/health')
def health():
    return 'OK'

