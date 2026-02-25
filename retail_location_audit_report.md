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
