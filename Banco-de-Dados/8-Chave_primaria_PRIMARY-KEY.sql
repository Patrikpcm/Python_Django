/*
Uma chave primária é uma coluna na tabela que torna cada registro único.
Isso significa que os dados na chave primária não podem ser repetidos.
PS: Também é possível criar uma chave primária composta. Ou seja, a
composição de 2 colunas não pode se repetir. Porém é raro de se usar.

-A PK não pode ser NULL
-Os valores da PK deve ser atribuída no momento em que o registro é inserido
-Os valores da PK não devem ser alterados
-a PK deve ser compacta
*/

/*Criando uma tabela com chave primária*/
CREATE TABLE produtos(
    pruduto_id INT UNSIGNED NOT NULL AUTO_INCREMENT, -- INT sem sinal e a AUTO_INCREMENT incrementa os valores automáticamente
    titulo VARCHAR(100),
    descricao TEXT,
    preco DECIMAL(15,2),
    categoria VARCHAR(70),
    marca VARCHAR(70),
    foto VARCHAR(70),
    PRIMARY KEY(produto_id),
    UNIQUE KEY (titulo) -- uma informação que não se repete ex: email, cpf, telefone, etc...
                        -- normalmente não é gerada de forma automática
);

INSERT INTO produtos VALUES (
    null, -- O valor nunca pode ser nulo, mas nesse caso a inserção do produto vai apenas ignorar o valor para não apresentar erro
    'Headphone Philips Wireless BT PRETO TAH1205BK/00',
    'Descrição longa...',
    94.34,
    'eletronicos',
    'philips',
    'foto1, foto2, foto3'
),
(
    null,
    'Câmera GoPro HERO9 Black - Standard Bunble com Cartão de Memória 64Gb Sandisk Extreme',
    'Descrição longa...',
    994.99,
    'cameras',
    'gopro',
    'foto1, foto2, foto3'
),
INSERT INTO produtos VALUES (
    null,
    'Console Nintendo Switch - Azul Neon e Vermelho Neon (Nacional)',
    'Descrição longa...',
    2199.90,
    'games',
    'nintendo',
    'foto1, foto2, foto3'
);