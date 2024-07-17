CREATE DATABASE facebook;
CREATE DATABASE facebook2;
-- utilizar "-- " com um espaço no final habilita a realizar comentários de 1 linha
/*Comentário de várias linhas*/

DROP DATABASE facebook2; -- removendo base

USE facebook; -- utilizando base facebook para criar as tabelas

CREATE TABLE usuarios(
                        nome VARCHAR(30),
                        email VARCHAR(30),
                        senha VARCHAR(10)
                     );

CREATE TABLE postagem_usuarios(
                                 nome VARCHAR(30),
                                 id INT,
                                 postagem VARCHAR(500)
                              );

DESCRIBE usuarios; -- descreve informações sobre a tabela 

DROP TABLE postagem_usuarios; -- removendo tabela