from bd.conexion_hook import Database

db = Database()

def group_list(column, tabla):
    # return 'Todas los subcircuitos'
    sql = "SELECT "+column+" FROM "+tabla+" GROUP BY "+column
    return db.getResult(sql, column)


def get_api(table):
    """Retorna el directorio """
    return db.getResult(
        "SELECT COLUMN_NAME AS `Field` FROM information_schema.COLUMNS  WHERE TABLE_SCHEMA = 'crimen' AND TABLE_NAME = '"+table+"'",
        'Field'
    )

def get_delito(table):
    """Retorna los estadisticos de delito"""
    sql = "SELECT delito, count(*) as 'numero' FROM "+table+" GROUP BY delito order by count(*) desc"
    return db.getResource(sql)

def get_delitoCircuitoMes(table, circuito):
    """Permite obtener los delito por circuito y mes"""
    sql = "SELECT delito, mes, count(*) numero FROM "+table+" WHERE circuito = '"+circuito+"' group by delito, mes order by count(*), mes desc;"
    return db.getResource(sql)

def predict_delito(delito):
    select = "SELECT fecha, count(*) AS numero, FLOOR(RAND()*(10-count(*)+1)+5) as pred FROM dwCrimen " 
    where = "WHERE delito = '"+delito+"'"
    group = "GROUP BY fecha ORDER BY fecha DESC"
    sql = select+" "+ where+" "+group
    return db.getResource(sql)

def predict_modalidad(modalidad):
    select = "SELECT fecha, count(*) AS numero, FLOOR(RAND()*(10-count(*)+1)+5) as pred FROM dwCrimen " 
    where = "WHERE modalidad = '"+modalidad+"'"
    group = "GROUP BY fecha ORDER BY fecha DESC"
    sql = select+" "+ where+" "+group
    return db.getResource(sql)

def predict_circuito(circuito):
    select = "SELECT fecha, count(*) AS numero, FLOOR(RAND()*(10-count(*)+1)+5) as pred FROM dwCrimen " 
    where = "WHERE circuito = '"+circuito+"'"
    group = "GROUP BY fecha ORDER BY fecha DESC"
    sql = select+" "+ where+" "+group
    return db.getResource(sql)

def predict_mes(mes):
    select = "SELECT fecha, count(*) AS numero, FLOOR(RAND()*(10-count(*)+1)+5) as pred FROM dwCrimen " 
    where = "WHERE mes = '"+mes+"'"
    group = "GROUP BY fecha ORDER BY fecha DESC"
    sql = select+" "+ where+" "+group
    return db.getResource(sql)