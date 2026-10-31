"""Parametrische Werkstattmodelle – Maße in mm."""
from dataclasses import dataclass

@dataclass
class Model:
    slug: str
    title: str
    description: str
    tags: list[str]
    scad: str
    caution: str

def simple_box(x, y, z, holes=""):
    return f"""
$fn=48;
difference() {{
  minkowski() {{
    cube([{x-4},{y-4},{z-2}],center=true);
    sphere(r=2);
  }}
  {holes}
}}
"""

def cable_clip(w=20, h=12, gap=6):
    return f"""
$fn=48;
difference() {{
  cube([{w},{gap+6},{h}],center=true);
  cylinder(d={gap},h={h+1},center=true);
  cube([{w+1},{gap},{h+1}],center=true);
}}
"""

def label_holder(w=48, h=22):
    return f"""
union() {{
 cube([{w},18,3],center=true);
 translate([0,0,{h/2}])
 difference() {{
  cube([{w},3,{h}],center=true);
  translate([0,0,3]) cube([{w-2},4,{h-6}],center=true);
 }}
}}
"""

def spacer(d=14,h=8,hole=5):
    return f"""
$fn=64;
difference() {{
 cylinder(d={d},h={h});
 translate([0,0,-0.5]) cylinder(d={hole},h={h+1});
}}
"""

def bit_holder(cols=6,rows=3,pitch=10.5,hole=6.7):
    holes=""
    for x in range(cols):
        for y in range(rows):
            holes+=f"translate([{(x-(cols-1)/2)*pitch},{(y-(rows-1)/2)*pitch},-1]) cylinder(d={hole},h=20);"
    return simple_box(cols*pitch,rows*pitch,13,holes)

def corner_guard(size=26,length=30,wall=2.4):
    return f"""
difference() {{
 cube([{size},{size},{length}]);
 translate([{wall},{wall},{wall}])
 cube([{size},{size},{length}]);
}}
"""

def marker_stand():
    holes=""
    for x in [-16,0,16]:
        for y in [-8,8]:
            holes+=f"translate([{x},{y},-10]) cylinder(d=11,h=30);"
    return simple_box(64,48,14,holes)

def screwdriver_rack():
    holes=""
    for i,d in enumerate([8,9,10,11,12,13]):
        holes+=f"translate([{(i-2.5)*16},0,-10]) cylinder(d={d},h=30);"
    return simple_box(104,34,14,holes)

def drill_bit_index():
    holes=""
    for i,d in enumerate([2.5,3,3.5,4,4.5,5,5.5,6,7,8,9,10]):
        holes+=f"translate([{(i-5.5)*9},0,-10]) cylinder(d={d+0.4},h=30);"
    return simple_box(122,30,14,holes)

def sanding_tray():
    return """
difference() {
 cube([100,70,20],center=true);
 translate([0,0,3]) cube([94,64,22],center=true);
}
"""

def tape_measure_holder():
    return """
union() {
 cube([82,48,3],center=true);
 translate([-27,0,14]) cube([3,48,28],center=true);
 translate([27,0,14]) cube([3,48,28],center=true);
}
"""

def build_catalog(day_seed: int):
    v=day_seed % 3
    return [
      Model("cable-clip","Kabelclip","Clip für leichte Kabel.",
        ["kabel","werkstatt","ordnung"],cable_clip(gap=5+v),
        "Nicht für Netzspannung oder Zuglast."),
      Model("label-holder","Beschriftungshalter","Halter für kleine Beschriftungsschilder.",
        ["beschriftung","werkstatt"],label_holder(),
        "Passung des Schildes prüfen."),
      Model("spacer","Ring-Abstandshalter","Einfacher Ring für Bastel- und Sortierarbeiten.",
        ["ring","abstandshalter"],spacer(d=14+v*2),
        "Nicht für sicherheitsrelevante Verbindungen."),
      Model("bit-holder","Bit-Organizer","Rasterhalter für passende Bits.",
        ["bits","werkzeug","organizer"],bit_holder(cols=5+v),
        "Nur zur Aufbewahrung, nicht unter Last."),
      Model("corner-guard","Kantenschutz-Ecke","Einfache Schutz-Ecke für leichte Kanten.",
        ["kantenschutz","möbel"],corner_guard(),
        "Kein geprüfter Personen- oder Stoßschutz."),
      Model("marker-stand","Stiftehalter","Organizer für Marker und Stifte.",
        ["stifte","marker","ordnung"],marker_stand(),
        "Stiftdurchmesser vorab prüfen."),
      Model("screwdriver-rack","Schraubendreher-Ablage","Ablage mit sechs unterschiedlichen Öffnungen.",
        ["schraubendreher","werkstatt"],screwdriver_rack(),
        "Nur zur Aufbewahrung, keine geprüfte Wandhalterung."),
      Model("drill-bit-index","Bohrer-Sortierleiste","Sortierleiste für kleine Bohrer.",
        ["bohrer","sortierung"],drill_bit_index(),
        "Lochmaße sind Startwerte und müssen geprüft werden."),
      Model("sanding-tray","Schleifmittel-Ablage","Schale für Schleifmittel und Zubehör.",
        ["schleifmittel","ablage"],sanding_tray(),
        "Nicht für heiße oder chemische Stoffe."),
      Model("tape-measure-holder","Maßband-Halter","Offene Ablage für ein passendes Maßband.",
        ["maßband","werkstatt"],tape_measure_holder(),
        "Passung am eigenen Maßband prüfen.")
    ]