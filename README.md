# MakerWorld Autopilot – MVP

Ein kostenlos startender Cloud-Prototyp, der täglich fünf **eigenständige, parametrisierte OpenSCAD-Entwürfe** erzeugt, STL-Dateien exportiert, einfache technische Prüfungen durchführt und ein MakerWorld-Veröffentlichungspaket vorbereitet.

## Was dieser Prototyp kann
- Läuft täglich in GitHub Actions (kein eigener PC nötig).
- Erzeugt fünf verschiedene parametrische Entwürfe pro Lauf.
- Exportiert `.scad` und – wenn OpenSCAD erfolgreich installiert ist – `.stl`.
- Erstellt eine `manifest.json`, Beschreibungsentwürfe und eine einfache HTML-Übersicht.
- Speichert die Ergebnisse als GitHub Actions-Artefakt.

## Was er bewusst NICHT macht
- Keine künstlichen Downloads, Drucke, Likes, Bewertungen oder Boosts.
- Kein Scraping mit Login-Cookies und keine inoffiziellen MakerWorld-Schreib-/Upload-Endpunkte.
- Kein automatischer MakerWorld-Upload: Für MakerWorld ist in diesem Projekt keine offiziell dokumentierte öffentliche Creator-Upload-API hinterlegt. Die erzeugten Pakete müssen im MakerWorld-Frontend geprüft und veröffentlicht werden.
- Keine Garantie, dass ein Modell technisch oder rechtlich für jeden Anwendungsfall geeignet ist.

## Enthaltene Modellfamilien
1. Kabelclip (nicht elektrisch/tragend)
2. Beschriftungsschild-Halter
3. Abstandshalter-Set
4. Bit-/Bohrer-Organizer
5. Kantenschutz-Ecke

Die fünf Entwürfe sind einfache Startmodelle, keine geprüften Werkzeuge oder sicherheitsrelevanten Bauteile. Vor einer Veröffentlichung: STL in Bambu Studio öffnen, slicen, Druckvorschau prüfen und einen realen Testdruck machen. Für den P2S Combo sind die STL-Dateien geometrieunabhängig; Material, Düse und Druckprofil werden in Bambu Studio festgelegt.

## Kostenloser Cloud-Start mit GitHub Actions

### 1. Repository erstellen
1. Bei https://github.com anmelden.
2. Neues Repository anlegen, z. B. `makerworld-autopilot`.
3. Für den kostenlosen Start **Public** wählen. Öffentliche Repositories sind öffentlich einsehbar. Keine Passwörter, Tokens oder privaten Daten hochladen.
4. ZIP entpacken und alle enthaltenen Dateien ins Repository hochladen.

### 2. Actions aktivieren
- Repository → **Actions** → Workflows aktivieren.
- Workflow `Daily model generation` öffnen.
- **Run workflow** drücken, um den ersten Test sofort auszuführen.
- Danach läuft er täglich um 06:00 UTC (07:00 Uhr deutscher Winterzeit / 08:00 Uhr Sommerzeit).

### 3. Ergebnisse laden
Nach erfolgreichem Lauf:
- Actions → letzter Workflow-Lauf → **Artifacts**
- `makerworld-daily-pack` herunterladen und entpacken.
- Unter `output/YYYY-MM-DD/` liegen die fünf Modellordner und `dashboard.html`.

### 4. Veröffentlichung
Für jedes Modell:
1. `.stl` in Bambu Studio öffnen.
2. Slicer-Vorschau und Druckbarkeit prüfen.
3. Einen Testdruck durchführen.
4. Eigenständige Fotos/Screenshots erstellen.
5. Beschreibung und Tags prüfen.
6. Manuell bei MakerWorld veröffentlichen.

## Lokal testen (optional)
Voraussetzungen: Python 3.11+ und OpenSCAD.
```bash
python src/generate.py
```
Ohne OpenSCAD entstehen `.scad`-Dateien und das Manifest; STL-Export wird als nicht verfügbar markiert.

## Anpassungen
Die Modellgeometrien liegen in `src/models.py`. Die tägliche Menge kann über `MODEL_COUNT` in `.github/workflows/daily.yml` geändert werden.

## Kosten / Limits
GitHub gibt für Standard-Runner öffentlicher Repositories die Nutzung von GitHub Actions kostenlos an. Für private Repositories gelten kontobezogene Kontingente. Artefakt-Speicherung und Limits können sich ändern; siehe:
https://docs.github.com/en/billing/concepts/product-billing/github-actions

## Sicherheit & Qualität
- Die Geometrieprüfung ist nur ein Basistest (Datei vorhanden, nicht leer, Mindestgröße).
- Keine Festigkeits-, Toleranz-, Material- oder Normprüfung.
- Die Modelle sind nicht für elektrische Sicherheit, Personenschutz, Fahrzeug-/Boots-Sicherheit, Lastaufnahme oder andere sicherheitskritische Zwecke vorgesehen.
- Verwende nur eigene oder rechtmäßig nutzbare Designs, Texte und Bilder.


## Version 2 – Handy-Dashboard mit GitHub Pages
Der Workflow veröffentlicht nach jedem erfolgreichen Lauf das statische Dashboard über GitHub Pages.

### Einmalige Pages-Einstellung
1. Repository → **Settings** → **Pages**.
2. Bei **Build and deployment / Source** die Option **GitHub Actions** auswählen.
3. Repository → **Actions** → `Daily model generation and dashboard deploy` → **Run workflow**.
4. Nach erfolgreichem `deploy`-Job findest du die Dashboard-Adresse unter **Settings → Pages** bzw. in der Workflow-Umgebung `github-pages`.
5. Dashboard auf dem iPhone öffnen und über „Zum Home-Bildschirm“ ablegen.

### Datenschutz
GitHub Pages ist bei einem öffentlichen Repository öffentlich erreichbar. Die Modelle, Beschreibungen und Dashboard-Daten sind damit öffentlich. Keine privaten Zugangsdaten oder persönlichen Daten eintragen.

Das Dashboard zeigt ausschließlich vom Generator erzeugte Daten. Es liest keine MakerWorld-Kontostatistiken und zeigt keine echten Punkte oder Gutscheine an.
