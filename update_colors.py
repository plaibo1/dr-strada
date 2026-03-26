import re

with open('/Users/leopold/projects/dr-strada/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Replace shadow rgb
text = text.replace('185,82,110', '74,107,83')

# 2. Replace a specific hex background
text = text.replace('background: #a24560;', 'background: var(--primary-dark);')

# 3. Replace nav background
text = text.replace('rgba(253,232,238,.88)', 'rgba(232, 240, 234, .88)')

# 4. Replace variable usages (do this before redefining the root variables if we want to trace them, or after... it doesn't matter for `var(...)` strings)
text = text.replace('var(--rose-deep)', 'var(--primary)')
text = text.replace('var(--rose-dark)', 'var(--primary-dark)')
text = text.replace('var(--rose)', 'var(--primary-light)')
text = text.replace('var(--blush-mid)', 'var(--bg-highlight-mid)')
text = text.replace('var(--blush)', 'var(--bg-highlight)')

# 5. Redefine :root values
root_replacements = {
    '--rose:      #F2A7B8;': '--primary-light: #A4BBAA;',
    '--rose-dark: #D97B96;': '--primary-dark: #324C3A;',
    '--rose-deep: #B8526E;': '--primary: #4A6B53;',
    '--blush:     #FDE8EE;': '--bg-highlight: #E8F0EA;',
    '--blush-mid: #F9D0DC;': '--bg-highlight-mid: #D5E5DA;',
    '--cream:     #FDF7F4;': '--cream: #F4F7F5;',
    '--warm-white:#FFFAF8;': '--warm-white: #FAFCFA;',
    '--text:      #2E1A22;': '--text: #1B2B22;',
    '--text-mid:  #6B3D4E;': '--text-mid: #496554;',
    '--text-soft: #A07080;': '--text-soft: #7C9987;',
    '--border:    #F0C9D4;': '--border: #CDE0D4;'
}
for k, v in root_replacements.items():
    text = text.replace(k, v)

# 6. Apply pink accents to gradients
# #hero::before
text = text.replace(
    'radial-gradient(circle, var(--bg-highlight-mid) 0%, transparent 70%)',
    'radial-gradient(circle, #F1B7B0 0%, transparent 70%)'
)

# #hero::after
text = text.replace(
    'radial-gradient(circle, var(--bg-highlight) 0%, transparent 70%)',
    'radial-gradient(circle, #FADBD8 0%, transparent 70%)'
)

# .photo-frame
text = text.replace(
    'linear-gradient(145deg, var(--bg-highlight-mid) 0%, var(--primary-light) 60%, var(--primary-dark) 100%)',
    'linear-gradient(145deg, #FADBD8 0%, #F1B7B0 40%, var(--primary) 100%)'
)

# #cta
text = text.replace(
    'linear-gradient(145deg, var(--primary) 0%, var(--primary-dark) 60%, var(--primary-light) 100%)',
    'linear-gradient(145deg, var(--primary-dark) 0%, var(--primary) 60%, #E08E84 100%)'
)

with open('/Users/leopold/projects/dr-strada/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done.")
