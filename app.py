from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = {}
    envs = []

    for env in os.environ:
        if 'HELLO' in env:
            envs.append({"key": env, "value": os.getenv(env)})

    data['message'] = "Hello from OpenShift!"
    data['branch'] = "test4"
    data['envVars'] = envs

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
