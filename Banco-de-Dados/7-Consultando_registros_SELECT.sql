CREATE TABLE vendas(
    usuario VARCHAR(30),
    produto VARCHAR(100),
    preco DECIMAL(15,2),
    quantidade int,
    categoria VARCHAR(60)
);

INSERT INTO /*vendas (usuario, produto, preco, quantidade, categoria)*/
            -- como estou inserindo em ordem, posso apenas chamar vendas
            vendas
    VALUES  ('ana.silva','Notebook HP', 1200.00, 1, 'eletronicos'), 
            ('marcos.almeida', 'Iphone', 3400.00, 3, 'eletronicos' ),
            ('julio.caracol', 'Guarda roupa 3 portas', 3400.00, 1, 'moveis'),
            ('ana.silva', 'Ar condicionado', 3400.00, 2, 'eletronicos'),
            ('sasilva.nascibrina', 'TV 32 polegadas', 3800.00, 5, 'eletronicos'),
            ('emergola.goson', 'Fonte 800W', 400.00, 1, 'eletronicos');

/*Selecionando todas as colunas de uma tabela*/
SELECT * FROM vendas;

/*Selecionando todas as colunas com uma condição de IGUALDADE*/
SELECT * FROM vendas WHERE usuario = 'ana.silva';
SELECT produto FROM vendas WHERE usuario = 'ana.silva';

/*Selecionando todas as colunas com uma condição de DIFERENTE*/
SELECT * FROM vendas WHERE usuario <> 'ana.silva';

/*Selecionando todas as colunas com uma condição de MENOR*/
SELECT * FROM vendas WHERE preco < 1500.00;

/*Selecionando todas as colunas com uma condição de MAIOR*/
SELECT * FROM vendas WHERE preco > 1500.00;

/*Selecionando todas as colunas com uma condição de MAIOR/IGUAL*/
SELECT * FROM vendas WHERE preco <=0 1200.00;

/*Selecionando todas as colunas com uma condição de MENOR/IGUAL*/
SELECT * FROM vendas WHERE preco >=0 1200.00;

/*Selecionando MAIS DE UMA CONDIÇÃO - AND e OR*/
/*AND retorna a consulta se AMBAS as condições forem VERDADEIRAS*/
SELECT * FROM vendas WHERE preco >= 1200.00 AND usuario = 'ana.silva';

/*OR retorna a consulta se PELO MENOS UMA das condições for VERDADEIRA*/
SELECT * FROM vendas WHERE preco >= 2200.00 OR usuario = 'ana.silva';

/*Selecionando dados com BETWEEN (entre)*/
SELECT * FROM vendas WHERE preco BETWEEN 1200 AND 2000;

/*IN e NOT IN*/
SELECT * FROM vendas WHERE categoria = 'moveis' OR 'eletronicos';
SELECT * FROM vendas WHERE categoria IN('moveis', 'eletronicos');
SELECT * FROM vendas WHERE categoria NOT IN('moveis', 'eletronicos');

/*PALAVRA CHAVE - LIKE*/
SELECT * FROM vendas WHERE produto LIKE'not%';
SELECT * FROM vendas WHERE produto LIKE'%dici%';

/*Ordenação com ORDER BY e LIMIT*/
SELECT * FROM vendas WHERE categoria = 'eletronicos' ORDER BY preco;
-- ASC -> ascendente A..Z 0...9
-- DESC -> descendente
SELECT * FROM vendas WHERE categoria = 'eletronicos' ORDER BY preco ASC;
SELECT * FROM vendas WHERE categoria = 'eletronicos' ORDER BY preco DESC;
-- LIMIT -> limita a quantidade de itens
SELECT * FROM vendas WHERE categoria = 'eletronicos' ORDER BY preco DESC LIMIT 2;

/*Consultas com agragação - SUM, MAX, MIN*/
/*Exemplo de como utilizar um ALIAS (Apelido)*/
SELECT produto AS p, preco, quantidade AS qtd FROM vendas;
SELECT produto, preco, quantidade, (preco * quantidade) AS Total FROM vendas;

ALTER TABLE vendas ADD COLUMN total decimal (15,2); -- adicionando a coluna total
UPDATE vendas SET total = preco * quantidade; -- atualizando o valor para a coluna

SELECT SUM(total) AS total_vendas FROM vendas; -- Selecionando o valor total de todas as vendas
SELECT MAX(total) AS maior_valor FROM vendas; -- selecionando o maior valor de venda
SELECT MIN(total) AS menor_valor FROM vendas;  -- selecionando o menor valor de venda

/*GROUP BY - agrupando informações*/
SELECT usuario, SUM(total) AS total_vendas FROM vendas GROUP BY usuario; -- agrupando o total de vendas por usuário

