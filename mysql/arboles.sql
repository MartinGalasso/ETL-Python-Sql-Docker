use arboles

CREATE TABLE if not exists infoArbol (
    id_arbol int not null AUTO_INCREMENT,
    altura_tot int NOT NULL,
    diametro int NOT NULL,
    inclinacio int NOT NULL,
    PRIMARY KEY (id_arbol)
);

CREATE TABLE if not exists Coordenadas (
    id_arbol int NOT NULL AUTO_INCREMENT,
    `long` int NOT NULL,
    lat int NOT NULL,
    coord_x float NOT NULL,
    coord_y float NOT NULL,
    FOREIGN KEY (id_arbol) REFERENCES infoArbol(id_arbol)
);

CREATE TABLE if not exists espacioVerde (
    espacio_ve varchar(100),
    ubication varchar(200)
);

CREATE TABLE if not exists origenArbol (
    nombre_fam varchar(100),
    nombre_gen varchar(100)
);

CREATE TABLE if not exists infoEspecie (
    id_especie int NOT NULL,
    nombre_comp varchar(100),
    nombre_cie varchar(100)

);

CREATE TABLE if not exists Caracteristicas (
    tipo_folla varchar(200)

);
    


