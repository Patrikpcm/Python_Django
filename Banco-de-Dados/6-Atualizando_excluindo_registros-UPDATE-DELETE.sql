/*Criando a tabela*/
CREATE TABLE usuarios(
    id INT,
    nome VARCHAR(30),
    email VARCHAR(30),
    senha VARCHAR(128)
);

/*Inserindo informações*/
INSERT INTO usuarios (nome, email, senha) 
            VALUES('PATRIK', 'patrik@patrik', 'sargjj');

INSERT INTO usuarios (nome, email, senha) 
            VALUES('LUIZ', 'luiz@patrik', 'jjsarg');

INSERT INTO usuarios (nome, email, senha) 
            VALUES('GOGOLA', 'gogola@patrik', 'asdv kiie');

INSERT INTO usuarios (nome, email, senha) 
            VALUES('JOBSON', 'joberval@patrik', 'asdv kiie');

INSERT INTO usuarios (nome, email, senha) 
            VALUES('GARGULA', 'gargula@patrik', 'asdv kiie');

/*DELETAR registros da tabela*/
DELETE FROM usuarios WHERE usuario.nome = 'JOBSON';

/*ATUALIZAR registros da tabela*/
UPDATE usuarios SET senha ='56789'; -- atualiza todos os registros para 56789
UPDATE usuarios SET nome = 'GEOVAN' WHERE usuario.nome = 'GARGULA'; -- atualiza só o nome de GARGULA

/*Criando nova coluna e definindo idades*/
ALTER TABLE usuarios ADD COLUMN idade TINYINT;

UPDATE usuarios SET usuarios.idade = 0;