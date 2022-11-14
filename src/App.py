import ConexionDb, ScrapperCelulares

#obtenemos datos de la página
celularesConInfoPrincipal = ScrapperCelulares.getCelularesConInfoPpal()

#guardamos los datos en la BD
conexion = ConexionDb.Conexion()
for celular in celularesConInfoPrincipal:
    conexion.insertarDato(celular)