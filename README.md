## Academic Periods API
Devuelve la información de un periodo académico.

Ejemplo de respuesta:
```json
{
  "id": 1,
  "name": "Periodo Academico 2023",
  "year": "2023",
  "semester": 1,
  "startDate": "2023-01-15",
  "endDate": "2023-05-15"
}
```
## Instalación
Asegúrate de tener Python instalado. Luego, instala las dependencias con:

```bash
pip install fastapi
pip install uvicorn
```
## Ejecución
Para iniciar el servidor:
```bash
uvicorn main:app --reload
```

La aplicación estará disponible en http://127.0.0.1:8000/. 
 Puedes acceder a los siguientes endpoints:

- Obtener todos los periodos: http://127.0.0.1:8000/periods

- Obtener un periodo específico (por ejemplo, el periodo con ID 1): http://127.0.0.1:8000/period/1

- Crear un periodo: http://127.0.0.1:8000/period/
request body:
```json
{
  "name": "Periodo Academico 2023",
  "year": "2023",
  "semester": 1,
  "startDate": "2023-01-15",
  "endDate": "2023-05-15"
}
```
