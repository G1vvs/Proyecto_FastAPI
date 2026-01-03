# 🚀 API RESTful con Python, FastAPI y MongoDB

Este proyecto consiste en el desarrollo de una API REST robusta y escalable, diseñada para gestionar usuarios y recursos de manera segura. Integra autenticación moderna, conexión a bases de datos NoSQL y procesamiento de datos.

## 🛠️ Tecnologías y Librerías

El proyecto utiliza un stack moderno optimizado para rendimiento y seguridad:

- **Core:** `Python 3.12`, `FastAPI` (Standard).
- **Base de Datos:** `MongoDB` (Soporte para conexión Local y MongoDB Atlas).
- **Driver:** `Pymongo`.
- **Seguridad y Autenticación:**
  - `OAuth2` con Password Flow.
  - `Python-Jose` para generación y validación de **JWT** (JSON Web Tokens).
  - `Passlib` y `Bcrypt` para el hashing y validación segura de contraseñas.
- **Ciencia de Datos:** `Pandas` y `NumPy` integrados para manipulación y estructuración de datos en el backend.
- **Despliegue:** Configuración lista para producción en **Vercel**.

## ✨ Funcionalidades Principales

1. **Autenticación Segura (Auth):** Sistema de Login y Registro que emite tokens de acceso (JWT) para proteger endpoints privados.
2. **CRUD Completo:** Operaciones de Crear, Leer, Actualizar y Eliminar recursos en la base de datos MongoDB.
3. **Documentación Automática:** Gracias a Swagger UI y Redoc (nativas de FastAPI).
4. **Procesamiento de Datos:** Endpoints específicos que utilizan Pandas/Numpy para transformar estructuras de datos complejas.

## 🔧 Instalación y Uso Local

Sigue estos pasos para ejecutar el proyecto en tu máquina:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/G1vvs/Proyecto_FastAPI.git](https://github.com/G1vvs/Proyecto_FastAPI.git)
cd Proyecto_FastAPI