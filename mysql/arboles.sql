
use arboles;

CREATE TABLE if not exists infoArbol (
    id_arbol int not null AUTO_INCREMENT,
    alturaTotal int NOT NULL,
    diametro int NOT NULL,
    inclinacion int NOT NULL,
    PRIMARY KEY (id_arbol)
);

CREATE TABLE if not exists Coordenadas (
    id_arbol int NOT NULL AUTO_INCREMENT,
    long int NOT NULL,
    lat int NOT NULL,
    coord_x float NOT NULL,
    coord_y float NOT NULL,
    FOREIGN KEY (id_arbol) REFERENCES infoArbol(id_arbol)
);

CREATE TABLE IF NOT EXISTS 

