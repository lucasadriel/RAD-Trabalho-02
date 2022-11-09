CREATE DATABASE BANCO;

use BANCO;

CREATE TABLE Pessoa(

cpf VARCHAR(14) NOT NULL,
primeiro_nome varchar(50),
nome_do_meio varchar(50),
sobrenome varchar(50),
idade int,
conta int,
id_pessoa int AUTO_INCREMENT,

PRIMARY KEY(id_pessoa)

);

CREATE TABLE Conta(

agencia VARCHAR(20) NOT NULL,
numero VARCHAR(20) NOT NULL,
saldo float,
gerente varchar(50),
titular int,
id_conta int AUTO_INCREMENT,

PRIMARY KEY(id_conta)

);


/*
alter table Pessoa add CONSTRAINT fk_conta FOREIGN KEY(conta) REFERENCES Conta (id_conta);
alter table Conta add CONSTRAINT fk_pessoa_titular FOREIGN KEY(titular) REFERENCES Pessoa (id_pessoa);
*/