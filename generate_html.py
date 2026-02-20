import os

base_dir = "public"

header_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | MurMade - Local Small-Batch Bakery</title>
    <meta name="description" content="MurMade is a local small-batch bakery in the Dalton, Georgia metro area offering handmade baked goods, sourdough, and sweet treats.">
    
    <!-- Open Graph for Facebook/SEO -->
    <meta property="og:title" content="{title} | MurMade">
    <meta property="og:description" content="Local handmade sourdough breads, sandwiches, and treats in Dalton, GA.">
    <meta property="og:image" content="/assets/images/fulllogo_nobuffer[1].webp">
    <meta property="og:url" content="https://murmade.local/">
    <meta property="og:type" content="website">

    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <div class="nav-container">
            <a href="index.html" class="logo">
                <img src="assets/images/fulllogo_nobuffer[1].webp" alt="MurMade Logo">
            </a>
            <button class="nav-mobile-btn">☰</button>
            <nav class="nav-links">
                <a href="index.html">Home</a>
                <a href="menu.html">Menu</a>
                <a href="schedule.html">Schedule</a>
                <a href="order.html">Order Request</a>
                <a href="about.html">About</a>
                <a href="faq.html">FAQ</a>
                <a href="contact.html">Contact</a>
            </nav>
        </div>
    </header>
"""

footer_html = """
    <footer>
        <div class="footer-content">
            <div class="footer-col" style="text-align: center;">
                <h3 style="color: var(--color-secondary); font-size: 1.8rem; margin-bottom: 0.5rem; display: inline-block;">MurMade</h3>
                <p>Local small-batch baked goods.</p>
                <p>Dalton, Georgia Area</p>
                <p>
                    <a href="mailto:mariannemurry@gmail.com">mariannemurry@gmail.com</a>
                </p>
                <p><a href="tel:7064638552">706-463-8552</a></p>
            </div>
            <div class="footer-col">
                <h4 style="color: var(--color-secondary);">Quick Links</h4>
                <a href="menu.html">Menu & Offerings</a>
                <a href="schedule.html">Market Schedule</a>
                <a href="order.html">Request an Order</a>
                <a href="faq.html">FAQ</a>
            </div>
            <div class="footer-col">
                <h4 style="color: var(--color-secondary);">Connect</h4>
                <a href="https://www.facebook.com/profile.php?id=61579601194967" target="_blank" rel="noopener noreferrer">Facebook Page</a>
                <br>
                <div class="required-disclosure">
                    "Produced at a residential property that is exempt from state inspection. May contain allergens."
                </div>
            </div>
        </div>
        <div class="footer-legal">
            <p>&copy; 2026 MurMade. All rights reserved.</p>
        </div>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
"""

pages = {
    "index.html": {
        "title": "Home",
        "content": """
    <main>
        <div class="container">
            <section class="hero text-center" style="background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.5)), url('assets/images/PXL_20250920_123340336.webp') center/cover; padding: 6rem 1.5rem;">
                <h1 style="color: #FFF; font-size: 3.5rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">Small batches...big flavors!</h1>
                <p style="color: #F8F8F8; text-shadow: 1px 1px 3px rgba(0,0,0,0.6); max-width: 700px; font-size: 1.3rem;">Bringing warmth and comfort to the Dalton metro area with locally crafted sourdough, cookies, and delicious creations.</p>
                <div class="hero-buttons mt-4">
                    <a href="order.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2rem;">Request an Order</a>
                    <a href="schedule.html" class="btn" style="background-color: rgba(255,255,255,0.9); color: #333; font-size: 1.1rem; padding: 1rem 2rem; border-radius: 30px;">Find Us Saturday</a>
                </div>
            </section>
            
            <section class="banner" style="background-color: var(--color-primary);">
                <h3>Next Market: Saturday, Feb 21, 2026</h3>
                <p>10:00 AM – 2:00 PM @ Fiddleheads Garden Center</p>
            </section>
            
            <section class="mb-4">
                <div class="section-title">
                    <h2 style="font-size: 2.5rem; color: #2D2721;">Featured Market Favorites</h2>
                    <p style="color: var(--color-text-light); max-width: 600px; margin: 0 auto; font-size: 1.1rem;">A glimpse at what makes our Saturday mornings so special.</p>
                </div>
                <div class="grid-3">
                    <div class="card">
                        <img src="assets/images/PXL_20250920_072425221.webp" alt="Traditional Sourdough Rustic Loaf" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Traditional Sourdough Loaves</h3>
                            <p class="card-desc">Our beautifully scored classic sourdough loaves built with simple ingredients.</p>
                            <div class="card-tags">
                                <span class="tag">Everyday Staple</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <img src="assets/images/PXL_20250913_082123134.webp" alt="Sourdough Cinnamon Rolls" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Sourdough Cinnamon Rolls</h3>
                            <p class="card-desc">Glistening with sweet vanilla icing, these massive rolls are a weekend treat.</p>
                            <div class="card-tags">
                                <span class="tag">Sweet Treat</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <img src="assets/images/garden_focaccia.png" alt="Garden Focaccia" class="card-img" loading="lazy" style="object-position: center;">
                        <div class="card-content">
                            <h3 class="card-title">Sourdough Garden Focaccia</h3>
                            <p class="card-desc">A fluffy center with an olive oil crust, topped beautifully with garden fresh veggies.</p>
                            <div class="card-tags">
                                <span class="tag">Savory</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                         <img src="assets/images/PXL_20250912_153308903.webp" alt="Gourmet Cookies" class="card-img" loading="lazy">
                         <div class="card-content">
                             <h3 class="card-title">Gourmet Cookies</h3>
                             <p class="card-desc">Thick, chocolatey, and simply irresistible small-batch cookies.</p>
                             <div class="card-tags">
                                 <span class="tag">Bestseller</span>
                             </div>
                         </div>
                    </div>
                    
                    <div class="card">
                        <img src="assets/images/PXL_20250920_035302658.webp" alt="Jalapeno Cheddar Sourdough" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Jalapeño & Cheddar Loaf</h3>
                            <p class="card-desc">A spicy, cheesy twist packed with fresh jalapeños throughout the crumb.</p>
                            <div class="card-tags">
                                <span class="tag">Savory Inclusions</span>
                            </div>
                        </div>
                    </div>
                    
                    <div class="card">
                        <img src="assets/images/PXL_20250922_134234358.webp" alt="Fresh Muffins" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Fresh Muffins</h3>
                            <p class="card-desc">Delicious, tall bakery-style muffins in blueberry, strawberry, and more.</p>
                            <div class="card-tags">
                                <span class="tag">Morning Treat</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-4" style="margin-top: 3rem;">
                    <a href="menu.html" class="btn btn-primary" style="font-size: 1.1rem; padding: 1rem 2rem;">Explore Full Menu</a>
                </div>
            </section>
            
            <section class="panel text-center" style="margin-top: 5rem;">
                <h2 style="font-size: 2.5rem;">How It Works</h2>
                <div class="grid-2 mt-4" style="text-align: left; gap: 3rem;">
                    <div>
                        <h3 style="color: var(--color-primary); font-size: 1.5rem;">1. Buy at the Market</h3>
                        <p style="font-size: 1.1rem;">Join us on Saturdays at Fiddleheads Garden Center from 10am to 2pm. Come early for the best selection, as quantities are limited and sell out fast!</p>
                        <a href="schedule.html" class="btn btn-outline" style="margin-top: 1rem;">View Schedule</a>
                    </div>
                    <div>
                        <h3 style="color: var(--color-primary); font-size: 1.5rem;">2. Request by Wednesday</h3>
                        <p style="font-size: 1.1rem;">Can't make it early? Submit an order request by Wednesday for Saturday pickup. Simply wait for your confirmation email to know your goods will be waiting for you.</p>
                        <a href="order.html" class="btn btn-primary" style="margin-top: 1rem;">Order Request Form</a>
                    </div>
                </div>
            </section>

            <section class="mb-4 text-center" style="margin-top: 5rem; margin-bottom: 5rem;">
                <h2 style="font-size: 2.5rem;">What Locals Say</h2>
                <div class="grid-3 mt-4 text-left">
                    <div class="panel" style="padding: 2rem; margin-bottom: 0; box-shadow: var(--shadow-sm); border: none; background-color: white;">
                        <p style="font-size: 1.1rem; color: #444;"><em>"Beautiful breads you have today!"</em></p>
                        <p style="margin-top: 1.5rem; color: var(--color-primary);"><strong>- L. P.</strong></p>
                    </div>
                    <div class="panel" style="padding: 2rem; margin-bottom: 0; box-shadow: var(--shadow-sm); border: none; background-color: white;">
                        <p style="font-size: 1.1rem; color: #444;"><em>"The apple cinnamon rolls were incredible. The organic apples made a huge difference."</em></p>
                        <p style="margin-top: 1.5rem; color: var(--color-primary);"><strong>- M. B.</strong></p>
                    </div>
                    <div class="panel" style="padding: 2rem; margin-bottom: 0; box-shadow: var(--shadow-sm); border: none; background-color: white;">
                        <p style="font-size: 1.1rem; color: #444;"><em>"I always make sure to grab a sourdough sandwich at the Dalton Farmer's Market."</em></p>
                        <p style="margin-top: 1.5rem; color: var(--color-primary);"><strong>- S. J.</strong></p>
                    </div>
                </div>
            </section>
        </div>
    </main>
"""
    },
    "menu.html": {
        "title": "Menu",
        "content": """
    <main>
        <div class="container">
            <div class="section-title">
                <h1>Our Offerings</h1>
                <p style="font-size: 1.2rem;">When ordinary won't cut it, let me create it! Please allow 2-3 days' notice for sourdough items.</p>
            </div>
            
            <div class="mb-4" style="margin-top: 3rem;">
                <h2 style="font-size: 2rem; border-bottom: 2px solid var(--color-secondary); padding-bottom: 0.5rem; display: inline-block;">Sourdough Loaves</h2>
                <p style="color: var(--color-text-light); margin-top: 0.5rem;">Available as Sandwich Bread or Rustic Loaves.</p>
                <div class="grid-2 mt-4">
                    <div class="card">
                        <img src="assets/images/PXL_20250920_072425221.webp" alt="Traditional Sourdough" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Traditional ($10)</h3>
                            <p class="card-desc mb-2">Wholesome enough for toast, hearty enough for sandwiches, and delicious enough to enjoy on its own.</p>
                            <p style="font-size: 0.85rem; color: #555;"><strong>Ingredients:</strong> King Arthur Special Patent Flour (unbleached hard wheat flour, malted barley flour, niacin, reduced iron, thiamin mononitrate, riboflavin, folic acid), Sourdough Starter (flour, water), Organic Honey, Avocado Oil, Salt.</p>
                        </div>
                    </div>
                    <div class="card">
                        <img src="assets/images/PXL_20250920_035302658.webp" alt="With Inclusions" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">With Inclusions ($13)</h3>
                            <ul style="list-style: disc; margin-left: 1.5rem; color: var(--color-text-light); font-size: 0.95rem; line-height: 1.5;">
                                <li style="margin-bottom: 4px;"><strong>Jalapeño & Cheddar:</strong> Made with fresh jalapeños and sharp cheddar cheese.</li>
                                <li style="margin-bottom: 4px;"><strong>Croissant (butter):</strong> Enriched with real butter for a soft, flaky texture.</li>
                                <li style="margin-bottom: 4px;"><strong>Chocolate Chip:</strong> Embedded with delicious semi-sweet chocolate chips.</li>
                                <li style="margin-bottom: 4px;"><strong>Parmesan & Pepper:</strong> Infused with savory parmesan and cracked black pepper.</li>
                                <li style="margin-bottom: 4px;"><strong>Dill Pickle:</strong> Tangy dill pickles packed right into the sourdough crumb.</li>
                                <li style="margin-bottom: 4px;"><strong>Roasted Garlic:</strong> Whole roasted garlic folded into our rustic dough.</li>
                                <li><strong>Pesto:</strong> Perfectly balanced with a flavorful basil pesto swirl.</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <img src="assets/images/PXL_20251004_075942937.webp" alt="Specialty Loaves" class="card-img" loading="lazy" style="object-position: top;">
                        <div class="card-content">
                            <h3 class="card-title">Specialty Loaves ($15)</h3>
                            <ul style="list-style: disc; margin-left: 1.5rem; color: var(--color-text-light); font-size: 0.95rem;">
                                <li><strong>Seeded Whole Wheat</strong> (Sandwich loaf only)</li>
                                <li><strong>Apple Pie</strong></li>
                                <li><strong>Cinnamon, Raisin, & Brown Sugar:</strong> Made with plump raisins, dark brown sugar, and rich cinnamon.</li>
                                <li>Pepperoni Pizza</li>
                                <li>Chocolate / Chocolate Chip</li>
                                <li>Chocolate Covered Cherry</li>
                                <li>Pumpkin Spice</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                         <img src="assets/images/sourdough_flight.png" alt="Sourdough Flight" class="card-img" loading="lazy" style="object-position: center;">
                         <div class="card-content">
                            <h3 class="card-title">Sourdough Flight ($20)</h3>
                            <p class="card-desc mb-2">Can't decide? Try a flight of four mini sandwich loaves! Choose your mix:</p>
                            <ul style="list-style: disc; margin-left: 1.5rem; color: var(--color-text-light); font-size: 0.95rem; line-height: 1.6;">
                                <li><strong>Sweet & Savory:</strong> Cinnamon Raisin, Apple Pie, Pesto, Jalapeño & Cheddar</li>
                                <li><strong>Savory:</strong> Pesto, Parmesan & Pepper, Jalapeño & Cheddar, Dill Pickle</li>
                                <li><strong>Sweet:</strong> Apple Pie, Cinnamon Raisin, Chocolate Covered Cherry, Chocolate Chip</li>
                                <li><strong>Mix and Match:</strong> Any flavors from the list above</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="mb-4" style="margin-top: 4rem;">
                <h2 style="font-size: 2rem; border-bottom: 2px solid var(--color-secondary); padding-bottom: 0.5rem; display: inline-block;">Sourdough Sweets & Savories</h2>
                <div class="grid-3 mt-4">
                    <div class="card">
                        <img src="assets/images/PXL_20250913_082123134.webp" alt="Sourdough Cinnamon Rolls" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Sourdough Cinnamon Rolls</h3>
                            <p class="card-desc"><strong>$30</strong> per pan of 8 large or 12 smaller.<br><br>
                            <strong>Specialty Flavors ($35):</strong> Strawberry, Cookies and Cream, Apple, or Orange Marmalade.</p>
                        </div>
                    </div>
                    <div class="card">
                        <img src="assets/images/garden_focaccia.png" alt="Garden Focaccia" class="card-img" loading="lazy" style="object-position: top;">
                        <div class="card-content">
                            <h3 class="card-title">Sourdough Garden Focaccia</h3>
                            <p style="font-size: 0.95rem;"><strong>8x8 Pan:</strong></p>
                            <ul style="margin-bottom: 0.5rem; list-style: none; font-size: 0.9rem;">
                                <li>Plain ($12) | Garlic & Rosemary ($13)</li>
                                <li>Apple Pie / Pepperoni Pizza / Garden Veggie ($17)</li>
                                <li>Specialty ($18)</li>
                            </ul>
                            <p style="font-size: 0.95rem;"><strong>9x13 Pan:</strong></p>
                            <ul style="list-style: none; font-size: 0.9rem;">
                                <li>Plain ($17) | Garlic & Rosemary ($18)</li>
                                <li>Apple Pie / Pepperoni Pizza / Garden Veggie ($25)</li>
                            </ul>
                        </div>
                    </div>
                    <div class="card">
                        <img src="assets/images/PXL_20250912_153308903.webp" alt="Cookies" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Cookies</h3>
                            <p class="card-desc">Decadent bakery cookies:</p>
                            <ul style="list-style: none; font-size: 0.95rem; line-height: 1.8;">
                                <li>• Chocolate Chip ($20/dz)</li>
                                <li>• Campfire S'mores ($22/dz)</li>
                                <li>• Chipotle Choc Chunk ($25/dz)</li>
                                <li>• Oatmeal Raisin ($30/dz)</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <div class="mb-4" style="margin-top: 4rem;">
                <h2 style="font-size: 2rem; border-bottom: 2px solid var(--color-secondary); padding-bottom: 0.5rem; display: inline-block;">Other Treats</h2>
                <div class="grid-3 mt-4">
                    <div class="card">
                        <img src="assets/images/PXL_20250922_134234358.webp" alt="Muffins" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Fresh Muffins</h3>
                            <p class="card-desc"><strong>$2 each</strong> (minimum 6 of the same flavor).<br><br>Available in Blueberry, Strawberry, Banana Nut, and Chocolate Chip.</p>
                        </div>
                    </div>
                    <div class="card">
                        <img src="assets/images/brioche_rolls.png" alt="Brioche Rolls" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Brioche Rolls & Buns</h3>
                            <p class="card-desc" style="margin-bottom: 0.5rem;"><strong>Sandwich Buns:</strong> $7 per pack of 4.</p>
                            <p class="card-desc"><strong>Dinner Rolls:</strong> $10 per dozen.</p>
                        </div>
                    </div>
                    <div class="card">
                        <img src="assets/images/sweet_savory_pecans.png" alt="Sweet Specialties" class="card-img" loading="lazy">
                        <div class="card-content">
                            <h3 class="card-title">Additional Specialties</h3>
                            <p style="font-size: 0.95rem; margin-bottom: 0.5rem;">• <strong>Sourdough Oatmeal Cream Pies:</strong> $20 per ½ dozen / $35 per dozen</p>
                            <p style="font-size: 0.95rem;">• <strong>Sweet & Savory Pecans:</strong> $20 per pound</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="panel text-center mt-4 mb-4" style="background-color: var(--color-bg);">
                <h3 style="color: var(--color-primary); font-size: 1.5rem;">Catering</h3>
                <p style="font-size: 1.1rem; max-width: 600px; margin: 0 auto;">Ask me about catering arrangements for events and gatherings.</p>
            </div>
            
            <div class="text-center mt-4 mb-4">
                <a href="order.html" class="btn btn-primary" style="padding: 1rem 2rem; font-size: 1.1rem;">Ready? Request an Order</a>
            </div>
        </div>
    </main>
"""
    },
    "order.html": {
        "title": "Order Request",
        "content": """
    <main>
        <div class="container">
            <div class="section-title">
                <h1>Request an Order</h1>
                <p>Submit your request for Saturday pickup. Limited quantities available.</p>
            </div>
            
            <div class="banner warning" style="max-width: 800px; margin: 0 auto 2rem auto; background-color: #DAB289;">
                <h3 style="color: #FFF; font-size: 1.3rem;">Friendly Reminder: Order requests must be submitted by Wednesday</h3>
                <p style="color: #FFF">I will confirm by email to let you know your order has been received! If you missed the cutoff, visit us early at the market for the best selection of extras.</p>
            </div>

            <div class="grid-2">
                <div class="panel">
                    <form id="order-form">
                        <div class="form-group">
                            <label for="name">Name *</label>
                            <input type="text" id="name" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="email">Email *</label>
                            <input type="email" id="email" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="phone">Phone (Optional)</label>
                            <input type="tel" id="phone" class="form-control">
                        </div>
                        <div class="form-group">
                            <label for="pickup-date">Desired Pickup Date * (Saturdays 10am - 2pm)</label>
                            <select id="pickup-date" class="form-control" required>
                                <option value="Feb 21, 2026">February 21, 2026</option>
                                <option value="Feb 28, 2026">February 28, 2026</option>
                                <option value="Mar 7, 2026">March 7, 2026</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label for="request">What would you like? *</label>
                            <textarea id="request" class="form-control" placeholder="E.g. 1 Traditional Sourdough Sandwich Loaf, 1 Pan of Cinnamon Rolls" required></textarea>
                            <small style="color: var(--color-text-light); display: block; margin-top: 0.5rem;"><a href="menu.html" target="_blank" style="text-decoration:underline;">View Menu</a> for pricing & flight options.</small>
                        </div>
                        <div class="form-group">
                            <label for="notes">Allergies / Notes (Optional)</label>
                            <textarea id="notes" class="form-control" placeholder="Any special requests or allergies" style="min-height: 80px;"></textarea>
                            <small style="color: var(--color-text-light); display: block; margin-top: 0.5rem;">Note: Items may contain allergens or undergo cross-contact.</small>
                        </div>
                        
                        <div class="form-group mt-4 text-center">
                            <button type="button" id="mailto-btn" class="btn btn-primary btn-block mb-3">Compose Email Request</button>
                            <p style="font-size: 0.9rem; color: #666; margin-bottom: 0.5rem;">If the button above doesn't open your email app:</p>
                            <button type="button" id="copy-btn" class="btn btn-secondary btn-block">Copy Request to Clipboard</button>
                            <p id="copy-feedback" style="display: none; color: green; margin-top: 0.5rem; font-weight: bold;">Copied! You can now paste it into an email to mariannemurry@gmail.com.</p>
                        </div>
                    </form>
                </div>
                
                <div>
                    <div class="panel" style="background-color: var(--color-bg); border-color: var(--color-secondary);">
                        <h3>Contact Info</h3>
                        <p>Feel free to reach out directly if you have questions.</p>
                        <p><strong>Email:</strong> <a href="mailto:mariannemurry@gmail.com" style="color: var(--color-primary)">mariannemurry@gmail.com</a></p>
                        <p><strong>Phone:</strong> <a href="tel:7064638552" style="color: var(--color-primary)">706-463-8552</a></p>
                        
                        <h4 class="mt-4 mb-2">Expectation Check</h4>
                        <ul style="list-style-type: disc; margin-left: 1.5rem; color: var(--color-text-light); line-height: 1.6;">
                            <li>Please allow 2-3 days' notice for sourdough items.</li>
                            <li>You will receive a confirmation email when I process your request.</li>
                            <li>Pickup is 10am - 2pm at <a href="schedule.html" style="text-decoration: underline;">Fiddleheads Garden Center</a>.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </main>
"""
    },
    "schedule.html": {
        "title": "Markets & Schedule",
        "content": """
    <main>
        <div class="container">
            <div class="section-title">
                <h1>Market Schedule</h1>
                <p>Find us at the market every Saturday. Arrive early for the best selection.</p>
            </div>
            
            <div class="grid-2">
                <div>
                    <div class="panel" style="height: 100%;">
                        <h2 style="color: var(--color-primary);">Upcoming Dates</h2>
                        <ul style="font-size: 1.1rem; line-height: 2; margin-bottom: 2rem; list-style: none;">
                            <li>📅 <strong>February 21, 2026</strong> — 10:00 AM – 2:00 PM</li>
                            <li>📅 <strong>February 28, 2026</strong> — 10:00 AM – 2:00 PM</li>
                            <li>📅 <strong>March 7, 2026</strong> — 10:00 AM – 2:00 PM</li>
                        </ul>
                        
                        <h2 style="color: var(--color-primary);">Location</h2>
                        <p style="font-size: 1.1rem;"><strong>Fiddleheads Garden Center</strong></p>
                        <p style="color: var(--color-text-light);">1237 W Walnut Ave<br>Dalton, GA 30720</p>
                        <a href="https://maps.google.com/?q=1237+W+Walnut+Ave,+Dalton,+GA+30720" target="_blank" class="btn btn-outline mt-3">View in Google Maps</a>
                        
                        <h3 class="mt-4" style="font-size: 1.25rem;">What to Expect</h3>
                        <p style="font-size: 0.95rem; color: var(--color-text-light); line-height: 1.6;">Selection is limited and items often sell out. Come early, say hi, and enjoy a beautiful day at the garden center!</p>
                        <a href="order.html" class="btn btn-primary mt-3">Request Preferred Pickup</a>
                    </div>
                </div>
                
                <div>
                    <img src="assets/images/PXL_20260110_170637015.webp" alt="Fiddleheads Garden Center Market" style="border-radius: var(--radius-lg); box-shadow: var(--shadow-md); width: 100%; height: 100%; object-fit: cover; min-height: 400px;" loading="lazy">
                </div>
            </div>
            
            <div class="mt-4 text-center">
                 <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3278.4357777271454!2d-84.99285092404368!3d34.74457787290518!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x885fa17eb2c1fffd%3A0xea8f7c97801cb180!2s1237%20W%20Walnut%20Ave%2C%20Dalton%2C%20GA%2030720!5e0!3m2!1sen!2sus!4v1700000000000!5m2!1sen!2sus" width="100%" height="450" style="border:0; border-radius: var(--radius-lg);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
        </div>
    </main>
"""
    },
    "about.html": {
        "title": "About",
        "content": """
    <main>
        <div class="container">
            <div class="section-title">
                <h1>About MurMade</h1>
                <p>Small batches...big flavors!</p>
            </div>
            
            <div class="grid-2 mt-4">
                <div style="display: flex; justify-content: center; align-items: center;">
                    <img src="assets/images/MurMade Cartoon.webp" alt="Marianne from MurMade" style="max-width: 90%; max-height: 400px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); display: block; margin: 0 auto;">
                </div>
                <div class="panel" style="display: flex; flex-direction: column; justify-content: center;">
                    <h2 style="color: var(--color-primary);">Community-Focused Baking</h2>
                    <p style="font-size: 1.1rem;">Welcome to MurMade! I'm Marianne, and I have a deep passion for creating delicious, high-quality, small-batch baked goods for the Dalton, Georgia community. Whether it's the perfect sandwich loaf, rustic sourdough, or a comforting cinnamon roll, everything is crafted locally with care.</p>
                    <p style="font-size: 1.1rem; margin-top: 1rem;">I believe in sharing good food with good neighbors. As a cottage food producer operating out of my residential kitchen, I pour genuine attention and dedication into every treat and loaf that reaches the market.</p>
                </div>
            </div>
        </div>
    </main>
"""
    },
    "faq.html": {
        "title": "FAQ & Policies",
        "content": """
    <main>
        <div class="container">
            <div class="section-title">
                <h1>Frequently Asked Questions</h1>
            </div>
            
            <div class="panel" style="max-width: 800px; margin: 0 auto;">
                <div class="faq-item">
                    <div class="faq-q">How do I buy your items?</div>
                    <div class="faq-a">For guaranteed treats, you can submit an Order Request online. Otherwise, come see me at the local market! Items are first-come, first-served on the table.</div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-q">What is the "Wednesday Cutoff" and why?</div>
                    <div class="faq-a">Sourdough is a multi-day process! To ensure that I have enough time to ferment, prep, shape, and bake your loaves and treats for Saturday morning, all requests must be submitted by the end of the day on Wednesday (a 2-3 day notice).</div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-q">What if I missed the Wednesday cutoff?</div>
                    <div class="faq-a">Don't worry! I always bake extras for the market. Arrive early at our market location (10:00 AM) to grab what you need.</div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-q">When and how do I pick up?</div>
                    <div class="faq-a">Pickup for requests is exclusively during market hours (Saturdays 10:00 AM – 2:00 PM) at Fiddleheads Garden Center.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">Do you deliver?</div>
                    <div class="faq-a">Delivery options are available at times for a modest fee! Please mention it in the notes of your order request to check availability.</div>
                </div>
                
                <div class="faq-item">
                    <div class="faq-q">Do you take custom orders outside the menu?</div>
                    <div class="faq-a">If you have a larger order for an event or a curated gift box request, send me an email to see if I am capable of accommodating it. Note: large requests require significant lead time depending on the item.</div>
                </div>

                <div class="faq-item">
                    <div class="faq-q">What about allergens?</div>
                    <div class="faq-a">Many of my baked goods contain common allergens like wheat (gluten), dairy, and occasionally tree nuts. Furthermore, <strong>all items are produced at a residential property that is exempt from state inspection and may be exposed to cross-contact with other allergens.</strong> For strict allergies, please consume with caution.</div>
                </div>
            </div>
            
            <div class="text-center mt-4">
                <p>Have a question not answered here?</p>
                <a href="contact.html" class="btn btn-primary" style="margin-top: 1rem; border-radius: 30px;">Contact Me</a>
            </div>
        </div>
    </main>
"""
    },
    "contact.html": {
        "title": "Contact",
        "content": """
    <main>
        <div class="container">
            <div class="section-title">
                <h1>Contact MurMade</h1>
                <p>Have questions? Reach out directly to Marianne.</p>
            </div>
            
            <div class="grid-2">
                <div class="panel text-center" style="display: flex; flex-direction: column; align-items: center; justify-content: center; background-color: var(--color-surface); border-color: var(--color-primary);">
                    <img src="assets/images/fulllogo_nobuffer[1].webp" alt="MurMade Logo" style="width: 150px; margin-bottom: 2rem;">
                    <a href="mailto:mariannemurry@gmail.com" class="btn btn-primary btn-block mb-3" style="max-width: 300px;">Email Me</a>
                    <a href="tel:7064638552" class="btn btn-secondary btn-block mb-3" style="max-width: 300px;">Call: 706-463-8552</a>
                    <a href="sms:7064638552" class="btn btn-outline btn-block mb-4" style="max-width: 300px;">Text: 706-463-8552</a>
                    
                    <a href="https://www.facebook.com/profile.php?id=61579601194967" target="_blank" style="text-decoration: underline; font-weight: 500; font-size: 1.1rem; color: var(--color-primary);">Connect on Facebook</a>
                </div>
                
                <div class="panel">
                    <h3 style="color: var(--color-text); font-size: 1.5rem; margin-bottom: 1.5rem;">Before you reach out...</h3>
                    <ul style="margin-left: 1.5rem; margin-top: 1rem; color: var(--color-text-light); line-height: 1.8; font-size: 1.05rem;">
                        <li><strong>Want to place an order?</strong> Use the <a href="order.html" style="color: var(--color-primary); text-decoration: underline;">Order Request Form</a> if possible, as it collects all the info I need!</li>
                        <li><strong>Wondering where to find me?</strong> Check the <a href="schedule.html" style="color: var(--color-primary); text-decoration: underline;">Market Schedule</a>.</li>
                        <li><strong>Have a question about allergens?</strong> Check our <a href="faq.html" style="color: var(--color-primary); text-decoration: underline;">FAQ Page</a> first.</li>
                        <li><strong>Response Times:</strong> As a busy baker, it may take me 24-48 hours to reply to non-urgent messages. Thank you for your patience!</li>
                    </ul>
                </div>
            </div>
        </div>
    </main>
"""
    }
}

for filename, data in pages.items():
    html_content = header_html.format(title=data["title"]) + data["content"] + footer_html
    file_path = os.path.join(base_dir, filename)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated {filename}")
