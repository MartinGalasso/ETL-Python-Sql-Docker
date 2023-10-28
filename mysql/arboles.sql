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
    longitud int NOT NULL,
    latitud int NOT NULL,
    coordx float NOT NULL,
    coordy float NOT NULL,
    FOREIGN KEY (id_arbol) REFERENCES infoArbol(id_arbol)
);

