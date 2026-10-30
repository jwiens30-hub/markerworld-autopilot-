"""Original starter geometries. Dimensions are millimetres."""
from dataclasses import dataclass
from typing import Callable

@dataclass
class Model:
    slug: str
    title: str
    description: str
    tags: list[str]
    scad: str
    caution: str

def cable_clip(w=18, h=12, base=3, gap=6):
    return f"""
$fn=48;
difference() {{
  union() {{
    cube([{w},{base+gap+base},{h}], center=true);
    translate([0,0,0]) cylinder(h={h}, d={w}, center=true);
  }}
  cylinder(h={h+1}, d={gap}, center=true);
  translate([0,0,0]) cube([{w+1},{gap},{h+1}], center=true);
}}
"""

def label_holder(w=48, h=22, base=3, slot=1.2):
    return f"""
$fn=32;
union() {{
  cube([{w},{base},{base}], center=true);
  translate([0,0,{h/2}])
    difference() {{
      cube([{w},{base},{h}], center=true);
      translate([0,0,{base}])
        cube([{w-2},{base+1},{h-2*base}], center=true);
    }}
}}
"""

def spacer_set(d=14, h=8, hole=5):
    return f"""
$fn=64;
difference() {{
  cylinder(d={d}, h={h});
  translate([0,0,-0.5]) cylinder(d={hole}, h={h+1});
}}
"""

def bit_holder(cols=5, rows=2, pitch=10, h=12, hole=6):
    w=(cols-1)*pitch+pitch
    d=(rows-1)*pitch+pitch
    holes = ""
    for x in range(cols):
      for y in range(rows):
        holes += f"translate([{(x-(cols-1)/2)*pitch},{(y-(rows-1)/2)*pitch},-0.5]) cylinder(d={hole},h={h+1},$fn=32);"
    return f"""
$fn=48;
difference() {{
  minkowski() {{
    cube([{w-4},{d-4},{h-2}],center=true);
    sphere(r=2);
  }}
  {holes}
}}
"""

def corner_guard(size=24, wall=2.4, length=28):
    return f"""
$fn=24;
difference() {{
  cube([{size},{size},{length}],center=false);
  translate([{wall},{wall},{wall}])
    cube([{size}-{wall},{size}-{wall},{length}-{wall}],center=false);
}}
"""

def build_catalog(day_seed: int):
    # Kleine Parameterrotation sorgt für Varianten, nicht für behauptete Nachfrage.
    v = day_seed % 3
    return [
      Model("cable-clip", "Kabelclip – parametrischer Entwurf",
        "Ein einfacher Kabelclip für leichte Kabelorganisation. Abmessungen vor dem Einsatz prüfen.",
        ["cable-clip","organization","utility"], cable_clip(w=18+v*2, gap=5+v),
        "Nicht für Netzspannung, Zuglast oder sicherheitskritische Anwendungen."),
      Model("label-holder", "Beschriftungsschild-Halter – parametrischer Entwurf",
        "Kleiner Halter für ein selbst erstelltes Beschriftungsschild. Schildmaß vor dem Druck anpassen.",
        ["label-holder","organization","workshop"], label_holder(w=46+v*3, h=20+v*2),
        "Nur als leichter Organizer; keine tragende Funktion."),
      Model("spacer", "Abstandshalter – parametrischer Entwurf",
        "Ein einfacher Ring-Abstandshalter. Bohrung und Höhe vor Verwendung messen.",
        ["spacer","workshop","utility"], spacer_set(d=14+v*2, h=8+v, hole=5),
        "Keine Verwendung an Fahrzeugen, Booten, Maschinen oder sicherheitsrelevanten Verbindungen."),
      Model("bit-holder", "Bit-Organizer – parametrischer Entwurf",
        "Kompakter Organizer für passende Bits oder Schäfte. Passung muss mit dem konkreten Werkzeug getestet werden.",
        ["bit-holder","tool-organizer","workshop"], bit_holder(cols=5+v, rows=2, pitch=10, h=12),
        "Nicht als Werkzeugaufnahme unter Last verwenden."),
      Model("corner-guard", "Kantenschutz-Ecke – parametrischer Entwurf",
        "Einfache Schutz-Ecke für leichte Kanten. Maße und Wandstärke am realen Gegenstand prüfen.",
        ["corner-guard","organizer","utility"], corner_guard(size=24+v*2, wall=2.4, length=28+v*2),
        "Kein geprüfter Stoß- oder Personenschutz.")
    ]
