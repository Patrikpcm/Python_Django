CREATE TABLE pessoas(
            numero TINYINT
                    );
INSERT INTO pessoas(numero) VALUES (12);
INSERT INTO pessoas(numero) VALUES (-128);
-- INSERT INTO pessoas(numero) VALUES (128); -- apresenta erro de Out of Range

DROP TABLE pessoas;
CREATE TABLE pessoas(
            numero SMALLINT
                    );

INSERT INTO pessoas(numero) VALUES (5000);
INSERT INTO pessoas(numero) VALUES (-32128);
--INSERT INTO pessoas(numero) VALUES (32800); -- apresenta erro de Out of Range

DROP TABLE pessoas;
CREATE TABLE pessoas(
            numero FLOAT
                    );

INSERT INTO pessoas (numero) VALUES(123.45); -- o valor é com "."

DROP TABLE pessoas;
CREATE TABLE pessoas(
            numero DECIMAL(10,4) -- 10 valores com 4 casas decimais
                    );

INSERT INTO pessoas (numero) VALUES(123456.7890); -- 10 valores com 4 casas decimais

DROP TABLE pessoas;
CREATE TABLE pessoas(
                    texto TINYTEXT
                    );

INSERT INTO pessoas (texto) VALUES('teste');

/*Para demais tipos de dados é só seguir exemplificando dessa forma feita até agora.*/