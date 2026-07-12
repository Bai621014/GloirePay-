from flask import Flask, render_template, jsonify, request
import json

# Imports relatifs depuis le package src
from .gloire_dev_ia import GloireDevIA
from .security import SecurityAudit

# Initialisation de Flask
app = Flask(__name__, template_folder='templates', static_folder='static')

# Instanciation des services
agent = GloireDevIA()
auditor = SecurityAudit()

def get_payload(req):
    """Fonction utilitaire pour extraire le JSON ou les données brutes."""
    if req.is_json:
        return req.get_json(silent=True) or {}
    
    raw = req.form.get('payload') or req.data.decode('utf-8')
    try:
        return json.loads(raw) if raw else {}
    except (ValueError, TypeError):
        return {"raw": raw}

@app.route('/')
def index():
    # Assurez-vous que agent.name existe dans votre classe GloireDevIA
    name = getattr(agent, 'name', 'GloireDevIA')
    return render_template('index.html', agent_name=name)

@app.post('/analyze')
def analyze():
    payload = get_payload(request)
    result = agent.analyze(payload)
    
    # Gestion automatique de la réponse (JSON vs HTML)
    if 'text/html' in request.headers.get('Accept', ''):
        return render_template('result.html', title='Analyse', result=result)
    return jsonify(result)

@app.post('/audit')
def audit():
    payload = get_payload(request)
    report = auditor.audit(payload)
    
    if 'text/html' in request.headers.get('Accept', ''):
        return render_template('result.html', title='Audit', result=report)
    return jsonify(report)

# Note : Ne pas utiliser app.run() sur Render (Gunicorn s'en charge)
# Mais utile pour vos tests locaux
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
