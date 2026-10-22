# Banner studio en marimo

Abre una terminal en esta carpeta y ejecuta:

```sh
uv run --with marimo --with pillow --with anywidget marimo run banner_studio.py
```

Esto abre la interfaz de widgets en el navegador, con los controles a la izquierda y la vista previa a la derecha. Mantén la terminal abierta mientras la usas.

Si además quieres editar las celdas de Python:

```sh
uv run --with marimo --with pillow --with anywidget marimo edit banner_studio.py
```

- **Textos**: edita nombre, descripción, tecnologías e iniciales.
- **Colores**: abre el selector visual de cada color o introduce un valor hex como `#d66c39`.
- **Diseño**: usa los deslizadores para tamaño, puntos, esfera y duración.
- Activa **Reproducir animación** para ver el movimiento; mientras está activo, cada cambio vuelve a generar la vista previa animada y puede tardar unos segundos.
- La vista previa reacciona a los controles; el deslizador de posición muestra distintos fotogramas.
- **Generar y guardar** crea el GIF completo, el PNG y `banner-settings.json` junto al notebook.
- Para conservar ajustes entre sesiones, pulsa el botón de guardar antes de cerrar.
- Puedes editar la celda `draw_banner` para modificar la composición con Python.
- Los textos largos pueden desbordar el diseño de 1200 × 600; revisa la vista previa.
- El README ya apunta a `./seukod-banner.gif`; sube el GIF y el README juntos.
