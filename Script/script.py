import csv

def extract_and_write_data(input_file, output_file, columns_to_extract):
    #Lee el archivo padre y crea los titulos de la columna
    with open(input_file, 'r', encoding='utf-8') as dataset:
        titulos = next(dataset).strip().split(',')

        #List comprehension, obtiene los nombres de las columnas.
        column_indices = [titulos.index(column) for column in columns_to_extract]

        #Prepara el archivo de salida
        with open(output_file, 'w', newline='', encoding='utf-8') as output:
            output_writer = csv.writer(output)
            output_writer.writerow(columns_to_extract)  # Escribe las cabeceras

            for linea in dataset:
                datos = linea.strip().split(',')
                output_writer.writerow([datos[i] for i in column_indices])

def main():
    #Archivo padre
    input_file = './dataset/arbolado-en-espacios-verdes.csv'
    
    
    #Extraer nombres de columnas y escribirlos en el archivo output designado.
    coordenadas_output = './dataset/coordenadas.csv'
    coordenadas_columns = ['long', 'lat', 'coord_x', 'coord_y']
    extract_and_write_data(input_file, coordenadas_output, coordenadas_columns)

    caracteristicas_output = './dataset/caracteristicas.csv'
    caracteristicas_columns = ['tipo_folla']
    extract_and_write_data(input_file, caracteristicas_output, caracteristicas_columns)
    
    infoarbol_output = './dataset/infoarbol.csv'
    infoarbol_columns = ['id_arbol', 'altura_tot', 'diametro', 'inclinacio']
    extract_and_write_data(input_file, infoarbol_output, infoarbol_columns)
    
    infoespecie_output = './dataset/infoespecie.csv'
    infoespecie_columns = ['id_especie', 'nombre_com', 'nombre_cie']
    extract_and_write_data(input_file, infoespecie_output, infoespecie_columns)
    
    origen_output = './dataset/origenarbol.csv'
    origen_columns = ['nombre_fam', 'nombre_gen', 'origen']
    extract_and_write_data(input_file, origen_output, origen_columns)
    
    espacioverde_output = './dataset/espacioverde.csv'
    espacioverde_columns = ['espacio_ve' , 'ubicacion']
    extract_and_write_data(input_file, espacioverde_output, espacioverde_columns)

if __name__ == "__main__":
    main()
