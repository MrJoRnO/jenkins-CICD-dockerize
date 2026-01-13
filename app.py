# from flask import Flask
# import os

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     # המשתנה הזה יעזור לנו במשימה 2 לזהות איזה שירות רץ
#     service_name = os.getenv('SERVICE_NAME', 'Default Service')
#     return f"<h1>Hello from {service_name}!</h1><p>Mission 1 is successful!</p>"

# if __name__ == "__main__":
#     # האזנה ל-0.0.0.0 קריטית כדי שתוכל לגשת מבחוץ דרך דוקר
#     app.run(host='0.0.0.0', port=5000) 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Mission 1: Success!</h1><p>The Dockerized app is running and accessible.</p>"

if __name__ == "__main__":
    # האזנה ל-0.0.0.0 קריטית לגישה מחוץ לקונטיינר
    app.run(host='0.0.0.0', port=5000)