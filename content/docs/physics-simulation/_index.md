---
title: Physics Simulation
---

## Overview

Pelota implements a realistic physics engine that simulates ball motion with gravity, air resistance, spin effects (Magnus force), and bouncing. The simulation is deterministic and can predict ball trajectory for future frames.

## Physics Constants

All physics calculations use the following constants (from GameConstants):

| Constant | Symbol | Value | Unit | Description |
|----------|--------|-------|------|-------------|
| Gravity | \(g\) | 9.81 | m/s² | Standard Earth gravity acceleration |
| Ball Damping (Bounce) | \(d_{\text{vert}}\) | 0.7 | - | Vertical velocity retention (70% energy) |
| Ball Damping (Horizontal) | \(d_{\text{horiz}}\) | 0.9 | - | Horizontal velocity retention after bounce |
| Spin Side Effect | \(k_{\text{side}}\) | 0.08 | - | Sidespin multiplier for velocity change |
| Spin Down Force | \(k_{\text{down}}\) | 0.1 | - | Topspin multiplier for Magnus downward force |
| Air Drag Coefficient | \(c_d\) | 0.02 | - | Air resistance factor |
| Ground Level | \(y_0\) | 0.035 | m | Ball contact threshold with ground |

## Velocity Update Algorithm

The ball velocity is updated each physics frame using this sequence:

$$\vec{v}_{n+1} = \text{ApplyMagnusAndGravity}(\vec{v}_n, \vec{s}, \Delta t) \rightarrow \text{ApplyAirDrag}(\vec{v}_{n+1}, \Delta t)$$

### 1. Magnus Force & Gravity

The Magnus force is a sideways and downward acceleration caused by ball spin. Combined with gravity:

$$\vec{F}_{\text{magnus}} = \begin{pmatrix}
s_x \cdot k_{\text{side}} \\
-s_y \cdot k_{\text{down}} \\
0
\end{pmatrix}$$

Where \(\vec{s} = (s_x, s_y, s_z)\) is the spin vector:
- \(s_x\): Sidespin (causes horizontal curve)
- \(s_y\): Topspin (positive) or Backspin (negative)
- \(s_z\): Forward spin

The total downward acceleration is:

$$a_y = -g + \vec{F}_{\text{magnus}}.y = -g - s_y \cdot k_{\text{down}}$$

The velocity update becomes:

$$v_x^{(n+1)} = v_x^{(n)} + s_x \cdot k_{\text{side}} \cdot \Delta t$$

$$v_y^{(n+1)} = v_y^{(n)} + \left(-g - s_y \cdot k_{\text{down}}\right) \cdot \Delta t$$

$$v_z^{(n+1)} = v_z^{(n)}$$

### 2. Air Drag

Air resistance creates a velocity-dependent drag that slows the ball:

$$\vec{v}_{\text{drag}} = \vec{v} \cdot \frac{1}{1 + c_d \cdot |\vec{v}| \cdot \Delta t}$$

This exponential decay approximates aerodynamic drag: \(\vec{v}(t) = \vec{v}_0 e^{-c_d |\vec{v}_0| \cdot t}\)

### 3. Position Update

After velocity is computed, position is integrated:

$$\vec{p}_{n+1} = \vec{p}_n + \vec{v}_{n+1} \cdot \Delta t$$

## Collision & Bounce Physics

### Ground Bounce

When the ball collides with the ground, velocity is decomposed into normal and tangential components:

$$\vec{v}_{\text{normal}} = (\vec{v} \cdot \hat{n}) \hat{n}$$
$$\vec{v}_{\text{tangent}} = \vec{v} - \vec{v}_{\text{normal}}$$

Where \(\hat{n} = (0, 1, 0)\) is the ground normal.

### Energy-Based Bounce

If the normal velocity magnitude is significant (\(|\vec{v}_{\text{normal}}| \geq v_{\min}\)):

$$\vec{v}'_{\text{normal}} = -\vec{v}_{\text{normal}} \cdot d_{\text{vert}}$$

$$\vec{v}'_{\text{tangent}} = \vec{v}_{\text{tangent}} \cdot d_{\text{horiz}}$$

$$\vec{v}'_{\text{side}} = \vec{v}'_{\text{tangent}}.x + s_x \cdot k_{\text{side}} \text{ (spin effect on sidespin)}$$

The new velocity is:

$$\vec{v}_{\text{bounce}} = \vec{v}'_{\text{normal}} + \vec{v}'_{\text{tangent}} + (s_x \cdot k_{\text{side}}, 0, 0)$$

### Rolling State

If normal velocity is below threshold, the ball rolls without bouncing:

$$\vec{v}'_{\text{rolling}} = (v_x \cdot d_{\text{horiz}}, 0, v_z \cdot d_{\text{horiz}})$$

This simulates friction and sliding on the court surface.

## Trajectory Prediction

The trajectory prediction simulates future ball motion for AI and aiming systems. It runs a deterministic physics loop:

```
for step in range(TRAJECTORY_PREDICTION_STEPS):
    v = ApplyMagnusAndGravity(v, spin, dt)
    v = ApplyAirDrag(v, dt)
    p += v * dt
    
    if p.y < GROUND_LEVEL:
        v = SimulateBounce(v)
        p.y = GROUND_LEVEL
        bounce_count += 1
    
    if |v| < VELOCITY_THRESHOLD:
        break
```

Each trajectory point records:
- **Position**: \((x, y, z)\) in world coordinates
- **Time**: Elapsed time in seconds
- **Bounce Count**: Number of ground contacts so far

### Prediction Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Steps | 200 | Maximum trajectory points |
| Time Step | 0.016 s (16 ms) | Matches 60 FPS refresh rate |
| Stop Threshold | 0.01 m/s | Minimum velocity to continue prediction |

## Velocity Calculation for Targeting

When a player executes a stroke, the AI must calculate the required velocity to land the ball at a target position:

$$\vec{v}_0 = (v_x, v_y, v_z)$$

Given:
- Start position: \(\vec{p}_0 = (x_0, y_0, z_0)\)
- Target position: \(\vec{p}_t = (x_t, y_t, z_t)\)
- Z-velocity constraint: \(v_z = \text{(player skill x power)}\)

The algorithm iteratively adjusts \(v_x\) and \(v_y\) to match the target:

$$\Delta x = x_t - \text{SimulateTrajectory}(\vec{p}_0, \vec{v}, \vec{s}).x$$

$$\Delta z = z_t - \text{SimulateTrajectory}(\vec{p}_0, \vec{v}, \vec{s}).z$$

Update rule:

$$v_x \leftarrow v_x + \Delta x \cdot \eta$$

$$v_y \leftarrow v_y + \text{sign}(v_z) \cdot \Delta z \cdot \eta$$

Where learning rate \(\eta = 0.2\) and typically 8 iterations are performed.

## Spin Parameter Conventions

The spin vector \(\vec{s} = (s_x, s_y, s_z)\) uses the following conventions:

### Component Meanings

| Component | Range | Effect | Example |
|-----------|-------|--------|---------|
| \(s_x\) (Sidespin) | -1 to +1 | Curves ball left (-) or right (+) | 0.1 = slight right curve |
| \(s_y\) (Topspin) | -15 to +1 | Topspin (+) creates downward curve, Backspin (-) creates upward curve | -10 = strong backspin, 0.8 = topspin |
| \(s_z\) (Forward Spin) | -1 to +1 | Rotation along forward axis (cosmetic effect) | -0.65 = significant forward spin |

### Physical Interpretation

- **Topspin** (\(s_y > 0\)): Ball dips down rapidly, short arc
- **Backspin** (\(s_y < 0\)): Ball stays up longer, float feel
- **Sidespin** (\(s_x \neq 0\)): Ball curves sideways during flight
- **Slice** (high \(s_y\) negative + \(s_x\)): Combination of backspin and sidespin

## Spin-Affected Stroke Examples

### Forehand Drive
- Spin: \((0.15, 0.5, 0.3)\)
- Power: 25 m/s
- Result: Forward-moving with topspin curve, slight sidespin

### Backhand Slice  
- Spin: \((0.2, -8.2, -0.65)\)
- Power: 18 m/s
- Result: Low arc with strong backspin and sidespin

### Serve
- Spin: \((0.3, 0.8, 0.4)\)
- Power: 35 m/s
- Result: Fast, flat serve with slight sidespin

### Drop Shot
- Spin: \((0.1, -10.0, -1.0)\)
- Power: 5 m/s
- Result: Short, high arc with heavy backspin

## Frame Rate Considerations

The physics engine runs at:
- **Simulation Rate**: 60 FPS (0.01667 s per frame)
- **Trajectory Simulation**: 240 FPS (0.00417 s per step) for finer prediction
- **Physics Time Step**: \(\Delta t = 1/60\) s in gameplay

This ensures smooth motion and accurate collision detection.

## Energy Conservation

The ball loses energy through:
1. **Bounce Damping**: \(d_{\text{vert}} = 0.7\) and \(d_{\text{horiz}} = 0.9\) (10-30% loss)
2. **Air Drag**: Exponential decay proportional to velocity
3. **Friction**: Horizontal damping during rolling

Total energy is never conserved, realistically modeling real tennis ball behavior.
