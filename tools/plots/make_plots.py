"""Draws the plots of the Pelota docs into static/images/plots/.

The numbers mirror the game's constants and formulas (see the comments next to each plot);
when the game changes, update them here and run:

    python3 tools/plots/make_plots.py
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Rectangle  # noqa: E402

OUT = Path(__file__).resolve().parents[2] / "static" / "images" / "plots"

# Colors that read on the light and the dark theme of the site
TEXT = "#8a909a"
GRID = "#8a909a33"
TEAL = "#1f9e89"
AMBER = "#f2a541"
CORAL = "#e4572e"
BLUE = "#3b82f6"
PURPLE = "#8b5cf6"
COURT = "#3b82f622"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 15,
        "text.color": TEXT,
        "axes.labelcolor": TEXT,
        "axes.edgecolor": TEXT,
        "xtick.color": TEXT,
        "ytick.color": TEXT,
        "axes.grid": True,
        "grid.color": GRID,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "savefig.transparent": True,
        "svg.fonttype": "none",
    }
)


def save(fig: plt.Figure, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(OUT / f"{name}.svg")
    plt.close(fig)
    print("wrote", name)


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def clamp01(t: float) -> float:
    return max(0.0, min(1.0, t))


# --- Ball flight (scenes/ball/ball.gd) -------------------------------------------------------

GRAVITY = 9.81
RADIUS = 0.033
AIR_DRAG = 0.022
TOPSPIN_ACCEL_MAX = 15.0
BACKSPIN_ACCEL_MAX = 12.0
RESTITUTION_SOFT, RESTITUTION_HARD, HARD_IMPACT = 0.78, 0.6, 12.0
HORIZONTAL_RETENTION = 0.6
SPIN_BOUNCE_LIFT, SPIN_FORWARD_KICK, SPIN_KICK_FULL_SPEED = 0.2, 0.8, 20.0
SPIN_RETENTION = 0.6
NET_HEIGHT = 0.914
BASELINE = 11.885  # GameConstants.COURT_LENGTH_HALF
SERVICE_LINE = 6.40
COURT_HALF_WIDTH = 4.115


def fly(distance: float, height: float, forward: float, up: float, spin: float,
        until: float = 30.0, dt: float = 1 / 240) -> tuple[list[float], list[float]]:
    """Side view of a flight (distance along the court, height) with one bounce and on."""
    d, h, vd, vh = distance, height, forward, up
    ds, hs = [d], [h]
    bounces = 0
    while d < until and bounces < 2:
        speed = math.hypot(vd, vh)
        speed_factor = min(speed / 40.0, 1.0)
        accel = TOPSPIN_ACCEL_MAX if spin > 0 else BACKSPIN_ACCEL_MAX
        vh += (-spin * accel * speed_factor - GRAVITY) * dt
        drag = 1.0 + AIR_DRAG * math.hypot(vd, vh) * dt
        vd, vh = vd / drag, vh / drag
        d, h = d + vd * dt, h + vh * dt
        if h < RADIUS:
            h = RADIUS
            impact = -vh
            kick = min(vd / SPIN_KICK_FULL_SPEED, 1.0)
            vd = vd * HORIZONTAL_RETENTION + spin * SPIN_FORWARD_KICK * kick
            restitution = lerp(RESTITUTION_SOFT, RESTITUTION_HARD, clamp01(impact / HARD_IMPACT))
            vh = impact * restitution * (1 + spin * SPIN_BOUNCE_LIFT)
            spin *= SPIN_RETENTION
            bounces += 1
        ds.append(d)
        hs.append(h)
    return ds, hs


def first_landing(ds: list[float], hs: list[float]) -> float:
    for d, h in zip(ds, hs):
        if h <= RADIUS + 1e-6 and d > ds[0] + 1:
            return d
    return ds[-1]


def aim(distance: float, height: float, forward: float, spin: float, target: float) -> float:
    """Upward speed that lands the ball at `target` (bisection, like the game's solver)."""
    low, high = -5.0, 15.0
    for _ in range(50):
        mid = (low + high) / 2
        ds, hs = fly(distance, height, forward, mid, spin, until=target + 20)
        if first_landing(ds, hs) < target:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def plot_trajectories() -> None:
    fig, ax = plt.subplots(figsize=(10, 3.8))
    start, contact, target = 0.5, 1.0, 2 * BASELINE - 2.5
    shots = [
        ("Flat drive · 37 m/s, little spin", 37.0, 0.1, BLUE),
        ("Topspin · 33 m/s, heavy topspin", 33.0, 0.9, TEAL),
        ("Slice · 24 m/s, backspin", 24.0, -0.8, AMBER),
    ]
    for label, speed, spin, color in shots:
        up = aim(start, contact, speed, spin, target)
        ds, hs = fly(start, contact, speed, up, spin, until=2 * BASELINE + 8)
        ax.plot(ds, hs, color=color, lw=2.2, label=label)
    ax.add_patch(Rectangle((0, -0.15), 2 * BASELINE, 0.15, color=COURT, lw=0))
    ax.plot([BASELINE, BASELINE], [0, NET_HEIGHT], color=TEXT, lw=3)
    ax.text(BASELINE, NET_HEIGHT + 0.15, "net", ha="center")
    for x, name in [(0, "hitter's\nbaseline"), (2 * BASELINE, "far\nbaseline")]:
        ax.axvline(x, color=TEXT, lw=1, ls=":")
        ax.text(x, 4.3, name, ha="center", va="top", fontsize=12)
    ax.set_xlim(-1, 2 * BASELINE + 7)
    ax.set_ylim(-0.15, 4.4)
    ax.set_yticks([0, 1, 2, 3])
    ax.set_xlabel("distance from the hitter's baseline (m)")
    ax.set_ylabel("height (m)")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3, fontsize=12)
    save(fig, "ball_trajectories")


# --- Contact window (scenes/player/contact_window.gd) ----------------------------------------


def window_anchors(after: list[tuple[float, float]], deepest: float):
    """Early, standard and late points of the contact window (ContactWindow.create): the steps
    after the bounce, ending where the player would move back farther than allowed."""
    bounce = next(i for i, (d, h) in enumerate(after) if h <= RADIUS + 1e-6)
    steps = [after[bounce]]
    for d, h in after[bounce + 1:]:
        if d > deepest:
            break
        steps.append((d, h))
    apex = max(range(len(steps)), key=lambda i: steps[i][1])
    early = next((steps[i] for i in range(apex) if steps[i][1] >= 0.8), steps[apex])
    standard = next((steps[i] for i in range(apex, len(steps)) if steps[i][1] <= 1.1), steps[apex])
    start = steps.index(standard)
    late = next((steps[i] for i in range(start, len(steps)) if steps[i][1] <= 0.5), steps[-1])
    return early, standard, late


def plot_contact_window() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.9), sharey=True)
    # Player depth (m from the net): well behind the baseline, and just behind it
    cases = [
        ("Standing well back: all in reach", 30.0, 0.4,
         2 * BASELINE - 5.5, BASELINE + 3.0),
        ("Near the baseline: taken earlier", 27.0, 0.8,
         2 * BASELINE - 3.6, BASELINE + 0.5),
    ]
    for ax, (title, speed, spin, target, stand) in zip(axes, cases):
        deepest = stand + 1.0
        up = aim(0.0, 1.0, speed, spin, target)
        ds, hs = fly(0.0, 1.0, speed, up, spin, until=60.0)
        after = [(d - BASELINE + 0.5, h) for d, h in zip(ds, hs) if d - BASELINE + 0.5 > 1.5]
        xs, ys = zip(*after)
        ax.plot(xs, ys, color=BLUE, lw=2.2)
        early, standard, late = window_anchors(after, deepest)
        ax.axvspan(early[0], late[0], color=TEAL, alpha=0.1)
        for point, label, color, dy in [
            (early, "early", CORAL, -24),
            (standard, "standard", TEAL, 14),
            (late, "late", AMBER, -22),
        ]:
            if label == "late" and late == standard:
                continue
            ax.plot(*point, "o", color=color, ms=10, zorder=5)
            ax.annotate(label, point, xytext=(0, dy), textcoords="offset points", ha="center",
                        color=color, fontsize=13, fontweight="bold")
        ax.axvline(stand, color=TEXT, lw=1.2)
        ax.text(stand - 0.2, 3.25, "player", ha="right", fontsize=12)
        ax.axvline(deepest, color=CORAL, lw=1.2, ls="--")
        ax.text(deepest + 0.2, 3.25, "1 m back", fontsize=12, color=CORAL)
        ax.axvline(BASELINE, color=TEXT, lw=1, ls=":")
        ax.plot([0, 0], [0, NET_HEIGHT], color=TEXT, lw=3)
        ax.set_title(title, fontsize=14, color=TEXT)
        ax.set_xlim(-0.5, 23)
        ax.set_ylim(0, 3.5)
        ax.set_xlabel("distance from the net (m)")
    axes[0].set_ylabel("ball height (m)")
    save(fig, "contact_window")


# --- Shot timing (scenes/player/controllers/human_controller.gd) -----------------------------

PERFECT_WINDOW = 0.12
EARLIEST = 0.8


def timing_quality(seconds: float, window: float) -> float:
    return 1.0 - clamp01((seconds - window) / (EARLIEST - window))


def plot_timing() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 3.6))
    seconds = [i / 400 for i in range(0, 361)]
    for factor, label, color in [(1.0, "standard contact", TEAL),
                                 (0.6, "taking it early (window × 0.6)", CORAL),
                                 (1.25, "taking it late (window × 1.25)", AMBER)]:
        ax1.plot(seconds, [timing_quality(s, PERFECT_WINDOW * factor) for s in seconds],
                 color=color, lw=2.2, label=label)
    ax1.axvspan(0, PERFECT_WINDOW, color=TEAL, alpha=0.12)
    ax1.text(PERFECT_WINDOW / 2, 0.08, "perfect\nwindow", ha="center", fontsize=12, color=TEAL)
    ax1.set_xlabel("button released … s before contact")
    ax1.set_ylabel("timing quality")
    ax1.set_ylim(0, 1.08)
    ax1.legend(fontsize=11.5, loc="upper right")

    quality = [i / 200 for i in range(0, 200)]
    ax2.plot(quality, [lerp(0.8, 0.92, q) for q in quality], color=BLUE, lw=2.2,
             label="rally speed")
    ax2.plot(quality, [lerp(0.0, 0.5, q) for q in quality], color=PURPLE, lw=2.2,
             label="attack pace")
    ax2.plot([1.0], [1.0], "o", color=AMBER, ms=12, zorder=5)
    ax2.annotate("PERFECT: 100 % speed\nand attack pace,\n130 % spin", (1.0, 1.0),
                 xytext=(0.03, 0.42), textcoords="data", color=AMBER, fontsize=12,
                 arrowprops=dict(arrowstyle="->", color=AMBER))
    ax2.set_xlabel("timing quality (just below perfect → 1)")
    ax2.set_ylabel("share the shot gets")
    ax2.set_ylim(0, 1.1)
    ax2.legend(fontsize=12, loc="lower right")
    save(fig, "timing")


def plot_positioning() -> None:
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    perfect = 0.15  # Player.PERFECT_CONTACT_DISTANCE
    # Farthest hit: Model.MAX_REACH + Player.RACKET_HEAD_RADIUS + Ball.RADIUS
    reach = 0.45 + 0.15 + 0.033
    xs = [i / 100 for i in range(0, 81)]
    ys = [1.0 - clamp01((x - perfect) / (reach - perfect)) if x <= reach else 0 for x in xs]
    ax.plot(xs, ys, color=TEAL, lw=2.2)
    ax.axvspan(0, perfect, color=TEAL, alpha=0.12)
    ax.text(perfect / 2, 0.15, "sweet\nspot", ha="center", fontsize=12, color=TEAL)
    ax.axvspan(reach, 0.8, color=CORAL, alpha=0.08)
    ax.text((reach + 0.8) / 2, 0.5, "out of\nreach", ha="center", color=CORAL, fontsize=12)
    ax.set_xlabel("distance of the ball from the swing's contact point (m)")
    ax.set_ylabel("positioning quality")
    save(fig, "positioning")


# --- Movement (scenes/player/movement_controller.gd, player.gd) -----------------------------

def plot_speed_by_direction() -> None:
    fig = plt.figure(figsize=(5.4, 4.6))
    ax = fig.add_subplot(projection="polar")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    angles = [math.radians(a) for a in range(0, 361, 2)]
    base = 5.6  # Player.move_speed (m/s) for an average player

    def facing_net(angle: float) -> float:
        alignment = math.cos(angle)
        straight = 1.0 if alignment >= 0 else 0.7
        return base * lerp(0.8, straight, alignment * alignment)

    ax.plot(angles, [facing_net(a) for a in angles], color=TEAL, lw=2.4,
            label="facing the net (backpedaling backward)")
    ax.plot(angles, [base if abs(math.cos(a)) > 0.5 and math.cos(a) < 0 else math.nan
                     for a in angles], color=CORAL, lw=2.4, ls="--",
            label="turned around and running")
    ax.set_xticks([0, math.pi / 2, math.pi, 3 * math.pi / 2])
    ax.set_xticklabels(["toward\nthe net", "right", "back", "left"])
    ax.set_rlim(0, 6.2)
    ax.set_rticks([2, 4, 6])
    ax.set_yticklabels(["2 m/s", "4 m/s", "6 m/s"], fontsize=11)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.32), fontsize=12)
    save(fig, "speed_by_direction")


# --- Animation (player_animation_tree.tres, player_animator.gd) ------------------------------

def plot_blend_space() -> None:
    fig, ax = plt.subplots(figsize=(6.2, 5.6))
    points = {
        "walk": (0, 1.49), "run": (0, 3.9),
        "walk back": (0, -1.49), "run back": (0, -3.9),
        "side step\nleft": (-1.54, 0), "side step\nright": (1.54, 0),
        "side run\nleft": (-4.03, 0), "side run\nright": (4.03, 0),
    }
    for name, (x, y) in points.items():
        ax.plot(x, y, "o", color=TEAL, ms=10, zorder=5)
        ax.annotate(name, (x, y), xytext=(0, 12), textcoords="offset points", ha="center",
                    fontsize=12)
    hull = ["run", "side run\nright", "run back", "side run\nleft", "run"]
    ax.plot([points[p][0] for p in hull], [points[p][1] for p in hull], color=TEAL, alpha=0.3)
    ax.plot(0, 0, "o", color=AMBER, ms=12)
    ax.annotate("idle (cross-faded\nbelow walking speed)", (0, 0), xytext=(14, -34),
                textcoords="offset points", fontsize=12, color=AMBER)
    ax.plot(2.2, 2.6, "*", color=CORAL, ms=16)
    ax.annotate("running diagonally forward right:\na blend of run and side run",
                (2.2, 2.6), xytext=(35, 38), textcoords="offset points", fontsize=12,
                color=CORAL, ha="center", arrowprops=dict(arrowstyle="->", color=CORAL))
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4.8, 5)
    ax.set_aspect("equal")
    ax.set_xlabel("sideways speed (m/s)")
    ax.set_ylabel("forward speed (m/s)")
    save(fig, "blend_space")


def plot_gait_cycle() -> None:
    fig, ax = plt.subplots(figsize=(10, 2.8))
    clips = [("walk", 1.033, TEAL), ("run", 0.7, CORAL)]
    for row, (name, cycle, color) in enumerate(clips):
        y = 1 - row
        ax.barh(y, cycle, left=0, height=0.32, color=color, alpha=0.25)
        ax.barh(y - 0.42, 1.0, left=0, height=0.32, color=color, alpha=0.55)
        for t, foot in [(0, "L"), (0.5, "R")]:
            ax.text(t * cycle + 0.01, y, f"{foot} down", va="center", fontsize=12)
            ax.text(t + 0.01, y - 0.42, f"{foot} down", va="center", fontsize=12)
        ax.text(-0.02, y, f"{name}: recorded ({cycle:.2f} s)", ha="right", va="center")
        ax.text(-0.02, y - 0.42, f"{name}: stored cycle (1 s)", ha="right", va="center")
    ax.set_xlim(-0.75, 1.15)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticks([])
    ax.set_xlabel("time in the clip (s)")
    ax.grid(False)
    save(fig, "gait_cycle")


def plot_cadence() -> None:
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    walk_speed, run_speed = 1.49, 3.9
    walk_cadence, run_cadence = 1 / 1.033, 1 / 0.7
    speeds = [i / 50 for i in range(0, 351)]

    def cadence(s: float) -> float:
        if s > run_speed:
            return run_cadence * math.sqrt(s / run_speed)
        return lerp(walk_cadence, run_cadence, clamp01((s - walk_speed) / (run_speed - walk_speed)))

    ax.plot(speeds, [cadence(s) for s in speeds], color=TEAL, lw=2.2)
    ax.axvline(walk_speed, color=TEXT, ls=":", lw=1)
    ax.axvline(run_speed, color=TEXT, ls=":", lw=1)
    ax.text(walk_speed, 2.05, "walk clip", ha="center", fontsize=12)
    ax.text(run_speed, 2.05, "run clip", ha="center", fontsize=12)
    ax.set_xlabel("running speed (m/s)")
    ax.set_ylabel("gait cycles per second")
    ax.set_ylim(0.8, 2.15)
    save(fig, "cadence")


def plot_swing_timing() -> None:
    fig, ax = plt.subplots(figsize=(10, 2.9))
    hit = 0.567  # g_forehand 'hit' marker (s)
    cases = [
        ("on time", 1.2, 1.0, 0.0, TEAL),
        ("late: sped up", 0.45, hit / 0.45, 0.0, AMBER),
        ("very late: shortened\nbackswing at 1.8×", 0.22, 1.8, hit - 0.22 * 1.8, CORAL),
    ]
    for row, (name, time_to_contact, speed, skip, color) in enumerate(cases):
        y = 2 - row
        start = 1.5 - time_to_contact if time_to_contact < hit else 1.5 - hit
        duration = (hit - skip) / speed
        ax.barh(y, duration, left=1.5 - duration, height=0.45, color=color, alpha=0.5)
        ax.text(1.5 - duration - 0.02, y, name, ha="right", va="center", fontsize=13)
    ax.axvline(1.5, color=CORAL, lw=2)
    ax.text(1.5, 2.55, "racket meets ball\n('hit' marker)", ha="center", fontsize=12, color=CORAL)
    ax.set_xlim(-0.2, 1.75)
    ax.set_ylim(-0.6, 3.0)
    ax.set_yticks([])
    ax.set_xlabel("time (s) — the bars are the swing from its start to the contact")
    ax.grid(False)
    save(fig, "swing_timing")


# --- Mental game (player_mental_state.gd, match_score.gd) -----------------------------------

DEFENDING = {"BREAK": 0.5, "SET": 0.65, "MATCH": 0.8}
CLOSING = {"SET": 0.2, "MATCH": 0.3}
TIEBREAK_PRESSURE = 0.2
TRAILING = 0.4
SET_STANDING, GAME_STANDING = 0.4, 0.12


def trailing_pressure(standing: float) -> float:
    deficit = max(-standing, 0.0)
    return TRAILING * 4 * deficit * (1 - deficit)


def plot_pressure_sources() -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.2), gridspec_kw={"width_ratios": [1, 1]})
    xs = [i / 100 for i in range(0, 101)]
    ax1.plot(xs, [trailing_pressure(-x) for x in xs], color=CORAL, lw=2.4)
    examples = [(1 * GAME_STANDING, "a break down\n(0-1)"), (4 * GAME_STANDING, "0-4"),
                (SET_STANDING + 4 * GAME_STANDING, "a set and\n0-4 down")]
    for deficit, label in examples:
        p = trailing_pressure(-deficit)
        ax1.plot(deficit, p, "o", color=CORAL, ms=8)
        ax1.annotate(label, (deficit, p), xytext=(0, 12), textcoords="offset points",
                     ha="center", fontsize=12)
    ax1.set_xlabel("how far behind on the score (standing deficit)")
    ax1.set_ylabel("pressure from trailing")
    ax1.set_ylim(0, 0.55)

    labels = ["break\npoint\nagainst", "set\npoint\nagainst", "match\npoint\nagainst",
              "serving\nfor the\nset", "serving\nfor the\nmatch", "tie-\nbreak"]
    values = [DEFENDING["BREAK"], DEFENDING["SET"], DEFENDING["MATCH"], CLOSING["SET"],
              CLOSING["MATCH"], TIEBREAK_PRESSURE]
    colors = [CORAL, CORAL, CORAL, AMBER, AMBER, PURPLE]
    ax2.bar(range(len(values)), values, color=colors, alpha=0.8)
    ax2.set_xticks(range(len(values)))
    ax2.set_xticklabels(labels, fontsize=11)
    ax2.set_ylabel("pressure of the point")
    ax2.set_ylim(0, 0.9)
    save(fig, "pressure_sources")


@dataclass
class Score:
    """Minimal tennis score (no tiebreak) mirroring scenes/match/match_score.gd."""

    points: list[int] = field(default_factory=lambda: [0, 0])
    games: list[int] = field(default_factory=lambda: [0, 0])
    sets: list[int] = field(default_factory=lambda: [0, 0])
    server: int = 0

    def copy(self) -> "Score":
        return Score(self.points[:], self.games[:], self.sets[:], self.server)

    def add_point(self, i: int) -> None:
        o = 1 - i
        if self.points[i] == 3 and self.points[o] == 4:
            self.points[o] = 3
        elif self.points[i] == 4 or (self.points[i] == 3 and self.points[o] < 3):
            self.points = [0, 0]
            self.games[i] += 1
            self.server = 1 - self.server
            if self.games[i] >= 6 and self.games[i] - self.games[o] >= 2:
                self.sets[i] += 1
                self.games = [0, 0]
        else:
            self.points[i] += 1

    def importance(self, i: int) -> str:
        after = self.copy()
        after.add_point(i)
        if after.sets[i] > self.sets[i]:
            return "MATCH" if after.sets[i] >= 2 else "SET"
        if sum(after.games) + 6 * sum(after.sets) != sum(self.games) + 6 * sum(self.sets):
            return "GAME" if i == self.server else "BREAK"
        return "NORMAL"

    def standing(self, i: int) -> float:
        o = 1 - i
        value = (self.sets[i] - self.sets[o]) * SET_STANDING + (self.games[i] - self.games[o]) * GAME_STANDING
        return max(-1.0, min(1.0, value))


def plot_match_story() -> None:
    """Pressure and confidence of player A through a scripted stretch of a match."""
    score = Score()
    pressure, confidence, momentum, form = 0.0, 0.5, 0.0, 0.0
    # A serves first. A holds, then gets broken after saving two break points, then breaks back.
    script = "AAAA" + "BBBB" + "ABBBABAB B".replace(" ", "") + "BBAB" + "AABBAA" + "BAAA"
    history = []
    for winner_char in script:
        situation = max(DEFENDING.get(score.importance(1), 0.0), CLOSING.get(score.importance(0), 0.0))
        situation += trailing_pressure(score.standing(0))
        pressure = lerp(pressure, min(situation, 1.0), 0.6)
        target = clamp01(0.5 + 0.25 * score.standing(0) + 0.2 * momentum + 0.08 * form)
        confidence = lerp(confidence, target, 0.3)
        history.append((pressure, confidence, score.importance(1) == "BREAK" and score.server == 0))
        games_before = sum(score.games)
        winner = 0 if winner_char == "A" else 1
        score.add_point(winner)
        if sum(score.games) != games_before:
            momentum = lerp(momentum, 1.0 if winner == 0 else -1.0, 0.35)
    fig, ax = plt.subplots(figsize=(10, 3.4))
    xs = range(1, len(history) + 1)
    ax.plot(xs, [h[0] for h in history], color=CORAL, lw=2.4, label="pressure")
    ax.plot(xs, [h[1] for h in history], color=TEAL, lw=2.4, label="confidence")
    for x, h in zip(xs, history):
        if h[2]:
            ax.axvspan(x - 0.5, x + 0.5, color=CORAL, alpha=0.12)
    ax.text(10, 0.92, "shaded: A defends a break point", color=CORAL, fontsize=12)
    ax.set_xlabel("point of the match (player A's view)")
    ax.set_ylabel("value")
    ax.set_ylim(0, 1)
    ax.legend(loc="upper left", fontsize=12)
    save(fig, "match_story")


# --- Court and tactics --------------------------------------------------------------------------

def draw_court(ax: plt.Axes, half: bool = False) -> None:
    lo = 0 if half else -BASELINE
    ax.add_patch(Rectangle((-5.5, lo), 11, BASELINE - lo + (0 if half else 0), color=COURT, lw=0))
    for x in (-COURT_HALF_WIDTH, COURT_HALF_WIDTH):
        ax.plot([x, x], [lo, BASELINE], color=TEXT, lw=1.4)
    for z in ([BASELINE] if half else [-BASELINE, BASELINE]):
        ax.plot([-COURT_HALF_WIDTH, COURT_HALF_WIDTH], [z, z], color=TEXT, lw=1.4)
    for z in ([SERVICE_LINE] if half else [-SERVICE_LINE, SERVICE_LINE]):
        ax.plot([-COURT_HALF_WIDTH, COURT_HALF_WIDTH], [z, z], color=TEXT, lw=1)
    ax.plot([0, 0], [-SERVICE_LINE if not half else 0, SERVICE_LINE], color=TEXT, lw=1)
    ax.plot([-5.0, 5.0], [0, 0], color=TEXT, lw=3)


def plot_court() -> None:
    fig, ax = plt.subplots(figsize=(5.2, 7.2))
    draw_court(ax)
    ax.annotate("", xy=(3.0, 0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=2.2))
    ax.annotate("", xy=(0, 3.0), xytext=(0, 0),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.2))
    ax.text(3.1, 0.25, "x", color=CORAL, fontsize=15, fontweight="bold")
    ax.text(0.2, 3.1, "z", color=BLUE, fontsize=15, fontweight="bold")
    ax.text(-4.9, 0.3, "net (z = 0)", fontsize=12)
    ax.text(0, BASELINE + 0.5, f"baseline z = +{BASELINE:g} m", ha="center", fontsize=12)
    ax.text(0, -BASELINE - 1.0, f"baseline z = −{BASELINE:g} m", ha="center", fontsize=12)
    ax.text(4.3, SERVICE_LINE + 0.2, f"service line\n±{SERVICE_LINE} m", fontsize=11.5)
    ax.text(COURT_HALF_WIDTH + 0.1, -9, f"singles sideline\nx = ±{COURT_HALF_WIDTH} m",
            fontsize=11.5)
    ax.text(0, 9.6, "near player's half\n(z > 0)", ha="center", fontsize=12, color=TEAL)
    ax.text(0, -9.6, "far player's half\n(z < 0)", ha="center", fontsize=12, color=AMBER)
    ax.set_xlim(-6, 7.5)
    ax.set_ylim(-BASELINE - 1.6, BASELINE + 1.2)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "court")


def plot_open_court() -> None:
    fig, ax = plt.subplots(figsize=(8.5, 6.2))
    # Top view: the AI hits from the near half (z > 0) into the far half (z < 0).
    draw_court(ax)
    ai = (2.5, 9.0)
    opponent_center = (0.6, -13.6)
    ax.plot(*ai, "o", color=BLUE, ms=12)
    ax.text(ai[0] + 0.3, ai[1] + 0.3, "AI meets a short ball", color=BLUE, fontsize=12)
    ax.plot(*opponent_center, "o", color=AMBER, ms=12)
    ax.text(opponent_center[0] + 0.3, opponent_center[1] - 0.9, "you, in position", color=AMBER,
            fontsize=12)
    angle_target = (-3.9, -7.2)
    ax.add_patch(FancyArrowPatch(ai, angle_target, arrowstyle="-|>", mutation_scale=16,
                                 color=CORAL, lw=2))
    ax.text(-6.9, -4.6, "① short angle\npulls you wide", color=CORAL, fontsize=12)
    stretched = (-4.6, -9.0)
    ax.plot(*stretched, "o", color=AMBER, ms=12, alpha=0.6)
    ax.add_patch(FancyArrowPatch(opponent_center, stretched, arrowstyle="-|>",
                                 mutation_scale=12, color=AMBER, lw=1.4, ls="--"))
    reply = (-1.5, 8.0)
    ax.add_patch(FancyArrowPatch(stretched, reply, arrowstyle="-|>", mutation_scale=12,
                                 color=TEXT, lw=1.2, ls=":"))
    winner = (3.6, -11.8)
    ax.add_patch(FancyArrowPatch(reply, winner, arrowstyle="-|>", mutation_scale=16,
                                 color=TEAL, lw=2))
    ax.text(4.6, -7.0, "② next ball into\nthe open court", color=TEAL, fontsize=12)
    ax.set_xlim(-7.2, 8.4)
    ax.set_ylim(-BASELINE - 1.5, BASELINE + 0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "open_court")


def plot_recovery() -> None:
    fig, ax = plt.subplots(figsize=(6.5, 7.2))
    draw_court(ax)
    hitter = (-3.2, -12.5)
    left, right = (-COURT_HALF_WIDTH, SERVICE_LINE), (COURT_HALF_WIDTH, SERVICE_LINE)
    for corner in (left, right):
        ax.plot([hitter[0], corner[0]], [hitter[1], corner[1]], color=AMBER, lw=1.2, ls="--")
    ux = [(c[0] - hitter[0], c[1] - hitter[1]) for c in (left, right)]
    norm = [math.hypot(*u) for u in ux]
    bis = ((ux[0][0] / norm[0] + ux[1][0] / norm[1]), (ux[0][1] / norm[0] + ux[1][1] / norm[1]))
    depth = BASELINE + 1.0
    t = (depth - hitter[1]) / bis[1]
    spot = (hitter[0] + t * bis[0], depth)
    ax.plot([hitter[0], spot[0]], [hitter[1], spot[1]], color=TEAL, lw=2)
    ax.plot(*hitter, "o", color=AMBER, ms=11)
    ax.text(hitter[0] + 0.3, hitter[1] - 1.0, "opponent hits from here", color=AMBER, fontsize=12)
    ax.plot(*spot, "o", color=TEAL, ms=12)
    ax.text(spot[0] + 0.35, spot[1] + 0.25, "AI recovers here:\non the bisector,\nat its play-style depth",
            color=TEAL, fontsize=12)
    ax.set_xlim(-6.5, 8)
    ax.set_ylim(-BASELINE - 1.5, BASELINE + 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "recovery")


if __name__ == "__main__":
    plot_trajectories()
    plot_contact_window()
    plot_timing()
    plot_positioning()
    plot_speed_by_direction()
    plot_blend_space()
    plot_gait_cycle()
    plot_cadence()
    plot_swing_timing()
    plot_pressure_sources()
    plot_match_story()
    plot_court()
    plot_open_court()
    plot_recovery()
