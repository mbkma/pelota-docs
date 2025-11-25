---
title: "Designing Tennis Players"
weight: 10
---

## Prerequisites

### Install Blender

1. Download Blender from [blender.org](https://www.blender.org/download/)
2. Install the latest stable version (4.0 or newer recommended)
3. Launch Blender and complete the initial setup

## Setup MPFB

### 1. Install MPFB Extension

1. Open Blender
2. Go to **Edit > Preferences > Extensions**
3. Search for "MPFB"
4. Click the result and select **Install**
5. Enable the extension after installation

![MPFB Extension Installation](/images/developers/artists/pelota_docs_blender_extension_mpfb.png)

### 2. Install System Assets

1. Download the system assets ZIP file from: https://files2.makehumancommunity.org/asset_packs/makehuman_system_assets/makehuman_system_assets_cc0.zip
2. In Blender, open the MPFB panel (usually on the right sidebar)
3. Navigate to **Settings > Assets**
4. Point to the downloaded ZIP file directly (no need to extract)
5. Wait for assets to load (this may take a moment)

## Creating a Tennis Player

### 1. Start with Base Model

1. Download [base_player.blend](https://github.com/mbkma/pelota-files/raw/refs/heads/main/player/base_player.blend?download=) from the pelota-files repository
2. Open the file in Blender
3. Select the human model in the scene

### 2. Customize the Body

1. Open the MPFB panel on the right sidebar
2. Go to the **Model** tab
3. Adjust features like:
   - Body shape (height, weight, muscle tone)
   - Face (eyes, nose, mouth, etc.)
   - Skin tone and details
4. Preview changes in real-time

![MPFB Side Panel](/images/developers/artists/pelota_docs_blender_mpfb_side_panel.png)

### 3. Add Clothing

1. In the MPFB panel, navigate to **Apply Assets**
2. Browse available clothing categories (shirts, shorts, shoes, etc.)
3. Select items to add to your player
4. Adjust colors and materials as needed


### 4. Submit Your Design

1. Create a pull request to the [pelota-files](https://github.com/mbkma/pelota-files) repository
2. Include your player blend file with clear naming
3. Describe the player design in the PR

For advanced customization and features, refer to the [MPFB documentation](https://static.makehumancommunity.org/mpfb.html).
