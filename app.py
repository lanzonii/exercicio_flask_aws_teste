from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    mensagem_1 = "Hello, world!"
    mensagem_2 = "I love DevOps!"
    style = '''
        body {
            background-color: #1C1C1C;
        }
        h1 {
            font-family: "Inter", sans-serif;
            font-weight: 800;
            color: #8F2FDB;
            font-size:700%;
        }
    '''
    return f'''
        <html>
        <head>
            <title>Exercício DevOps</title>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
            <style>
                {style}
            </style>
        </head>
        <body>
            <div style="margin:5%;">
                <h1>{mensagem_1.upper()}</h1>
                <h1>{mensagem_2.upper()}</h1>
            </div>
        </body>
        </html>
    '''


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
