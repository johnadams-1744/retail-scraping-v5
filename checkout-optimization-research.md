# Checkout Conversion Optimization: Research & Recommendation Review

**Store context: Shopify Plus, majority-mobile audience, using AfterSell for checkout customization**

## Executive Summary

After researching current (2025-2026) checkout conversion rate optimization best practices, the original suggestions are **largely sound and well-aligned with current data**. However, there are refinements worth making to specific placement recommendations, one significant strategic addition regarding upsells, and several critical mobile-first and Shopify Plus-specific considerations that affect every recommendation.

---

## Shopify Plus & Mobile-First Considerations (NEW SECTION)

These two facts -- Shopify Plus checkout extensibility and a mobile-dominant audience -- materially affect every recommendation below.

### Shopify Plus Checkout Extensibility Constraints

Since August 28, 2025, Shopify Plus stores must use Checkout Extensibility instead of the deprecated `checkout.liquid`. All customizations (trust badges, upsells, custom content) are now placed via **Checkout UI Extensions** using the `purchase.checkout.block.render` target, positioned through the **Checkout Editor** in the admin.

Available block placement slots are:

| Reference | Location |
|---|---|
| `INFORMATION1` - `INFORMATION3` | Contact/address section (3 slots) |
| `DELIVERY1` - `DELIVERY2` | Shipping/delivery section (2 slots) |
| `PAYMENT1` - `PAYMENT4` | Payment section (4 slots) |

This means placement recommendations must map to actual available positions. You cannot arbitrarily place content "between the payment fields and the Pay Now button" unless a `PAYMENT` slot target supports that position. The recommendations below are adjusted accordingly.

### AfterSell: Available Checkout Widget Types

This store uses **AfterSell** for checkout customization. AfterSell provides the following checkout widget types, all placed via drag-and-drop in the Shopify Checkout Editor:

| Widget Type | Purpose | Relevant To |
|---|---|---|
| **Upsells** | Single product, multi-product (stack or carousel), or checkmark format | Upsell recommendation (Section 4) |
| **Rewards** | "Spend X get Y" reward/progress bar | Free shipping progress bar (Section 5) |
| **Trust Badges** | Security and trust icons with messaging | Shipping/Warranty, Secure Payments (Sections 1, 3) |
| **Testimonials** | Customer review social proof | Social Proof badge (Section 2) |
| **Cart Controls** | Variant selection, quantity adjustment, item removal | Not directly relevant to badges/upsells |
| **Notes** | Additional text messaging | Supplementary trust messaging |
| **Images** | Visual content blocks | Custom badge graphics if needed |
| **Text** | Custom text blocks | Fallback for custom messaging |

AfterSell also supports:
- **12+ smart triggers** for conditional display (e.g., show Gift Box upsell only during November-December, or show different trust messaging for first-time vs. returning customers).
- **Built-in A/B testing** for optimizing messages, offers, and layouts.
- **Post-purchase upsells** with one-click acceptance on the thank-you page.
- **White-glove onboarding** for Shopify Plus customers.

**Performance benchmark:** AfterSell checkout upsells generate an average of **$0.87 added per order**, with top users seeing **$450K/month** in revenue boosts.

All placement recommendations below are mapped to AfterSell's specific widget types.

### Mobile-First Imperatives

With most customers on mobile, every element added to checkout increases vertical scroll. This matters because:

- **Mobile checkout abandonment is 75.5%** -- roughly 5 points higher than overall averages (ScaleShopify).
- On mobile, **54% of users make action decisions without scrolling past the first ~550px** (Sacha Goureau mobile UX study).
- Adding too many custom form fields causes **18-22% abandonment** (EcomHint).
- Even a **one-second delay** in checkout load time reduces conversions by **7%** (SpeedBoostr).
- Tap targets must be at least **44-48px** for reliable one-handed use; 49% of mobile users hold their phone with one hand (InkBot Design).

**Practical implication:** Badge bloat is even more dangerous on mobile than desktop. Each badge/upsell block adds ~50-120px of vertical height. Three badges + one upsell widget could add 300-500px to the checkout, which on a ~667px mobile viewport means pushing the Pay Now button almost a full screen further down. Every element must earn its place.

### One-Page Checkout Recommendation

Shopify Plus now defaults to one-page checkout. For a jewelry store with a mobile-dominant audience, one-page checkout is strongly recommended:

- **7.5% average conversion improvement** over multi-page (Digismoothie).
- Some stores report **7-22% lift** after switching (EcomHint).
- Mobile shoppers specifically prefer one-page because it eliminates back-button drop-off (ShopLift, StoreDataLab).
- One-page checkout is best suited for **simpler product categories** -- jewelry (unlike apparel) typically does not require complex sizing decisions at checkout, making it an ideal fit.

### Shop Pay Priority

Shop Pay delivers **up to 50% higher conversion** vs. guest checkout and **at least 10% better** than other accelerated checkouts (Shopify). Returning Shop Pay users complete checkout over **90% of the time**. The express checkout section (Shop Pay, Apple Pay, Google Pay) is the single highest-converting element on the page. **Nothing should clutter or distract from it.**

---

## Original Suggestions vs. Research-Backed Recommendations

### 1. Shipping Policy & Warranty Trust Badges

**Original suggestion:** Either right below the express checkout options or right below the delivery details.

**Verdict: Slight refinement recommended.**

The two placement options are not equally strong. **Below delivery details is the better of the two**, and here is why:

- Trust signals placed immediately adjacent to the payment form drive **18% higher payment completion rates** (Digital Applied, 2026 UX Guide).
- The highest-leverage location for trust badges on checkout is **near the payment fields**, not earlier in the flow (TrustZ, SmartSMS Solutions).
- Shipping/warranty badges address the #1 abandonment driver: unexpected costs and unclear policies. Placing them *after* delivery details and *before* payment entry gives the shopper clarity on what they are paying for right before they commit.

**AfterSell implementation:** Use AfterSell's **Trust Badges** widget, placed at `DELIVERY2` (the second slot in the delivery section, which renders below the shipping method selector). This is the closest available target to "below delivery details."

**Mobile-specific note:** Keep this badge **compact and single-line** on mobile. Use a small icon + short text (e.g., a truck icon + "Free Shipping & 30-Day Returns" or a shield icon + "2-Year Warranty Included"). Avoid multi-line blocks or large graphics that push payment fields further down the viewport. On a ~667px mobile screen, every 50px matters.

**Refined recommendation:** `DELIVERY2` placement (below delivery details). Remove the "below express checkout" option entirely. The express checkout area must remain completely clean -- Shop Pay alone delivers a 50% conversion lift over guest checkout, and cluttering that zone with badges undermines its performance.

---

### 2. Social Proof Trust Badge (e.g., "1,000+ Five Star Reviews")

**Original suggestion:** Right above the payment details section or right below the Pay Now button.

**Verdict: Keep the first option, drop the second.**

- Social proof positioned near action/decision points eases **last-second purchase friction** (Zipify, ProveSource).
- Products with 5+ reviews boost purchase likelihood by **270%**; 1,000+ reviews correlate with **187.6% conversion lift** on Amazon Beauty (Zipify).
- **Above payment details** is the stronger placement because it provides reassurance right as the customer is about to enter their most sensitive information. It serves as a psychological "green light."
- **Below the Pay Now button** is *after the decision point*. By the time a customer scrolls past Pay Now, they have either already clicked it or decided not to. Social proof there has minimal influence on the conversion decision.

**AfterSell implementation:** Use AfterSell's **Testimonials** widget, placed at `PAYMENT1` (the first slot in the payment section, which renders above the payment method inputs). AfterSell's Testimonials widget is purpose-built for this -- it displays customer reviews/social proof natively.

**Mobile-specific note:** This is an area where mobile scroll budget becomes a concern. If the checkout is already feeling long due to upsell widgets (see section 4), **consider merging this into the Shipping/Warranty Trust Badges widget** as a single compact trust bar at `DELIVERY2`. For example: "Free Shipping | 2-Year Warranty | 1,000+ Five Star Reviews" on one line with small icons. This consolidation saves ~50-80px of vertical space on mobile, which can be the difference between the Pay Now button being visible or requiring an extra scroll.

**Refined recommendation:** `PAYMENT1` placement using AfterSell's Testimonials widget (above payment inputs) as a standalone element. However, if mobile scroll testing reveals the checkout is too long, consolidate social proof into the `DELIVERY2` Trust Badges widget and eliminate this as a separate element. Use AfterSell's built-in A/B testing to compare both versions.

---

### 3. Secure Payments Trust Badge (lock icon + payment logos)

**Original suggestion:** Right below the Pay Now button.

**Verdict: Consider moving it above the Pay Now button instead.**

- **19-25% of shoppers abandon carts** specifically because they do not feel their payment information is secure (CheckoutWC, Hashmeta).
- Security badges near payment fields increase conversion by **15-30%** for unfamiliar/newer brands (SmartSMS Solutions).
- The secure payments badge addresses anxiety about entering card details. Ideally, this reassurance should appear *before* the customer takes the action (clicking Pay Now), not after.
- Placing it **between the payment input fields and the Pay Now button** addresses the anxiety at exactly the right moment.
- Below Pay Now, the badge only serves as post-action reassurance for those who scroll past, which is less impactful.

**AfterSell implementation:** Use AfterSell's **Trust Badges** widget (a second instance, separate from the Shipping/Warranty one), placed at `PAYMENT3` or `PAYMENT4` (the later slots in the payment section render below the payment method inputs, closer to the Pay Now button). The exact slot depends on where the upsell widgets are placed -- secure payments should be the last element before Pay Now.

**Mobile-specific note:** This badge pulls double duty on mobile. Because Shopify's one-page checkout already shows recognizable payment logos (Visa, MC, Amex, etc.) as part of the native payment method selector, the secure payments badge should **complement rather than duplicate** that visual. Use a lock icon with a short message like "256-bit SSL Encrypted" or "Guaranteed Safe Checkout" rather than repeating the same card logos the customer just saw. This avoids redundancy and saves vertical space.

Also critical on mobile: ensure this badge does **not** push the Pay Now button below the fold. On a typical mobile viewport (~667px), if the customer has scrolled to the payment fields, the Pay Now button should ideally be visible without additional scrolling. A compact, single-line secure payments badge (lock icon + ~4 words) adds only ~40px; a large multi-icon banner adds 80-120px and may push Pay Now out of view.

**Refined recommendation:** `PAYMENT3` or `PAYMENT4` placement (below payment inputs, above Pay Now). Keep it to a single compact line on mobile. Prioritize a lock icon + concise trust message over repeating card brand logos that Shopify already displays natively.

---

### 4. Upsell Widgets

**Original suggestion:** One-click to add, no customization/sizing required. For jewelry: Order Protection, Gift Boxes, Cleaning/Care Kits, Matching Sets. Placement right above payment methods or right above Pay Now button.

**Verdict: Strong recommendation with one important addition and a mobile-critical design constraint.**

The core advice is excellent and aligns with current best practices:

- **One-click acceptance** is essential. Requiring re-entry of any information kills upsell conversion (Loopwork, AfterSell).
- **No customization/sizing** is a smart constraint. Upsells that require decisions (size, color) introduce friction and slow down checkout. This is especially wise for jewelry where sizing is complex.
- The **product categories are well-chosen** for jewelry:
  - **Order Protection**: Low-cost, high-margin, universal appeal.
  - **Gift Boxes**: Especially strong during occasion-based purchases (birthdays, anniversaries) which dominate jewelry buying.
  - **Cleaning/Care Kits**: Complementary, extends product life, low price point.
  - **Matching Sets**: Highest AOV potential; aligns with jewelry industry data showing matching items as top upsells (Identixweb, 2026).

**Placement refinement:** Above payment methods is the better of the two options. Placing upsells above Pay Now (but below payment fields) creates congestion in the most sensitive part of checkout. Above payment methods gives the upsell its own "space" and the customer encounters it before they start entering card details, when they are still in "shopping" mode rather than "paying" mode.

**AfterSell implementation:** Use AfterSell's **Upsells** widget (single product or checkmark format works best for low-friction items), placed at `PAYMENT1` or `PAYMENT2` (above the payment method selector). If the Testimonials widget (social proof) is also placed at `PAYMENT1`, stack upsells at `PAYMENT2` below it (or consolidate social proof into the delivery section Trust Badges widget to free up `PAYMENT1` for upsells -- see section 2).

For post-purchase: AfterSell natively supports **post-purchase one-click upsells** on the thank-you page. This is a core AfterSell feature and ideal for the Matching Set and Care Kit offers. AfterSell's post-purchase upsells use the customer's existing payment method on file, enabling true one-tap acceptance with no re-entry of information.

**Mobile-specific note -- this is critical:**

On mobile, the in-checkout upsell widget is the element most likely to cause problems. Here is why:

1. **Scroll budget:** Each upsell item with an image, title, price, and "Add" button takes ~80-120px of height. Showing 3 in-checkout upsells (Order Protection + Gift Box + Care Kit) adds **240-360px** to the checkout. On a ~667px mobile viewport, that is over half the screen dedicated to upsells, pushing payment fields and the Pay Now button significantly further down.

2. **Perception risk:** Too many upsells on mobile can feel pushy, especially for jewelry where the average order value is already high. Research shows in-checkout upsells risk **cart abandonment if perceived as overwhelming** (Amote, Cart-X).

3. **Thumb zone:** "Add" buttons must be at least **44-48px tall** for reliable one-handed tapping on mobile. Small, fiddly add buttons lead to mis-taps and frustration.

**Refined recommendation for mobile:**

- **Limit in-checkout upsells to 2 items maximum on mobile.** Prioritize the two highest-converting, lowest-friction options: Order Protection and Gift Box. These are low-cost, universally relevant, and require zero product knowledge to accept.
- **Move Care Kits and Matching Sets to post-purchase.** This keeps the checkout lean on mobile while still capturing the AOV uplift. Post-purchase one-click offers carry zero risk to the primary conversion and actually convert better for higher-consideration items.
- **Use a compact card layout** for in-checkout upsells: small thumbnail (or icon only), product name, price, and a large "Add" button on a single row. Avoid expanded product descriptions or multi-line layouts on mobile.
- **Consider a collapsible/accordion pattern** if more than 2 in-checkout upsells are desired. Show the top 1-2 expanded with others collapsed behind a "See more add-ons" toggle. This preserves scroll budget while keeping options available.

**Critical addition: Also implement post-purchase upsells via AfterSell.**

This is the biggest gap in the original recommendations, and AfterSell makes it easy since post-purchase upsells are one of its core features. Current data strongly supports a **hybrid approach**:

- Post-purchase one-click upsells convert at **4.7-30% acceptance rates** depending on implementation (Loopwork, AfterSell).
- They carry **zero risk to the primary conversion** since the order is already placed.
- Olivia Jewelry generated **$138,678 in extra revenue** through post-purchase upsells alone at a 3.68% conversion rate (ReConvert case study).
- On mobile, post-purchase upsells avoid the scroll-length penalty entirely since they appear on a separate page.
- AfterSell's post-purchase flow uses the customer's payment method on file, enabling true one-tap acceptance with no re-entry of information. Use AfterSell's smart triggers to show contextually relevant offers (e.g., Matching Set upsell only when the customer bought a single piece, Care Kit upsell for higher-value items).

**Refined recommendation:** Keep 2 in-checkout upsells at `PAYMENT1` or `PAYMENT2` using AfterSell's Upsells widget (Order Protection, Gift Box). Move Care Kits and Matching Sets to AfterSell's post-purchase one-click offers. This hybrid approach maximizes AOV while protecting the primary mobile conversion rate.

---

## 5. Free Shipping Progress Bar (NEW)

**Question: Where should a free shipping progress bar go on the checkout page?**

**Short answer: At the very top of the checkout, above or within the order summary area.**

### Why a Free Shipping Progress Bar Works

The free shipping progress bar leverages the **Goal Gradient Effect** -- people naturally accelerate effort as they approach a goal. Showing a customer "You're $12 away from free shipping!" is significantly more motivating than static text about a threshold. Data supports this:

- Dynamic free shipping progress bars on Shopify Plus checkout deliver an average **+10-12% conversion rate lift** (SplitDev, 2026).
- Broader checkout optimizations including shipping bars contribute to **+12-38% total revenue growth** (SplitDev).
- Stores see **10-15% AOV growth** from well-calibrated thresholds (SplitDev).
- Free shipping bars drive **15-20% conversion jumps** when they clearly communicate proximity to the threshold (BetterShipping).

### AfterSell Implementation

Use AfterSell's **Rewards** widget ("spend X get Y" reward bar). This is purpose-built for this use case. Configure it with:
- A clear threshold (recommended: **20-30% above the store's current AOV** -- high enough to motivate additional spending, low enough that 40-60% of customers can realistically reach it).
- Dynamic messaging: "You're $X away from FREE shipping!" when below threshold, and "You've unlocked FREE shipping!" when above.
- AfterSell's smart triggers can conditionally hide the bar for customers who already qualify.

### Placement

**`INFORMATION1`** -- the very first slot in the checkout, above the contact information fields. This is the optimal placement for three reasons:

1. **Immediate visibility:** On mobile, the progress bar appears in the first ~550px the customer sees (above the fold). It immediately communicates the shipping value proposition before any scrolling.
2. **AOV function, not trust function:** Unlike trust badges (which work best near the payment form), the free shipping bar serves an AOV/motivation function. Its job is to encourage the customer to go back and add more items -- or to reassure them they already qualify. This function is most effective at the top of the flow, before the customer mentally commits to "just checking out with what I have."
3. **Cart-level context:** The progress bar relates to the overall order value, which the customer is orienting to at the top of checkout (near the order summary). By the time they reach payment fields, the shipping threshold decision is already made.

**Alternative placement:** If `INFORMATION1` feels too aggressive or the store wants to keep the very top of checkout clean, place it within the order summary sidebar (on desktop) or at `DELIVERY1` (above the shipping method selector on mobile). The `DELIVERY1` position is contextually natural since the customer is already thinking about shipping at that point.

### Mobile-Specific Notes

- The Rewards bar is compact (~40-50px) and adds minimal scroll penalty.
- On mobile, if the customer already qualifies for free shipping, consider showing a brief "Free Shipping Included" confirmation instead of the full progress bar. This saves space and provides instant reassurance without the visual weight of an unnecessary progress element.
- If the store does NOT use a free shipping threshold (i.e., all orders ship free), skip the progress bar entirely and include "Free Shipping" in the Trust Badges widget at `DELIVERY2` instead.

### Threshold Calibration

- **Optimal threshold reach rate:** 40-60% of customers should reach the threshold. Higher than 80% means the threshold is set too low (leaving AOV on the table). Lower than 30% means it is discouraging and may feel unachievable (GrowthSuite).
- **Set at ~20-30% above current AOV.** For example, if the average jewelry order is $85, a $99 or $110 free shipping threshold encourages a meaningful but achievable bump.
- AfterSell supports **tiered rewards** -- consider stacking incentives (e.g., free shipping at $99, free gift box at $149) for extended motivation.

---

## 6. Free Shipping & Warranty Above the Fold -- Is There Merit? (NEW)

**Question: Is there value in placing Free Shipping and Warranty trust badges right near the top of checkout (above the fold on mobile) to reduce quick abandonment?**

**Short answer: Yes, there IS merit, but the type of trust signal matters. Shipping/cost information belongs near the top. Security information belongs near the payment form. Split them.**

### The Case FOR Above-the-Fold Placement

The data supports early trust signals reducing immediate checkout bounce:

- **61% of shoppers abandon** if trust signals are missing entirely (Emplicit).
- **48% of abandonment** is driven by unexpected extra costs (shipping, taxes) -- this is the #1 reason (Baymard). Addressing it immediately upon checkout entry, before the customer has time to doubt, is logical.
- Placing trust elements above the fold resulted in a **21% increase in add-to-cart rates** on product pages (Sacha Goureau). While this data is from product pages, the principle of "first-impression reassurance" applies to checkout.
- Victorian Trading saw an **8.2% conversion lift** by prominently displaying their free shipping threshold messaging across multiple touchpoints including checkout (ConversionTeam).
- **54% of mobile users make action decisions without scrolling** past the first ~550px. If the customer's first impression of the checkout is neutral (just form fields), you miss the opportunity to immediately reinforce their purchase decision.

### The Case AGAINST Moving Everything to the Top

However, there is an important nuance: **not all trust signals serve the same purpose at the same moment.**

- **Security badges** (lock icon, SSL, payment logos) address **payment anxiety**, which peaks when the customer sees the credit card fields -- not at the top of checkout. Baymard's research shows 18% of users explicitly look for security indicators specifically before entering card details. Placing a secure checkout badge at `INFORMATION1` would be premature -- the customer is not yet anxious about payment security; they are anxious about cost and commitment.
- **Shipping/returns/warranty** badges address **cost and commitment anxiety**, which peaks at the very beginning of checkout when the customer first sees their total. This IS the right anxiety to address above the fold.
- **Social proof** ("1,000+ Five Star Reviews") addresses **general purchase confidence**. This works well at the top OR near payment, but is slightly more impactful near payment where it serves as the final "green light."

### Refined Recommendation: A Split Strategy

For this mobile-dominant jewelry store, consider a **two-tier trust architecture:**

**Tier 1 -- Above the fold (`INFORMATION1` or `DELIVERY1`):**
Address cost/commitment anxiety immediately.

Use AfterSell's **Trust Badges** widget OR **Text** widget with:
- "Free Shipping on Orders $X+" or "Free Shipping Included" (if applicable)
- "Hassle-Free 30-Day Returns"
- "2-Year Warranty"

These three messages address the top abandonment driver (unexpected costs/unclear policies) at the exact moment the customer lands on checkout. On mobile, this occupies the first ~550px and gives the customer an immediate reason to continue rather than bouncing.

**Tier 2 -- Near the payment form (`PAYMENT3` or `PAYMENT4`):**
Address payment anxiety at the right moment.

Use AfterSell's **Trust Badges** widget with:
- Lock icon + "Guaranteed Safe Checkout" or "256-bit Encrypted"

This stays where it is most effective -- adjacent to the card input fields.

### Does This Conflict with the Previous Recommendation?

Partially. The previous recommendation placed the Shipping/Warranty trust badge at `DELIVERY2` (below delivery details). Moving it to `INFORMATION1` (above contact info) is a meaningful shift that changes the checkout flow:

- **`INFORMATION1` (above the fold):** Customer sees trust messaging FIRST, before entering any information. Best for reducing immediate bounce. Drawback: adds ~50px before the customer even starts filling in contact info, which on mobile pushes everything else slightly down.
- **`DELIVERY2` (below delivery details):** Customer sees trust messaging AFTER entering contact and shipping info, right before payment. Best for reinforcing commitment just before the most anxiety-inducing step. Drawback: customer may have already bounced before reaching this point.

**Recommendation:** If the store is seeing high checkout **bounce rates** (customers landing on checkout and immediately leaving), `INFORMATION1` is the better position -- it prevents the initial bounce. If checkout bounce is low but **payment abandonment** is high (customers fill in details but leave before paying), `DELIVERY2` is better -- it reinforces confidence at the critical transition.

**Best approach:** Use AfterSell's A/B testing to test both placements. Start with `INFORMATION1` if bounce data is unknown, as preventing the initial bounce has a larger absolute impact (you cannot convert someone who leaves immediately, but someone who makes it to payment fields is already somewhat committed).

### Updated Layout Options

**Option A-1: Above-the-Fold Trust (Recommended starting point)**

| Order | Element | AfterSell Widget | Target |
|---|---|---|---|
| 1 | Express Checkout (Shop Pay, Apple Pay, Google Pay) | Native | -- |
| 2 | **Free Shipping Progress Bar** (if threshold-based) | Rewards | `INFORMATION1` |
| 3 | **Shipping/Returns/Warranty Trust Bar** ("Free Shipping | 30-Day Returns | 2-Year Warranty") | Trust Badges | `INFORMATION2` |
| 4 | Contact Information | Native | -- |
| 5 | Delivery Details / Shipping Method | Native | -- |
| 6 | Upsell Widgets (Order Protection + Gift Box) | Upsells | `PAYMENT1` |
| 7 | Payment Details | Native | -- |
| 8 | Secure Payments Badge (lock + "Guaranteed Safe Checkout") | Trust Badges | `PAYMENT3` |
| 9 | Pay Now Button | Native | -- |
| -- | Post-purchase: Care Kit + Matching Set upsells | Post-purchase | Thank-you page |

**Option A-2: Below-Delivery Trust (If bounce rate is low but payment abandonment is high)**

Same as previous Option A layout, with trust badges at `DELIVERY2` instead.

---

## Important Cross-Cutting Principle: Avoid Badge Bloat (Especially on Mobile)

The original recommendations include 3 distinct badge types (Shipping/Warranty, Social Proof, Secure Payments) plus upsell widgets. Research shows:

- **3-4 badge types is the sweet spot.** More than this creates skepticism and can *decrease* conversion by 5-8% (SmartSMS Solutions).
- **6+ badges signal desperation**, not legitimacy. One case study showed removing 11 of 17 badges increased conversion from 2.1% to 3.4% - a 62% improvement.
- 85% of e-commerce customers look for trust badges, but are "turned off when a site has too many" (CyberSource).

**The original recommendations are within the safe zone** at 3 badge types, which is good. However, emphasize to the customer that they should not add additional badges beyond these three. If they already have other badges on the checkout page, they should audit and potentially remove them.

**Mobile-specific amplification:** Badge bloat is more damaging on mobile than desktop for two compounding reasons:

1. **Vertical scroll:** On desktop, badges sit alongside a spacious layout. On mobile (~375px wide), everything stacks vertically. Three separate badge blocks + two upsell widgets could add **400-600px** of height to the checkout, essentially adding an entire extra "screen" of scrolling before the customer reaches Pay Now.

2. **Cognitive overload on small screens:** Mobile users process information more quickly and impatiently. Research shows mobile checkout abandonment (75.5%) is already higher than desktop. Each additional visual element competes for limited attention.

**Practical recommendation for this store:** Since the audience is majority mobile, strongly consider the **consolidated trust bar** approach -- merging the Shipping/Warranty badge and Social Proof badge into a single compact element at `DELIVERY2`. This reduces the total from 3 separate badge blocks to 2, saving one full block (~60-100px) of vertical space. Example: a single bar with "Free Shipping | 2-Year Warranty | 1,000+ Five Star Reviews" with small icons. Then keep Secure Payments as a standalone compact badge at `PAYMENT3`/`PAYMENT4` right above Pay Now.

---

## Recommended Checkout Page Layout (Top to Bottom)

### Option A: Maximum Mobile Optimization (Recommended for this store)

Consolidates badges to minimize scroll length. Best for majority-mobile audiences.

| Order | Element | Shopify Plus Target | Approx. Mobile Height |
|---|---|---|---|
| 1 | **Express Checkout** (Shop Pay, Apple Pay, Google Pay) -- clean, uncluttered | Native (no extension) | ~120px |
| 2 | **Contact Information** | Native | ~200px |
| 3 | **Delivery Details / Shipping Method** | Native | ~250px |
| 4 | **Consolidated Trust Bar** (Free Shipping + Warranty + "1,000+ Five Star Reviews") | `DELIVERY2` | ~50px |
| 5 | **Upsell Widgets** (Order Protection + Gift Box only -- compact cards, one-click add) | `PAYMENT1` | ~140px |
| 6 | **Payment Details** (card number, expiry, CVV) | Native | ~180px |
| 7 | **Secure Payments Badge** (lock icon + "Guaranteed Safe Checkout") | `PAYMENT3` or `PAYMENT4` | ~40px |
| 8 | **Pay Now Button** | Native | ~60px |
| -- | *Post-purchase page:* One-click upsells (Care Kit, Matching Set) | `Checkout::PostPurchase::Render` | Separate page |

**Total estimated mobile checkout height: ~1,040px** (approximately 1.5 scrolls on a typical 667px viewport). The Pay Now button appears within ~2 scrolls of page load, keeping the experience tight.

### Option B: Full Badge Separation (Better for desktop-heavy audiences)

Keeps all three badge types as separate elements. Only use this if A/B testing shows it outperforms Option A for this store's mobile audience.

| Order | Element | Shopify Plus Target |
|---|---|---|
| 1 | **Express Checkout** (Shop Pay, Apple Pay, Google Pay) | Native |
| 2 | **Contact Information** | Native |
| 3 | **Delivery Details / Shipping Method** | Native |
| 4 | **Shipping Policy & Warranty Trust Badge** | `DELIVERY2` |
| 5 | **Social Proof Badge** ("1,000+ Five Star Reviews") | `PAYMENT1` |
| 6 | **Upsell Widgets** (Order Protection + Gift Box -- compact, one-click) | `PAYMENT2` |
| 7 | **Payment Details** | Native |
| 8 | **Secure Payments Badge** (lock icon + concise trust message) | `PAYMENT3` or `PAYMENT4` |
| 9 | **Pay Now Button** | Native |
| 10 | *Post-purchase:* Care Kit + Matching Set one-click offers | `Checkout::PostPurchase::Render` |

**Total estimated mobile checkout height: ~1,140px** (~100px taller than Option A due to the extra badge block).

---

## Summary of All Changes from Original

| Element | Original Suggestion | Recommended Change | AfterSell Widget | Reason |
|---|---|---|---|---|
| Shipping/Warranty Badge | Below express checkout OR below delivery details | `INFORMATION2` (above fold) or `DELIVERY2` (below delivery) -- A/B test both | Trust Badges | Above fold reduces immediate bounce; `DELIVERY2` reinforces before payment. Keep express checkout clean for Shop Pay. |
| Social Proof Badge | Above payment OR below Pay Now | `PAYMENT1` (above payment) or merge into the Trust Badges bar | Testimonials | Below Pay Now is past the decision point; merging saves mobile scroll height |
| Secure Payments Badge | Below Pay Now | `PAYMENT3`/`PAYMENT4` (above Pay Now) | Trust Badges | Addresses anxiety *before* the action; avoid duplicating card logos Shopify already shows natively |
| Upsell Widgets | Above payment methods OR above Pay Now; all 4 categories in-checkout | `PAYMENT1`/`PAYMENT2`; limit to 2 in-checkout on mobile (Order Protection + Gift Box) | Upsells | Above Pay Now creates congestion; 3-4 upsells add 300-400px on mobile, risking abandonment |
| Post-Purchase Upsells | Not mentioned | AfterSell post-purchase flow (Care Kits + Matching Sets) | Post-purchase | Zero risk to primary conversion; separate page avoids mobile scroll penalty; 4.7-30% acceptance rates |
| Free Shipping Progress Bar | Not mentioned | `INFORMATION1` (very top of checkout, above the fold) | Rewards | +10-12% conversion lift; addresses #1 abandonment reason (unexpected costs) immediately; leverages Goal Gradient Effect for AOV |
| Checkout Layout | Not mentioned | Use one-page checkout (Shopify Plus default) | N/A | 7.5% average conversion lift; mobile shoppers specifically prefer it |
| Badge Consolidation | Not mentioned | Consider consolidating Shipping/Warranty + Social Proof into one compact bar on mobile | Trust Badges | Saves ~60-100px; reduces badge bloat risk on small screens |

---

## Sources

**Checkout CRO & Trust Badges:**
- Digital Applied: eCommerce Checkout Optimization UX Guide 2026
- SmartSMS Solutions: Trust Badges That Boost Conversion (Evidence-Based Guide)
- Stripe: Checkout Screen Best Practices; How to Increase Checkout Conversion
- TrustZ: How Trust Badges Increase Conversion Rates (2025)
- CheckoutWC: Guaranteed Safe Checkout Badge Guide
- Hashmeta: Why Trust Blocks Increase Conversions
- Reacheffect: Best Website Trust Badges (2025)
- CyberSource: Trust Badge Survey (2020)
- Emplicit: How To Use Trust Badges For Higher Conversions
- Mobiloud: The Role of Trust Signals in Reducing Cart Abandonment
- Baymard Institute: How Users Perceive Security During the Checkout Flow (2023)
- Baymard Institute: Checkout UX Best Practices 2025
- ConversionTeam: Simple Free Shipping Test Drives 8.2% Conversion Boost

**Upsells & AOV:**
- Loopwork: One-Click Upsell Shopify (2026); Cart vs Checkout Upsell (2026)
- AfterSell: 2025 Upsell & Revenue Benchmarks Report
- ReConvert: Olivia Jewelry Post-Purchase Upsell Case Study
- Amote: Post-Purchase Upsell vs In-Cart Upsell Comparison
- Cart-X: Pre Purchase vs Post Purchase Upsell Analysis
- Identixweb: Proven Tips to Upsell Jewelry in Shopify (2026)

**Free Shipping Progress Bar:**
- SplitDev: 9 Shopify Plus Checkout Tweaks That Add 12-38% Revenue (2026)
- GrowthSuite: Progress Bars to Boost AOV: Complete Psychology & Strategy Guide
- JCodex: Guide Shoppers to Spend More: Free Shipping Thresholds and Progress Bars
- BetterShipping: Add a Free Shipping Progress Bar to Your Shopify Store
- Blockify: Add a Free Shipping Bar (Shopify Plus)
- CrocArt: Progress Bar A/B Testing: What To Measure

**Social Proof:**
- Zipify: 11 High-Impact Places to Put Reviews
- ProveSource: Social Proof Notifications (2026)
- Yotpo: Ultimate Guide to Social Proof for Shopify Stores

**AfterSell:**
- AfterSell: Checkout Widget Types (Help Center)
- AfterSell: Adding a Checkout Widget to Your Shopify Checkout (Help Center)
- AfterSell: Boost Shopify Plus ROI with AfterSell Checkout Tools
- AfterSell: How to Customize Checkout Page in Shopify (Blog)

**Shopify Plus & Checkout Extensibility:**
- SpeedBoostr: Mastering Shopify Checkout Extensibility (2025 Migration Guide)
- EcomHint: How to Customize Shopify Checkout (2026 Guide)
- Shopify Dev Docs: Checkout UI Extension Targets Overview (2025-04)
- Shopify Dev Docs: purchase.checkout.block.render Target
- Shopify Dev Docs: UX for Pre-Purchase and Post-Purchase Product Offers
- Shopify Dev Docs: Post-Purchase Extension Points API
- Shopify: Shop Pay Is the Best-Converting Accelerated Checkout

**Mobile UX & Checkout:**
- ScaleShopify: How to Optimize Shopify Mobile Checkout for Conversions
- InkBot Design: Mobile UX Best Practices: Designing For Thumbs (2026)
- Sacha Goureau: Mobile eCommerce Optimization Above the Fold
- CaptivateClick: Optimizing Mobile Checkout for Maximum Conversions
- SplitDev: 9 Shopify Plus Checkout Tweaks That Add 12-38% Revenue (2026)

**Checkout Layout:**
- StoreDataLab: Shopify One-Page vs Multi-Step Checkout
- ShopLift: Shopify Checkout Comparison: Single-Page vs Three-Page
- Digismoothie: One-Page Checkout vs Multi-Page Checkout
