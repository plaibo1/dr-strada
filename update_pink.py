with open('/Users/leopold/projects/dr-strada/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# adding standard variables
text = text.replace(
    '--bg-highlight-mid: #D5E5DA;',
    '--bg-highlight-mid: #D5E5DA;\n    --accent-pink: #E85A7E;\n    --accent-pink-hover: #D44468;'
)

# Text accents
text = text.replace('h1 em { font-style: italic; color: var(--primary); }', 'h1 em { font-style: italic; color: var(--accent-pink); }')
text = text.replace('h2 em { font-style: italic; color: var(--primary); }', 'h2 em { font-style: italic; color: var(--accent-pink); }')
text = text.replace('.section-label {\n    display: inline-block;\n    font-size: 11px; font-weight: 500;\n    letter-spacing: .12em; text-transform: uppercase;\n    color: var(--primary-dark); margin-bottom: 16px;\n  }', '.section-label {\n    display: inline-block;\n    font-size: 11px; font-weight: 500;\n    letter-spacing: .12em; text-transform: uppercase;\n    color: var(--accent-pink); margin-bottom: 16px;\n  }')

# Small dots and stars
text = text.replace('.divider-dot  { width: 6px; height: 6px; border-radius: 50%; background: var(--primary-light); flex-shrink: 0; }', '.divider-dot  { width: 6px; height: 6px; border-radius: 50%; background: var(--accent-pink); flex-shrink: 0; }')
text = text.replace('.hero-badge span { width: 6px; height: 6px; border-radius: 50%; background: var(--primary-dark); }', '.hero-badge span { width: 6px; height: 6px; border-radius: 50%; background: var(--accent-pink); }')
text = text.replace('.review-stars { color: var(--primary-dark); font-size: 14px; letter-spacing: 2px; margin-bottom: 14px; }', '.review-stars { color: var(--accent-pink); font-size: 14px; letter-spacing: 2px; margin-bottom: 14px; }')

# Gradients (increasing brightness)
text = text.replace(
    'radial-gradient(circle, #F1B7B0 0%, transparent 70%)',
    'radial-gradient(circle, #FFA1B5 0%, transparent 70%)'
)
text = text.replace(
    'radial-gradient(circle, #FADBD8 0%, transparent 70%)',
    'radial-gradient(circle, #FFB8C9 0%, transparent 70%)'
)

# Photo frame gradient - adding bright pink in the middle
text = text.replace(
    'linear-gradient(145deg, #FADBD8 0%, #F1B7B0 40%, var(--primary) 100%)',
    'linear-gradient(145deg, var(--accent-pink) 0%, #FFB8C9 40%, var(--primary) 100%)'
)

# Format price non-featured
text = text.replace('.format-card:not(.featured) .format-price { color: var(--primary); }', '.format-card:not(.featured) .format-price { color: var(--accent-pink); }')

# Stat pill strong number
text = text.replace('.stat-pill strong { display: block; font-size: 20px; font-family: var(--serif); color: var(--primary); font-weight: 600; }', '.stat-pill strong { display: block; font-size: 20px; font-family: var(--serif); color: var(--accent-pink); font-weight: 600; }')

# Author avatar background
text = text.replace(
    '    background: var(--bg-highlight-mid);\n    display: flex; align-items: center; justify-content: center;\n    font-size: 16px; font-weight: 500; color: var(--primary);',
    '    background: #FFEDF1;\n    display: flex; align-items: center; justify-content: center;\n    font-size: 16px; font-weight: 500; color: var(--accent-pink);'
)

with open('/Users/leopold/projects/dr-strada/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Done.")
