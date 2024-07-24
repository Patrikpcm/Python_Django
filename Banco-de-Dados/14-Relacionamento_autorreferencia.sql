/*Esse exemplo utiliza as informações do exemplo 13-Relacionamento muitos para muitos.*/
ALTER TABLE clientes ADD COLUMN id_cliente_indicacao INT UNSIGNED;

INSERT INTO clientes VALUES (null, 'Patrik', 'Gogola',1); -- indicado pelo cliente de id 1

SELECT c.nome, c.sobrenome, c2.nome nome_indicacao
FROM clientes c LEFT JOIN clientes c2
ON c.id_cliente_indicacao = c2.id_cliente; 

UPDATE clientes SET id_indicacao = 1 WHERE id_clientes = 3;