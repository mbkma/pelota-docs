---
title: Game Concepts
---

## Overview

Pelota is a 3D tennis simulation game that faithfully recreates the physics and mechanics of professional tennis. Players control realistic tennis strokes with variations in power, spin, and targeting.

## Core Game Elements

### The Ball

The ball is the central game object with realistic physics properties:

- **Diameter**: Standard tennis ball size
- **Weight**: Realistic mass affecting physics calculations
- **Spin Properties**: Affected by stroke application (sidespin, topspin, forward spin)
- **Bounce Characteristics**: Energy retention based on surface and velocity

### The Court

The court follows official tennis dimensions:

- **Width**: 8.11 meters (singles court)
- **Length**: 26.0 meters (baseline to baseline)
- **Surface**: Grass or hard court with realistic bounce characteristics
- **Net**: 0.914 meters high at center

### Players

Players are characterized by:

- **Position**: Dynamic 3D position on the court
- **Movement**: CharacterBody3D movement system for realistic locomotion
- **Stamina**: Energy system affecting performance over time
- **Skills**: Attributes determining shot accuracy and power

## Stroke Types

Pelota implements several distinct stroke types:

### Forehand
- **Power**: High velocity potential
- **Spin**: Topsin or flat
- **Trajectory**: Forward and upward

### Backhand
- **Power**: Moderate to high
- **Variants**: Standard backhand or slice (backspin)
- **Execution**: Cross-body motion

### Volley
- **Description**: Shot taken at the net before ball bounces
- **Power**: Lower power, high precision required
- **Advantage**: Offensive positioning

### Serve
- **Power**: Highest velocity potential (up to 36 m/s in-game)
- **Spin**: Variable sidespin and topspin
- **Rules**: First serve must land in service box, second serve if first fails

### Drop Shot
- **Trajectory**: Short distance, high arc
- **Spin**: Backspin (negative topspin)
- **Purpose**: Force opponent to net

## Stroke Properties

Each stroke has three primary attributes:

### 1. Power (velocity_z0)
- **Range**: 8.0 to 36.0 m/s
- **Impact**: Determines how far and fast the ball travels
- **Factors**: Player skill, stamina, ball position

### 2. Spin (Vector3)
- **X Component (Sidespin)**: Horizontal curve (positive right, negative left)
- **Y Component (Topspin)**: Vertical rotation (positive down, negative up for backspin)
- **Z Component (Forward Spin)**: Forward rotation along travel axis
- **Effect**: Modifies ball trajectory via Magnus effect

### 3. Target
- **Vector3 Position**: Where the player aims on the court
- **Calculation**: From stroke application point to target
- **Correction**: AI and physics adjust for accuracy

## Match Structure

### Scoring System

Pelota follows standard tennis scoring:

- **Points**: 0, 15, 30, 40, Deuce (40-40), Advantage, Game
- **Games**: First to 6 with 2-game lead wins set
- **Sets**: Match typically best of 3 or 5 sets

### Rally Phases

A rally progresses through distinct phases:

1. **Serve**: Server initiates play
2. **Rally**: Both players exchange strokes
3. **Point Decision**: Ball out of bounds, net contact, or ground contact
4. **Point Reset**: Preparation for next point

## Game Mechanics

### Anticipation & Positioning

Players must:
- **Anticipate** opponent's shot target
- **Position** themselves optimally on court
- **Time** movement to reach ball for stroke execution

### Stamina System

Stamina affects:
- **Shot Power**: Reduced power when fatigued
- **Movement Speed**: Slower court coverage with low stamina
- **Recovery**: Gradual stamina regeneration between points

### Trajectory Prediction

The game predicts ball trajectory to:
- **Inform AI Decision**: Help AI decide optimal response
- **Display Information**: Show anticipated landing zone
- **Collision Detection**: Determine if ball will be playable

## Shot Intent System

AI players evaluate shots with different strategic intents:

- **Neutral**: Standard play maintaining rally
- **Attack**: Aggressive shot aiming for winner
- **Defend**: Conservative shot recovering position
- **Approach Net**: Offensive move advancing toward net
- **Serve**: Initiating point

Each intent modifies power, spin, and targeting calculations.

## Ball States

The ball can be in several states during gameplay:

- **In Play**: Active during rally
- **Served**: Recently served, traveling to opponent
- **Dead**: Out of play (out of bounds, net contact, etc.)
- **Prediction**: Trajectory being calculated for analysis
