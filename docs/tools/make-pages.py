#!/usr/bin/env python3
"""Writes the pages of the Donna Freed site into site/. Run: python3 docs/tools/make-pages.py
The seeded pages /start/, /agents/ and /admin/ keep their own text (taken from the file as it stands);
the others are written here. Every claim carries its source on /about/. Plain British English, no dashes."""
import re, pathlib
S = pathlib.Path('site')
HOST = 'https://donna-freed.author.sovereignweb.site'
DESC = 'Writer and translator. Her books, her writing and her podcast.'
NAV = [('/books/', 'Books'), ('/podcast/', 'Podcast'), ('/writing/', 'Writing'), ('/about/', 'About'), ('/questions/', 'Questions')]
DESIGNS = [('1', 'Shelf'), ('2', 'Memoir'), ('3', 'Studio'), ('4', 'Translator'), ('5', 'Newsroom')]
FAMILY = '''<details class="family-credit">
  <summary>Sovereign Website</summary>
  <ul>
    <li><a href="/start/">Start here</a></li>
    <li><a href="/agents/">Use with your AI</a></li>
    <li class="family-gap"><a href="/admin/">How this site was made</a></li>
    <li><a href="https://sovereignwebsite.ai/">Sovereign Website</a></li>
    <li><a href="https://sovereignwebsite.org/">Principles</a></li>
    <li><a href="https://sovereignwebsite.site/">Hosted</a></li>
    <li><a href="https://hub.sovereignweb.site/">Hub</a></li>
    <li><a href="https://agents.sovereignweb.site/">Agents</a></li>
    <li><a href="https://vault.sovereignwebsite.site/">Vault</a></li>
    <li><a href="https://agenticcells.ai/">AgentiCCells</a></li>
    <li><a href="https://riskmandate.ai/">RiskMandate</a></li>
    <li><a href="https://newsroom.sgit.ai/">Newsroom</a></li>
  </ul>
</details>'''
FOOT = '''<footer>
<nav class="site-links" aria-label="About this site">
  <a href="/start/">Start here</a>
  <a href="/agents/">Use with your AI</a>
  <a href="/admin/">How this site was made</a>
  <a href="/policy/">How this site is governed</a>
</nav>
A sovereign website, made with the <a href="https://sovereignwebsite.org/">open pattern</a>. Source: <a href="https://github.com/SovereignWebsite/Site__Author__Donna-Freed">github.com/SovereignWebsite/Site__Author__Donna-Freed</a>.
</footer>'''

def page(path, title, desc, body, kicker=None):
    url = HOST + path
    full = 'Donna Freed' if path == '/' else f'{title} | Donna Freed'
    nav = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{t}</a>' for h, t in NAV)
    des = ''.join(f'<li><a href="?design={n}" data-design="{n}"{" aria-current=\"true\"" if n == "1" else ""}>{n} {t}</a></li>' for n, t in DESIGNS)
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Donna Freed">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{HOST}/assets/share/card-1200x630.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Donna Freed, writer and translator">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{full}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{HOST}/assets/share/card-1200x630.jpg">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="/assets/site.css">
<script src="/assets/design.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{FAMILY}
<header class="top">
  <a class="name" href="/">Donna Freed</a>
  <nav class="own" aria-label="This site">{nav}</nav>
</header>
<nav class="designs" aria-label="Choose a design"><span>Choose a design:</span><ul>{des}</ul></nav>
<aside class="draft" aria-label="Draft notice"><strong>Draft for Donna's approval.</strong> Written by the site's agent from public sources, each named on <a href="/about/">About</a>. She has not yet seen it. Nothing here is in her own words until she says so.</aside>
<main id="main">
{body}
{FOOT}
</main>
</body>
</html>
'''
    out = S / path.strip('/') / 'index.html' if path != '/' else S / 'index.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def wave():
    hs = [14, 22, 10, 26, 18, 30, 12, 24, 16, 28, 8, 20]
    bars = ''.join(f'<rect x="{(32 - h) / 2}" y="{4 + i * 7}" width="{h}" height="3" rx="1.5"/>' for i, h in enumerate(hs))
    return f'<svg viewBox="0 0 32 88" aria-hidden="true" focusable="false" fill="currentColor">{bars}</svg>'

def mark():
    return ('<svg viewBox="0 0 32 90" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
            '<path d="M4 6h8M4 14h14M4 22h10M4 30h12M28 60h-8M28 68h-14M28 76h-10M28 84h-12"/>'
            '<path d="M20 6C30 14 4 70 10 84" opacity=".7"/><path d="M18 14C28 24 6 62 14 76" opacity=".5"/></svg>')

SHELF = f'''<nav class="shelf-wrap" aria-label="The books, shown as a shelf of spines">
<div class="shelf">
<div class="bookend" aria-hidden="true"></div>
<a class="spine s-hard" href="/books/#hardback" aria-label="Duplicity, hardback edition"><span class="a" aria-hidden="true">Donna Freed</span><span class="t" aria-hidden="true">Duplicity</span><span class="e" aria-hidden="true">Hardback</span></a>
<a class="spine s-paper" href="/books/#paperback" aria-label="Duplicity, paperback edition"><span class="a" aria-hidden="true">Donna Freed</span><span class="t" aria-hidden="true">Duplicity</span><span class="e" aria-hidden="true">Paperback</span></a>
<a class="spine s-audio" href="/books/#audiobook" aria-label="Duplicity, audiobook edition"><span class="t" aria-hidden="true">Duplicity</span>{wave()}<span class="e" aria-hidden="true">Audiobook</span></a>
<a class="spine s-kafka" href="/books/#kafka" aria-label="The Metamorphosis and Other Stories, Kafka, translated by Donna Freed"><span class="a" aria-hidden="true">Kafka</span><span class="t" aria-hidden="true">The Metamorphosis</span>{mark()}</a>
<div class="bookend" aria-hidden="true"></div>
</div>
<div class="plank" aria-hidden="true"></div>
</nav>
<p class="shelf-note">Duplicity in three editions, and the Kafka translation. The spines are drawn for this site and are not the real book designs. Each one opens its section.</p>'''

# ---------- written pages ----------
page('/', 'Donna Freed', DESC, '''<section class="hero">
<div class="hero-in">
<div class="hero-head">
<div class="kicker">Writer and translator</div>
<h1><span>Donna</span> <span>Freed</span></h1>
</div>
<div class="hero-shelf">
''' + SHELF + '''
</div>
<div class="hero-lead">
<p class="lead">A New York native, a writer and a translator. Her translation of Kafka has been in print since 1996. She has written for The Oldie and the BBC, and co-presented the Radio Gorgeous podcast.</p>
<p class="src">Source: <a href="/about/#sources">Jewish Book Council author profile</a>, read 22 November 2026.</p>
<p class="buy"><a href="https://www.amazon.co.uk/Duplicity-Mothers-Secrets-Donna-Freed/dp/1739879430">Buy <em>Duplicity</em> now</a> <span>on Amazon UK, or see <a class="plain" href="/books/">all editions</a></span></p>
</div>
</div>
</section>
<div class="cards">
<div class="card"><h2><a href="/books/">Books</a></h2><p><em>Duplicity: My Mothers' Secrets</em>, a memoir from Muswell Press, and her translation of Kafka's <em>The Metamorphosis and Other Stories</em>.</p></div>
<div class="card"><h2><a href="/podcast/">Podcast</a></h2><p>Radio Gorgeous, where she has talked with writers about their books.</p></div>
<div class="card"><h2><a href="/writing/">Writing</a></h2><p>Her journalism, for The Oldie and the BBC. Links to follow when she chooses them.</p></div>
</div>
<h2>About this draft</h2>
<p>This is a first version, made so that Donna can see what a site of her own could be. The <a href="/designs/">five designs</a> above are five ways to read the same pages. Her photographs, her own words and the links she wants are what will make it hers; the <a href="/questions/">questions page</a> says what is needed.</p>''')

page('/books/', 'Books', 'Duplicity: My Mothers\' Secrets, and the Kafka translation.', '''<div class="books-head">
<div class="kicker">Books</div>
<h1>Books</h1>
</div>
<div class="books-shelf">
''' + SHELF + '''
</div>
<section class="book" id="duplicity" aria-labelledby="t-dup">
<div class="book-title">
<div class="kicker">A memoir</div>
<h2 id="t-dup">Duplicity: My Mothers' Secrets</h2>
<p class="pub">Muswell Press</p>
</div>
<div class="book-body">
<p class="lead">A memoir, published by Muswell Press, in three editions.</p>
<ol class="editions">
<li id="hardback" class="ed-hard"><span class="fmt">Hardback</span><span class="when">November 2022</span></li>
<li id="paperback" class="ed-paper"><span class="fmt">Paperback</span><span class="when">July 2023</span></li>
<li id="audiobook" class="ed-audio"><span class="fmt">Audiobook</span><span class="when">December 2023, read by the author</span></li>
</ol>
<p class="buy"><a href="https://www.amazon.co.uk/Duplicity-Mothers-Secrets-Donna-Freed/dp/1739879430">Buy now: hardback</a> <a href="https://www.amazon.co.uk/Duplicity-Mothers-Secrets-Donna-Freed-ebook/dp/B0BGQXQFN3">Buy now: Kindle</a> <span>on Amazon UK</span></p>
<p class="src">Source: retailer and publisher listings, for example the <a href="https://www.theportobellobookshop.com/9781739638290">paperback at The Portobello Bookshop</a> (ISBN 9781739638290), the <a href="https://jewishbookcouncil.org/book/duplicity-my-mothers-secrets">Jewish Book Council page</a> and the <a href="https://books.apple.com/audiobook/id1721198948">audiobook on Apple Books</a>, all read 22 November 2026. Dates and edition details are to be confirmed with Donna. Some listings spell the title "My Mother's Secrets"; she should say which is right.</p>
<p><strong>Her own words about the book:</strong> not yet supplied. This space is hers.</p>
</div>
</section>
<section class="book" id="kafka" aria-labelledby="t-kafka">
<div class="book-title">
<div class="kicker">In print since 1996</div>
<h2 id="t-kafka">Translation: Kafka</h2>
<div class="year" aria-hidden="true">1996</div>
</div>
<div class="book-body">
<p class="lead">She translated Franz Kafka's <em>The Metamorphosis and Other Stories</em>, in print since 1996, and listed as its translator in a Barnes &amp; Noble Classics edition.</p>
<p class="src">Sources: <a href="https://www.jewishbookcouncil.org/donna-freed">Jewish Book Council author profile</a> and <a href="https://www.librarything.nl/author/freeddonna">LibraryThing</a>, read 22 November 2026.</p>
</div>
</section>''')

page('/podcast/', 'Podcast', 'Radio Gorgeous, the podcast Donna Freed has co-presented.', '''<div class="kicker">Podcast</div>
<h1>Radio Gorgeous</h1>
<p class="lead">A podcast she has co-presented, in which she talks with writers about their work.</p>
<p class="src">Source: <a href="https://www.jewishbookcouncil.org/donna-freed">Jewish Book Council author profile</a>, read 22 November 2026.</p>
<h2>Some conversations</h2>
<p>Examples of episodes listed under her name on a podcast directory, read 22 November 2026:</p>
<ul class="episodes">
<li><a href="https://de.player.fm/series/radio-gorgeous/donna-freed-with-polly-samson-author-of-a-theatre-of-dreamers">Donna Freed with Polly Samson, author of A Theatre for Dreamers</a></li>
<li><a href="https://de.player.fm/series/radio-gorgeous/donna-freed-with-wanda-whiteley-author-of-the-goldhanger-dog">Donna Freed with Wanda Whiteley, author of The Goldhanger Dog</a></li>
<li><a href="https://de.player.fm/series/radio-gorgeous/part-2-donna-freed-with-christina-ford-author-of-in-search-of-mr-darcy">Part 2: Donna Freed with Christina Ford, author of In Search of Mr Darcy</a></li>
</ul>
<p class="note">The show's own home page, her current role and the episodes she wants to point to are for her to give. The links above are to a third-party directory, used until then.</p>''')

page('/writing/', 'Writing', 'Donna Freed has written for The Oldie and the BBC.', '''<div class="kicker">Writing</div>
<h1>Writing</h1>
<p class="lead">She has written for The Oldie and the BBC.</p>
<p class="src">Source: <a href="https://www.jewishbookcouncil.org/donna-freed">Jewish Book Council author profile</a>, read 22 November 2026.</p>
<p>No individual articles are listed yet. A search on 22 November 2026 found no Oldie piece under her name that could be cited, so this page waits for the pieces she wants to show, with her own links.</p>''')

page('/about/', 'About', 'What this site says about Donna Freed, and where each point comes from.', '''<div class="kicker">About</div>
<h1>About Donna Freed</h1>
<p class="lead">Everything here is a claim from a public source, named below. It becomes her biography only when she writes or approves it.</p>
<ul class="facts">
<li>A native of New York, a writer and a translator. <span class="src">Jewish Book Council profile; Google Books author overview.</span></li>
<li>Her Kafka translation has been in print since 1996. <span class="src">Jewish Book Council profile.</span></li>
<li>Has written for The Oldie and the BBC, and co-presented Radio Gorgeous. <span class="src">Jewish Book Council profile.</span></li>
<li>Has lived in London since 2005. <span class="src">Google Books author overview only, not yet confirmed by a second source.</span></li>
</ul>
<h2 id="sources">Sources and dates</h2>
<ul>
<li><a href="https://www.jewishbookcouncil.org/donna-freed">Jewish Book Council, Donna Freed</a>, read 22 November 2026.</li>
<li>Google Books author overview, seen 22 November 2026.</li>
<li><a href="https://www.librarything.nl/author/freeddonna">LibraryThing, Donna Freed</a>, read 22 November 2026.</li>
<li><a href="https://jewishbookcouncil.org/book/duplicity-my-mothers-secrets">Jewish Book Council, Duplicity: My Mothers' Secrets</a>, read 22 November 2026.</li>
<li><a href="https://www.theportobellobookshop.com/9781739638290">The Portobello Bookshop, Duplicity</a>, read 22 November 2026.</li>
<li><a href="https://books.apple.com/audiobook/id1721198948">Apple Books, Duplicity (audiobook)</a>, read 22 November 2026.</li>
</ul>
<h2>What is deliberately not here</h2>
<p>No photograph, no contact details and nothing about her family or private life. She agreed to a public site; anything beyond her work goes on only if she gives it for the site. Her photographs will appear when she, or the photographer, gives permission in writing.</p>
<h2>Not on the hub</h2>
<p>This site is not listed on the Sovereign Website hub, by the owner's decision.</p>''')

page('/questions/', 'Questions', 'What the site needs from Donna Freed.', '''<div class="kicker">Questions</div>
<h1>Questions for Donna</h1>
<p class="lead">This is a draft site for you to shape. Each answer below makes it more yours.</p>
<ol>
<li><strong>Your words.</strong> A short biography in your own voice, and a line about each book. We will use nothing we have written as yours without your approval.</li>
<li><strong>Photographs.</strong> Which photographs would you like, and do you give written permission for them? If another person took one, we need theirs. We use no picture of other people without their consent.</li>
<li><strong>Your books.</strong> Which titles, in which editions? Is <em>Duplicity</em> described, and in what words? Which spelling of the title is right?</li>
<li><strong>Writing and the podcast.</strong> Which articles and episodes do you want shown, with which links?</li>
<li><strong>Other work.</strong> Translations, talks, festivals or anything else you want listed.</li>
<li><strong>Links.</strong> Which accounts and pages, if any, may we link? We add none that you do not choose.</li>
<li><strong>Reaching you.</strong> Do you want a way for readers to contact you or your publisher, and which? We add no contact details unless you give them.</li>
<li><strong>The look.</strong> Which of the five designs do you like, or what would you change?</li>
</ol>
<p>Tell the person who made the site, or open an issue in <a href="https://github.com/SovereignWebsite/Site__Author__Donna-Freed/issues/new">the repository</a>. You can edit every page yourself: see <a href="/start/">Start here</a>.</p>''')

page('/designs/', 'Designs', 'Five designs for the same site, and how to choose one.', '''<div class="kicker">Designs</div>
<h1>Five designs, one site</h1>
<p class="lead">Every page carries the same five choices. Pick one with the control at the top; your choice is kept in this browser only.</p>
<div class="cards">
<div class="card"><h2>1 Shelf</h2><p>Deep ink blue, a large serif and a shelf of book spines. The default.</p></div>
<div class="card"><h2>2 Memoir</h2><p>Large italic titles on cream, with a bold berry accent.</p></div>
<div class="card"><h2>3 Studio</h2><p>Dark and close, like a microphone and a lamp.</p></div>
<div class="card"><h2>4 Translator</h2><p>Light type, hairlines and a lot of white, for a careful eye.</p></div>
<div class="card"><h2>5 Newsroom</h2><p>Masthead rules and columns, for a writer's byline.</p></div>
</div>
<p class="note">A design is the same words in a different dress. Without a script, design 1 shows. You can also open any page with <code>?design=3</code> on the end to share a choice.</p>''')

# ---------- seeded pages: keep their text, give them the shared look and the control ----------
for p, title, desc in [('/start/', 'Start here', 'How the owner takes over this site.'), ('/agents/', 'Use with your AI', 'How to use this site through your own AI agent or an LLM.'), ('/admin/', 'How this site was made', 'How this site was made: the request, the agents, the commits, the design rounds and the test runs.')]:
    f = S / p.strip('/') / 'index.html'
    src = f.read_text()
    m = re.search(r'<main id="main">\n(.*?)\n<footer>', src, re.S)
    if not m:
        raise SystemExit(f'cannot find main text in {f}')
    page(p, title, desc, m.group(1))
