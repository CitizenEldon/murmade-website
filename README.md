# MurMade - Local Small-Batch Bakery

A minimal, static-site built for Marianne's Home Baking Business.

## Local Development & Viewing

Since this is a fully static site (no backend server), you can view it directly in your browser:

1. Open the `public/` folder on your computer.
2. Double-click on `index.html` to open it in your default web browser.

Alternatively, for a better mobile testing experience or to ensure features work correctly, you can run a simple local web server:

```bash
cd public
python -m http.server 3000
```
Then visit `http://localhost:3000` in your web browser.

## Editing the Site

- **Styling (`public/css/style.css`)**: Modify colors, fonts, or responsive breakpoints here to adjust the overarching aesthetic.
- **Interactions (`public/js/script.js`)**: Modifies the mobile menu function and constructs the "mailto" logic for order requests.

### Updating the HTML (The Quick Way)
All HTML pages inside `public/` can simply be edited directly using a text editor (e.g. Visual Studio Code, TextEdit). Look for `<main>...</main>` to adjust the content. 
*Note:* The python generator script (`generate_html.py`) can also be used if you need to bulk-update headers/footers in the future!

### How to Update Dates & Offerings

- **Upcoming Schedule (`schedule.html`)**: Search for the dates currently listed (e.g. `February 21, 2026`) and swap them out manually inside `schedule.html`.
- **Menu Offerings (`menu.html`)**: Copy the `div.card` block of an existing item and update its text and `<img src="...">` path. 
- **Order Form Dates (`public/js/script.js` & `order.html`)**:
  - Open `order.html` and look for the `<select id="pickup-date">` snippet. Update the `<option>` values.
  - Doing this will automatically pass the correct dates into the mailto generator.

## Important Note

- This website implements the **"mailto"** fallback approach since a backend server is not available and user input is kept totally static. This generates an email in the customer's native mail client but does NOT handle database submissions automatically. The site provides a clear expectation about the lack of ordering guarantees.
