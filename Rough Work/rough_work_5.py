import tkinter as tk
import random
import math
import time

# ============================================================
# NEON SURVIVOR
# 2D GAME - NO PYGAME NEEDED
# ============================================================

WIDTH = 1100
HEIGHT = 700

root = tk.Tk()
root.title("NEON SURVIVOR")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.configure(bg="#0F0606")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#050812",
    highlightthickness=0
)
canvas.pack()

# ============================================================
# COLORS
# ============================================================

BG = "#050812"
GRID = "#10182b"

WHITE = "#f2f7ff"
CYAN = "#28e7ff"
PINK = "#ff3fa4"
PURPLE = "#9b5cff"
GREEN = "#42ff91"
YELLOW = "#ffe34d"
RED = "#ff4655"
ORANGE = "#ff9138"

# ============================================================
# GAME STATE
# ============================================================

state = "menu"

score = 0
high_score = 0

wave = 1
wave_time = 0
spawn_timer = 0

combo = 1
combo_timer = 0

mouse_x = WIDTH // 2
mouse_y = HEIGHT // 2

keys = set()

last_time = time.time()
background_scroll = 0

# ============================================================
# PLAYER
# ============================================================

player = {
    "x": WIDTH // 2,
    "y": HEIGHT // 2,

    "speed": 300,

    "health": 100,
    "max_health": 100,

    "energy": 100,

    "radius": 18,

    "angle": 0,

    "shoot_timer": 0,

    "invincible": 0,

    "shield": 0,

    "rapid": 0
}

# ============================================================
# OBJECTS
# ============================================================

bullets = []
enemy_bullets = []
enemies = []
particles = []
powerups = []

# ============================================================
# STARFIELD
# ============================================================

stars = []

for i in range(160):
    stars.append({
        "x": random.randint(0, WIDTH),
        "y": random.randint(80, HEIGHT),
        "speed": random.uniform(20, 90),
        "size": random.randint(1, 3)
    })

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def draw_text(x, y, message, color=WHITE, size=20, anchor="center"):
    canvas.create_text(
        x,
        y,
        text=message,
        fill=color,
        font=("Consolas", size, "bold"),
        anchor=anchor
    )

# ============================================================
# BACKGROUND
# ============================================================

def draw_background(dt):

    global background_scroll

    background_scroll += dt * 25

    canvas.create_rectangle(
        0,
        0,
        WIDTH,
        HEIGHT,
        fill=BG,
        outline=""
    )

    # Stars

    for star in stars:

        y = (
            star["y"]
            + background_scroll * star["speed"] / 25
        ) % HEIGHT

        if y < 80:
            y += 80

        canvas.create_oval(
            star["x"],
            y,
            star["x"] + star["size"],
            y + star["size"],
            fill="#263c70",
            outline=""
        )

    # Grid

    grid_size = 55
    offset = int(background_scroll % grid_size)

    for x in range(
        -grid_size + offset,
        WIDTH,
        grid_size
    ):

        canvas.create_line(
            x,
            80,
            x,
            HEIGHT,
            fill=GRID
        )

    for y in range(
        80 - grid_size + offset,
        HEIGHT,
        grid_size
    ):

        canvas.create_line(
            0,
            y,
            WIDTH,
            y,
            fill=GRID
        )

# ============================================================
# PARTICLES
# ============================================================

def create_explosion(x, y, color, amount=20):

    for i in range(amount):

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(60, 280)

        particles.append({
            "x": x,
            "y": y,

            "vx": math.cos(angle) * speed,
            "vy": math.sin(angle) * speed,

            "life": random.uniform(0.25, 0.8),

            "max_life": 0.8,

            "size": random.randint(2, 5),

            "color": color
        })


def update_particles(dt):

    for particle in particles[:]:

        particle["x"] += particle["vx"] * dt
        particle["y"] += particle["vy"] * dt

        particle["vx"] *= 0.95
        particle["vy"] *= 0.95

        particle["life"] -= dt

        if particle["life"] <= 0:
            particles.remove(particle)


def draw_particles():

    for particle in particles:

        ratio = particle["life"] / particle["max_life"]

        size = max(
            1,
            particle["size"] * ratio
        )

        canvas.create_oval(
            particle["x"] - size,
            particle["y"] - size,
            particle["x"] + size,
            particle["y"] + size,
            fill=particle["color"],
            outline=""
        )

# ============================================================
# PLAYER
# ============================================================

def update_player(dt):

    dx = 0
    dy = 0

    if "w" in keys or "up" in keys:
        dy -= 1

    if "s" in keys or "down" in keys:
        dy += 1

    if "a" in keys or "left" in keys:
        dx -= 1

    if "d" in keys or "right" in keys:
        dx += 1

    if dx != 0 or dy != 0:

        length = math.hypot(dx, dy)

        dx /= length
        dy /= length

        player["x"] += dx * player["speed"] * dt
        player["y"] += dy * player["speed"] * dt

    player["x"] = clamp(
        player["x"],
        30,
        WIDTH - 30
    )

    player["y"] = clamp(
        player["y"],
        110,
        HEIGHT - 35
    )

    # Aim at mouse

    player["angle"] = math.atan2(
        mouse_y - player["y"],
        mouse_x - player["x"]
    )

    # Timers

    player["shoot_timer"] = max(
        0,
        player["shoot_timer"] - dt
    )

    player["invincible"] = max(
        0,
        player["invincible"] - dt
    )

    player["shield"] = max(
        0,
        player["shield"] - dt
    )

    player["rapid"] = max(
        0,
        player["rapid"] - dt
    )

    # Energy regeneration

    player["energy"] = min(
        100,
        player["energy"] + 12 * dt
    )

    # Space shooting

    if "enter" in keys:
        shoot()


def draw_player():

    x = player["x"]
    y = player["y"]

    angle = player["angle"]

    # Glow

    canvas.create_oval(
        x - 35,
        y - 35,
        x + 35,
        y + 35,
        outline="#123b49",
        width=3
    )

    # Shield

    if player["shield"] > 0:

        canvas.create_oval(
            x - 32,
            y - 32,
            x + 32,
            y + 32,
            outline=CYAN,
            width=3
        )

    # Ship

    size = 25

    shape = [
        (0, -size),
        (size * 0.72, size),
        (0, size * 0.42),
        (-size * 0.72, size)
    ]

    points = []

    for px, py in shape:

        rx = (
            px * math.cos(angle)
            -
            py * math.sin(angle)
        )

        ry = (
            px * math.sin(angle)
            +
            py * math.cos(angle)
        )

        points.extend([
            x + rx,
            y + ry
        ])

    # Engine flame

    back_x = x - math.cos(angle) * 16
    back_y = y - math.sin(angle) * 16

    flame_length = random.randint(12, 22)

    flame_x = (
        back_x
        -
        math.cos(angle)
        *
        flame_length
    )

    flame_y = (
        back_y
        -
        math.sin(angle)
        *
        flame_length
    )

    canvas.create_line(
        back_x,
        back_y,
        flame_x,
        flame_y,
        fill=ORANGE,
        width=7
    )

    canvas.create_polygon(
        points,
        fill=CYAN,
        outline=WHITE,
        width=2
    )

# ============================================================
# SHOOTING
# ============================================================

def shoot():

    if player["energy"] < 5:
        return

    if player["shoot_timer"] > 0:
        return

    angle = player["angle"]

    bullets.append({
        "x":
            player["x"]
            +
            math.cos(angle) * 25,

        "y":
            player["y"]
            +
            math.sin(angle) * 25,

        "vx":
            math.cos(angle) * 750,

        "vy":
            math.sin(angle) * 750,

        "life": 1.5
    })

    player["energy"] -= 5

    if player["rapid"] > 0:
        player["shoot_timer"] = 0.055
    else:
        player["shoot_timer"] = 0.13


def update_bullets(dt):

    for bullet in bullets[:]:

        bullet["x"] += bullet["vx"] * dt
        bullet["y"] += bullet["vy"] * dt

        bullet["life"] -= dt

        if (
            bullet["life"] <= 0
            or bullet["x"] < -30
            or bullet["x"] > WIDTH + 30
            or bullet["y"] < 70
            or bullet["y"] > HEIGHT + 30
        ):

            bullets.remove(bullet)
            continue

        canvas.create_oval(
            bullet["x"] - 4,
            bullet["y"] - 4,
            bullet["x"] + 4,
            bullet["y"] + 4,
            fill=WHITE,
            outline=CYAN,
            width=2
        )

# ============================================================
# ENEMIES
# ============================================================

def spawn_enemy():

    side = random.choice([
        "top",
        "bottom",
        "left",
        "right"
    ])

    if side == "top":

        x = random.randint(40, WIDTH - 40)
        y = 90

    elif side == "bottom":

        x = random.randint(40, WIDTH - 40)
        y = HEIGHT + 40

    elif side == "left":

        x = -40
        y = random.randint(110, HEIGHT - 40)

    else:

        x = WIDTH + 40
        y = random.randint(110, HEIGHT - 40)

    chance = random.random()

    # ========================================================
    # TANK
    # ========================================================

    if wave >= 5 and chance < 0.15:

        tank_health = 170 + wave * 15

        enemies.append({

            "type": "tank",

            "x": x,
            "y": y,

            "radius": 29,

            # SLOW TANK
            "speed": 25 + wave,

            "health": tank_health,
            "max_health": tank_health,

            "damage": 25,

            "points": 350,

            "color": ORANGE
        })

    # ========================================================
    # SHOOTER
    # ========================================================

    elif wave >= 3 and chance < 0.40:

        shooter_health = 55 + wave * 5

        enemies.append({

            "type": "shooter",

            "x": x,
            "y": y,

            "radius": 17,

            # SLOWER SHOOTER
            "speed": 40 + wave,

            "health": shooter_health,
            "max_health": shooter_health,

            "damage": 15,

            "points": 180,

            "shoot_timer":
                random.uniform(1, 2),

            "color": PURPLE
        })

    # ========================================================
    # NORMAL CIRCULAR ENEMY
    # ========================================================

    else:

        normal_health = 35 + wave * 4

        enemies.append({

            "type": "chaser",

            "x": x,
            "y": y,

            "radius": 17,

            # MUCH SLOWER CIRCULAR ENEMY
            "speed": 45 + wave * 2,

            "health": normal_health,
            "max_health": normal_health,

            "damage": 12,

            "points": 100,

            "color": PINK
        })


def update_enemies(dt):

    for enemy in enemies[:]:

        dx = player["x"] - enemy["x"]
        dy = player["y"] - enemy["y"]

        dist = max(
            0.001,
            math.hypot(dx, dy)
        )

        # ====================================================
        # NORMAL CIRCULAR ENEMY
        # ====================================================

        if enemy["type"] == "chaser":

            enemy["x"] += (
                dx / dist
                *
                enemy["speed"]
                *
                dt
            )

            enemy["y"] += (
                dy / dist
                *
                enemy["speed"]
                *
                dt
            )

        # ====================================================
        # SHOOTER
        # ====================================================

        elif enemy["type"] == "shooter":

            if dist < 300:

                enemy["x"] -= (
                    dx / dist
                    *
                    enemy["speed"]
                    *
                    dt
                )

                enemy["y"] -= (
                    dy / dist
                    *
                    enemy["speed"]
                    *
                    dt
                )

            else:

                enemy["x"] += (
                    dx / dist
                    *
                    enemy["speed"]
                    *
                    dt
                )

                enemy["y"] += (
                    dy / dist
                    *
                    enemy["speed"]
                    *
                    dt
                )

            enemy["shoot_timer"] -= dt

            if enemy["shoot_timer"] <= 0:

                enemy_bullets.append({

                    "x": enemy["x"],
                    "y": enemy["y"],

                    "vx":
                        dx / dist * 320,

                    "vy":
                        dy / dist * 320,

                    "life": 3
                })

                enemy["shoot_timer"] = 1.5

        # ====================================================
        # TANK
        # ====================================================

        else:

            enemy["x"] += (
                dx / dist
                *
                enemy["speed"]
                *
                dt
            )

            enemy["y"] += (
                dy / dist
                *
                enemy["speed"]
                *
                dt
            )

        # ====================================================
        # PLAYER COLLISION
        # ====================================================

        if distance(
            enemy["x"],
            enemy["y"],
            player["x"],
            player["y"]
        ) < enemy["radius"] + player["radius"]:

            damage_player(enemy["damage"])

            create_explosion(
                enemy["x"],
                enemy["y"],
                enemy["color"],
                15
            )

            if enemy in enemies:
                enemies.remove(enemy)

            continue

        draw_enemy(enemy)


def draw_enemy(enemy):

    x = enemy["x"]
    y = enemy["y"]
    r = enemy["radius"]

    # Glow

    canvas.create_oval(
        x - r - 7,
        y - r - 7,
        x + r + 7,
        y + r + 7,
        outline=enemy["color"],
        width=2
    )

    # ========================================================
    # NORMAL CIRCLE
    # ========================================================

    if enemy["type"] == "chaser":

        canvas.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            fill=PINK,
            outline=WHITE,
            width=2
        )

        canvas.create_oval(
            x - 5,
            y - 5,
            x + 5,
            y + 5,
            fill=BG,
            outline=""
        )

    # ========================================================
    # SHOOTER
    # ========================================================

    elif enemy["type"] == "shooter":

        points = []

        for i in range(6):

            angle = i * math.pi / 3

            points.extend([
                x + math.cos(angle) * r,
                y + math.sin(angle) * r
            ])

        canvas.create_polygon(
            points,
            fill=PURPLE,
            outline=WHITE,
            width=2
        )

        canvas.create_oval(
            x - 5,
            y - 5,
            x + 5,
            y + 5,
            fill=BG,
            outline=""
        )

    # ========================================================
    # TANK
    # ========================================================

    else:

        canvas.create_oval(
            x - r,
            y - r,
            x + r,
            y + r,
            fill=ORANGE,
            outline=WHITE,
            width=3
        )

        canvas.create_rectangle(
            x - 10,
            y - 10,
            x + 10,
            y + 10,
            fill=BG,
            outline=""
        )

    # Health bar

    ratio = enemy["health"] / enemy["max_health"]

    if ratio < 1:

        canvas.create_rectangle(
            x - r,
            y - r - 9,
            x + r,
            y - r - 5,
            fill="#292d3b",
            outline=""
        )

        canvas.create_rectangle(
            x - r,
            y - r - 9,
            x - r + 2 * r * ratio,
            y - r - 5,
            fill=GREEN,
            outline=""
        )

# ============================================================
# ENEMY BULLETS
# ============================================================

def update_enemy_bullets(dt):

    for bullet in enemy_bullets[:]:

        bullet["x"] += bullet["vx"] * dt
        bullet["y"] += bullet["vy"] * dt

        bullet["life"] -= dt

        if bullet["life"] <= 0:

            enemy_bullets.remove(bullet)
            continue

        if distance(
            bullet["x"],
            bullet["y"],
            player["x"],
            player["y"]
        ) < 24:

            damage_player(12)

            if bullet in enemy_bullets:
                enemy_bullets.remove(bullet)

            continue

        canvas.create_oval(
            bullet["x"] - 5,
            bullet["y"] - 5,
            bullet["x"] + 5,
            bullet["y"] + 5,
            fill=RED,
            outline=ORANGE,
            width=2
        )

# ============================================================
# BULLET COLLISIONS
# ============================================================

def bullet_collisions():

    for bullet in bullets[:]:

        for enemy in enemies[:]:

            if distance(
                bullet["x"],
                bullet["y"],
                enemy["x"],
                enemy["y"]
            ) < enemy["radius"] + 6:

                enemy["health"] -= 25

                create_explosion(
                    bullet["x"],
                    bullet["y"],
                    CYAN,
                    5
                )

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy["health"] <= 0:
                    destroy_enemy(enemy)

                break


def destroy_enemy(enemy):

    global score
    global high_score
    global combo
    global combo_timer

    score += enemy["points"] * combo

    high_score = max(
        high_score,
        score
    )

    combo = min(
        10,
        combo + 1
    )

    combo_timer = 2.5

    create_explosion(
        enemy["x"],
        enemy["y"],
        enemy["color"],
        28
    )

    # Power-up chance

    if random.random() < 0.12:

        create_powerup(
            enemy["x"],
            enemy["y"]
        )

    if enemy in enemies:
        enemies.remove(enemy)

# ============================================================
# POWERUPS
# ============================================================

def create_powerup(x, y):

    powerups.append({

        "x": x,
        "y": y,

        "type": random.choice([
            "heal",
            "shield",
            "rapid",
            "energy"
        ]),

        "life": 10
    })


def update_powerups(dt):

    for powerup in powerups[:]:

        powerup["life"] -= dt

        if powerup["life"] <= 0:

            powerups.remove(powerup)
            continue

        if distance(
            powerup["x"],
            powerup["y"],
            player["x"],
            player["y"]
        ) < 30:

            activate_powerup(
                powerup["type"]
            )

            create_explosion(
                powerup["x"],
                powerup["y"],
                CYAN,
                15
            )

            powerups.remove(powerup)
            continue

        colors = {
            "heal": GREEN,
            "shield": CYAN,
            "rapid": YELLOW,
            "energy": PURPLE
        }

        symbols = {
            "heal": "+",
            "shield": "S",
            "rapid": "R",
            "energy": "E"
        }

        color = colors[powerup["type"]]

        canvas.create_oval(
            powerup["x"] - 17,
            powerup["y"] - 17,
            powerup["x"] + 17,
            powerup["y"] + 17,
            outline=color,
            width=3
        )

        draw_text(
            powerup["x"],
            powerup["y"],
            symbols[powerup["type"]],
            color,
            18
        )


def activate_powerup(powerup_type):

    if powerup_type == "heal":

        player["health"] = min(
            player["max_health"],
            player["health"] + 30
        )

    elif powerup_type == "shield":

        player["shield"] = 6

    elif powerup_type == "rapid":

        player["rapid"] = 6

    elif powerup_type == "energy":

        player["energy"] = 100

# ============================================================
# DAMAGE
# ============================================================

def damage_player(amount):

    if player["invincible"] > 0:
        return

    if player["shield"] > 0:

        player["shield"] = 0
        player["invincible"] = 0.6

        create_explosion(
            player["x"],
            player["y"],
            CYAN,
            18
        )

        return

    player["health"] -= amount

    player["invincible"] = 0.8

    create_explosion(
        player["x"],
        player["y"],
        RED,
        15
    )

    if player["health"] <= 0:

        player["health"] = 0

        create_explosion(
            player["x"],
            player["y"],
            RED,
            70
        )

        end_game()

# ============================================================
# HUD
# ============================================================

def draw_hud():

    canvas.create_rectangle(
        0,
        0,
        WIDTH,
        80,
        fill="#080d1b",
        outline="#17223b"
    )

    # Score

    draw_text(
        25,
        18,
        f"SCORE  {score:,}",
        WHITE,
        22,
        "nw"
    )

    # Wave

    draw_text(
        WIDTH // 2,
        23,
        f"WAVE  {wave}",
        CYAN,
        25
    )

    # Combo

    draw_text(
        WIDTH - 25,
        18,
        f"x{combo} COMBO",
        YELLOW,
        21,
        "ne"
    )

    # HP

    canvas.create_rectangle(
        25,
        58,
        255,
        68,
        fill="#292e3d",
        outline=""
    )

    health_ratio = (
        player["health"]
        /
        player["max_health"]
    )

    canvas.create_rectangle(
        25,
        58,
        25 + 230 * health_ratio,
        68,
        fill=(
            GREEN
            if health_ratio > 0.35
            else RED
        ),
        outline=""
    )

    draw_text(
        265,
        63,
        f"HP {int(player['health'])}",
        WHITE,
        13,
        "w"
    )

    # Energy

    canvas.create_rectangle(
        420,
        59,
        650,
        67,
        fill="#292e3d",
        outline=""
    )

    canvas.create_rectangle(
        420,
        59,
        420 + 230 * player["energy"] / 100,
        67,
        fill=PURPLE,
        outline=""
    )

    draw_text(
        660,
        63,
        "ENERGY",
        WHITE,
        12,
        "w"
    )

    # Abilities

    if player["shield"] > 0:

        draw_text(
            760,
            62,
            "SHIELD",
            CYAN,
            12
        )

    if player["rapid"] > 0:

        draw_text(
            850,
            62,
            "RAPID FIRE",
            YELLOW,
            12
        )

    # Controls

    draw_text(
        WIDTH // 2,
        HEIGHT - 14,
        "WASD / ARROWS   MOVE     SPACE / LEFT CLICK   FIRE     P   PAUSE",
        "#73809b",
        11
    )

# ============================================================
# MENU
# ============================================================

def draw_menu():

    canvas.delete("all")

    draw_background(0)

    draw_text(
        WIDTH // 2,
        190,
        "NEON",
        CYAN,
        65
    )

    draw_text(
        WIDTH // 2,
        260,
        "SURVIVOR",
        PINK,
        65
    )

    draw_text(
        WIDTH // 2,
        320,
        "SURVIVE THE WAVES",
        WHITE,
        22
    )

    # Start button

    canvas.create_rectangle(
        WIDTH // 2 - 220,
        375,
        WIDTH // 2 + 220,
        450,
        fill="#0c1426",
        outline=CYAN,
        width=2
    )

    draw_text(
        WIDTH // 2,
        412,
        "PRESS ENTER TO START",
        CYAN,
        23
    )

    draw_text(
        WIDTH // 2,
        500,
        "WASD / ARROWS  =  MOVE",
        "#a8b4c9",
        15
    )

    draw_text(
        WIDTH // 2,
        530,
        "SPACE / LEFT CLICK  =  SHOOT",
        "#a8b4c9",
        15
    )

    draw_text(
        WIDTH // 2,
        575,
        "Destroy enemies • Collect power-ups • Build your combo",
        "#66738e",
        13
    )

    draw_text(
        WIDTH // 2,
        620,
        f"HIGH SCORE  {high_score:,}",
        YELLOW,
        18
    )

# ============================================================
# PAUSE
# ============================================================

def draw_pause():

    canvas.create_rectangle(
        0,
        80,
        WIDTH,
        HEIGHT,
        fill="#02040a",
        stipple="gray50",
        outline=""
    )

    draw_text(
        WIDTH // 2,
        290,
        "PAUSED",
        CYAN,
        55
    )

    draw_text(
        WIDTH // 2,
        360,
        "PRESS P TO CONTINUE",
        WHITE,
        20
    )

# ============================================================
# GAME OVER
# ============================================================

def draw_game_over():

    canvas.delete("all")

    draw_background(0)

    draw_text(
        WIDTH // 2,
        230,
        "SYSTEM FAILURE",
        RED,
        55
    )

    draw_text(
        WIDTH // 2,
        310,
        f"FINAL SCORE   {score:,}",
        WHITE,
        28
    )

    draw_text(
        WIDTH // 2,
        355,
        f"WAVE REACHED   {wave}",
        CYAN,
        20
    )

    if score >= high_score and score > 0:

        draw_text(
            WIDTH // 2,
            395,
            "NEW HIGH SCORE!",
            YELLOW,
            20
        )

    canvas.create_rectangle(
        WIDTH // 2 - 250,
        445,
        WIDTH // 2 + 250,
        510,
        fill="#0d1527",
        outline=PINK,
        width=2
    )

    draw_text(
        WIDTH // 2,
        478,
        "ENTER = RESTART     ESC = MENU",
        WHITE,
        17
    )

# ============================================================
# START GAME
# ============================================================

def start_game():

    global state
    global score
    global wave
    global wave_time
    global spawn_timer
    global combo
    global combo_timer

    canvas.delete("all")

    score = 0
    wave = 1
    wave_time = 0

    # Initial enemies spawn slowly
    spawn_timer = 1.5

    combo = 1
    combo_timer = 0

    bullets.clear()
    enemy_bullets.clear()
    enemies.clear()
    particles.clear()
    powerups.clear()

    player["x"] = WIDTH // 2
    player["y"] = HEIGHT // 2

    player["health"] = 100
    player["energy"] = 100

    player["shoot_timer"] = 0
    player["invincible"] = 0

    player["shield"] = 0
    player["rapid"] = 0

    state = "playing"

# ============================================================
# END GAME
# ============================================================

def end_game():

    global state

    state = "gameover"

# ============================================================
# GAME UPDATE
# ============================================================

def update_game(dt):

    global wave
    global wave_time
    global spawn_timer
    global combo
    global combo_timer

    update_player(dt)

    update_bullets(dt)

    update_enemies(dt)

    update_enemy_bullets(dt)

    update_powerups(dt)

    bullet_collisions()

    update_particles(dt)

    # ========================================================
    # WAVES
    # ========================================================

    wave_time += dt

    if wave_time >= 20:

        wave += 1
        wave_time = 0

        player["health"] = min(
            100,
            player["health"] + 10
        )

        player["energy"] = 100

    # ========================================================
    # SPAWNING
    # ========================================================

    spawn_timer -= dt

    maximum_enemies = min(
        30,
        4 + wave
    )

    if (
        spawn_timer <= 0
        and len(enemies) < maximum_enemies
    ):

        spawn_enemy()

        # Slower spawning

        spawn_timer = max(
            0.45,
            1.15 - wave * 0.025
        )

    # ========================================================
    # COMBO
    # ========================================================

    if combo_timer > 0:

        combo_timer -= dt

    else:

        combo = 1

# ============================================================
# KEYBOARD
# ============================================================

def key_press(event):

    global state

    key = event.keysym.lower()

    keys.add(key)

    # ENTER

    if key == "return":

        if state == "menu":

            start_game()

        elif state == "gameover":

            start_game()

    # PAUSE

    if key == "p":

        if state == "playing":

            state = "paused"

        elif state == "paused":

            state = "playing"

    # ESCAPE

    if key == "escape":

        if state == "gameover":

            state = "menu"

        elif state == "paused":

            state = "menu"


def key_release(event):

    keys.discard(
        event.keysym.lower()
    )

# ============================================================
# MOUSE
# ============================================================

def mouse_move(event):

    global mouse_x
    global mouse_y

    mouse_x = event.x
    mouse_y = event.y


def mouse_click(event):

    if state == "playing":

        shoot()

# ============================================================
# MAIN GAME LOOP
# ============================================================

def game_loop():

    global last_time

    current_time = time.time()

    dt = current_time - last_time

    last_time = current_time

    # Prevent lag spikes

    dt = min(
        dt,
        0.033
    )

    # ========================================================
    # MENU
    # ========================================================

    if state == "menu":

        draw_menu()

    # ========================================================
    # PLAYING
    # ========================================================

    elif state == "playing":

        canvas.delete("all")

        draw_background(dt)

        update_game(dt)

        draw_player()

        draw_particles()

        draw_hud()

    # ========================================================
    # PAUSED
    # ========================================================

    elif state == "paused":

        draw_pause()

    # ========================================================
    # GAME OVER
    # ========================================================

    elif state == "gameover":

        draw_game_over()

    root.after(
        16,
        game_loop
    )

# ============================================================
# CONTROLS
# ============================================================

root.bind(
    "<KeyPress>",
    key_press
)

root.bind(
    "<KeyRelease>",
    key_release
)

canvas.bind(
    "<Motion>",
    mouse_move
)

canvas.bind(
    "<Button-1>",
    mouse_click
)

# ============================================================
# START
# ============================================================

draw_menu()

game_loop()

root.mainloop()