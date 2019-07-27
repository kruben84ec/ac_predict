from routes import api
from flask import session
from flask_cors import CORS 
from controllers import api_controller
from controllers import api_predict

servicio = api.Api()

app = servicio.run_server
app.secret_key = ''
CORS(app)

method = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']
result = []
#rutas
@app.route('/', methods = method)
def index():
    result = api_controller.get_column('base_2018')
    return  servicio.responseApi(result)

@app.route('/<string:base>/<string:columna>', methods= method)
def subcircuito(base, columna):
    result = api_controller.getAll_api(base, columna)
    return servicio.responseApi(result)

@app.route('/delito/<string:base>', methods= method)
def delito(base):
    result = api_controller.get_delito(base)
    return servicio.responseApi(result)

@app.route('/circuito/<string:base>/<string:circuito>', methods= method)
def get_circuito_mes(base, circuito):
    result = api_controller.get_circuito_mes(base, circuito)
    return servicio.responseApi(result) 

"""Predice los delitos cometidos"""
@app.route('/ac_delito/<string:delito>', methods = method)
def predict_delito(delito):
    result = api_predict.predict_delito(delito)
    return servicio.responseApi(result)

"""Predice los delitos comentidos por circuito """
@app.route('/ac_circuito/<string:circuito>', methods = method)
def predict_circuito(circuito):
    result = api_predict.predict_circuito(circuito)
    return servicio.responseApi(result)

"""Predice los delitos comentidos por circuito """
@app.route('/ac_mes/<string:mes>', methods = method)
def predict_mes(mes):
    result = api_predict.predict_mes(mes)
    return servicio.responseApi(result)

@app.route('/ac_modalidad/<string:mes>', methods = method)
def predict_modalidad(mes):
    result = api_predict.predict_modalidad(mes)
    return servicio.responseApi(result)

#https://www.aprendemachinelearning.com/pronostico-de-series-temporales-con-redes-neuronales-en-python/
#https://www.aprendemachinelearning.com/tu-propio-servicio-de-machine-learning/
#https://github.com/jbagnato/machine-learning/blob/master/Red_Neuronal_Xor.ipynb
#https://www.aprendemachinelearning.com/una-sencilla-red-neuronal-en-python-con-keras-y-tensorflow/
#https://www.highcharts.com/docs/chart-and-series-types/tilemap-series
#https://www.highcharts.com/docs/advanced-chart-features/bubble-legend
#https://www.highcharts.com/blog/post/timeline-series/