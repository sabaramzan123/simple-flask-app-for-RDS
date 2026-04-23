from flask import Flask

app = Flask(__name__)

# Route to the root URL
@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask on Docker</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: Arial, sans-serif;
                background: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .card {
                background: white;
                padding: 40px 60px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #2c3e50;
                font-size: 2rem;
                margin-bottom: 10px;
            }
            p {
                color: #7f8c8d;
                font-size: 1rem;
                margin-bottom: 20px;
            }
            .badge {
                background: #27ae60;
                color: white;
                padding: 6px 16px;
                border-radius: 20px;
                font-size: 0.85rem;
            }
            .links {
                margin-top: 25px;
            }
            .links a {
                display: inline-block;
                margin: 5px;
                padding: 8px 20px;
                background: #3498db;
                color: white;
                border-radius: 6px;
                text-decoration: none;
                font-size: 0.9rem;
            }
            .links a:hover {
                background: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, Flask on Docker!</h1>
            <p>Your containerized Flask app is running successfully</p>
            <span class="badge">Running on AWS EC2</span>
            <div class="links">
                <a href="/greet/Saba">Greet Saba</a>
                <a href="/greet/World">Greet World</a>
                <a href="/status">App Status</a>
            </div>
        </div>
    </body>
    </html>
    '''

# Route to greet a custom name
@app.route('/greet/<name>')
def greet(name):
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Greet</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: Arial, sans-serif;
                background: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .card {{
                background: white;
                padding: 40px 60px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                text-align: center;
            }}
            h1 {{ color: #2c3e50; font-size: 2rem; margin-bottom: 10px; }}
            p {{ color: #7f8c8d; font-size: 1rem; margin-bottom: 20px; }}
            a {{
                display: inline-block;
                margin-top: 15px;
                padding: 8px 20px;
                background: #3498db;
                color: white;
                border-radius: 6px;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, {name}!</h1>
            <p>Welcome to Flask on Docker</p>
            <a href="/">Back to Home</a>
        </div>
    </body>
    </html>
    '''

# Route to check app status
@app.route('/status')
def status():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>App Status</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: Arial, sans-serif;
                background: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .card {{
                background: white;
                padding: 40px 60px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                text-align: center;
                min-width: 300px;
            }}
            h2 {{ color: #2c3e50; margin-bottom: 20px; }}
            .row {{
                display: flex;
                justify-content: space-between;
                padding: 10px 0;
                border-bottom: 1px solid #ecf0f1;
                font-size: 0.95rem;
            }}
            .label {{ color: #7f8c8d; }}
            .value {{ color: #27ae60; font-weight: bold; }}
            a {{
                display: inline-block;
                margin-top: 20px;
                padding: 8px 20px;
                background: #3498db;
                color: white;
                border-radius: 6px;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>App Status</h2>
            <div class="row">
                <span class="label">Status</span>
                <span class="value">Running</span>
            </div>
            <div class="row">
                <span class="label">Platform</span>
                <span class="value">AWS EC2</span>
            </div>
            <div class="row">
                <span class="label">Container</span>
                <span class="value">Docker</span>
            </div>
            <div class="row">
                <span class="label">Port</span>
                <span class="value">3000</span>
            </div>
            <a href="/">Back to Home</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)