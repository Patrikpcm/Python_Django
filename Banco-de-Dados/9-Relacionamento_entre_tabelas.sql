CREATE TABLE IF NOT EXISTS produtos( -- crie a tabela se ela não existir
    produto_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(100),
    descricao TEXT,
    preco DECIMAL(15,2),
    categoria VARCHAR(70),
    marca VARCHAR(70),
    foto VARCHAR(70),
    PRIMARY KEY(produto_id),
    UNIQUE KEY (titulo) 
);

CREATE TABLE pedidos(
    pedido_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, -- definindo a PK diretamente na declaração da coluna
    produto_id INT UNSIGNED NOT NULL,
    preco DECIMAL (15,2),
    quantidade SMALLINT,
    usuario VARCHAR (30),
    CONSTRAINT produtos_id_fk -- cria uma constraint(uma regra e dá um nome a mesma. Faz referência a tabela de produtos). Este nome é opcional, mas é uma boa prática faze-lo, caso não seja definido um nome aleatório será atribuído
    FOREIGN KEY (produto_id) REFERENCES produtos(pedido_id)
);

INSERT INTO pedidos VALUES(null, 2, 2199.90, 1, 'masil.varia'); -- o id do produto faz referência a um ID de produto na tabela produtos. Se tentarmos inserir um valor que não existe, o BD não permite.

DELETE FROM produtos WHERE id = 2; -- esse comando gerará um erro pois tenho um pedido associado a este produto na tabela de pedidos. Só posso deletar esse produto se eu excluir o pedido.
DELETE FROM pedidos WHERE id = 1; -- se executar esse pedido, posso excluir o produto.

/*JUNTANDO TABELAS*/
SELECT * FROM pedidos JOIN produtos.titulo USING(produto_id); -- juntando as duas tabelas com JOIN