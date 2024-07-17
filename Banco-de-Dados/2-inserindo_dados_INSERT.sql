INSERT INTO usuarios (nome, email, senha) 
            VALUES('PATRIK', 'patrik@patrik', 'sargjj');

INSERT INTO usuarios (nome, email, senha) 
            VALUES('LUIZ', 'luiz@patrik', 'jjsarg');

INSERT INTO usuarios (nome, email, senha) 
            VALUES('GOGOLA', 'gogola@patrik', 'asdv kiie');

SELECT * FROM facebook.usuarios; -- selecionando todas as colunas da usuarios na base facebook
SELECT nome FROM facebook.usuarios; -- Selecionando apenas os nomes dos usuarios em facebook

TRUNCATE TABLE usuarios; -- diferente do DROP que remove a tabela, o TRUNCATE apenas limpa os dados da tabela