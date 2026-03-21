# ✅ Django CRUD Auth — Gestión de Tareas con Autenticación

Aplicación web de gestión de tareas construida con Django. Implementa un CRUD completo sobre un modelo `Tarea` con sistema de autenticación de usuarios, protección de rutas y registro/login personalizado.

Este repositorio documenta además el proceso de depuración y resolución de errores reales encontrados durante el desarrollo, incluyendo problemas de configuración, inconsistencias de modelo y corrección de templates.

---

## 🧱 Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend | Python 3 + Django |
| Base de datos | SQLite (ORM Django) |
| Frontend | HTML + Django Template Language (DTL) |
| Autenticación | `django.contrib.auth` |
| Gestión de entorno | `venv` |

---

## ⚙️ Funcionalidades

- ✅ Registro de usuarios (`sign_up`)
- ✅ Login / Logout con redirección configurada
- ✅ Listado de tareas por usuario autenticado
- ✅ Crear nueva tarea
- ✅ Ver detalle de tarea
- ✅ Marcar tarea como completada
- ✅ Eliminar tarea
- ✅ Listado de tareas completadas
- ✅ Protección de rutas con `@login_required`

---

## 🗂️ Estructura del proyecto

```
Django-CRUD-auth/
├── django_crud_auth/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tareas/
│   ├── models.py         ← Modelo Tarea con date_completed
│   ├── views.py          ← Lógica CRUD + autenticación
│   ├── urls.py
│   └── templates/
│       ├── base.html
│       ├── tareas.html
│       ├── create_tarea.html
│       ├── tarea_detail.html
│       ├── tareas_completed.html
│       ├── sign_up.html
│       └── registration/login.html
├── manage.py
├── requirements.txt
└── v.12-deploy.md        ← Log de debugging y resolución de errores
```

---

## 🚀 Instalación y uso local

### 1. Clonar el repositorio

```bash
git clone https://github.com/dvasquez-design/Django-CRUD-auth.git
cd Django-CRUD-auth
```

### 2. Crear y activar entorno virtual

```bash
python -m venv django-crud-auth

# Windows
.\django-crud-auth\Scripts\activate

# Linux / Mac
source django-crud-auth/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Acceder en: **http://127.0.0.1:8000**

> ⚠️ Usar el Python del entorno virtual, no el del sistema.

---

## 🔗 URLs disponibles

| URL | Descripción |
|---|---|
| `/` | Redirige a lista de tareas (requiere login) |
| `/signin/login/` | Inicio de sesión |
| `/signin/sign_up/` | Registro de nuevo usuario |
| `/tasks/` | Lista de tareas del usuario |
| `/tasks/create/` | Crear nueva tarea |
| `/tasks/<id>/` | Detalle de una tarea |
| `/tasks/<id>/complete/` | Marcar tarea como completada |
| `/tasks/<id>/delete/` | Eliminar tarea |
| `/tasks/completed/` | Historial de tareas completadas |

---

## 🐛 Debugging documentado

Este proyecto incluye [`v.12-deploy.md`](./v.12-deploy.md), un log técnico real con los problemas encontrados durante el desarrollo y sus soluciones:

| Problema | Solución aplicada |
|---|---|
| Entorno virtual no activado | Uso explícito del Python del venv |
| `DEBUG=False` rompía el servidor | Configuración correcta para entorno local |
| `LOGIN_URL` mal configurado | Corregido a `/signin/login/` |
| Import incorrecto de `timezone` | Reemplazado por `django.utils.timezone` |
| Rutas sin protección | Decoradores `@login_required` aplicados |
| Templates faltantes o con errores | Creación y corrección de todos los templates |
| Inconsistencia `data_completed` / `date_completed` | Resuelto con `db_column` en el modelo |

---

## 🔐 Configuración de autenticación

```python
LOGIN_URL = '/signin/login/'
LOGIN_REDIRECT_URL = '/tasks/'
LOGOUT_REDIRECT_URL = '/signin/login/'
```

---

## 📋 Comandos rápidos

```bash
python manage.py runserver        # levantar servidor
python manage.py migrate          # aplicar migraciones
python manage.py createsuperuser  # crear superusuario
python manage.py shell            # consola interactiva ORM
```

---

## 👤 Autor

**Diego Vásquez** — [@dvasquez-design](https://github.com/dvasquez-design)  
Desarrollador Fullstack en formación | Python · Django · Bootstrap

---

> Proyecto de práctica desarrollado durante bootcamp Alkemy — Módulo Django con autenticación.
