DROP DATABASE IF EXISTS dbEducaZone;
CREATE DATABASE dbEducaZone;
USE dbEducaZone;

CREATE TABLE Admin (
	idAdmin INT NOT NULL AUTO_INCREMENT,
    nome varchar(50),
    senha varchar(50),
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
    nomeTurma varchar(50),
    período varchar(50),
    anoLetivo datetime,
    email varchar(50),
    PRIMARY KEY (idTurma)
);
CREATE TABLE Aluno(
	idAluno INT NOT NULL AUTO_INCREMENT,
    idTurma INT NOT NULL,
    nome varchar(50),
    usuario varchar(50),
    senha varchar(50),
    email varchar(50),
    PRIMARY KEY (idAluno),
    FOREIGN KEY(idAluno) REFERENCES Turma(idTurma)
);
CREATE TABLE Materia(
	idMateria INT NOT NULL AUTO_INCREMENT,
    nomeMateria varchar(30),
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
)