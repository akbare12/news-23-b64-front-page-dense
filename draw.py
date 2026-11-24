#!/usr/bin/env python3
"""news-23 b64 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FDIR = "/usr/share/fonts/truetype/dejavu/"

def fb(sz):
    return ImageFont.truetype(FDIR + "DejaVuSans-Bold.ttf", sz)

def fr(sz):
    return ImageFont.truetype(FDIR + "DejaVuSans.ttf", sz)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 30, 30)
DARKRED = (178, 24, 24)
GOLD = (212, 175, 55)
TEAL = (14, 122, 107)
NAVY = (13, 27, 62)
CREAM = (247, 240, 220)
GRAY = (110, 110, 110)
LGRAY = (230, 230, 230)
GREEN = (178, 214, 158)
BLUE = (30, 80, 180)


def wrap(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(x, y, s, font, fill=BLACK):
    d.text((x, y), s, font=font, fill=fill)


# ---------- masthead ----------
d.rectangle([0, 0, W, 48], fill=BLACK)
text(10, 6, "THE WORLD TODAY", fb(34), WHITE)
r = d.textlength("MONDAY 23 NOVEMBER 2026", font=fb(17))
text(W - 10 - r, 15, "MONDAY 23 NOVEMBER 2026", fb(17), GOLD)

# ---------- kicker ----------
text(10, 52, "AI rout hits Asia  \u00b7  UN chief urges AI rules  \u00b7  US lead over China at record low  \u00b7  Anthropic IPO $107.3B",
     fb(14), RED)

# ---------- number strip (5 cols x 2 rows) ----------
nums = [
    ("-3.3%", "KOSPI", RED), ("5.3", "US-CHINA POWER GAP", BLUE),
    ("11,762", "EBOLA CASES, DRC", (0, 130, 60)), ("10T won", "SEOUL STABILISATION FUND", (150, 100, 0)),
    ("2%", "BILLIONAIRE TAX IN PARIS", (120, 40, 160)),
    ("$450M", "SKUBAL DEAL", (140, 40, 180)), ("165", "RUSSIAN MISSILES/WEEK", DARKRED),
    ("12,000", "CLEARED IN MANCHESTER", BLUE), ("264 kg", "EXPLOSIVES SEIZED", (150, 100, 0)),
    ("$107.3B", "ANTHROPIC IPO", (120, 40, 160)),
]
for i, (val, lab, col) in enumerate(nums):
    cx = 10 + (i % 5) * 204
    cy = 67 + (i // 5) * 30
    text(cx, cy, val, fb(18), col)
    text(cx, cy + 19, lab, fb(9), BLACK)

# ---------- region bar ----------
regions = [("ASIA-PACIFIC 7", (0, 130, 120)), ("AMERICAS 8", (30, 80, 180)),
           ("MIDDLE EAST 6", (170, 110, 30)), ("EUROPE 5", (110, 60, 160)),
           ("AFRICA 3", (180, 30, 30)), ("WORLD 2", (100, 100, 100))]
rx = 6
for name, col in regions:
    wdt = d.textlength(name, font=fb(12)) + 22
    d.rectangle([rx, 126, rx + wdt, 142], fill=col)
    text(rx + 11, 129, name, fb(12), WHITE)
    rx += wdt + 2

# ---------- UTC strip ----------
text(10, 146, "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   ~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles",
     fr(11), BLACK)
ar = d.textlength("~ APPROX", font=fr(10))
text(W - 10 - ar, 147, "~ APPROX", fr(10), GRAY)

# ---------- hero scenes ----------
SX, SW, SG = 9, 330, 8
SY, SH = 156, 116
# scene 1: Kospi skyline + chart
x0 = SX
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=NAVY)
text(x0 + 8, SY + 4, "-3.3%", fb(30), (255, 80, 60))
import random
random.seed(64)
bx = x0 + 6
while bx < x0 + SW - 14:
    bw = random.randint(14, 26)
    bh = random.randint(22, 52)
    d.rectangle([bx, SY + SH - bh, bx + bw, SY + SH], fill=(20, 40, 80))
    for wy in range(SY + SH - bh + 4, SY + SH - 3, 7):
        for wx in range(bx + 3, bx + bw - 3, 6):
            if random.random() < 0.55:
                d.rectangle([wx, wy, wx + 2, wy + 3], fill=(255, 220, 100))
    bx += bw + 3
pts = [(x0 + 8 + i * 30, SY + SH - 18 - v) for i, v in enumerate([8, 26, 14, 34, 22, 40, 30, 46, 36, 52, 44])]
d.line(pts, fill=(255, 160, 40), width=3)
for px, py in pts:
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 200, 90))
# scene 2: Guterres teal
x1 = SX + SW + SG
d.rectangle([x1, SY, x1 + SW, SY + SH], fill=TEAL)
text(x1 + 10, SY + 8, "150 DELEGATES", fb(26), GOLD)
text(x1 + 10, SY + 38, "BACK A RISK", fb(26), GOLD)
text(x1 + 10, SY + 68, "FRAMEWORK", fb(26), GOLD)
gx, gy, gr = x1 + SW - 62, SY + 58, 44
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=WHITE, width=2)
d.ellipse([gx - gr // 2, gy - gr, gx + gr // 2, gy + gr], outline=WHITE, width=1)
d.line([gx - gr, gy, gx + gr, gy], fill=WHITE, width=1)
d.arc([gx - gr, gy - gr // 2, gx + gr, gy + gr // 2], 0, 360, fill=WHITE, width=1)
# scene 3: Power Index bars
x2 = SX + 2 * (SW + SG)
d.rectangle([x2, SY, x2 + SW, SY + SH], fill=CREAM)
text(x2 + 10, SY + 4, "NARROWEST SINCE 2018", fb(12), BLACK)
gr2 = d.textlength("GAP 5.3", font=fb(12))
text(x2 + SW - 10 - gr2, SY + 4, "GAP 5.3", fb(12), (170, 130, 20))
bars = [("78.9", "US", NAVY, 70), ("73.6", "CHINA", DARKRED, 65), ("40.5", "INDIA", (170, 130, 20), 36)]
for j, (val, lab, col, bh) in enumerate(bars):
    bxc = x2 + 40 + j * 100
    text(bxc + 8, SY + 26, val, fb(16), BLACK)
    d.rectangle([bxc, SY + 48 + (70 - bh), bxc + 52, SY + 48 + 70], fill=col)
    lw = d.textlength(lab, font=fb(11))
    text(bxc + (52 - lw) / 2, SY + 54 + (70 - bh), lab, fb(11), WHITE)
# label strips under scenes
labels = ["KOSPI 4,708.54  \u00b7  -161 PTS", "UN  \u00b7  BRIDGETOWN", "ASIA POWER INDEX 2026"]
for j, lab in enumerate(labels):
    lx = SX + j * (SW + SG)
    d.rectangle([lx, SY + SH, lx + SW, SY + SH + 18], fill=BLACK)
    text(lx + 8, SY + SH + 3, lab, fb(11), WHITE)

# ---------- hero text blocks ----------
heroes = [
    ("1", "AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE"),
    ("2", "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 back a risk framework.",
     "UNITED NATIONS"),
    ("3", "US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 \u2014 gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE"),
]
HY = SY + SH + 18 + 8
for j, (num, head, body, src) in enumerate(heroes):
    hx = SX + j * (SW + SG)
    d.ellipse([hx, HY, hx + 20, HY + 20], fill=RED)
    nw = d.textlength(num, font=fb(12))
    text(hx + (20 - nw) / 2, HY + 3, num, fb(12), WHITE)
    hl = wrap(head, fb(20), SW - 28)
    yy = HY
    for ln in hl[:2]:
        text(hx + 26, yy, ln, fb(20), BLACK)
        yy += 23
    bl = wrap(body, fr(12), SW - 6)
    yy = HY + 48
    for ln in bl[:2]:
        text(hx, yy, ln, fr(12), BLACK)
        yy += 15
    text(hx, HY + 82, src, fr(10), GRAY)
    cw = d.textlength("REPORTED", font=fb(10)) + 12
    d.rectangle([hx + SW - cw, HY + 80, hx + SW, HY + 94], fill=BLUE)
    text(hx + SW - cw + 6, HY + 82, "REPORTED", fb(10), WHITE)

# ---------- MORE OF THE DAY ----------
d.rectangle([0, 398, W, 414], fill=BLACK)
text(10, 401, "MORE OF THE DAY  \u2014  10 STORIES", fb(12), WHITE)

# ---------- cards (5 cols x 2 rows, 196 wide, 8 gap) ----------
cards = [
    ("AMERICAS", DARKRED, "BESSENT: NVIDIA ANSWERS", "Treasury wants answers.", "Reuters", "REPORTED"),
    ("FBI", DARKRED, "FBI PROBES NCIC HACK", "NCIC database hacked.", "AP", "REPORTED"),
    ("WHITE HOUSE", (170, 110, 30), "TRUMP: IRAN STRIKES MAY RESUME", "May resume in New Year.", "Reuters", "REPORTED"),
    ("MARKETS", BLUE, "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED"),
    ("SPORT", DARKRED, "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED"),
    ("SPORT", DARKRED, "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED"),
    ("LEGAL", (110, 60, 160), "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED"),
    ("TECH", (110, 60, 160), "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED"),
    ("EUROPE", (110, 60, 160), "POLAND: 3 MISSILES CROSSED AIRSPACE", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM"),
    ("SPACE", (100, 100, 100), "RUSSIAN NUCLEAR SATELLITE", "May carry a nuke.", "Reuters", "CLAIM"),
]
CW, CG = 196, 8
for i, (cat, col, head, body, src, chip) in enumerate(cards):
    cx = 6 + (i % 5) * (CW + CG)
    cy = 418 + (i // 5) * 68
    d.rectangle([cx, cy, cx + CW, cy + 14], fill=col)
    text(cx + 4, cy + 2, cat, fb(10), WHITE)
    nw2 = d.textlength(str(i + 1), font=fb(10))
    text(cx + CW - 4 - nw2, cy + 2, str(i + 1), fb(10), WHITE)
    hl = wrap(head, fb(12), CW - 4)
    yy = cy + 17
    for ln in hl[:2]:
        text(cx + 2, yy, ln, fb(12), BLACK)
        yy += 14
    text(cx + 2, cy + 44, body, fr(10), BLACK)
    text(cx + 2, cy + 55, src, fr(9), GRAY)
    cc = BLUE if chip == "REPORTED" else DARKRED
    cw = d.textlength(chip, font=fb(9)) + 10
    d.rectangle([cx + CW - cw, cy + 53, cx + CW, cy + 66], fill=cc)
    text(cx + CW - cw + 5, cy + 55, chip, fb(9), WHITE)

# ---------- WHERE IT HAPPENED / ALSO bar ----------
d.rectangle([0, 556, W, 572], fill=BLACK)
text(10, 559, "WHERE IT HAPPENED", fb(12), WHITE)
text(345, 559, "ALSO ON MONDAY", fb(12), WHITE)

# ---------- map ----------
MX, MY, MW, MH = 6, 576, 330, 186
d.rectangle([MX, MY, MX + MW, MY + MH], fill=(245, 245, 240))
for gx in range(MX, MX + MW + 1, 22):
    d.line([gx, MY, gx, MY + MH], fill=(225, 225, 220), width=1)
for gy in range(MY, MY + MH + 1, 22):
    d.line([MX, gy, MX + MW, gy], fill=(225, 225, 220), width=1)
d.ellipse([MX + 8, MY + 18, MX + 130, MY + 150], fill=GREEN)
d.ellipse([MX + 150, MY + 8, MX + 320, MY + 140], fill=GREEN)
d.ellipse([MX + 70, MY + 130, MX + 170, MY + 178], fill=GREEN)
pins = [(285, 595, 1), (35, 710, 2), (300, 620, 3), (55, 640, 4), (75, 670, 5),
        (230, 660, 6), (45, 600, 7), (25, 680, 8), (60, 720, 9), (85, 720, 10),
        (255, 630, 11), (270, 655, 12), (295, 670, 13)]
for px, py, n in pins:
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=DARKRED, outline=WHITE, width=1)
    nw3 = d.textlength(str(n), font=fb(9))
    text(px - nw3 / 2, py - 6, str(n), fb(9), WHITE)
legend = ["Pins 1\u201313: 1 Seoul  \u00b7  2 Bridgetown  \u00b7  3 Beijing",
          "4 Washington  \u00b7  5 New York  \u00b7  6 Tehran  \u00b7  7 Chicago",
          "8 SF  \u00b7  9 Denver  \u00b7  10 Austin  \u00b7  11 Warsaw  \u00b7  12 Kyiv  \u00b7  13 Moscow"]
ly = MY + MH + 4
for ln in legend:
    text(MX, ly, ln, fr(9), BLACK)
    ly += 12

# ---------- ALSO list ----------
also = [
    "Paris: 100+ back 2% billionaire tax", "Manchester: 12,000 cleared",
    "Zelenskyy: 165 missiles in a week", "COP31: the day after pact rejected",
    "Benghazi: UN demands port probe", "Israel unity talks resume",
    "Gaza: two killed in Israeli strike", "West Bank settler attacks",
    "Iran war: no deal in sight", "Lebanon seizes 264 kg explosives",
    "Bahrain: strike hits plant, 2 hurt", "Sudan: defences down drones",
    "DRC: fighting traps Ebola teams", "Bangladesh: Hasina jailed if she returns",
    "Seoul minister quits in exam row", "SK Telecom -7.3% as hype cools",
    "China eases margin rules", "Seoul readies 10T-won fund",
]
for i, item in enumerate(also):
    ax = 345 + (i // 9) * 340
    ay = 578 + (i % 9) * 22
    text(ax, ay, f"{14 + i}. {item}", fr(12), BLACK)

# ---------- DATE CHECK ----------
d.rectangle([6, 802, W - 6, 866], outline=DARKRED, width=2)
text(12, 807, "DATE CHECK", fb(13), DARKRED)
rt = "READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY"
rw = d.textlength(rt, font=fb(10))
text(W - 12 - rw, 809, rt, fb(10), DARKRED)
text(12, 826, "LEFT OUT \u2014 NOT 23 NOV: Dems 258 (22 Nov)  \u00b7  Sparta II fire (22 Nov)  \u00b7  El Chapo (22 Nov)  \u00b7  EU-Indonesia pact (21 Nov)  \u00b7  Nigeria boat (21 Nov)  \u00b7  ICJ Myanmar (19 Nov)",
     fr(11), BLACK)
text(12, 844, "NOT YET: Dymer search continues (14 missing)  \u00b7  4 House races uncalled  \u00b7  COP32 venue not set  \u00b7  WHO evacuating trapped Ebola staff",
     fr(11), BLACK)

# ---------- footer ----------
text(10, 874, "Sources: Reuters  \u00b7  AP  \u00b7  Bloomberg  \u00b7  AFP  \u00b7  Yonhap  \u00b7  BBC  \u00b7  WSJ  \u00b7  NYT  \u00b7  ESPN  \u00b7  Lowy Institute (Asia Power Index 2026).",
     fr(10), GRAY)
text(10, 888, "CHIPS: REPORTED = confirmed by wires.  CLAIM = one side's claim, not independently confirmed.  ONGOING = still developing.",
     fr(10), GRAY)
text(10, 902, "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn illustrations, not photographs.",
     fr(10), GRAY)

# ---------- bottom bar ----------
d.rectangle([0, 936, W, H], fill=BLACK)
bt = "THE WORLD TODAY  \u2014  Monday 23 November 2026  \u00b7  31 stories  \u00b7  6 regions"
bw = d.textlength(bt, font=fb(20))
text((W - bw) / 2, 962, bt, fb(20), GOLD)

img.save("entry.png")
print("saved entry.png", img.size)
