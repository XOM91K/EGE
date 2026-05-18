from pathlib import Path
import zipfile, math, html

out_dir = Path("/mnt/data/ege_svg_icons_1_27")
out_dir.mkdir(parents=True, exist_ok=True)

SIZE = 1024

COMMON_DEFS = '''
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#06164D"/>
      <stop offset="45%" stop-color="#0A3492"/>
      <stop offset="100%" stop-color="#4A148C"/>
    </linearGradient>
    <linearGradient id="panel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#122DA5"/>
      <stop offset="100%" stop-color="#24105F"/>
    </linearGradient>
    <linearGradient id="cyan" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#25F4FF"/>
      <stop offset="100%" stop-color="#2874FF"/>
    </linearGradient>
    <linearGradient id="violet" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#9D74FF"/>
      <stop offset="100%" stop-color="#4C21BF"/>
    </linearGradient>
    <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FFE979"/>
      <stop offset="100%" stop-color="#FF9000"/>
    </linearGradient>
    <linearGradient id="red" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#FF8E8E"/>
      <stop offset="100%" stop-color="#D01818"/>
    </linearGradient>
    <filter id="softShadow" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#000028" flood-opacity="0.48"/>
    </filter>
    <filter id="glowGold" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="9" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="glowCyan" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="7" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <style>
      .bg { fill: url(#bg); }
      .panel { fill: url(#panel); stroke: #45F0FF; stroke-width: 8; filter: url(#softShadow); }
      .cyan { fill: url(#cyan); }
      .violet { fill: url(#violet); }
      .gold { fill: url(#gold); }
      .red { fill: url(#red); }
      .white { fill: #EAF7FF; }
      .line { stroke: #6BB9FF; stroke-width: 20; stroke-linecap: round; opacity: .95; }
      .thin { stroke: #7F8FFF; stroke-width: 12; stroke-linecap: round; opacity: .9; }
      .stroke-cyan { stroke: #45F0FF; stroke-width: 18; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .stroke-gold { stroke: #FFC43D; stroke-width: 22; stroke-linecap: round; stroke-linejoin: round; fill: none; filter: url(#glowGold); }
      .symbol { fill: #F4FBFF; font-family: Arial, sans-serif; font-weight: 900; }
      .number { fill: #F8FCFF; font-family: Arial, sans-serif; font-weight: 900; }
    </style>
  </defs>
'''

def bg_and_number(n):
    return f'''
  <rect class="bg" x="0" y="0" width="1024" height="1024"/>
  <g opacity="0.65">
    <path d="M-110 860 L430 410" stroke="rgba(72,230,255,.16)" stroke-width="24" stroke-linecap="round"/>
    <path d="M-70 240 L490 430" stroke="rgba(72,230,255,.13)" stroke-width="20" stroke-linecap="round"/>
    <path d="M1120 110 L600 440" stroke="rgba(158,105,255,.18)" stroke-width="24" stroke-linecap="round"/>
    <path d="M1120 870 L610 530" stroke="rgba(158,105,255,.15)" stroke-width="24" stroke-linecap="round"/>
  </g>
  <g opacity="0.45">
    <circle cx="842" cy="110" r="8" fill="#9CA8FF"/><circle cx="884" cy="144" r="8" fill="#9CA8FF"/><circle cx="928" cy="110" r="8" fill="#9CA8FF"/>
    <circle cx="828" cy="188" r="8" fill="#9CA8FF"/><circle cx="878" cy="228" r="8" fill="#9CA8FF"/><circle cx="930" cy="188" r="8" fill="#9CA8FF"/>
    <circle cx="808" cy="270" r="8" fill="#9CA8FF"/><circle cx="860" cy="300" r="8" fill="#9CA8FF"/><circle cx="914" cy="270" r="8" fill="#9CA8FF"/>
  </g>
  <g filter="url(#softShadow)">
    <rect x="54" y="54" width="150" height="112" rx="0" fill="url(#gold)" stroke="#FFF2A6" stroke-width="6"/>
    <text x="129" y="134" text-anchor="middle" class="number" font-size="{82 if n < 10 else 70}">{n}</text>
  </g>
'''

def svg(title, n, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{SIZE}" height="{SIZE}" viewBox="0 0 1024 1024" role="img" aria-label="{html.escape(title)}">
  <title>{html.escape(title)}</title>
{COMMON_DEFS}
{bg_and_number(n)}
{body}
</svg>'''

def file_icon(x,y,w,h,fold=True, cls="white"):
    foldpath = f'<path d="M{x+w-110} {y}v110h110" fill="#CFEAFF"/>' if fold else ''
    return f'''
    <path d="M{x} {y}h{w-110 if fold else w}l{110 if fold else 0} {110 if fold else 0}v{h-110 if fold else h}c0 30-24 54-54 54H{x+54}c-30 0-54-24-54-54V{y+54}c0-30 24-54 54-54z" class="{cls}" filter="url(#softShadow)"/>
    {foldpath}
    '''

def monitor(x,y,w,h):
    return f'''
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" class="panel"/>
    <rect x="{x+w*0.42}" y="{y+h}" width="{w*0.16}" height="70" rx="18" fill="#123D9B"/>
    <path d="M{x+w*0.3} {y+h+70}h{w*0.4}" class="stroke-cyan" opacity=".55"/>
    '''

def grid_panel(x,y,w,h,cols=4,rows=4):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" class="panel"/>'
    for i in range(1,cols):
        xx=x+w*i/cols
        s += f'<path d="M{xx} {y}v{h}" stroke="#5876FF" stroke-width="7" opacity=".85"/>'
    for j in range(1,rows):
        yy=y+h*j/rows
        s += f'<path d="M{x} {yy}h{w}" stroke="#5876FF" stroke-width="7" opacity=".85"/>'
    return s

def star(cx,cy,r=40,color="url(#gold)"):
    pts=[]
    for i in range(10):
        a=math.radians(-90+i*36)
        rr=r if i%2==0 else r*0.43
        pts.append((cx+rr*math.cos(a),cy+rr*math.sin(a)))
    return '<path d="' + "M " + " L ".join(f"{px:.1f} {py:.1f}" for px,py in pts) + f' Z" fill="{color}" filter="url(#glowGold)"/>'

bodies = {}

# 1 info models
bodies[1] = '''
<g filter="url(#softShadow)">
  <rect x="210" y="210" width="250" height="200" rx="28" class="panel"/>
  <path d="M250 350 C310 280 350 400 420 270" class="stroke-gold"/>
  <rect x="560" y="190" width="300" height="220" rx="28" class="panel"/>
  <path d="M610 330h200M610 270h120M610 220h170" class="line"/>
  <path d="M210 570h220l70 115-70 115H210l-70-115z" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <circle cx="315" cy="685" r="58" class="cyan"/>
  <path d="M600 540h270v270H600z" class="panel"/>
  <path d="M600 630h270M600 720h270M690 540v270M780 540v270" stroke="#5876FF" stroke-width="7"/>
  <circle cx="690" cy="630" r="22" class="gold"/><circle cx="780" cy="720" r="22" class="gold"/>
</g>
'''

# 2 truth table logic
bodies[2] = '''
<g filter="url(#softShadow)">
  <rect x="180" y="190" width="330" height="470" rx="34" class="panel"/>
  <path d="M180 310h330M180 430h330M180 550h330M290 190v470M400 190v470" stroke="#5C7DFF" stroke-width="8"/>
  <circle cx="235" cy="250" r="26" class="cyan"/><circle cx="345" cy="250" r="26" class="gold"/>
  <circle cx="455" cy="370" r="26" class="cyan"/><circle cx="345" cy="490" r="26" class="gold"/>
  <text x="305" y="810" text-anchor="middle" class="symbol" font-size="105">0 1</text>
  <path d="M600 300h110c70 0 125 55 125 125s-55 125-125 125H600z" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <path d="M560 365h95M560 485h95M835 425h80" class="stroke-cyan"/>
</g>
'''

# 3 relational database search
bodies[3] = '''
<g filter="url(#softShadow)">
  <rect x="190" y="170" width="600" height="470" rx="36" class="panel"/>
  <path d="M190 270h600M190 370h600M190 470h600M340 170v470M520 170v470M670 170v470" stroke="#5B78FF" stroke-width="8"/>
  <rect x="220" y="205" width="90" height="32" rx="12" class="cyan"/>
  <rect x="370" y="405" width="120" height="32" rx="12" class="gold"/>
  <rect x="550" y="505" width="90" height="32" rx="12" class="cyan"/>
  <circle cx="690" cy="620" r="145" fill="none" stroke="#FFC43D" stroke-width="24" filter="url(#glowGold)"/>
  <path d="M770 700l140 140" stroke="#FFC43D" stroke-width="42" stroke-linecap="round"/>
  <path d="M275 735h300" class="stroke-cyan"/>
  <path d="M360 800h180" class="stroke-cyan" opacity=".7"/>
</g>
'''

# 4 encoding decoding
bodies[4] = '''
<g filter="url(#softShadow)">
  <path d="M80 340 C220 260 350 300 450 360" fill="none" stroke="#21D7FF" stroke-width="90" opacity=".78"/>
  <rect x="385" y="250" width="260" height="360" rx="48" class="panel"/>
  <path d="M465 380l-55 65 55 65M565 380l55 65-55 65" class="stroke-cyan"/>
  <path d="M645 420 C730 440 775 440 860 420" stroke="#FFC43D" stroke-width="54" stroke-linecap="round" filter="url(#glowGold)"/>
  <path d="M735 285h170c28 0 50 22 50 50v200c0 28-22 50-50 50h-58l-60 70v-70h-52c-28 0-50-22-50-50V335c0-28 22-50 50-50z" class="gold"/>
  <rect x="770" y="375" width="115" height="20" rx="10" fill="#8A5300" opacity=".45"/>
  <rect x="770" y="440" width="90" height="20" rx="10" fill="#8A5300" opacity=".45"/>
  <g fill="#EAF7FF" opacity=".9"><rect x="130" y="305" width="38" height="38" rx="6"/><circle cx="215" cy="330" r="20"/><path d="M278 305l30 52h-60z"/></g>
</g>
'''

# 5 natural algorithm/executor
bodies[5] = '''
<g filter="url(#softShadow)">
  <rect x="240" y="180" width="540" height="470" rx="48" class="panel"/>
  <path d="M320 270h260M320 350h210M320 430h290M320 510h170" class="line"/>
  <circle cx="685" cy="505" r="72" class="gold"/>
  <path d="M660 500l20 22 45-55" stroke="#fff" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="105" y="360" width="150" height="150" rx="26" class="cyan"/>
  <path d="M150 435h60M180 405v60" stroke="#09245E" stroke-width="18" stroke-linecap="round"/>
  <path d="M255 435h115" class="stroke-cyan"/>
  <path d="M690 650v110M635 705h110" class="stroke-gold"/>
  <rect x="610" y="760" width="160" height="95" rx="24" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
</g>
'''

# 6 Turtle/Kumir algorithms
bodies[6] = '''
<g filter="url(#softShadow)">
  <rect x="145" y="190" width="730" height="570" rx="34" class="panel"/>
  <path d="M250 650 C270 430 440 310 700 275" class="stroke-gold"/>
  <path d="M700 275l-55-25 18 58z" class="gold"/>
  <circle cx="315" cy="520" r="70" class="cyan"/>
  <path d="M285 545c35 30 80 30 115 0" stroke="#0D2C71" stroke-width="16" fill="none" stroke-linecap="round"/>
  <path d="M295 500h40M385 500h40" stroke="#0D2C71" stroke-width="12" stroke-linecap="round"/>
  <path d="M520 420h190M520 490h130M520 560h170" class="line"/>
  <circle cx="685" cy="620" r="44" class="gold"/>
</g>
'''

# 7 graphics/audio memory
bodies[7] = '''
<g filter="url(#softShadow)">
  <rect x="150" y="210" width="330" height="260" rx="34" class="panel"/>
  <circle cx="390" cy="285" r="34" class="gold"/>
  <path d="M190 430l110-115 70 75 60-60" class="stroke-cyan"/>
  <path d="M640 220v360" stroke="#45F0FF" stroke-width="36" stroke-linecap="round"/>
  <path d="M640 260 C775 260 775 405 640 405" stroke="#45F0FF" stroke-width="36" fill="none" stroke-linecap="round"/>
  <circle cx="570" cy="610" r="65" class="gold"/>
  <path d="M685 610h190" class="stroke-gold"/>
  <rect x="205" y="610" width="260" height="170" rx="30" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <rect x="255" y="660" width="35" height="80" rx="10" class="cyan"/><rect x="325" y="640" width="35" height="100" rx="10" class="gold"/><rect x="395" y="680" width="35" height="60" rx="10" fill="#8C5BFF"/>
</g>
'''

# 8 combinatorics itertools
bodies[8] = '''
<g filter="url(#softShadow)">
  <circle cx="300" cy="310" r="80" class="cyan"/><circle cx="510" cy="310" r="80" class="violet"/><circle cx="720" cy="310" r="80" class="gold"/>
  <path d="M380 310h50M590 310h50" class="stroke-cyan"/>
  <path d="M255 540 C360 455 490 455 595 540 C665 595 725 600 805 560" class="stroke-gold"/>
  <circle cx="255" cy="540" r="42" class="cyan"/><circle cx="420" cy="490" r="42" class="violet"/><circle cx="595" cy="540" r="42" class="gold"/><circle cx="805" cy="560" r="42" class="cyan"/>
  <text x="508" y="760" text-anchor="middle" class="symbol" font-size="120">×</text>
  <circle cx="405" cy="760" r="45" class="violet"/><circle cx="610" cy="760" r="45" class="gold"/>
</g>
'''

# 9 spreadsheet numeric info
bodies[9] = '''
<g filter="url(#softShadow)">
  <rect x="125" y="160" width="760" height="560" rx="34" class="panel"/>
  <path d="M125 260h760M125 360h760M125 460h760M125 560h760M275 160v560M435 160v560M595 160v560M755 160v560" stroke="#5876FF" stroke-width="7" opacity=".9"/>
  <rect x="305" y="395" width="95" height="28" rx="14" class="gold"/>
  <rect x="465" y="495" width="95" height="28" rx="14" class="cyan"/>
  <text x="260" y="835" class="symbol" font-size="115">fx</text>
  <rect x="620" y="760" width="250" height="150" rx="26" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <rect x="665" y="835" width="34" height="45" rx="8" class="cyan"/><rect x="725" y="800" width="34" height="80" rx="8" fill="#36B6FF"/><rect x="785" y="770" width="34" height="110" rx="8" class="gold"/>
</g>
'''

# 10 OS/text search
bodies[10] = '''
<g filter="url(#softShadow)">
  <path d="M220 160h320l125 125v430c0 32-26 58-58 58H220c-32 0-58-26-58-58V218c0-32 26-58 58-58z" class="white"/>
  <path d="M540 160v125h125" fill="#CFEAFF"/>
  <path d="M250 350h300M250 430h345M250 510h260M250 590h310" class="line"/>
  <circle cx="690" cy="575" r="145" fill="none" stroke="#FFC43D" stroke-width="24" filter="url(#glowGold)"/>
  <path d="M760 645l130 130" stroke="#FFC43D" stroke-width="42" stroke-linecap="round"/>
  <rect x="290" y="415" width="130" height="36" rx="18" class="gold"/>
</g>
'''

# 11 info volume message
bodies[11] = '''
<g filter="url(#softShadow)">
  <path d="M250 160h310l125 125v420H250z" class="white"/>
  <path d="M560 160v125h125" fill="#CFEAFF"/>
  <path d="M320 365h250M320 435h310M320 505h230" class="line"/>
  <rect x="570" y="590" width="260" height="220" rx="34" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <rect x="625" y="650" width="38" height="95" rx="10" class="cyan"/><rect x="690" y="650" width="38" height="95" rx="10" fill="#367CFF"/><rect x="755" y="650" width="38" height="95" rx="10" class="gold"/>
  <text x="235" y="785" class="symbol" font-size="105">i</text>
  <circle cx="250" cy="750" r="80" fill="none" stroke="#45F0FF" stroke-width="12"/>
</g>
'''

# 12 Turing machine
bodies[12] = '''
<g filter="url(#softShadow)">
  <rect x="125" y="330" width="770" height="190" rx="22" class="panel"/>
  <path d="M125 330h770M235 330v190M345 330v190M455 330v190M565 330v190M675 330v190M785 330v190" stroke="#5876FF" stroke-width="8"/>
  <text x="290" y="455" text-anchor="middle" class="symbol" font-size="82">0</text>
  <text x="400" y="455" text-anchor="middle" class="symbol" font-size="82">1</text>
  <text x="510" y="455" text-anchor="middle" class="symbol" font-size="82">1</text>
  <text x="620" y="455" text-anchor="middle" class="symbol" font-size="82">0</text>
  <path d="M455 260h110l60 70H395z" class="gold"/>
  <path d="M510 250v-110" class="stroke-gold"/>
  <rect x="380" y="650" width="260" height="130" rx="28" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <path d="M435 715h150" class="stroke-cyan"/>
</g>
'''

# 13 subnet mask
bodies[13] = '''
<g filter="url(#softShadow)">
  <circle cx="510" cy="340" r="210" fill="#1255B8" stroke="#45F0FF" stroke-width="8"/>
  <path d="M300 340h420M510 130c-80 95-80 325 0 420M510 130c80 95 80 325 0 420" stroke="#7DEEFF" stroke-width="8" opacity=".55" fill="none"/>
  <rect x="185" y="600" width="650" height="120" rx="28" fill="#EAF7FF" stroke="#8C5BFF" stroke-width="10"/>
  <rect x="230" y="635" width="95" height="50" rx="14" class="cyan"/><circle cx="350" cy="660" r="12" fill="#0B2358"/>
  <rect x="375" y="635" width="95" height="50" rx="14" class="cyan"/><circle cx="495" cy="660" r="12" fill="#0B2358"/>
  <rect x="520" y="635" width="95" height="50" rx="14" class="violet"/><circle cx="640" cy="660" r="12" fill="#0B2358"/>
  <rect x="665" y="635" width="95" height="50" rx="14" class="gold"/>
  <path d="M305 790h410" class="stroke-gold"/>
</g>
'''

# 14 positional systems
bodies[14] = '''
<g filter="url(#softShadow)">
  <rect x="120" y="285" width="310" height="250" rx="40" class="panel"/>
  <text x="275" y="435" text-anchor="middle" class="symbol" font-size="105">101</text>
  <rect x="460" y="355" width="150" height="110" rx="28" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <path d="M430 410h225" class="stroke-gold"/>
  <path d="M625 410l-58-45v90z" class="gold"/>
  <rect x="640" y="285" width="270" height="250" rx="40" class="panel"/>
  <text x="775" y="435" text-anchor="middle" class="symbol" font-size="115">A7</text>
  <circle cx="275" cy="610" r="38" class="cyan"/><circle cx="775" cy="610" r="38" class="gold"/>
  <path d="M313 610h424" class="stroke-cyan"/>
</g>
'''

# 15 logic algebra
bodies[15] = '''
<g filter="url(#softShadow)">
  <circle cx="260" cy="280" r="92" class="cyan"/><circle cx="450" cy="280" r="92" class="violet"/><circle cx="640" cy="280" r="92" class="gold"/>
  <text x="260" y="310" text-anchor="middle" class="symbol" font-size="76">A</text>
  <text x="450" y="310" text-anchor="middle" class="symbol" font-size="76">B</text>
  <text x="640" y="310" text-anchor="middle" class="symbol" font-size="76">C</text>
  <path d="M250 520h160c70 0 125 55 125 125s-55 125-125 125H250z" fill="url(#violet)" stroke="#45F0FF" stroke-width="8"/>
  <path d="M175 590h130M175 700h130M535 645h150" class="stroke-cyan"/>
  <path d="M720 560l80 85-80 85" class="stroke-gold"/>
</g>
'''

# 16 recurrence
bodies[16] = '''
<g filter="url(#softShadow)">
  <rect x="210" y="170" width="620" height="430" rx="44" class="panel"/>
  <path d="M300 280h250M300 360h340M300 440h230" class="line"/>
  <text x="330" y="755" class="symbol" font-size="98">F</text>
  <text x="400" y="775" class="symbol" font-size="58">n</text>
  <path d="M500 730h150" class="stroke-gold"/>
  <text x="685" y="755" class="symbol" font-size="98">F</text>
  <text x="755" y="775" class="symbol" font-size="58">n+1</text>
  <path d="M640 500 C760 540 795 660 720 760" class="stroke-cyan"/>
  <path d="M720 760l-20-70 70 22z" class="cyan"/>
</g>
'''

# 17 numeric sequence program
bodies[17] = '''
<g filter="url(#softShadow)">
  <rect x="230" y="165" width="560" height="520" rx="44" class="panel"/>
  <path d="M310 275h250M310 350h330M310 425h230M310 500h290M310 575h170" class="line"/>
  <path d="M140 350 C210 420 210 540 140 610" stroke="#45F0FF" stroke-width="30" fill="none" opacity=".45"/>
  <text x="135" y="335" class="symbol" font-size="78">5</text><text x="135" y="455" class="symbol" font-size="78">8</text><text x="135" y="575" class="symbol" font-size="78">2</text>
  <circle cx="705" cy="705" r="85" class="gold"/>
  <path d="M680 700l22 24 50-62" stroke="#fff" stroke-width="18" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</g>
'''

# 18 robot coins spreadsheet
bodies[18] = '''
<g filter="url(#softShadow)">
  <rect x="130" y="160" width="760" height="590" rx="28" class="panel"/>
  <path d="M130 278h760M130 396h760M130 514h760M130 632h760M282 160v590M434 160v590M586 160v590M738 160v590" stroke="#5876FF" stroke-width="7"/>
  <circle cx="358" cy="337" r="32" class="gold"/><circle cx="510" cy="455" r="32" class="gold"/><circle cx="662" cy="573" r="32" class="gold"/>
  <path d="M205 690 C340 570 470 520 662 573" class="stroke-gold"/>
  <rect x="180" y="685" width="110" height="95" rx="22" fill="#EAF7FF"/>
  <rect x="205" y="710" width="60" height="35" rx="10" fill="#0B245B"/>
  <circle cx="225" cy="728" r="7" class="cyan"/><circle cx="248" cy="728" r="7" class="cyan"/>
</g>
'''

# 19 game stones simple
bodies[19] = '''
<g filter="url(#softShadow)">
  <circle cx="280" cy="500" r="80" class="cyan"/><circle cx="430" cy="500" r="80" class="violet"/><circle cx="580" cy="500" r="80" class="gold"/>
  <path d="M280 365v-120h300v120" class="stroke-cyan"/>
  <circle cx="280" cy="245" r="50" class="cyan"/><circle cx="580" cy="245" r="50" class="gold"/>
  <path d="M430 500v170" class="stroke-gold"/>
  <circle cx="430" cy="700" r="55" fill="url(#red)"/>
  <path d="M700 250h130v300" class="stroke-cyan" opacity=".65"/>
  <circle cx="830" cy="550" r="44" class="violet"/>
</g>
'''

# 20 winning strategy
bodies[20] = '''
<g filter="url(#softShadow)">
  <circle cx="220" cy="610" r="62" class="cyan"/><circle cx="400" cy="610" r="62" class="violet"/><circle cx="580" cy="610" r="62" class="gold"/><circle cx="760" cy="610" r="62" class="red"/>
  <path d="M220 548v-150h180v150M400 548v-150h180v150M580 548v-150h180v150" class="stroke-cyan"/>
  <circle cx="400" cy="330" r="58" class="gold"/>
  <circle cx="580" cy="330" r="58" class="cyan"/>
  <path d="M490 200l42 85 94 14-68 66 16 93-84-44-84 44 16-93-68-66 94-14z" fill="url(#gold)" filter="url(#glowGold)"/>
  <path d="M305 790h410" class="stroke-gold"/>
</g>
'''

# 21 game tree complex
bodies[21] = '''
<g filter="url(#softShadow)">
  <circle cx="512" cy="180" r="58" class="gold"/>
  <path d="M512 238v90M512 328L320 450M512 328l192 122" class="stroke-cyan"/>
  <circle cx="320" cy="450" r="54" class="cyan"/><circle cx="704" cy="450" r="54" class="violet"/>
  <path d="M320 504l-130 120M320 504l100 120M704 504l-100 120M704 504l130 120" class="stroke-cyan" opacity=".85"/>
  <circle cx="190" cy="650" r="48" class="gold"/><circle cx="420" cy="650" r="48" class="red"/><circle cx="604" cy="650" r="48" class="gold"/><circle cx="834" cy="650" r="48" class="red"/>
  <path d="M170 790h700" class="stroke-gold"/>
  <text x="512" y="825" text-anchor="middle" class="symbol" font-size="70">WIN</text>
</g>
'''

# 22 parallel processes
bodies[22] = '''
<g filter="url(#softShadow)">
  <rect x="150" y="230" width="740" height="420" rx="34" class="panel"/>
  <path d="M230 330h180M230 450h250M230 570h130" class="line"/>
  <rect x="560" y="300" width="210" height="70" rx="20" class="cyan"/>
  <rect x="560" y="430" width="300" height="70" rx="20" class="gold"/>
  <rect x="560" y="560" width="150" height="70" rx="20" class="violet"/>
  <path d="M175 760h680" class="stroke-cyan"/>
  <path d="M260 720v80M510 720v80M760 720v80" class="stroke-gold"/>
  <circle cx="260" cy="760" r="22" class="gold"/><circle cx="510" cy="760" r="22" class="gold"/><circle cx="760" cy="760" r="22" class="gold"/>
</g>
'''

# 23 recursion branches/cycle
bodies[23] = '''
<g filter="url(#softShadow)">
  <rect x="240" y="150" width="520" height="360" rx="44" class="panel"/>
  <path d="M320 250h220M320 325h280M320 400h170" class="line"/>
  <path d="M500 510 C500 610 420 620 420 710" class="stroke-cyan"/>
  <path d="M500 510 C500 610 580 620 580 710" class="stroke-cyan"/>
  <circle cx="420" cy="745" r="58" class="gold"/><circle cx="580" cy="745" r="58" class="violet"/>
  <path d="M670 235 C780 310 770 450 670 500" class="stroke-gold"/>
  <path d="M670 500l10-65 55 35z" class="gold"/>
</g>
'''

# 24 string processing
bodies[24] = '''
<g filter="url(#softShadow)">
  <path d="M225 160h330l125 125v440H225z" class="white"/>
  <path d="M555 160v125h125" fill="#CFEAFF"/>
  <path d="M305 355h260M305 425h315M305 495h220M305 565h290" class="line"/>
  <rect x="360" y="410" width="140" height="34" rx="17" class="gold"/>
  <path d="M690 610h120l55 55-55 55H690l55-55z" class="violet"/>
  <text x="760" y="690" text-anchor="middle" class="symbol" font-size="82">S</text>
</g>
'''

# 25 integer brute force
bodies[25] = '''
<g filter="url(#softShadow)">
  <rect x="190" y="170" width="640" height="420" rx="44" class="panel"/>
  <path d="M280 280h250M280 355h320M280 430h210M280 505h280" class="line"/>
  <path d="M250 710h520" class="stroke-cyan"/>
  <circle cx="250" cy="710" r="46" class="cyan"/><circle cx="770" cy="710" r="46" class="gold"/>
  <path d="M380 665v90M510 665v90M640 665v90" class="stroke-gold" opacity=".75"/>
  <text x="510" y="825" text-anchor="middle" class="symbol" font-size="86">N</text>
</g>
'''

# 26 sorting
bodies[26] = '''
<g filter="url(#softShadow)">
  <rect x="190" y="610" width="90" height="150" rx="16" class="cyan"/>
  <rect x="330" y="520" width="90" height="240" rx="16" class="violet"/>
  <rect x="470" y="430" width="90" height="330" rx="16" class="gold"/>
  <rect x="610" y="330" width="90" height="430" rx="16" fill="url(#red)"/>
  <path d="M770 680V330" class="stroke-gold"/>
  <path d="M770 330l-42 55M770 330l42 55" class="stroke-gold"/>
  <rect x="225" y="205" width="520" height="120" rx="28" class="panel"/>
  <path d="M285 265h70M405 265h70M525 265h70M645 265h70" class="line"/>
</g>
'''

# 27 numeric sequence/clustering centroid
bodies[27] = '''
<g filter="url(#softShadow)">
  <g>
    <circle cx="275" cy="330" r="20" class="cyan"/><circle cx="330" cy="280" r="20" class="cyan"/><circle cx="370" cy="360" r="20" class="cyan"/><circle cx="300" cy="410" r="20" class="cyan"/>
    <circle cx="690" cy="330" r="20" class="gold"/><circle cx="735" cy="285" r="20" class="gold"/><circle cx="770" cy="370" r="20" class="gold"/><circle cx="705" cy="425" r="20" class="gold"/>
    <circle cx="510" cy="650" r="20" class="violet"/><circle cx="455" cy="710" r="20" class="violet"/><circle cx="570" cy="725" r="20" class="violet"/><circle cx="515" cy="780" r="20" class="violet"/>
  </g>
  <path d="M318 345m-95 0a95 95 0 1 0 190 0a95 95 0 1 0 -190 0" fill="none" stroke="#45F0FF" stroke-width="9" opacity=".75"/>
  <path d="M725 355m-100 0a100 100 0 1 0 200 0a100 100 0 1 0 -200 0" fill="none" stroke="#FFC43D" stroke-width="9" opacity=".75"/>
  <path d="M510 720m-100 0a100 100 0 1 0 200 0a100 100 0 1 0 -200 0" fill="none" stroke="#9D74FF" stroke-width="9" opacity=".75"/>
  <path d="M318 345l407 10M318 345l192 375M725 355L510 720" class="stroke-cyan" opacity=".35"/>
  <circle cx="318" cy="345" r="32" fill="#EAF7FF"/><circle cx="725" cy="355" r="32" fill="#EAF7FF"/><circle cx="510" cy="720" r="32" fill="#EAF7FF"/>
</g>
'''

files=[]
for n in range(1,28):
    title = f"ЕГЭ информатика — задание {n}"
    content = svg(title, n, bodies[n])
    path = out_dir / f"Task{n}.svg"
    path.write_text(content, encoding="utf-8")
    files.append(path)

readme = out_dir / "ege_icons_order.txt"
readme.write_text(
"SVG-иконки для заданий ЕГЭ по информатике 1–27.\n"
"Формат: квадратный SVG 1024×1024, без скругления внешних углов, с крупным номером задания.\n",
encoding="utf-8"
)

zip_path = Path("ege_svg_icons_1_27.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for p in files + [readme]:
        z.write(p, arcname=p.name)

print(f"Создано SVG: {len(files)}")
print(zip_path.as_posix())
