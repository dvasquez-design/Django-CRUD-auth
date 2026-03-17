# 🛠️ Debug y Estado del Proyecto Django CRUD Auth

## ✅ Estado actual

El proyecto está **funcional en entorno local** (`localhost:8000`).

* El servidor inicia correctamente
* Redirección al login funciona (`/signin/login/`)
* CRUD de tareas operativo
* Autenticación funcional

---

## 🔍 Problemas detectados y soluciones aplicadas

### 1) Uso incorrecto del entorno virtual

**Problema:**
Se ejecutaba Django con Python del sistema.

**Solución:**
Ejecutar con el Python del entorno virtual:

```ps1
.\django-crud-auth\Scripts\python.exe manage.py runserver
```

---

### 2) Configuración incorrecta en `settings.py`

**Problema:**

* `DEBUG=False`
* `ALLOWED_HOSTS=[]`

Esto rompía el servidor.

**Solución:**

* DEBUG habilitado en desarrollo
* Hosts permitidos para local

```python
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

---

### 3) LOGIN_URL mal configurado

**Problema:**
Ruta incorrecta (`/signin/`)

**Solución:**

```python
LOGIN_URL = '/signin/login/'
```

---

### 4) Problemas en `views.py`

#### a) timezone incorrecto

```python
# ❌ Incorrecto
from datetime import timezone

# ✅ Correcto
from django.utils import timezone
```

#### b) Falta de protección de rutas

Se agregaron decoradores:

```python
from django.contrib.auth.decorators import login_required
```

Aplicado en:

* create_tarea
* tarea_detail
* complete_tarea
* delete_tarea

---

### 5) Plantillas con errores y faltantes

**Problemas detectados:**

* Errores de sintaxis
* Templates inexistentes
* Login no renderizaba

**Solución:**
Se crearon/corrigieron:

* base.html
* tareas.html
* create_tarea.html
* tarea_detail.html
* tareas_completed.html
* sign_up.html
* registration/login.html

---

### 6) Inconsistencia en modelo

**Problema:**

* DB: `data_completed`
* Código: `date_completed`

**Solución:**

```python
date_completed = models.DateTimeField(null=True, blank=True, db_column='data_completed')
```

---

## 🧪 Pruebas realizadas

* curl a rutas:

  * `/`
  * `/signin/`
  * `/signin/login/`
* Confirmación de redirecciones correctas

---

## ⚠️ Pendiente

* Limpieza de archivos residuales
* Revisión de estructura

---


## 🧠 Notas finales

* No modificar estructura antes del deploy
* Mantener consistencia de nombres
* Evitar cambios grandes sin commit previo

---


