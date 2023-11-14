from flask import Flask, request, render_template
from src.model.user_request import UserRequest
from src.service.ally_service import getAlly
from src.service.product_service import getProduct

app = Flask(__name__, template_folder = "./src/templates")
app.config["DEBUG"] = True

@app.route('/api/v1/aliados', methods = ['POST'])
def allyTable():
    jsonData = request.get_json()
    dto = UserRequest(**jsonData)
    url = dto.url+dto.Codigo
    ally = getAlly(url)
    return render_template('ally_response.html', ally=ally)

@app.route('/api/v1/productos', methods = ['POST'])
def productTable():
    jsonData = request.get_json()
    dto = UserRequest(**jsonData)
    url = dto.url+dto.Codigo
    product = getProduct(url)
    return render_template('product_response.html', product=product)


if __name__ == '__main__':
    app.run('localhost', 3000)