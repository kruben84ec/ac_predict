from bd.conexion_hook import Database


class subcircuito():

    def list():
        # return 'Todas los subcircuitos'
        db = Database()
        return db.getResult(
            "SELECT subcircuito FROM base_2018 group by subcircuito",
            "subcircuito"
        )
         


