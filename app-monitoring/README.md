# Cargo Express - Sistema de Monitoreo de Pedidos

## Descripción

Este sistema permite monitorear las entregas de pedidos de **Cargo Express** en tiempo cercano al real. La aplicación proporciona métricas clave sobre los repartidores y los productos, y está protegida mediante autenticación JWT (JSON Web Token).

### Funcionalidades:

- **Autenticación JWT** para asegurar el acceso.
- Métricas en tiempo cercano al real:
  - **Cantidad de entregas por hora por repartidor**.
  - **Productos más vendidos**.
  - **Tiempo promedio de entrega por repartidor**.
  
## Tecnologías Utilizadas

- **Flask** (Python 3.12)
- **Flask-JWT-Extended** para autenticación con JWT.
- **SQLAlchemy** y **Flask-Migrate** para manejo de base de datos.
- **PostgreSQL** como base de datos.
- **Docker** y **Docker Compose** para contenedores.
- Arquitectura modular con Blueprints para organización del código.

## Requisitos

### Software Necesario:

- **Python 3.12**
- **PostgreSQL**
- **Docker** (opcional, recomendado para entornos de producción)
- **pip** (manejador de paquetes de Python)






## Ejecución de la Aplicación

### Opción 1: Usando Docker

1. **Construir y ejecutar los contenedores:**

   Si deseas utilizar Docker para una configuración más rápida y consistente, sigue estos pasos para levantar la aplicación y la base de datos en contenedores:

   ```bash
   docker-compose up --build