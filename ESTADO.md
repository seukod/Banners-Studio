# Estado al 22 de octubre de 2026

## Hecho

- Banner inspirado en la referencia: fondo claro con cuadrícula, nombre en puntos y esfera animada.
- Contenido adaptado a Unity, videojuegos, release operations, AcusPy, Basic Pitch y marimo.
- Widgets de texto, selectores visuales de color, deslizadores y vista previa estática o animada.
- Exportación a GIF y PNG y persistencia de ajustes en JSON.
- Corregida la reactividad de textos y deslizadores: usar `mo.ui.dictionary` y leer `controls.value`. El diseño debe insertar los elementos clonados de ese contenedor.
- Verificados el enrutamiento de eventos de los widgets, los cambios de texto, tamaño y color en el renderizado, y la exportación con esos valores.
- El proyecto funciona con archivos locales; no se ha publicado en GitHub.

## Para retomar

1. Ejecutar `uv run marimo edit banner_studio.py`.
2. Ajustar el diseño y contenido desde los widgets o la función `draw_banner`.
3. Revisar el aspecto en GitHub antes de publicar el README del perfil.

## Ideas pendientes (opcionales)

- Incorporar un avatar propio en lugar del monograma.
- Ajustar textos largos para evitar desbordamientos.
- Optimizar la velocidad de la vista previa animada.
- Revisar contraste y legibilidad en pantallas pequeñas.
- Añadir enlaces públicos de contacto si se desea.

Los archivos originales siguen en `/Users/sakura/Documents/Codex/2026-10-22/ten-a-2/outputs`.
