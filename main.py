rom flask import Flask 
import random 

app = Flask(__name__)

# Rotas
@app.route('/')
def homepage():
    return 'bem-vindo à homepage, digite "/dois-dados" para começar.'

@app.route('/dois-dados')
def dois_dados():
    rand1 = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    total = rand1 + rand2
    return f'atualize a página para rolar novamente <br>{rand1} {rand2} <br> {total}'

if __name__ == '__main__':
    app.run(debug=True)
# cd dois_dados, cd flask, python3 main.py
