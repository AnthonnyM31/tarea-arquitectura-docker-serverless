# Comparativa de Arquitecturas (Docker vs Serverless)

## 1. Introducción
Este proyecto implementa un servicio simple de saludo bajo dos paradigmas diferentes:
* **Microservicio containerizado** con Docker.
* **Función Serverless** con Serverless Framework.

## 2. Fase 1 y 2: Microservicio con Docker
Se desarrolló una API en Python (Flask) y se containerizó.
* **Imagen en Docker Hub:** hub.docker.com/r/anthonnym31/mi-api-docker
* **Comando para ejecutarlo:** `docker pull anthonnym31/mi-api-docker:v1`

## 3. Fase 3: Serverless
Se implementó la misma lógica como una función FaaS.
* **Framework:** Serverless Framework V4.
* **Proveedor:** AWS (Simulado localmente).
* **Ventaja observada:** Reducción drástica en la configuración de servidores y dependencias del sistema operativo.

## 4. Respuestas a la Tarea
* **¿Qué fue más rápido de implementar?** Serverless, debido a que permite enfocarse 100% en la lógica de negocio sin gestionar el entorno de ejecución.
* **Complejidades:** En Docker, la gestión de autenticación y permisos de red. En Serverless, la dependencia de herramientas de terceros y sus flujos de login.
* **Recomendación para alto tráfico:** **Serverless**, por su capacidad de escalado horizontal automático e instantáneo sin gestión de clústeres.
