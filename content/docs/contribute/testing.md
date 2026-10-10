---
title: Playing and testing
weight: 6
---

The most valuable help needs no skills at all: **play the game and tell us what feels wrong.**
Tennis players notice things no code review finds, like a ball that bounces too high, a player
who moves strangely, or an AI that never goes for the obvious winner.

## Reporting a bug

Open an [issue](https://github.com/mbkma/pelota/issues) with:

- **What happened**, and what you expected instead.
- **How to make it happen again**: the mode (match or training), the players, what you did.
- **A screenshot or a short clip** if it is about something you see. A clip of a few seconds says
  more than a long description.
- **Your system**: operating system, and whether you use a keyboard or a gamepad.

One issue per problem, please; it makes them easier to track and close.

## Giving feedback on how it feels

Feedback on the feel of the game is just as welcome as bug reports. The most helpful feedback is
specific:

| Instead of… | Try… |
|---|---|
| "The AI is too hard." | "The AI wins almost every point with a short angle after my second serve." |
| "Movement feels off." | "When I run back for a lob, the player turns around too late and the ball goes over." |
| "Shots are boring." | "Perfect and good forehands land almost in the same place; I can't tell them apart." |

If you know real tennis, compare with it: "Real players would take this ball on the rise."
The [How it works](../../how-it-works/) pages explain what the game is trying to do, which helps
to tell a bug from a design choice.

## Testing changes

When someone opens a pull request that changes how the game plays, trying it out and writing what
you noticed is a real contribution, even without reading the code.
