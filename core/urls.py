from django.urls import path
from . import views

urlpatterns = [
    # ===============================
    # INICIO
    # ===============================
    path('', views.inicio, name='inicio'),

    # ===============================
    # ESTUDIANTES
    # ===============================
    path('estudiantes/', views.estudiante_list, name='estudiante'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    # ===============================
    # DOCENTES
    # ===============================
    path('docentes/', views.docente_list, name='docente'),
    path('docentes/crear/', views.crear_docente, name='crear_docente'),
    path('docentes/editar/<int:pk>/', views.editar_docente, name='editar_docente'),
    path('docentes/eliminar/<int:pk>/', views.eliminar_docente, name='eliminar_docente'),

    # ===============================
    # PERIODOS
    # ===============================
    path('periodos/', views.periodo_list, name='periodo'),
    path('periodos/crear/', views.crear_periodo, name='crear_periodo'),
    path('periodos/editar/<int:pk>/', views.editar_periodo, name='editar_periodo'),
    path('periodos/eliminar/<int:pk>/', views.eliminar_periodo, name='eliminar_periodo'),

    # ===============================
    # CURSOS
    # ===============================
    path('cursos/', views.curso_list, name='curso'),
    path('cursos/crear/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),

    # ===============================
    # INSCRIPCIONES
    # ===============================
    path('inscripciones/', views.inscripcion_list, name='inscripcion'),
    path('inscripciones/crear/', views.crear_inscripcion, name='crear_inscripcion'),
    path('inscripciones/editar/<int:pk>/', views.editar_inscripcion, name='editar_inscripcion'),
    path('inscripciones/eliminar/<int:pk>/', views.eliminar_inscripcion, name='eliminar_inscripcion'),
]
