# seukod Banner Studio

Editor de banners animados para el perfil de GitHub de seukod, hecho con marimo y Pillow.

## Abrir la app

Desde esta carpeta:

```sh
uv run marimo run banner_studio.py
```

Se abre en el navegador. Mantén la terminal abierta mientras usas la app.

Para editar también las celdas Python:

```sh
uv run marimo edit banner_studio.py
```

uv instala las dependencias declaradas en pyproject.toml. La primera ejecución puede necesitar Internet.

## Uso

1. Cambia los widgets de Textos, Colores y Diseño.
2. La vista previa refleja los cambios; activa el interruptor para reproducir la animación.
3. Pulsa **Generar y guardar** para exportar el GIF, el PNG y tus ajustes.
4. Los ajustes guardados se cargan la próxima vez que abras la app.

## Archivos

- `banner_studio.py`: notebook y app de marimo; modifica la función `draw_banner` para cambiar la composición.
- `banner-settings.json`: textos, colores y parámetros guardados.
- `seukod-banner.gif`: banner animado para GitHub.
- `seukod-banner.png`: vista estática.
- `PROFILE_README.md`: borrador del README del perfil, separado de este README del proyecto.
- `ESTADO.md`: estado y posibles siguientes pasos.

Para actualizar tu perfil, copia `PROFILE_README.md` como `README.md` al repositorio `seukod/seukod`, junto a `seukod-banner.gif`.
