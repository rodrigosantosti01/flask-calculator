from flask import Flask,request,Response,json

app = Flask(__name__)

@app.route('/calcula', methods=['POST'])
def hello_world():
    data = request.json
    # verifica o tipo os valores a serem calculados
    if type(data['primeiro_numero']) == type(int()) and type(data['segundo_numero'])==type(int()):
        # verifica qual operação foi solicitada
        
        calculo = 0 
        if data['operacao']=="*" or data['operacao']=="multiplicacao":
            calculo = data['primeiro_numero'] * data['segundo_numero']
        elif data['operacao']=="+" or data['operacao']=="soma":
            calculo = data['primeiro_numero'] + data['segundo_numero']
        elif data['operacao']=="-" or data['operacao']=="subtracao":
            calculo = data['primeiro_numero'] - data['segundo_numero']
        elif data['operacao']=="/" or data['operacao']=="divisao":
            calculo = data['primeiro_numero'] / data['segundo_numero']
        else:
            message = {"mensagem":"A operação deverá ser (*,+,-,/) ou (multiplicacao,soma,subtracao,divisao) e do tipo String",
            "status_code":400}
            
            return Response(
                response=json.dumps(message),
                status=400,
                mimetype='application/json'),200

        return Response(
                response=json.dumps({"resultado":calculo}),
                status=200,
                mimetype='application/json'),200

    else:
        message = {"mensagem":"Certifique que o tipo dos dados que foram enviados para o cálculo são inteiros",
        "status_code":400}
        return Response(
            response=json.dumps(message),
            status=400,
            mimetype='application/json'),200



if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)