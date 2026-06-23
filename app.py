from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    return f"""
    <html>
      <body style="font-family: sans-serif; text-align: center; padding: 60px; background: #0f172a; color: #f8fafc;">
        <h1 style="font-size: 2.5rem; color: #22c55e;">✅ Version 2 is live.</h1>
        <p style="font-size: 1.2rem; color: #94a3b8;">Your app is running inside a container.</p>
        <p style="margin-top: 40px; background: #1e293b; padding: 16px; border-radius: 8px; display: inline-block;">
          <strong style="color: #f472b6;">Hostname:</strong>
          <span style="color: #4ade80; margin-left: 8px;">{hostname}</span>
        </p>
        <p style="color: #64748b; margin-top: 8px; font-size: 0.85rem;">
          (This hostname is your container ID — proof you're inside Docker)
        </p>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
