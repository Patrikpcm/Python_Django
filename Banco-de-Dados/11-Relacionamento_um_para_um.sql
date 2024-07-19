/*
Relação 1 para 1:   1 Funcionário tem somente 1 Cargo e recebe apenas 1 salário. 
                    Relação 1 para 1 entre 3 tabelas.
*/

CREATE TABLE funcionarios(
    id_funcionario INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30),
    sobrenome VARCHAR(30) 
);

INSERT INTO funcionarios VALUES (null, 'Maria', 'Almeida'),
                                (null, 'João', 'Silva'),
                                (null, 'Carla', 'Carvalho'),
                                (null, 'Pedro', 'Silverio'),
                                (null, 'Ana', 'Carla');


CREATE TABLE IF NOT EXISTS cargos(
    id_cargo INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50),
    salario DECIMAL(15,2)
);

INSERT INTO cargos VALUES   (null, 'CEO', 30000.00),
                            (null, 'Diretor', 20000.00),
                            (null, 'Gerente', 15000.00),
                            (null, 'Programador', 10000.00),
                            (null, 'Auxiliar Administrativo', 5000.00);


CREATE TABLE salarios(
    id_salario INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_funcionario INT UNSIGNED NOT NULL UNIQUE KEY,
    id_cargo INT UNSIGNED NOT NULL,
    CONSTRAINT funcionarios_id_funcionario_fk
    FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id_funcionario),
    CONSTRAINT cargos_id_cargo_fk
    FOREIGN KEY (id_cargo) REFERENCES cargos(id_cargo)
);

INSERT INTO salarios VALUES (NULL, 5, 1); -- Ana Carla, CEO
INSERT INTO salarios VALUES (NULL, 1, 2); -- Maria Almeida, Diretor
INSERT INTO salarios VALUES (NULL, 2, 4); -- João, Programador
INSERT INTO salarios VALUES (NULL, 3, 4); -- Carla, Programador
INSERT INTO salarios VALUES (NULL, 4, 5); -- Pedro, Auxiliar