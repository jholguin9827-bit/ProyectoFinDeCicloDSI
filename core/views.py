from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Docente, Periodo, Curso, Inscripcion
from .forms import EstudianteForm, DocenteForm, PeriodoForm, CursoForm, InscripcionForm

# ===============================
# CRUD ESTUDIANTES
# ===============================
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'core/estudiante_list.html', {'estudiantes': estudiantes})

def crear_estudiante(request):
    form = EstudianteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('estudiante')
    return render(request, 'core/estudiante_form.html', {'form': form, 'estudiante': None})

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, estudiante_id=pk)
    form = EstudianteForm(request.POST or None, instance=estudiante)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('estudiante')
    return render(request, 'core/estudiante_form.html', {'form': form, 'estudiante': estudiante})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, estudiante_id=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiante')
    return render(request, 'core/estudiante_confirm_delete.html', {'estudiante': estudiante})

# ===============================
# CRUD DOCENTES
# ===============================
def docente_list(request):
    docentes = Docente.objects.all()
    return render(request, 'core/docente_list.html', {'docentes': docentes})

def crear_docente(request):
    form = DocenteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('docente')
    return render(request, 'core/docente_form.html', {'form': form, 'docente': None})

def editar_docente(request, pk):
    docente = get_object_or_404(Docente, docente_id=pk)
    form = DocenteForm(request.POST or None, instance=docente)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('docente')
    return render(request, 'core/docente_form.html', {'form': form, 'docente': docente})

def eliminar_docente(request, pk):
    docente = get_object_or_404(Docente, docente_id=pk)
    if request.method == 'POST':
        docente.delete()
        return redirect('docente')
    return render(request, 'core/docente_confirm_delete.html', {'docente': docente})

# ===============================
# CRUD PERIODOS
# ===============================
def periodo_list(request):
    periodos = Periodo.objects.all()
    return render(request, 'core/periodo_list.html', {'periodos': periodos})

def crear_periodo(request):
    form = PeriodoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('periodo')
    return render(request, 'core/periodo_form.html', {'form': form, 'periodo': None})

def editar_periodo(request, pk):
    periodo = get_object_or_404(Periodo, periodo_id=pk)
    form = PeriodoForm(request.POST or None, instance=periodo)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('periodo')
    return render(request, 'core/periodo_form.html', {'form': form, 'periodo': periodo})

def eliminar_periodo(request, pk):
    periodo = get_object_or_404(Periodo, periodo_id=pk)
    if request.method == 'POST':
        periodo.delete()
        return redirect('periodo')
    return render(request, 'core/periodo_confirm_delete.html', {'periodo': periodo})

# ===============================
# CRUD CURSOS
# ===============================
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'core/curso_list.html', {'cursos': cursos})

def crear_curso(request):
    form = CursoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('curso')
    return render(request, 'core/curso_form.html', {'form': form, 'curso': None})

def editar_curso(request, pk):
    curso = get_object_or_404(Curso, curso_id=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('curso')
    return render(request, 'core/curso_form.html', {'form': form, 'curso': curso})

def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, curso_id=pk)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso')
    return render(request, 'core/curso_confirm_delete.html', {'curso': curso})

# ===============================
# CRUD INSCRIPCIONES
# ===============================
def inscripcion_list(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'core/inscripcion_list.html', {'inscripciones': inscripciones})

def crear_inscripcion(request):
    form = InscripcionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inscripcion')
    return render(request, 'core/inscripcion_form.html', {'form': form, 'inscripcion': None})

def editar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, inscripcion_id=pk)
    form = InscripcionForm(request.POST or None, instance=inscripcion)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('inscripcion')
    return render(request, 'core/inscripcion_form.html', {'form': form, 'inscripcion': inscripcion})

def eliminar_inscripcion(request, pk):
    inscripcion = get_object_or_404(Inscripcion, inscripcion_id=pk)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('inscripcion')
    return render(request, 'core/inscripcion_confirm_delete.html', {'inscripcion': inscripcion})

# ===============================
# INICIO
# ===============================
def inicio(request):
    return render(request, 'core/inicio.html')
