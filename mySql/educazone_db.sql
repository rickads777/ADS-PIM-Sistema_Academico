DROP DATABASE IF EXISTS dbEducaZone;
CREATE DATABASE dbEducaZone;
USE dbEducaZone;

CREATE TABLE Admin (
	idAdmin INT NOT NULL AUTO_INCREMENT,
    nome varchar(50),
    senha varchar(50),
    usuario varchar(50),
    email varchar(50),
    PRIMARY KEY (idAdmin)
);

CREATE TABLE Professor(
	idProfessor INT NOT NULL AUTO_INCREMENT,
    nome varchar(50),
    usuario varchar(50),
    senha varchar(50),
    email varchar(50),
    PRIMARY KEY (idProfessor)
);

CREATE TABLE Turma(
	idTurma INT NOT NULL AUTO_INCREMENT,
    idProfessor INT NOT NULL,
    nome varchar(50),
    periodo varchar(50),
    anoLetivo int,
    PRIMARY KEY (idTurma),
    FOREIGN KEY(idProfessor) REFERENCES Professor(idProfessor)
);
CREATE TABLE Professor_Turma(
    idProfessor int,
    idTurma int,
    FOREIGN KEY(idProfessor) REFERENCES Professor(idProfessor),
    FOREIGN KEY(idTurma) REFERENCES Turma(idTurma)
    
);
CREATE TABLE Aluno(
	idAluno INT NOT NULL AUTO_INCREMENT,
    idTurma INT NOT NULL,
    nome varchar(50),
    usuario varchar(50),
    senha varchar(50),
    email varchar(50),
    PRIMARY KEY (idAluno),
    FOREIGN KEY(idTurma) REFERENCES Turma(idTurma)
);
CREATE TABLE Materia(
	idMateria INT NOT NULL AUTO_INCREMENT,
    nome varchar(30),
    PRIMARY KEY (idMateria)
);
CREATE TABLE Aula(
	idAula INT NOT NULL AUTO_INCREMENT,
    idProfessor int,
    idMateria int,
    idTurma int,
    nomeAula varchar(30),
    PRIMARY KEY (idAula),
    FOREIGN KEY(idProfessor) REFERENCES Professor(idProfessor),
    FOREIGN KEY(idMateria) REFERENCES Materia(idMateria),
    FOREIGN KEY(idTurma) REFERENCES Turma(idTurma)

);

CREATE TABLE Professor_Materia(
    idProfessor int,
    idMateria int,
    FOREIGN KEY(idProfessor) REFERENCES Professor(idProfessor),
    FOREIGN KEY(idMateria) REFERENCES Materia(idMateria)
    
);
CREATE TABLE Atividade(
	idAtividade INT NOT NULL AUTO_INCREMENT,
    idProfessor INT,
    idMateria INT,
    nomeMateria varchar(30),
    PRIMARY KEY (idAtividade),
    FOREIGN KEY(idProfessor) REFERENCES Professor(idProfessor),
    FOREIGN KEY(idMateria) REFERENCES Materia(idMateria)
    
);
CREATE TABLE Aluno_Atividade(
    idAluno_Atividade INT NOT NULL AUTO_INCREMENT,
    idAluno INT,
    idAtividade INT,
    Nota int,
    PRIMARY KEY (idAluno_Atividade),
    FOREIGN KEY(idAluno) REFERENCES Aluno(idAluno),
    FOREIGN KEY(idAtividade) REFERENCES Atividade(idAtividade)
);

insert into Admin (nome, usuario, email, senha) values ("Cadastro0","admin","email@email.com", "admin"); 
insert into Professor (nome, usuario, email, senha) values ("Sr.Teste","P1","email@email.com", "prof"); 
insert into Turma (idprofessor,nome, periodo, anoletivo) values (1,"A","Tarde",2025); 
insert into Materia (nome) values ("Ciência"); 
insert into Professor_Materia (idProfessor, idmateria) values (1,1);
insert into Materia (nome) values ("Ciências  Humanas"); 
insert into Professor_Materia (idProfessor, idmateria) values (1,2);
select * from Professor as p inner join Professor_materia as mp on p.idprofessor = mp.idprofessor inner join materia as m on m.idmateria = mp.idmateria;
select m.nome from Materia as m inner join professor_materia as mp on m.idmateria = mp.idmateria inner join professor as p on p.idprofessor = mp.idprofessor where p.idprofessor = 1;

select * from professor_materia;
select * from aluno;

INSERT INTO Materia (nome) VALUES
('Matemática'),
('Português'),
('História'),
('Geografia'),
('Física'),
('Química'),
('Biologia'),
('Educação Física'),
('Inglês');

INSERT INTO Materia (nome) VALUES
('Artes'),
('Filosofia'),
('Sociologia'),
('Tecnologia da Informação'),
('Programação'),
('Robótica'),
('Música'),
('Literatura'),
('Empreendedorismo'),
('Educação Financeira');

