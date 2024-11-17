create database calculadora
default character set utf8
default collate utf8_general_ci;

create table users (
`id` int not null auto_increment,
`nome` varchar(20) not null,
`sobrenome` varchar(30) not null,
`municipio` varchar(50) not null,
`UF` char(2) not null,
`usuario` varchar(30) not null unique,
`senha` varchar(255) not null,
`email` varchar(100) unique,
`telefone` bigint(14) not null,
`termos` enum('S', 'N') not null,
primary key (id)
) default charset = utf8;

create table prazos (
    `id` int not null auto_increment,
    `nomeEvento` varchar(100) not null,
    `processo` varchar(100) not null,
    `evento` varchar(100) not null,
    `dataPubli` date not null,
    `prazoDias` varchar(10) not null default '8',
    `notificar` enum('S', 'N'),
    `dataFicto` date not null,
    `dataFinal` date not null,
    `user_id` int not null,
    primary key (id),
    foreign key (`user_id`) references users(`id`) on delete cascade on update cascade
) default charset = utf8;

create table feriados (
    id int not null auto_increment,
    feriado varchar(100) not null,
    dataFeriado date not null,
    primary key (id)
) default charset = utf8;


DELIMITER //

CREATE FUNCTION DiasUteis(dataInicial DATE, dias INT) RETURNS DATE
BEGIN
    DECLARE cont INT DEFAULT 0;
    DECLARE dataAtual DATE DEFAULT dataInicial;

    -- Loop até que a contagem de dias úteis atinja o prazo desejado
    WHILE cont < ABS(dias) DO
        -- Adiciona ou subtrai um dia conforme o valor de 'dias'
        SET dataAtual = DATE_ADD(dataAtual, INTERVAL IF(dias > 0, 1, -1) DAY);

        -- Verificar se o dia não é sábado ou domingo, e se não é feriado
        IF DAYOFWEEK(dataAtual) NOT IN (1, 7) AND NOT EXISTS (
            SELECT 1 FROM feriados WHERE dataFeriado = dataAtual
        ) THEN
            SET cont = cont + 1;
        END IF;
    END WHILE;

    RETURN dataAtual;
END //

DELIMITER ;

DELIMITER //

CREATE TRIGGER trg_calcular_prazos
BEFORE INSERT ON prazos
FOR EACH ROW
BEGIN
    DECLARE prazo INT;
    SET prazo = CAST(NEW.prazoDias AS UNSIGNED);  -- Convertendo o prazo para inteiro, caso esteja em string

    -- Calcula a data final desconsiderando finais de semana e feriados
    SET NEW.dataFinal = DiasUteis(NEW.dataPubli, prazo);

    -- Calcula a data ficta como dois dias úteis antes da data final
    SET NEW.dataFicto = DiasUteis(NEW.dataFinal, -2);
END //

DELIMITER ;

SELECT * FROM users;





