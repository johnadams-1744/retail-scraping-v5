# Retail Location Validation Audit Report

**Audit Date:** February 25, 2026
**Method:** Web search verification against each specific domain's published location data

---

## Summary

| # | Business | Domain | Claimed | Verified | Status |
|---|----------|--------|---------|----------|--------|
| 1 | Grit Coffee | gritcoffee.com | 9 | 9 | ACCURATE |
| 2 | Love Shop | loveshop.ca | 6 | 9 | WRONG (under-counted) |
| 3 | Lofty Coffee | loftycoffee.com | 6 | 6 | ACCURATE |
| 4 | Montana Gift Corral | www.giftcorral.com | 5 | 6 | WRONG (under-counted) |
| 5 | The Armoury | store.thearmoury.com | 4 | 0 | WRONG (subdomain issue) |
| 6 | Isalis | www.shopisalis.com | 4 | ~1-2 | WRONG (over-counted; closures) |
| 7 | FloorPlay Socks | floorplaysocks.com | 4 | 3 | WRONG (over-counted) |
| 8 | shoesbylara | shoesaleshop.com | 4 | 0 | WRONG (subdomain/domain issue) |
| 9 | McIntosh Laboratory | shop.mcintoshlabs.com | 1 | 0 | WRONG (subdomain issue) |
| 10 | Gregorian Rugs | gregorianrugs.com | 1 | 1 | ACCURATE |
| 11 | Majorwavezlab | majorwavezlab.com | 3 | 1 | WRONG (over-counted) |
| 12 | Goldstruck Coffee | shop.goldstruckcoffee.ca | 3 | 3 | ACCURATE |
| 13 | Antonello Shoes | antonelloshoes.com | 3 | 2 | WRONG (over-counted; closure) |
| 14 | Mom's Apple Pie Co. | holidayorders.momsapplepieco.com | 3 | 0 | WRONG (subdomain issue) |
| 15 | OmarsJewelers | omarsjewelers.com | 2 | 2 | ACCURATE |

**Accuracy Rate: 5/15 (33%)**

---

## Detailed Findings

### 1. Grit Coffee | gritcoffee.com | 9 claimed -- ACCURATE

**What the domain shows:** gritcoffee.com/pages/locations lists exactly 9 locations across Virginia.

**Verified locations:**
- Charlottesville (6): Crozet, Downtown, Elliewood/UVA Corner, Pantops, Stonefield, UVA Nau Hall
- Richmond (2): Libbie Avenue, Scott's Addition
- Williamsburg (1): Midtown Row

**Verdict:** Claimed count of 9 is **correct**.

---

### 2. Love Shop | loveshop.ca | 6 claimed -- WRONG (should be 9)

**What the domain shows:** loveshop.ca/pages/locations lists significantly more than 6 locations across Ontario.

**Verified locations (at least 9):**
1. Yonge St, Toronto (NEW)
2. Etobicoke
3. Brampton
4. Oshawa (NEW)
5. Mississauga
6. Burlington
7. Cambridge (NEW)
8. Brantford
9. Guelph

Additional locations found on external directories: Hamilton, and a second Mississauga store -- these may bring the total to 10-11, though the loveshop.ca locations page itself lists at least 9.

**Verdict:** Claimed count of 6 is **too low**. The dataset appears to be using outdated information. The correct count is at least **9** based on loveshop.ca's own locations page, which shows several locations marked as "NEW" that were added after the original count.

---

### 3. Lofty Coffee | loftycoffee.com | 6 claimed -- ACCURATE

**What the domain shows:** loftycoffee.com/pages/locations lists exactly 6 cafes in the San Diego area.

**Verified locations:**
1. Encinitas
2. Roasting Works (Encinitas) -- 97 N Coast Hwy 101
3. La Costa
4. State Street (Carlsbad)
5. Little Italy
6. Solana Beach

**Verdict:** Claimed count of 6 is **correct**.

---

### 4. Montana Gift Corral | www.giftcorral.com | 5 claimed -- WRONG (should be 6)

**What the domain shows:** giftcorral.com/pages/locations lists 6 locations, not 5.

**Verified locations:**
1. Historic Downtown Bozeman -- 237 E. Main St., Bozeman, MT
2. Bozeman Walmart -- 1500 N. 7th Ave., Bozeman, MT
3. Gallatin Valley Mall -- 2825 W Main St., Bozeman, MT
4. Bozeman Yellowstone International Airport -- 850 Gallatin Field Road, Belgrade, MT
5. Downtown Missoula -- 117 W. Front Street, Missoula, MT
6. Lewis & Clark Caverns State Park -- 1455 Hwy. 2 E., Whitehall, MT (seasonal)

**Verdict:** Claimed count of 5 is **too low by 1**. The dataset is missing the **Gallatin Valley Mall** location. Correct count is **6**.

---

### 5. The Armoury | store.thearmoury.com | 4 claimed -- WRONG (subdomain issue)

**What the domain shows:** store.thearmoury.com is The Armoury's e-commerce/online shop subdomain (appears to be a Shopify storefront). It does NOT list its own physical retail locations. The 4 physical stores (Tribeca NYC, Upper East Side NYC, Pedder Building HK, Carlyle Club HK) are listed on the **parent domain** thearmoury.com/contact, not on the store.thearmoury.com subdomain.

A search for `site:store.thearmoury.com locations` returned zero results. The subdomain contains product collections (e.g., "The Armoury Upstate" collection) but no location/contact pages with physical addresses.

**Verdict:** The 4 locations exist for the parent brand (thearmoury.com) but are **not listed on store.thearmoury.com** itself. For this specific subdomain, the correct count is **0**. The dataset incorrectly attributed the parent domain's locations to the e-commerce subdomain.

---

### 6. Isalis | www.shopisalis.com | 4 claimed -- WRONG (over-counted)

**What the domain shows:** shopisalis.com/pages/our-locations exists as a page, but its content could not be retrieved via web search (the page appears to load dynamically). External sources provide the following picture:

- **NYC (active):** 22 Prince St, New York, NY (Nolita) -- confirmed active on Yelp
- **SF - 50 Post St:** PERMANENTLY CLOSED (confirmed on MapQuest)
- **SF - 910 Valencia St:** Status unclear, but multiple indicators suggest this is also closed

The claim of "4 locations in SF & NYC" appears to significantly overstate the current situation. At most 1-2 locations appear active.

**Verdict:** Claimed count of 4 is **too high**. At least 1 SF location is confirmed permanently closed. The correct count is likely **1-2** active locations. The dataset should be updated to reflect closures.

---

### 7. FloorPlay Socks | floorplaysocks.com | 4 claimed -- WRONG (should be 3)

**What the domain shows:** floorplaysocks.com/pages/store-locations lists exactly 3 retail locations.

**Verified locations:**
1. West Queen West (Flagship) -- 762 Queen St West, Toronto
2. Distillery District -- 45 Tank House Lane, Toronto
3. Locke Street -- 194 Locke St. South, Hamilton

**Missing from website:** The dataset claims an "Uptown Yonge" Toronto location (2585 Yonge St), which appears on MapQuest but is **not listed on FloorPlay's own store locations page**. This location may have closed or been removed.

**Verdict:** Claimed count of 4 is **too high by 1**. The FloorPlay website's own locations page lists only **3** stores. The Yonge St location is not listed on the domain.

---

### 8. shoesbylara | shoesaleshop.com | 4 claimed -- WRONG (domain issue)

**What the domain shows:** shoesaleshop.com is an e-commerce storefront for Shoes By Lara. A `site:shoesaleshop.com` search returned zero indexed pages with location information. The domain functions purely as an online shop.

The 3-4 physical Shoes By Lara locations are listed on the **separate domain** shoesbylara.com/locations.html:
1. Crystal City Shops North -- 1622 Crystal Square Arcade, Arlington, VA
2. L'Enfant Plaza -- 470 L'Enfant Plaza SW, Washington, DC
3. 1139 18th St NW, Washington, DC

The claim references shoesaleshop.com specifically, which does not contain location information.

**Verdict:** The physical stores exist under the shoesbylara.com domain, **not** shoesaleshop.com. For the specific domain audited, the count should be **0** (online shop only). If the intent is to audit the brand, the correct domain is shoesbylara.com, which lists **3-4** locations.

---

### 9. McIntosh Laboratory | shop.mcintoshlabs.com | 1 claimed -- WRONG (subdomain issue)

**What the domain shows:** shop.mcintoshlabs.com is McIntosh's Shopify e-commerce store for purchasing audio equipment online. It does not list its own physical retail locations. The site contains product collections (Electronics, etc.) but no store locator or location pages.

The "House of Sound" NYC showroom is a real McIntosh-affiliated space, but it:
- Has its own domain: houseofsoundnyc.com
- Is referenced on the parent domain mcintoshlabs.com
- Is **not listed as a retail location on shop.mcintoshlabs.com**

The parent domain mcintoshlabs.com lists dealer locations and the factory in Binghamton, NY, but these belong to the parent domain, not the shop subdomain.

**Verdict:** Claimed count of 1 is **incorrect for this subdomain**. shop.mcintoshlabs.com is an online-only e-commerce store. The correct count for this specific subdomain is **0**. The House of Sound belongs to the parent brand/separate domain.

---

### 10. Gregorian Rugs | gregorianrugs.com | 1 claimed -- ACCURATE

**What the domain shows:** gregorianrugs.com confirms a single showroom location.

**Verified location:**
- 2284 Washington Street, Newton Lower Falls, MA 02462
- 40,000+ square feet with 8 galleries
- Hours: Tue-Fri 10am-4pm, Sat 10am-2pm (appointments necessary)
- In business since 1934, three generations

**Verdict:** Claimed count of 1 and the 40,000 sqft detail are both **correct**.

---

### 11. Majorwavezlab | majorwavezlab.com | 3 claimed -- WRONG (should be 1)

**What the domain shows:** majorwavezlab.com has a "Miami Location" collection page confirming an active presence in Wynwood, Miami (125 NW 23rd Street).

However:
- **Las Vegas:** The Vegas location is on a SEPARATE domain (majorwavezlabvegas.com) and is behind a "Coming Soon" password page -- it is **not open**.
- **Los Angeles:** The founder is LA-based and has discussed plans to open there, but no active LA retail location exists. No location page for LA was found on majorwavezlab.com.

**Verdict:** Claimed count of 3 is **too high**. Only **1** location (Miami/Wynwood) is confirmed active on majorwavezlab.com. Las Vegas is not yet open, and LA is aspirational only.

---

### 12. Goldstruck Coffee | shop.goldstruckcoffee.ca | 3 claimed -- ACCURATE

**What the domain shows:** shop.goldstruckcoffee.ca/pages/contact lists 3 Toronto cafe locations.

**Verified locations:**
1. Yorkville Village
2. 133 Richmond St. W
3. 25 Carlton Street

Unlike other subdomains in this audit, this subdomain **does** list its own physical cafe locations on its contact/about page.

**Verdict:** Claimed count of 3 is **correct**. The subdomain legitimately lists 3 brand-owned cafe locations.

---

### 13. Antonello Shoes | antonelloshoes.com | 3 claimed -- WRONG (should be 2)

**What the domain shows:** antonelloshoes.com's own site does not have a clear locations page. However, cross-referencing the brand's Instagram and external sources:

**Active locations (2):**
1. Dolphin Mall -- 11401 NW 12th St, Suite 472, Miami, FL
2. Pembroke Lakes Mall -- 11401 Pines Blvd, Suite 330, Pembroke Pines, FL

**Closed location:**
3. Midway Crossings (formerly Mall of the Americas) -- 7795 W Flagler St, Miami, FL -- **CLOSED**

The dataset lists this third location as "Westland Mall (Hialeah)" which appears to be a misidentification of the Midway Crossings location, which is now permanently closed.

**Verdict:** Claimed count of 3 is **too high by 1**. The correct count is **2** active locations. The third FL mall location has closed.

---

### 14. Mom's Apple Pie Co. | holidayorders.momsapplepieco.com | 3 claimed -- WRONG (subdomain issue)

**What the domain shows:** holidayorders.momsapplepieco.com is a holiday-specific online ordering subdomain (Shopify-style). It does NOT list bakery locations on its own pages. The subdomain functions as an e-commerce ordering portal.

The 3 bakery locations are listed on the **parent domain** momsapplepieco.com/locations:
1. Leesburg -- 220 Loudoun St SE, Leesburg, VA
2. Hill High (Round Hill) -- 35246 Leesburg Pike, Round Hill, VA
3. Occoquan (The Golden Plum) -- 126A Commerce St, Occoquan, VA

**Verdict:** The 3 bakeries are real but belong to momsapplepieco.com, **not** the holiday orders subdomain. For the specific subdomain audited, the correct count is **0** (online ordering portal only).

---

### 15. OmarsJewelers | omarsjewelers.com | 2 claimed -- ACCURATE

**What the domain shows:** omarsjewelers.com confirms a family-owned jewelry business with 2 NYC locations.

**Verified locations:**
1. Jackson Heights, Queens -- 73-13A 37th Rd, Jackson Heights, NY 11372
2. Staten Island -- 2048 Victory Blvd, Staten Island, NY 10314

**Verdict:** Claimed count of 2 is **correct**.

---

## Key Issues Found

### 1. Subdomain Attribution Errors (4 cases)
The most systemic issue: e-commerce subdomains (shop.X, store.X, holidayorders.X) were credited with the parent brand's physical locations even though those subdomains are online-only storefronts:
- **store.thearmoury.com** -- 4 locations credited but belongs to thearmoury.com
- **shop.mcintoshlabs.com** -- 1 location credited but belongs to mcintoshlabs.com / houseofsoundnyc.com
- **holidayorders.momsapplepieco.com** -- 3 locations credited but belongs to momsapplepieco.com
- **shoesaleshop.com** -- 4 locations credited but belongs to shoesbylara.com

### 2. Stale/Outdated Counts (4 cases)
Location counts haven't been updated for openings or closures:
- **Love Shop** -- under-counted by 3+ (new locations added)
- **Montana Gift Corral** -- under-counted by 1 (Gallatin Valley Mall missing)
- **Antonello Shoes** -- over-counted by 1 (Midway Crossings closed)
- **Isalis** -- over-counted by 2-3 (SF locations closed)

### 3. Aspirational/Planned Locations Counted as Active (1 case)
- **Majorwavezlab** -- Las Vegas (not yet open) and LA (aspirational) counted alongside 1 actual Miami location

### 4. Location Not on Domain's Own Page (1 case)
- **FloorPlay Socks** -- 4th location (Yonge St) not listed on the brand's own store locator page

---

## Phase 2 Audit: Subdomain & Portal Retail Location Verification

**Audit Date:** February 25, 2026
**Rule Applied:** "If the domain is a gift card store, merch portal, or fulfillment site for a larger brand, the parent brand's locations do NOT count for this domain."

### Phase 2 Summary

| # | Business | Domain | Claimed | Verified | Status |
|---|----------|--------|---------|----------|--------|
| 1 | Hotel Emma | shop.thehotelemma.com | 1 | 0 | WRONG (subdomain issue) |
| 2 | Riverboat Discovery | shopify.riverboatdiscovery.com | 1 | 0 | WRONG (subdomain issue) |
| 3 | Chihuly Garden and Glass | chihuly-garden-and-glass.myshopify.com | 1 | 0 | WRONG (subdomain issue) |
| 4 | Stickley Museum | stickley-museum.myshopify.com | 1 | 0 | WRONG (subdomain issue) |
| 5 | Cressi | store.cressi.com | 1 | 0 | WRONG (subdomain issue) |
| 6 | J.R. Watkins | jrwatkins.com | 1 | 1 | ACCURATE |
| 7 | Clevens Face and Body | shop.drclevens.com | 0 | 0 | ACCURATE |
| 8 | Dreyer Farms | dreyer-farms.myshopify.com | 1 | 0 | WRONG (subdomain issue) |
| 9 | Del Taco Webstore | deltacowebstore.com | 0 | 0 | ACCURATE |
| 10 | Alan Jackson Official Webstore | store.alanjackson.com | 0 | 0 | ACCURATE |

**Accuracy Rate:** 4/10 (40%) -- 6 entries need correction

---

### Phase 2 Detailed Findings

### P2-1. Hotel Emma | shop.thehotelemma.com | 1 claimed -- WRONG (should be 0)

**Domain type:** Shopify e-commerce subdomain for Hotel Emma.

**What we found:** shop.thehotelemma.com is the online store for Hotel Emma's physical gift shop called "Curio." It sells hotel-branded merchandise (fragrances, candles, apparel, glassware, pillows) and gift cards redeemable at the hotel, its restaurants, and the Curio gift shop.

**The physical location:** Curio is located at 136 E Grayson St, San Antonio, TX 78215, inside Hotel Emma in the Pearl District. It is listed on atpearl.com as a Pearl District tenant and described as Hotel Emma's gift shop -- open 7 days/week with its own phone number (210.448.8356).

**Why this should be 0:** The Curio gift shop is a physical amenity of Hotel Emma (the hotel), not a standalone retail operation of shop.thehotelemma.com. The Shopify subdomain is simply the online extension of the hotel's gift shop. The physical location belongs to the parent entity (thehotelemma.com / Hotel Emma). Per the portal rule, this subdomain should not get credit for the hotel's physical gift shop.

**Verdict: NO -- 0 locations.** Subdomain e-commerce portal; physical gift shop belongs to Hotel Emma.

---

### P2-2. Riverboat Discovery | shopify.riverboatdiscovery.com | 1 claimed -- WRONG (should be 0)

**Domain type:** Shopify-hosted online store subdomain for Riverboat Discovery.

**What we found:** shopify.riverboatdiscovery.com is one of two online storefronts (the other is store.riverboatdiscovery.com) selling Alaska-themed souvenirs, Captain Jim's Smoked Salmon, and Gold Dredge 8 merchandise. It carries approximately 14 products and ships internationally.

**The physical location:** The gift shop at 1975 Discovery Dr, Fairbanks, AK is part of the Riverboat Discovery sternwheeler tour operation (riverboatdiscovery.com), a Fairbanks tourism attraction that also operates Gold Dredge 8. The gift shop is an ancillary feature of the tour business.

**Why this should be 0:** The Shopify subdomain is a merch/souvenir portal for the Riverboat Discovery tour company. The physical gift shop at the tour dock belongs to the parent brand (riverboatdiscovery.com), not to this Shopify subdomain. This is functionally identical to any tourism company's online souvenir store.

**Verdict: NO -- 0 locations.** Merch/gift portal for tour company; physical gift shop belongs to riverboatdiscovery.com.

---

### P2-3. Chihuly Garden and Glass | chihuly-garden-and-glass.myshopify.com | 1 claimed -- WRONG (should be 0)

**Domain type:** Shopify-hosted online store for the Chihuly Garden and Glass museum.

**What we found:** chihuly-garden-and-glass.myshopify.com is branded as "The Bookstore" and sells art books, Chihuly studio glass, fine art prints, apparel, home decor, and collectibles. The parent website chihulygardenandglass.com/visit/bookstore describes The Bookstore and links to this Shopify store for online purchases.

**The physical location:** The Bookstore is physically located inside the Chihuly Garden and Glass museum at 305 Harrison St, Seattle, WA (at the Seattle Center). The museum is the parent entity; the bookstore is an amenity within it.

**Why this should be 0:** The myshopify.com domain is the online ordering portal for the museum's gift shop/bookstore. The physical bookstore location belongs to Chihuly Garden and Glass (the museum, chihulygardenandglass.com), not to this Shopify subdomain. This is a textbook case of a museum gift shop's e-commerce portal.

**Verdict: NO -- 0 locations.** Online store for museum gift shop; physical location belongs to chihulygardenandglass.com.

---

### P2-4. Stickley Museum | stickley-museum.myshopify.com | 1 claimed -- WRONG (should be 0)

**Domain type:** Shopify-hosted online store for The Stickley Museum at Craftsman Farms.

**What we found:** The Stickley Museum at Craftsman Farms (stickleymuseum.org) is a National Historic Landmark in Parsippany/Morris Plains, NJ, built by Gustav Stickley between 1908-1917. The museum operates "The Craftsman Shop," a physical gift shop open weekends (Sat-Sun 11am-4pm) selling handcrafted goods, jewelry, candles, lamps, and Arts & Crafts-inspired items. The museum's online shop is at stickleymuseum.org/shop/ and there is also a Shopify storefront at stickley-museum.myshopify.com.

**The physical location:** The Craftsman Shop at 2352 State Route 10, Parsippany, NJ is operated by the museum (stickleymuseum.org), not by the Shopify subdomain.

**Why this should be 0:** The myshopify.com domain is the online ordering portal for the museum's gift shop. The physical Craftsman Shop belongs to the Stickley Museum (stickleymuseum.org). Per the portal rule, this Shopify subdomain should not get credit for the museum's physical gift shop.

**Verdict: NO -- 0 locations.** Online store for museum gift shop; physical location belongs to stickleymuseum.org.

---

### P2-5. Cressi | store.cressi.com | 1 claimed -- WRONG (should be 0)

**Domain type:** E-commerce subdomain for Cressi, the Italian diving equipment manufacturer.

**What we found:** store.cressi.com is Cressi's main online retail storefront, selling diving, snorkeling, and swimming equipment. It has a "Store Locator" page, but this shows Cressi offices, authorized dealers, dive centers, and service centers worldwide -- NOT brand-owned retail stores operated by store.cressi.com. The dataset claims a flagship store in Roatan, Honduras ("first Cressi Store worldwide"), but web searches found no verification of this location on store.cressi.com's store locator or elsewhere. The dealer locator on cressiamerica.com does not list Honduras at all.

**Why this should be 0:** Even if a Cressi-branded store exists in Honduras, it would be a retail location of the Cressi parent brand (cressi.com), not of the e-commerce subdomain store.cressi.com. The subdomain is Cressi's online shop -- an e-commerce portal for the larger brand. Additionally, the claimed Honduras location could not be independently verified through any Cressi web property.

**Verdict: NO -- 0 locations.** E-commerce subdomain for parent brand Cressi; any physical stores belong to cressi.com. Honduras location unverified.

---

### P2-6. J.R. Watkins | jrwatkins.com | 1 claimed -- ACCURATE

**Domain type:** This is the **main brand domain** for J.R. Watkins personal care products (not a subdomain or portal).

**What we found:** J.R. Watkins is a heritage brand (since 1868) headquartered at 150 Liberty Street, Winona, MN 55987. The company operates a Museum & Store at their headquarters that is open to the public (Wed-Fri 10am-4pm, free admission). The museum showcases 157+ years of company history and the store sells Watkins products including exclusive gift boxes available only at this location.

**Important nuance:** The museum/store page is hosted on watkins1868.com (the company's culinary products domain), not on jrwatkins.com (the personal care domain). Both domains belong to the same Watkins company. jrwatkins.com has a "Find Our Store" page that functions as a "where to buy" retailer locator (showing third-party retailers like Target and Walmart), not a brand-owned store locator.

**Why this counts:** jrwatkins.com is the main brand domain, not a subdomain/portal/merch site. The subdomain portal rule does not apply. The Watkins company demonstrably operates a brand-owned retail store open to the public at their Winona HQ. The store sells Watkins products directly to consumers. While the museum page lives on the sister domain watkins1868.com, both domains are owned and operated by the same entity, and the physical store sells products from both lines.

**Verdict: YES -- 1 location.** Main brand domain with 1 brand-owned retail store/museum in Winona, MN.

---

### P2-7. Clevens Face and Body | shop.drclevens.com | 0 claimed -- ACCURATE

**Domain type:** Shopify e-commerce subdomain for Dr. Ross Clevens' cosmetic surgery practice.

**What we found:** shop.drclevens.com sells medical-grade skincare products and cosmetic service packages (Botox, fillers, peels, facials, etc.) online. The parent practice (drclevens.com) has physical locations in Melbourne FL, Merritt Island, and Orlando, but these are medical clinics and surgical facilities, not retail stores.

**Why 0 is correct:** The physical locations are medical practice offices, not retail storefronts. The online shop is an e-commerce portal for a medical practice. Neither the subdomain nor the parent brand operates retail stores in the traditional sense.

**Verdict: Confirmed NO -- 0 locations.** Medical practice e-commerce portal; physical locations are clinics, not retail.

---

### P2-8. Dreyer Farms | dreyer-farms.myshopify.com | 1 claimed -- WRONG (should be 0)

**Domain type:** Shopify-hosted online store for Dreyer Farms.

**What we found:** Dreyer Farms is a family-owned farm and garden center since 1904 at 831 Springfield Ave, Cranford, NJ. The Shopify store (dreyer-farms.myshopify.com) appears to sell CSA subscriptions and gift cards online. The actual farm/garden center is a physical retail destination with a market building, nursery, greenhouses, and working fields. The main website is dreyerfarms.com.

**The physical location:** The farm/garden center at 831 Springfield Ave, Cranford, NJ is a real physical retail location open Mon-Sat 8am-6pm, Sun 8am-5pm (closed Dec 25 - Mar 15). It sells nursery plants, fresh produce, baked goods, and gardening supplies.

**Why this should be 0:** The myshopify.com domain is the online ordering/e-commerce portal for Dreyer Farms. The physical garden center belongs to the parent brand (dreyerfarms.com), not to the Shopify subdomain. Per the portal rule, this Shopify store should not get credit for the parent brand's physical location.

**Verdict: NO -- 0 locations.** Shopify e-commerce portal; physical garden center belongs to dreyerfarms.com.

---

### P2-9. Del Taco Webstore | deltacowebstore.com | 0 claimed -- ACCURATE

**Domain type:** Branded merchandise webstore for Del Taco restaurant chain.

**What we found:** deltacowebstore.com sells Del Taco branded merchandise (apparel, accessories, pet items, home goods, hot sauce). Most items are currently sold out. This is a standalone merch domain, not a subdomain, but it functions purely as a merchandise portal for the Del Taco brand. Del Taco's 600+ restaurant locations belong to deltaco.com, not to this merch store.

**Verdict: Confirmed NO -- 0 locations.** Merch portal for Del Taco restaurant chain; no brand-owned retail.

---

### P2-10. Alan Jackson Official Webstore | store.alanjackson.com | 0 claimed -- ACCURATE

**Domain type:** E-commerce subdomain for country music artist Alan Jackson.

**What we found:** store.alanjackson.com sells artist merchandise (apparel, CDs, DVDs, vinyl, souvenirs, posters, books, tour merch). It also links to the fan club and related products like Silverly Whiskey. This is a standard artist merch portal.

**Verdict: Confirmed NO -- 0 locations.** Artist merch portal; no brand-owned retail stores.

---

## Phase 2 Key Issues Found

### Subdomain/Portal Attribution Errors (5 new cases)
Five additional cases were identified where Shopify/e-commerce subdomains were incorrectly credited with the parent brand's physical locations:
- **shop.thehotelemma.com** -- Curio gift shop belongs to Hotel Emma (thehotelemma.com)
- **shopify.riverboatdiscovery.com** -- Gift shop belongs to tour company (riverboatdiscovery.com)
- **chihuly-garden-and-glass.myshopify.com** -- Bookstore belongs to museum (chihulygardenandglass.com)
- **stickley-museum.myshopify.com** -- Craftsman Shop belongs to museum (stickleymuseum.org)
- **dreyer-farms.myshopify.com** -- Garden center belongs to farm (dreyerfarms.com)

### E-commerce Subdomain for Parent Brand (1 new case)
- **store.cressi.com** -- E-commerce subdomain for Cressi diving brand; any physical stores belong to cressi.com. The claimed Honduras location could not be verified.

### Correctly Flagged as 0 (3 confirmations)
- **shop.drclevens.com** -- Medical clinics, not retail stores
- **deltacowebstore.com** -- Merch portal, no retail
- **store.alanjackson.com** -- Artist merch portal, no retail

### Main Domain Correctly Credited (1 confirmation)
- **jrwatkins.com** -- Main brand domain with legitimate retail store/museum in Winona, MN
