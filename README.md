# CRUD de productos con SQLAlchemy

Aplicación de consola en Python para administrar productos mediante las operaciones CRUD usando SQLAlchemy 2.x y SQLite.

## Modelo Product
- `id`: entero, clave primaria.
- `name`: texto obligatorio.
- `price`: número decimal obligatorio.
- `stock`: entero, valor predeterminado 0.

## Requisitos
- Python 3.10 o superior.
- Visual Studio Code (opcional, recomendado).

## Instalación y ejecución
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python main.py
```

La base `products.db` se crea automáticamente al iniciar.

## Operaciones
1. CREATE: registrar producto.
2. READ: listar todos o consultar por ID.
3. UPDATE: modificar nombre, precio o stock (Enter conserva el valor).
4. DELETE: eliminar por ID.

## Evidencias para el informe
Ejecuta la aplicación y toma capturas reales de:
- menú inicial,
- creación de un producto,
- listado/búsqueda,
- actualización,
- eliminación y listado final.

No se incluyen capturas simuladas: deben tomarse de la ejecución local para demostrar el funcionamiento real.
