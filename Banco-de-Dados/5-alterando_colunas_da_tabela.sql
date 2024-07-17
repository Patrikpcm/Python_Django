CREATE TABLE postagens(
    titulo VARCHAR(30) NOT NULL DEFAULT 'Titulo default',
    qtd_visualizacoes INT NOT NULL DEFAULT 0 -- Quando NOT NULL é definido, é necessário preencher um valor
                                             -- Entretanto, podemos definir um valor padrão usando DEFAULT
);

INSERT INTO postagens(titulo, qtd_visualizacoes) VALUES ("postagem 1", 1);

/*Alterar o nome de uma tabela*/
ALTER TABLE postagens RENAME TO postagens_blog;

/*Adicionar uma coluna*/
ALTER TABLE postagens_blog ADD COLUMN data_postagem DATETIME; -- insere no final da tabela 
-- posso incluir o atributo "FIRST" para a informação ficar na primeira linha da tabela ou
-- utilizar "AFTER titulo" para definir uma posição. 
-- Ex: ALTER TABLE postagens_blog ADD COLUMN data_postagem DATETIME FIRST;
-- Ex2: ALTER TABLE postagens_blog ADD COLUMN data_postagem DATETIME AFTER titulo;

/*Adicionando VARIAS colunas novas*/
ALTER TABLE postagens_blog  ADD COLUMN data_postagem_2 DATETIME,
                            ADD COLUMN usuario VARCHAR(120) FIRST;

/*Remover uma coluna*/                            
ALTER TABLE postagens_blog DROP COLUMN data_postagem_2;

/*Mudar o nome  e tipo de uma coluna*/
ALTER TABLE postagens_blog CHANGE COLUMN data_postagem dt_postagem DATE; -- algumas informações podem ser perdidas

/*Mudar apenas o tipo da coluna*/
ALTER TABLE postagens_blog MODIFY COLUMN dt_postagem DATETIME;  -- mudando de DATE para DATETIME novamente
                                                                -- também posso usar FIRST e AFTER




