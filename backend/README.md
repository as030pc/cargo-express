



# Como usar este proyecto
Este proyecto es una aplicación de backend para la empresa de mensajería Cargo Express, desarrollada en Flask.

## Requisitos
- Docker
- Docker Compose

## Cómo usar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-repo/cargo_express.git
   cd cargo_express
2. Levanta los servicios de la aplicación y la base de datos:
- docker-compose up

3. Aplica las migraciones de la base de datos:
 - docker-compose exec web flask db upgrade

4. La aplicación estará disponible en http://localhost:8000.