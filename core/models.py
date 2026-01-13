from django.db import models

# -----------------------------
# ESTUDIANTE
# -----------------------------
class Estudiante(models.Model):
    estudiante_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(unique=True)

    class Meta:
        db_table = 'estudiantes'

    def __str__(self):
        return self.nombre


# -----------------------------
# DOCENTE
# -----------------------------
class Docente(models.Model):
    docente_id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = 'docentes'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# -----------------------------
# PERIODO
# -----------------------------
class Periodo(models.Model):
    periodo_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        db_table = 'periodos'

    def __str__(self):
        return self.nombre


# -----------------------------
# CURSO
# -----------------------------
class Curso(models.Model):
    curso_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.PROTECT, db_column='docente_id')
    periodo = models.ForeignKey(Periodo, on_delete=models.PROTECT, db_column='periodo_id')

    class Meta:
        db_table = 'cursos'

    def __str__(self):
        return self.nombre


# -----------------------------
# INSCRIPCION / MATRICULA
# -----------------------------
class Inscripcion(models.Model):
    inscripcion_id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, db_column='estudiante_id')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='curso_id')
    fecha = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'inscripciones'
        unique_together = ('estudiante', 'curso')

    def __str__(self):
        return f"{self.estudiante} - {self.curso}"
