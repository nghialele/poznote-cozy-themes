# Poznote Cozy Themes

> **A small blanket fort for your notes.** 21 optional palettes for Poznote, because apparently the default theme button was not enough ways to procrastinate productively.

[Poznote](https://github.com/timothepoznanski/Poznote) is required. These are plain CSS token overrides: no plugins, no build step, no remote fonts, and absolutely no AI-powered beige gradients.

## Pick your reading weather

| Theme | Base | Mood |
|---|---|---|
| **The Hearth** | Light | Oat paper, walnut ink, cinnamon. A book and a mug that is still warm. |
| **The Greenhouse** | Light | Cream and sage. Your notes are thriving; the houseplants remain unconvinced. |
| **Rainy Window** | Light | Misty blue-grey with copper warmth. Excellent for staring thoughtfully at a TODO list. |
| **Library Moss** | Light | Parchment and leafy green. Quiet enough to hear the overdue books judging you. |
| **Sunday Linen** | Light | Airy cream and soft clay. The digital equivalent of fresh sheets. |
| **Cocoa Nook** | Light | Toasted cocoa and caramel. No actual cocoa included; we checked. |
| **Fireside Cardigan** | Light | Soft rosewood and woolly neutrals. Emotionally available, unlike your inbox. |
| **Bookshop Cat** | Light | Paper, old wood, and a plum accent. Cat hair not included. Probably. |
| **Toasted Chai** | Light | Spiced tea, honey, and warm wood. Cinnamon levels are legally moderate. |
| **Fern & Fig** | Light | Fern green with a quiet berry note. Botanically adjacent to doing your taxes. |
| **Peach Scone** | Light | Peach, cream, and a gentle terracotta accent. Crumbs are CSS-free. |
| **Apricot Jam** | Light | Golden apricot and oat. A cheerful spread, not a breakfast substitute. |
| **Cabin Quilt** | Light | Muted patchwork earth tones. Like borrowing a cabin without the plumbing problems. |
| **Midnight Library** | Dark | Ink-green shelves, parchment text, brass details. Sleep is for people without one more note. |
| **Emberlight** | Dark | Charcoal and ember orange. The fire is metaphorical; please keep it that way. |
| **Rain on the Roof** | Dark | Storm-slate and warm copper. Cozy weather, zero wet socks. |
| **Moss at Dusk** | Dark | Deep forest greens and soft leaf accents. A forest walk without the mosquitoes. |
| **Cocoa After Hours** | Dark | Dark cocoa and caramel light. The mug is imaginary; the late-night edits are real. |
| **Candlelit Desk** | Dark | Warm charcoal and candle-gold accents. No open flames near the laptop, please. |
| **Blue Hour Blanket** | Dark | Night-sky blue and soft silver. For notes made after saying “last one.” |
| **Pine Cabin** | Dark | Deep pine, quiet green, and woodsmoke warmth. You still have to do the dishes. |

The light set includes Sepia-adjacent earth tones, but keeps each one distinct: Hearth leans walnut/cinnamon, Cocoa Nook caramel, Chai honey, and Apricot golden fruit. Greenhouse is sage; Fern & Fig is greener and plum-accented; Library Moss is parchment/olive. If two feel too similar on your screen, theme choice is personal and nobody gets graded.

## Install in Poznote

1. Download the `.css` files from [`themes/light/`](themes/light/) and [`themes/dark/`](themes/dark/).
2. In Poznote, open **Settings → Admin Tools → Custom CSS path** and upload the files.
3. Open **Settings → Admin Tools → Theme list**. Add the uploaded files you want to offer.
4. Set every `themes/light/*.css` file to the **Light** base, and every `themes/dark/*.css` file to the **Dark** base. Save.
5. Use the theme button in the icon rail to cycle through the enabled themes. Each user chooses their own active theme.

**Important distinction:** Uploading a stylesheet stores it. Selecting it as the instance-wide **Custom CSS path** applies it to everyone; adding it to the **Theme list** makes it an optional theme. For this collection, upload the files and add them to Theme list—leave the global override set to **No custom CSS** unless you intentionally want one palette forced on everyone.

To undo: remove a theme from the Theme list, or choose any built-in theme. The built-ins—Light, Dark, Black, Lavender, Sepia, and Terminal—remain yours to keep. There is no theme lock-in contract. Not even a tiny one.

## Files

```text
themes/
├── light/   # 13 light palettes; pair these with Poznote's Light base
└── dark/    # 8 dark palettes; pair these with Poznote's Dark base
```

Each stylesheet stands alone. Upload only the themes you actually want; the admin theme list is global, while each user's selected theme is personal. Run `python3 tools/validate_themes.py` to check contrast and accent-channel consistency across the collection.

The original root-level paths `hearth.css` and `greenhouse.css` moved into `themes/light/` in this collection update. Use those new paths when downloading.

## Compatibility and references

Built against Poznote's documented `--pz-*` token contract. Token names were checked against upstream `tokens.css` on 18 November 2026; the connected instance reported Poznote **6.151.0**. Custom CSS themes require a Poznote version that supports uploaded CSS files and the Theme list.

- [Poznote personalization and custom CSS](https://github.com/timothepoznanski/Poznote#personalization)
- [Poznote CSS token guide](https://github.com/timothepoznanski/Poznote/blob/main/src/public/css/README.md)
- [Poznote design tokens](https://github.com/timothepoznanski/Poznote/blob/main/src/public/css/tokens.css)

## License

[WTFPL](LICENSE). Do what the heck you want with these themes. If they make your notes look like a particularly tasteful bakery, that is between you and your CSS variables.
