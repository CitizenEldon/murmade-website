# Site Content Summary

## 1. Page Structure

The static site contains 7 distinct main pages located inside the `public/` directory:

1. **Home (`index.html`)**: Features the primary hero statement, upcoming market schedule, popular featured items (Jalapeno Cheddar Sourdough, Apple Cinnamon Rolls, Granola), a visual layout on how it works (Market vs. Order Request), and inferred customer testimonials.
2. **Menu / Offerings (`menu.html`)**: Focuses on showing the inferred offerings split into "Sourdough Breads & Loaves" and "Sweet & Savory Treats." Clear warnings noting prices vary and selection varies.
3. **Order Request (`order.html`)**: A minimal and static free-form workflow using `mailto` link generation via JavaScript (and a clipboard fallback). Prominently displays the "Order requests must be submitted by Wednesday" note.
4. **Markets / Schedule (`schedule.html`)**: Highlights the Saturday 10:00 AM – 2:00 PM timeframe and specific upcoming dates. Shows Fiddleheads Garden Center map via Google iFrame.
5. **About (`about.html`)**: Values-based narrative on small-batch, cottage food, local community focus, featuring the business name and Marianne as the founder, based on inferred context without over-promising details. 
6. **FAQ / Policies (`faq.html`)**: Lists core business boundaries (pre-requests vs. markets, cutoff rationale, allergens, no-delivery, large orders).
7. **Contact (`contact.html`)**: Clickable contact links, a Facebook external link, and expectations for response time to mitigate chaotic DMs.

## 2. Inferred Assumptions

- **Offerings:** Based on images provided from `MurMade Pictures` and `facebook_content.txt`. We categorized items such as *Jalapeno & Cheddar Sourdough Rustic Loaf*, *Seeded Whole Wheat Sourdough*, *Sourdough Garden Focaccia*, and *Sourdough Apple Cinnamon Rolls*.
- **Testimonials:** Inferred based on typical Facebook comments on small bakeries combined with the real comment logged ("Beautiful breads you have today!" - Lucky Penny Candle Company) modified to fit typical small-site quotes.
- **Prices:** Missing explicitly; omitted intentionally with a "Ask about an item's specific price" placeholder language and pushing them to check weekly Facebook highlights.
- **Aesthetic:** A modern "sourdough" color palette was defined: Warm Crust `#B26435`, Sourdough Crumb `#DAB289`, Garden Sage `#6F8B6C`, against a clean off-white `#FAF8F5`. Used *Poppins* via Google Web Fonts to match modern, rounded aesthetics. Images converted to WebP for modern performance rules.

## 3. Placeholders to Review

- **Prices (If desired later):** Edit `public/menu.html` or the python generator file to manually add numeric values. Currently denoted globally as varying based on quantity.
- **Form Output Target Date (`public/order.html` & `public/js/script.js`):** The exact pickup dates inside the `<select id="pickup-date">` are tied to the provided specs (Feb 21, Feb 28, Mar 7) and must be manually rotated every few weeks if operations continue past those dates.
- **Map Focus (`public/schedule.html`):** Tested the *Fiddleheads Garden Center* location to provide an embedded live Google Maps tile iframe. Check visually to confirm the placement matches your physical stall.
- **Testimonials (`public/index.html`):** Feel free to swap the paraphrased initial-based quotes if newer/better quotes arise on your Facebook page in the coming weeks.
