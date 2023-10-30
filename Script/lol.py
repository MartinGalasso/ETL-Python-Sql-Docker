import csv


with open('./dataset/arbolado-en-espacios-verdes.csv', 'r', encoding='utf-8') as dataset:
    titulos = dataset.readline().split(',')
    
    #QUITAMOS EL /n creado con esta funcion.
    titulos[-1] = titulos[-1].rstrip('\n')
    
    id_arbol_index = titulos.index('id_arbol')
    long_index = titulos.index('long')
    lat_index = titulos.index('lat')
    altura_tot_index = titulos.index('altura_tot')
    diametro_index = titulos.index('diametro')
    inclinacio_index = titulos.index('inclinacio')
    id_especie_index = titulos.index('id_especie')
    nombre_com_index = titulos.index('nombre_com')
    nombre_cie_index = titulos.index('nombre_cie')
    tipo_folla_index = titulos.index('tipo_folla')
    espacio_ve_index = titulos.index('espacio_ve')
    ubicacion_index = titulos.index('ubicacion')
    nombre_fam_index= titulos.index('nombre_fam')
    nombre_gen_index= titulos.index('nombre_gen')
    origen_index= titulos.index('origen')
    coord_x_index= titulos.index('coord_x')
    coord_y_index = titulos.index('coord_y')
    
    with open('./dataset/coordenadas.csv', 'w') as coordenadas:
        coordenadas.write('long, lat, coord_x, coord_y\n')
        
        for linea in dataset:
            datos = linea.split(',')
            long = datos[long_index]
            lat = datos[lat_index]
            coord_x = datos[coord_x_index]
            coord_y = datos[coord_y_index]
            coordenadas.write(long + ',' + lat + ',' + coord_x + ',' + coord_y + '\n')
            
    
    with open('./dataset/caracteristicas.csv', 'w') as caracteristicas:
        caracteristicas.write('tipo_folla\n')
        
        for linea in dataset:
            datos = linea.split(',')
            tipo_folla = datos[tipo_folla_index]
            caracteristicas.write(tipo_folla + '\n')

