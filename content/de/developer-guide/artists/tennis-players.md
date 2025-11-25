---
title: "Tennisspieler gestalten"
weight: 10
---

## Voraussetzungen

### Blender installieren

1. Blender von [blender.org](https://www.blender.org/download/) herunterladen
2. Die neueste stabile Version installieren (Version 4.0 oder neuer empfohlen)
3. Blender starten und die Ersteinrichtung abschließen

## MPFB einrichten

### 1. MPFB-Erweiterung installieren

1. Blender öffnen
2. Zu **Edit > Preferences > Extensions** gehen
3. Nach "MPFB" suchen
4. Auf das Ergebnis klicken und **Install** wählen
5. Die Erweiterung nach der Installation aktivieren

![MPFB-Erweiterungsinstallation](/pelota-docs/images/developers/artists/pelota_docs_blender_extension_mpfb.png)

### 2. Systemassets installieren

1. Systemassets-ZIP-Datei herunterladen von: https://files2.makehumancommunity.org/asset_packs/makehuman_system_assets/makehuman_system_assets_cc0.zip
2. In Blender das MPFB-Bedienfeld öffnen (normalerweise auf der rechten Seite)
3. Zu **Settings > Assets** navigieren
4. Direkt auf die heruntergeladene ZIP-Datei verweisen (kein Extrahieren erforderlich)
5. Warten Sie, bis die Assets geladen sind (dies kann einen Moment dauern)

## Tennisspieler erstellen

### 1. Mit Basismodell beginnen

1. [base_player.blend](https://github.com/mbkma/pelota-files/raw/refs/heads/main/player/base_player.blend?download=) aus dem pelota-files Repository herunterladen
2. Die Datei in Blender öffnen
3. Das menschliche Modell in der Szene auswählen

### 2. Den Körper anpassen

1. Das MPFB-Bedienfeld auf der rechten Seite öffnen
2. Zur Registerkarte **Model** gehen
3. Funktionen anpassen wie:
   - Körperform (Größe, Gewicht, Muskeltonus)
   - Gesicht (Augen, Nase, Mund, etc.)
   - Hautfarbe und Details
4. Änderungen in Echtzeit in der Vorschau anzeigen

![MPFB-Seitenpanel](/pelota-docs/images/developers/artists/pelota_docs_blender_mpfb_side_panel.png)

### 3. Kleidung hinzufügen

1. Im MPFB-Bedienfeld zu **Apply Assets** navigieren
2. Verfügbare Kleidungskategorien durchsuchen (Hemden, Shorts, Schuhe, etc.)
3. Artikel auswählen, um sie zum Spieler hinzuzufügen
4. Farben und Materialien nach Bedarf anpassen

### 4. Design einreichen

1. Erstellen Sie einen Pull Request im [pelota-files](https://github.com/mbkma/pelota-files) Repository
2. Fügen Sie Ihre Player Blender-Datei mit klarer Benennung hinzu
3. Beschreiben Sie das Player Design in der PR

Weitere Informationen und erweiterte Anpassungen finden Sie in der [MPFB-Dokumentation](https://static.makehumancommunity.org/mpfb.html).
