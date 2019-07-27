from models import api_model


def predict_delito(delito):
    """Debe tomar los datos y realizar la busqueda"""
    return api_model.predict_delito(delito)
def predict_modalidad(modalidad):
    """Debe tomar los datos y realizar la busqueda"""
    return api_model.predict_modalidad(modalidad)
def predict_circuito(circuito):
    """Debe tomar los datos y realizar la busqueda"""
    return api_model.predict_circuito(circuito)
def predict_mes(mes):
    """Debe tomar los datos y realizar la busqueda"""
    return api_model.predict_mes(mes)