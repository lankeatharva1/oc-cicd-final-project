"""
Service Routes
"""
from flask import jsonify
from service import app


@app.route("/health")
def health():
    """Health endpoint"""
    return jsonify(status=200, message="OK"), 200


@app.route("/")
def index():
    """Root endpoint"""
    return jsonify(name="CI/CD Pipeline Demo Service", version="1.0"), 200
