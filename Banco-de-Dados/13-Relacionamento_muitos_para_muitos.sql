CREATE TABLE IF NOT EXISTS clientes(
    id_cliente INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    sobrenome VARCHAR (100)
);

INSERT INTO clientes VALUES (null, 'Maria', 'Celina'),
                            (null, 'João', 'Silva'),
                            (null, 'Carla', 'Carvalho');



CREATE TABLE IF NOT EXISTS pedidos(
    id_pedido INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT UNSIGNED NOT NULL,
    data_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    quantidade_itens INT UNSIGNED NOT NULL,
    total DECIMAL(15,2),
    CONSTRAINT clientes_id_cliente_fk
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

INSERT INTO pedidos VALUES  (null, 1, DEFAULT, 2, 6000),
                            (null, 2, DEFAULT, 1, 2499);


CREATE TABLE IF NOT EXISTS produtos(
    id_produto INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    preco DECIMAL(15,2),
    categoria VARCHAR(50),
    marca VARCHAR(50),
    foto VARCHAR (50)
);

INSERT INTO produtos VALUES (null, "Notebook Samsung Book", 3000, 'informática', 'Samsung', 'Foto1, foto2, foto3'),
                            (null, "Notebook Dell Inspiron i5", 3000, 'informática', 'Dell', 'Foto1, foto2, foto3'),
                            (null, "Smart TV LED 32 HD", 2499, 'eletrônico', 'AOC', 'Foto1, foto2, foto3');


CREATE TABLE IF NOT EXISTS pedidos_produtos(
    id_pedido INT UNSIGNED NOT NULL,
    id_produto INT UNSIGNED NOT NULL,
    quantidade INT NOT NULL,
    preco DECIMAL (15,2),
    CONSTRAINT pedidos_id_pedido_fk
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    CONSTRAINT produtos_ir_produto_fk
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto),
    PRIMARY KEY (id_pedido, id_produto)
);

INSERT INTO pedidos_produtos VALUES (1,1,1,3000), (1,2,1,2499);

SELECT * FROM pedidos JOIN pedidos_produtos USING (id_pedido);