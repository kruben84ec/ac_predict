from models import api_model

def validate_base(base):
    if(base == '2018' or base == '2019'):
        return {
            'base': 'base_'+base,
            'error': True,
            'mensaje':''
        }
    else:
        return {
            'base': '',
            'error': False,
            'mensaje':'No exiten datos'
        }

def getAll_api(table, column):
    isValid = validate_base(table)
    if(isValid['error']):
        return api_model.group_list(column, isValid['base'])
    else:
        return isValid

def get_column(table):
    return api_model.get_api(table)

def get_delito(table):
    isValid = validate_base(table)
    if(isValid['error']):
        return api_model.get_delito(isValid['base'])
    else:
        return isValid

def get_circuito_mes(table, circuito):
    isValid = validate_base(table)
    if(isValid['error']):
        return api_model.get_delitoCircuitoMes(isValid['base'], circuito)
    else:
        return isValid