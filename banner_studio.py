# /// script
# requires-python = ">=3.12"
# dependencies = ["marimo>=0.25.1,<1", "pillow>=11", "anywidget>=0.9", "traitlets>=5"]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="full")

@app.cell
def _():
    import marimo as mo
    import math
    import io
    import json
    import anywidget
    import traitlets
    from pathlib import Path
    from PIL import Image, ImageDraw, ImageFont, ImageColor
    return Image, ImageColor, ImageDraw, ImageFont, Path, anywidget, io, json, math, mo, traitlets

@app.cell
def _(anywidget, traitlets):
    class PalettePicker(anywidget.AnyWidget):
        """Native color pickers and hex fields, synchronized with marimo."""
        colors = traitlets.Dict().tag(sync=True)
        _esm = """
        export default {
          render({model, el}) {
            const labels = {background: 'Fondo', ink: 'Texto', muted: 'Texto secundario', accent: 'Acento', orb_color: 'Esfera'};
            const inputs = {};
            const sync = () => {
              const colors = model.get('colors');
              for (const [key, [picker, hex]] of Object.entries(inputs)) {
                picker.value = colors[key]; hex.value = colors[key];
              }
            };
            for (const [key, label] of Object.entries(labels)) {
              const row = document.createElement('label');
              row.style.cssText = 'display:flex;align-items:center;gap:12px;margin:14px 0;font:14px system-ui';
              const title = document.createElement('span'); title.textContent = label; title.style.flex = '1';
              const picker = document.createElement('input'); picker.type = 'color'; picker.setAttribute('aria-label', label);
              picker.style.cssText = 'width:48px;height:36px;border:0;padding:0;background:none;cursor:pointer';
              const hex = document.createElement('input'); hex.type = 'text'; hex.setAttribute('aria-label', label + ' hexadecimal');
              hex.style.cssText = 'width:90px;padding:6px;border:1px solid #bbb;border-radius:6px;background:transparent;color:inherit;font:13px monospace';
              const update = (value) => {
                model.set('colors', {...model.get('colors'), [key]: value}); model.save_changes();
              };
              picker.addEventListener('input', () => update(picker.value));
              hex.addEventListener('input', () => {
                const valid = /^#[0-9a-fA-F]{6}$/.test(hex.value);
                hex.setAttribute('aria-invalid', String(!valid));
                if (valid) update(hex.value);
              });
              inputs[key] = [picker, hex]; row.append(title, picker, hex); el.append(row);
            }
            sync(); model.on('change:colors', sync);
            return () => model.off('change:colors', sync);
          }
        };
        """
    return (PalettePicker,)

@app.cell
def _(Image, ImageColor, ImageDraw, ImageFont, math):
    def draw_banner(c, phase=0):
        W, H = 1200, 600
        FONT = '/System/Library/Fonts/Supplemental/'
        def get_font(size, bold=False):
            candidates = [
                c.get('font_path', ''),
                FONT + ('Courier New Bold.ttf' if bold else 'Courier New.ttf'),
                '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
                'C:/Windows/Fonts/consola.ttf',
            ]
            for candidate in candidates:
                if candidate:
                    try:
                        return ImageFont.truetype(candidate, size)
                    except OSError:
                        pass
            return ImageFont.load_default(size=size)
        def font(size, bold=False):
            return get_font(size, bold)

        ink = c['ink']
        muted = c['muted']
        orange = c['accent']
        def tint(hex_color, fraction):
            rgb = ImageColor.getrgb(hex_color)
            return tuple(round(v*(1-fraction)+255*fraction) for v in rgb)
        base = Image.new('RGB', (W, H), c['background'])
        d = ImageDraw.Draw(base)
        for x in range(0, W, 24):
            d.line((x, 0, x, H), fill=tint(c['ink'], .94))
        for y in range(0, H, 24):
            d.line((0, y, W, y), fill=tint(c['ink'], .94))
        d.rounded_rectangle((1, 1, W-2, H-2), radius=28, outline=tint(c['ink'], .78), width=2)
        d.text((48, 34), c['brand'], font=font(15, True), fill=muted)
        d.text((1056, 34), c['handle'], font=font(15), fill=ink)
        d.ellipse((48, 107, 55, 114), fill=orange)
        d.text((69, 101), c['greeting'], font=font(15, True), fill=orange)

        # Dot-matrix lettering, generated from a text mask.
        mask = Image.new('L', (770, 175))
        md = ImageDraw.Draw(mask)
        md.text((0, -5), c['first_name'], font=font(c['name_size'], True), fill=255)
        md.text((0, 76), c['last_name'], font=font(c['name_size'], True), fill=255)
        for y in range(0, 175, c['dot_spacing']):
            for x in range(0, 770, c['dot_spacing']):
                if mask.getpixel((x, y)) > 90:
                    d.ellipse((48+x, 144+y, 50+x, 146+y), fill=ink)
        d.text((48, 342), c['headline'], font=font(22, True), fill=ink)
        d.text((48, 379), c['stack'], font=font(17), fill=muted)
        d.text((48, 417), c['project_line'], font=font(17), fill=orange)

        d.line((48, 477, 1152, 477), fill=tint(c['ink'], .78), width=2)
        for x, title, value in [(48, 'IN USE', c['in_use']), (342, 'LEARNING', c['learning']), (636, 'ALSO LEARNING', c['also_learning']), (930, 'PROJECT', c['project'])]:
            d.text((x, 503), title, font=font(12, True), fill=muted)
            d.text((x, 531), value, font=font(20, True), fill=ink)
        d.text((48, 577), c['footer'], font=font(10), fill=muted)
        d.text((1068, 577), c['signature'], font=font(10), fill=muted)

        cx, cy, radius = 964, 279, c['radius']
        im = base.copy()
        draw = ImageDraw.Draw(im)
        draw.ellipse((cx-radius-22, cy-radius-22, cx+radius+22, cy+radius+22), outline=tint(c['ink'], .85), width=1)
        for start, extent in [(0, 77), (130, 54), (237, 85)]:
            a = start + math.degrees(phase)
            draw.arc((cx-radius-22, cy-radius-22, cx+radius+22, cy+radius+22), a, a+extent, fill=orange, width=2)
        # Rotating dot sphere with a fixed, legible identity at its center.
        pts = []
        for lat in range(-75, 80, 10):
            p = math.radians(lat)
            for lon in range(0, 360, 10):
                q = math.radians(lon)+phase
                x = radius*math.cos(p)*math.sin(q)
                z = math.cos(p)*math.cos(q)
                y = radius*math.sin(p)
                if z > -0.15:
                    pts.append((z, cx+x, cy+y))
        for z, x, y in sorted(pts):
            r = 0.8 + max(0, z)*1.1
            color = tint(c['orb_color'], .48) if z < .5 else c['orb_color']
            draw.ellipse((x-r, y-r, x+r, y+r), fill=color)
        draw.rounded_rectangle((cx-79, cy-59, cx+79, cy+59), radius=18, fill=c['background'], outline=tint(c['ink'], .72), width=1)
        draw.text((cx, cy-8), c['monogram'], font=font(74, True), anchor='mm', fill=ink)
        draw.text((cx, cy+40), c['orb_label'], font=font(12, True), anchor='mm', fill=orange)
        # A moving tracer evokes both an audio waveform and interactive data.
        line=[]
        for x in range(cx-130, cx+131, 3):
            t=(x-cx)/130
            y=cy+math.sin(t*13+phase)*19*(1-t*t)
            line.append((x,y))
        # Keep the monogram unobstructed.
        draw.line(line[:17], fill=orange, width=2)
        draw.line(line[-17:], fill=orange, width=2)
        return im
    return (draw_banner,)

@app.cell
def _(Path, json):
    output_dir = Path(__file__).resolve().parent
    defaults = {
        "brand": "SEUKOD / PLAYER PROFILE", "handle": "@seukod",
        "greeting": "HELLO, WORLD. I'M", "first_name": "Francisco", "last_name": "Contreras",
        "headline": "Game development & release operations",
        "stack": "Unity / C# / Steam / team coordination",
        "project_line": "AcusPy: Basic Pitch benchmarks + marimo",
        "in_use": "Unity / Git", "learning": "Python / marimo",
        "also_learning": "Node.js", "project": "AcusPy",
        "footer": "BUILD. EXPLORE. PLAY.", "signature": "seukod / 01",
        "monogram": "sk", "orb_label": "INSERT COIN", "font_path": "",
        "ink": "#273c3a", "muted": "#667a77", "accent": "#d66c39",
        "background": "#f0f2ed", "orb_color": "#6b8e79",
        "name_size": 76, "dot_spacing": 4, "radius": 158,
        "frame_count": 60, "duration_ms": 80,
    }
    settings_notice = ""
    _saved = output_dir / "banner-settings.json"
    if _saved.exists():
        try:
            defaults.update(json.loads(_saved.read_text()))
        except (ValueError, OSError):
            settings_notice = "No se pudo leer banner-settings.json; se usan los valores iniciales."
    return defaults, output_dir, settings_notice

@app.cell
def _(defaults, mo, settings_notice):
    mo.md("# seukod · Banner studio\nEdita los widgets de la izquierda: la vista previa se actualiza a la derecha.\n\n" + settings_notice)
    return

@app.cell
def _(PalettePicker, defaults, mo):
    _elements = {}
    _labels = {
        "brand": "Cabecera", "handle": "Usuario", "greeting": "Saludo",
        "first_name": "Nombre", "last_name": "Apellido", "headline": "Descripción principal",
        "stack": "Tecnologías", "project_line": "Descripción del proyecto",
        "in_use": "En uso", "learning": "Aprendiendo", "also_learning": "También aprendiendo",
        "project": "Proyecto", "footer": "Pie de página", "signature": "Firma",
        "monogram": "Iniciales", "orb_label": "Texto del círculo", "font_path": "Ruta de fuente .ttf (opcional)",
    }
    for _key, _label in _labels.items():
        _elements[_key] = mo.ui.text(value=defaults[_key], label=_label, full_width=True, debounce=250)
    _color_labels = {"background": "Fondo", "ink": "Texto", "muted": "Texto secundario", "accent": "Acento", "orb_color": "Esfera"}
    palette = mo.ui.anywidget(PalettePicker(colors={_key: defaults[_key] for _key in _color_labels}))
    for _key, _label, _min, _max, _step in [
        ("name_size", "Tamaño del nombre", 40, 94, 2),
        ("dot_spacing", "Separación de puntos", 3, 7, 1),
        ("radius", "Radio de esfera", 110, 158, 2),
        ("frame_count", "Fotogramas por vuelta", 30, 120, 10),
        ("duration_ms", "Milisegundos por fotograma", 40, 200, 10),
    ]:
        _elements[_key] = mo.ui.slider(_min, _max, step=_step, value=defaults[_key], show_value=True, full_width=True, debounce=True)
    # marimo tracks this UI container and propagates child events to cells
    # referencing controls.value. A plain Python dict is not reactive.
    # Build the layout from these cloned elements, not from _elements.
    controls = mo.ui.dictionary(_elements)
    phase_control = mo.ui.slider(0, 100, value=0, label="Posición en la animación (%)", show_value=True)
    animate_preview = mo.ui.switch(value=False, label="Reproducir animación en la vista previa")
    export_button = mo.ui.run_button(label="Generar y guardar GIF + PNG + ajustes")
    editor_panel = mo.vstack([
        mo.md("### Editar banner"),
        mo.ui.tabs({
            "Textos": mo.accordion({
                "Identidad": mo.vstack([controls[_k] for _k in ("first_name", "last_name", "handle", "monogram")]),
                "Descripción y proyecto": mo.vstack([controls[_k] for _k in ("headline", "stack", "project_line")]),
                "Tecnologías": mo.vstack([controls[_k] for _k in ("in_use", "learning", "also_learning", "project")]),
                "Otros textos": mo.vstack([controls[_k] for _k in ("brand", "greeting", "footer", "signature", "orb_label", "font_path")]),
            }),
            "Colores": palette,
            "Diseño": mo.vstack([controls[_k] for _k in ("name_size", "dot_spacing", "radius", "frame_count", "duration_ms")]),
        }),
        animate_preview,
        phase_control,
        export_button,
    ]).style({"max-height": "75vh", "overflow-y": "auto", "padding-right": "12px"})
    return animate_preview, controls, editor_panel, export_button, palette, phase_control

@app.cell
def _(ImageColor, controls, mo, palette):
    config = dict(controls.value)
    config.update(palette.value["colors"])
    _errors = []
    for _key in ("background", "ink", "muted", "accent", "orb_color"):
        try:
            ImageColor.getrgb(config[_key])
        except ValueError:
            _errors.append(_key)
    mo.stop(bool(_errors), mo.md("Revisa estos colores: " + ", ".join(_errors) + ". Ejemplo: #d66c39."))
    return (config,)

@app.cell
def _(animate_preview, config, draw_banner, editor_panel, io, math, mo, phase_control):
    _buffer = io.BytesIO()
    if animate_preview.value:
        _count = min(config["frame_count"], 36)
        _frames = [draw_banner(config, 2 * math.pi * _idx / _count) for _idx in range(_count)]
        _frames[0].save(_buffer, format="GIF", save_all=True, append_images=_frames[1:],
                        duration=round(config["duration_ms"] * config["frame_count"] / _count / 10) * 10, loop=0)
    else:
        _frame = draw_banner(config, 2 * math.pi * phase_control.value / 100)
        _frame.save(_buffer, format="PNG")
    _preview_panel = mo.vstack([
        mo.md("### Vista previa"),
        mo.image(_buffer.getvalue(), width="100%", alt="Vista previa del banner"),
        mo.md(f"Una vuelta: **{config['frame_count'] * config['duration_ms'] / 1000:.1f} segundos**. "
              "Si un texto se corta, acórtalo o ajusta el tamaño del nombre."),
        mo.md("Los cambios se previsualizan sin guardar. Pulsa **Generar y guardar** para exportarlos."),
    ]).style({"position": "sticky", "top": "12px"})
    mo.hstack([editor_panel, _preview_panel], widths=[1, 2], align="start", gap=2, wrap=True)
    return

@app.cell
def _(config, draw_banner, export_button, io, json, math, mo, output_dir):
    mo.stop(not export_button.value)
    _frames = [
        draw_banner(config, 2 * math.pi * _idx / config["frame_count"])
        for _idx in range(config["frame_count"])
    ]
    _gif = io.BytesIO()
    _frames[0].save(_gif, format="GIF", save_all=True, append_images=_frames[1:],
                    duration=config["duration_ms"], loop=0, optimize=True)
    (output_dir / "seukod-banner.gif").write_bytes(_gif.getvalue())
    _frames[0].save(output_dir / "seukod-banner.png")
    (output_dir / "banner-settings.json").write_text(json.dumps(config, indent=2, ensure_ascii=False))
    mo.vstack([
        mo.md(f"## Exportado\nGuardado en: **{output_dir}**\n\n"
              f"GIF: **{len(_gif.getvalue()) / 1024:.0f} KB**. Los ajustes se cargarán al abrir el notebook de nuevo."),
        mo.image("data:image/gif;base64," + __import__("base64").b64encode(_gif.getvalue()).decode(), width="100%"),
    ])
    return

if __name__ == "__main__":
    app.run()
