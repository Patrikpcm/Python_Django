CREATE TABLE IF NOT EXISTS clientes(
    id_cliente INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    sobrenome VARCHAR (100)
);

INSERT INTO clientes VALUES (null, 'Maria', 'Celina'),
                            (null, 'João', 'Silva'),
                            (null, 'Carla', 'Carvalho');


/*
Compras da Maria
    -notebook samsumg boot, qtd:1, preco:3000
    -Smart TV LED 32" HD, qtd:1, preco: 2499
*/


CREATE TABLE IF NOT EXISTS pedidos(
    id_pedido INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT UNSIGNED NOT NULL,
    data_pedido DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    produto VARCHAR (200),
    quantidade INT UNSIGNED NOT NULL,
    preco DECIMAL(15,2),
    CONSTRAINT clientes_id_cliente_fk
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

INSERT INTO pedidos VALUES  (null, 1, DEFAULT, 'Notebook Samsung Book', 2, 6000),
                            (null, 1, DEFAULT, 'Smart TV LED 32" HD', 1, 2499);

INSERT INTO pedidos VALUES  (null, 2, DEFAULT, 'Smart TV LED 32" HD', 1, 2499);