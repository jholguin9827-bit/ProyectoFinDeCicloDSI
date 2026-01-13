CREATE TABLE estudiantes (
    estudiante_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    cedula VARCHAR(10) NOT NULL UNIQUE,
    correo VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE docentes (
    docente_id SERIAL PRIMARY KEY,
    cedula VARCHAR(10) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    titulo VARCHAR(100)
);

CREATE TABLE periodos (
    periodo_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    CHECK (fecha_inicio < fecha_fin)
);

CREATE TABLE cursos (
    curso_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    docente_id INT NOT NULL,
    periodo_id INT NOT NULL,

    CONSTRAINT fk_curso_docente
        FOREIGN KEY (docente_id)
        REFERENCES docentes(docente_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT fk_curso_periodo
        FOREIGN KEY (periodo_id)
        REFERENCES periodos(periodo_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE inscripciones (
    inscripcion_id SERIAL PRIMARY KEY,
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    fecha DATE NOT NULL DEFAULT CURRENT_DATE,

    CONSTRAINT fk_inscripcion_estudiante
        FOREIGN KEY (estudiante_id)
        REFERENCES estudiantes(estudiante_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_inscripcion_curso
        FOREIGN KEY (curso_id)
        REFERENCES cursos(curso_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT uq_estudiante_curso
        UNIQUE (estudiante_id, curso_id)
);
