# 🚀 FastAPI Calculadora API

API construida con FastAPI que permite realizar operaciones básicas como suma, multiplicación y manejo de configuración simulada.

---

## 📌 Tecnologías usadas

* FastAPI
* Python 3.10+
* Pydantic
* Uvicorn

---

## 📂 Estructura del proyecto

```
app/
 ├── main.py
 ├── routers/
 ├── models/
```

---

## ⚙️ Instalación

```bash
git clone https://github.com/tu-usuario/fastapi-calculadora.git
cd fastapi-calculadora
pip install -r requirements.txt
```

---

## ▶️ Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

---

## 📖 Documentación automática

Accede a:

👉 http://127.0.0.1:8000/docs

---

## 📌 Endpoints

### ➕ Sumar

`GET /calculadora/sumar?a=5&b=10`

### ✖️ Multiplicar

`POST /calculadora/multiplicar`

Body:

```json
{
  "a": 5,
  "b": 10
}
```

### ⚙️ Actualizar Config

`PUT /calculadora/actualizar-config`

### 🔄 Reset

`DELETE /calculadora/reset`

---

## 🎯 Objetivo del proyecto

Practicar:

* Uso de FastAPI
* Routers
* Validación con Pydantic
* Estructura de proyecto backend

---

## 🚀 Autor

Gael Osbaldo Fernandez Garcia
