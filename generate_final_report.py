#!/usr/bin/env python3
"""
Final Report Generator - Retail Location Validation Funnel
Combines all Phase 1, 2, and 3 data into the final output CSV.
"""

import csv
import re
import json

INPUT_FILE = "/home/ubuntu/.cursor/projects/workspace/uploads/potential_retail_-_Sheet1__1_.csv"
OUTPUT_FILE = "/workspace/retail_location_validation_report.csv"

def clean_domain(url):
    url = url.strip()
    url = re.sub(r'^https?://', '', url)
    url = re.sub(r'^www\.', '', url)
    url = url.rstrip('/')
    return url

def normalize_domain(d):
    return re.sub(r'^www\.', '', d.lower().strip())

# ============================================================
# PHASE 1: Product Eligibility Results
# ============================================================

INELIGIBLE = {
    'fogervapes.com': 'Prohibited: e-cigarettes, vaping devices, and nicotine products',
    'hiddenhybridholsters.com': 'Prohibited: firearm holsters',
    'bakedhhc.com': 'Prohibited: HHC (hemp-derived cannabinoid) vape products',
    'piedmonthempco.com': 'Prohibited: hemp/CBD products including tinctures and CBD-infused balms',
    'iloveexcitementsmokin.com': 'Prohibited: smoking paraphernalia and drug paraphernalia (head shop selling dab rigs, water pipes, nectar collectors)',
    'dabbingwarehouse.com': 'Prohibited: drug paraphernalia (dabbing equipment, dab rigs, quartz bangers for cannabis consumption)',
}

REVIEW_NEEDED = {
    'highmonkkratom.com': 'Gray area: kratom products — may be classified as pseudo-pharmaceutical with unverified health claims',
    'cryokratom.com': 'Gray area: kratom extract products — may be classified as pseudo-pharmaceutical with unverified health claims',
    'armament.com': 'Gray area: military weapon sighting systems and riflescopes — closely associated with firearms use',
    'blackmarketgear.com': 'Gray area: tactical surplus gear including holsters (a prohibited category) as part of broader inventory',
    'opticsforce.com': 'Gray area: primary products are rifle scopes and firearm optics — closely associated with firearms use',
    'nightprowleroptics.com': 'Gray area: thermal scopes and night vision equipment primarily for hunting/firearms',
}

# ============================================================
# PHASE 2: Retail Location Data
# ============================================================

RETAIL_LOCATIONS = {
    # Batch 1 - Food/Coffee/Bakery
    'riverstreetsweets.com': {'count': 2, 'details': '13 E River Street, Savannah, GA; 32 E Broughton St, Savannah, GA'},
    'roosroast.com': {'count': 2, 'details': '1155 Rosewood St, Ann Arbor, MI; 117 E Liberty St, Ann Arbor, MI'},
    'gritcoffee.com': {'count': 9, 'details': '6 locations in Charlottesville, 2 in Richmond, 1 in Williamsburg, VA'},
    'loftycoffee.com': {'count': 6, 'details': 'Encinitas (2), Carlsbad (2), San Diego, Solana Beach, CA'},
    'and-sons.com': {'count': 1, 'details': '9548 Brighton Way, Beverly Hills, CA'},
    'zcioccolato.com': {'count': 1, 'details': '474 Columbus Ave, San Francisco, CA'},
    'josephsorganicbakery.com': {'count': 1, 'details': '18228 W Dixie Hwy, Miami, FL'},
    'sarkispastry.com': {'count': 3, 'details': 'Glendale, CA; Pasadena, CA; Anaheim, CA'},
    'petalumapiecompany.com': {'count': 1, 'details': '125 Petaluma Blvd N, Suite B, Petaluma, CA'},
    'thebutchersblocknj.com': {'count': 1, 'details': '235 West Ave, Long Branch, NJ'},
    'sonomacountymeatco.com': {'count': 1, 'details': '35 Sebastopol Ave, Santa Rosa, CA'},
    'prospectcoffee.com': {'count': 1, 'details': '92 S. Laurel Street, Ventura, CA'},
    'coastroast.com': {'count': 3, 'details': 'Gulfport, MS; New Orleans, LA (St. Roch Market); Long Beach, MS'},
    'laidrey.com': {'count': 3, 'details': 'Tarzana, CA; Encino, CA; Agoura Hills, CA'},
    'bcandy.com': {'count': 1, 'details': '3100 E Coast Hwy, Corona del Mar, CA'},
    'yeolesweets.com': {'count': 1, 'details': '402 State St, Erie, PA'},
    'germansausageaz.com': {'count': 1, 'details': '4900 E Indian School Rd, Phoenix, AZ'},
    'stagecoachmeatcompany.com': {'count': 1, 'details': '600 W 3rd Ave, Wiggins, CO'},
    'smgeneralstore.com': {'count': 1, 'details': '139 E Wears Valley Rd, Pigeon Forge, TN'},
    'dreyer-farms.myshopify.com': {'count': 1, 'details': '831 Springfield Ave, Cranford, NJ'},
    'shop.goldstruckcoffee.ca': {'count': 3, 'details': 'Yorkville Village, Toronto; 133 Richmond St W, Toronto; 25 Carlton St, Toronto'},
    'tenderlovingcoffee.com': {'count': 1, 'details': '365 E 6th St, Chico, CA'},
    
    # Batch 2 - Jewelry/Shoes/Fashion/Boutiques
    'lukeslocker.com': {'count': 2, 'details': '3046 Mockingbird Lane, Dallas, TX; The Shops at Clearfork, 5255 Monahans Avenue, Fort Worth, TX'},
    'loveshop.ca': {'count': 18, 'details': '500 Yonge Street, Toronto; Oshawa; Brampton; Brantford; Burlington; Cambridge; Etobicoke; Guelph; Waterloo; Hamilton; Niagara Falls; Oakville; Kitchener; Newmarket; Mississauga; London (2); Whitby, ON'},
    'townshop.com': {'count': 1, 'details': '2270 Broadway, New York, NY 10024'},
    'mannsjewelers.com': {'count': 1, 'details': '2945 Monroe Ave, Rochester, NY'},
    'qdjewelers.com': {'count': 1, 'details': '861 6th Avenue, Suite 165, San Diego, CA'},
    'omarsjewelers.com': {'count': 2, 'details': '73-13A 37th Rd, Jackson Heights, NY; 2048 Victory Blvd, Staten Island, NY'},
    'mastshoes.com': {'count': 1, 'details': '2519 Jackson Ave, Ann Arbor, MI'},
    'davesboots.com': {'count': 1, 'details': '478 Antelope Boulevard, Red Bluff, CA'},
    'theheadspace.net': {'count': 1, 'details': '250 Broadway Unit 100B, Denver, CO'},
    'boutiquelbismarck.com': {'count': 1, 'details': '1001 W Interstate Ave, Bismarck, ND'},
    'meridianboutique.com': {'count': 2, 'details': '101 East Main Street, Bozeman, MT (Women); 107 East Main Street, Bozeman, MT (Men)'},
    'custardboutique.com': {'count': 2, 'details': '422 Whitaker Street, Savannah, GA; 718 A South Main Street, Greenville, SC'},
    'boutiquesisi.com': {'count': 1, 'details': '361 Victoria Avenue, Westmount, QC, Canada'},
    'shopchictx.com': {'count': 1, 'details': '1243 Gruene Road, New Braunfels, TX'},
    'shopoxfordstreet.com': {'count': 1, 'details': '15555 East 14th Street, San Leandro, CA (Bayfair Center)'},
    'fashionablyyours.com': {'count': 1, 'details': '707 Queen St W, Toronto, ON, Canada'},
    'snsnola.com': {'count': 1, 'details': '3771A Gen Degaulle Dr, New Orleans, LA'},
    
    # Batch 3 - Hardware/Furniture/Specialty
    'store.thearmoury.com': {'count': 4, 'details': '168 Duane Street, New York, NY (Tribeca); 13 East 69th Street, New York, NY (Upper East Side); 501 Pedder Building, Central, Hong Kong; Rosewood Hotel, Tsim Sha Tsui, Hong Kong'},
    'baltimorebilliards.com': {'count': 1, 'details': '8906 Waltham Woods Rd, Parkville, MD'},
    'frawleysvarietystore.com': {'count': 1, 'details': '225 Main Street SW, New Albin, IA'},
    'thefurniture-nest.com': {'count': 1, 'details': '329 Civic Ave, Salisbury, MD'},
    'galeriajoliet.com': {'count': 2, 'details': '692 Theodore St #A, Joliet, IL; 2134 West Jefferson Street, Joliet, IL'},
    'hadleyolivia.com': {'count': 1, 'details': '31896 Plaza Drive Suite D1, San Juan Capistrano, CA'},
    'marksfurnituredirect.com': {'count': 1, 'details': '2180 GI Maddox Parkway Suite A, Chatsworth, GA'},
    'rework-furniture.com': {'count': 1, 'details': '7550 Roosevelt Rd, Forest Park, IL (showroom by appointment)'},
    'furnituredepot.ca': {'count': 1, 'details': '6075 Mavis Rd, Mississauga, ON (Heartland Town Centre)'},
    'cheapoliberty.com': {'count': 1, 'details': '1915 Industrial Dr, Liberty, MO'},
    'americanhomeexpress.com': {'count': 1, 'details': '4722 Eisenhauer Rd #105, San Antonio, TX'},
    'shop.thehotelemma.com': {'count': 1, 'details': '136 E. Grayson Street, San Antonio, TX (Curio at Hotel Emma)'},
    'royhenryvickers.com': {'count': 1, 'details': '350 Campbell Street, Tofino, BC (Eagle Aerie Gallery)'},
    'kincaidsmusic.com': {'count': 1, 'details': '1325 W 1st St, Springfield, OH'},
    'shop.jessebrowns.com': {'count': 1, 'details': '4732 Sharon Road, Suite 2M, Charlotte, NC'},
    'libertysafeofcollegestation.com': {'count': 1, 'details': '1055 Texas Ave S, Suite 104, College Station, TX'},
    'recreationsoutlet.com': {'count': 2, 'details': '885 Business 28, Milford, OH; 484 W Olentangy/Powell Road, Powell, OH'},
    'shop.btbconsignments.com': {'count': 2, 'details': '1820-A2 6th Avenue SE, Decatur, AL; 124 4th Street SW, Cullman, AL'},
    'giftcorral.com': {'count': 5, 'details': '237 E. Main St, Bozeman, MT; Bozeman Yellowstone Int\'l Airport; 117 W. Front St, Missoula, MT; and 2 more MT locations'},
    'tigertraditions.com': {'count': 2, 'details': '5134 Sunset Blvd, Lexington, SC; 481 Town Center Place, Columbia, SC'},
    'holidaywarehouse.com': {'count': 1, 'details': '2819 W 15th St, Plano, TX (30,000 sqft showroom — note: physical store reported closed Jan 2024)'},
    'quiltexpressions.com': {'count': 1, 'details': '1200 East Watertower Street, Suite 120, Meridian, ID (by appointment)'},
    
    # Batch 4 - Spas/Miscellaneous
    'batlgrounds-com-online-store.myshopify.com': {'count': 13, 'details': '8 Ontario venues + 5 US venues (Scottsdale AZ, Charlotte NC x2, Houston TX, Novi MI)'},
    'shoptheroselakemary.com': {'count': 1, 'details': '156 N 4th St, Suite 1470, Lake Mary, FL'},
    'valowellnessspa.com': {'count': 1, 'details': '120 Regency Pkwy, Suite 104, Omaha, NE'},
    'chihuly-garden-and-glass.myshopify.com': {'count': 1, 'details': '305 Harrison St, Seattle, WA (museum gift shop)'},
    'theufbrand.com': {'count': 1, 'details': '208 S State St, Geneseo, IL'},
    'redbrickemporium.com': {'count': 1, 'details': '64 Gore St E, Perth, ON'},
    'goldenearsspecialtystore.com': {'count': 1, 'details': '22378 132 Ave, Maple Ridge, BC'},
    'loennursery.com': {'count': 2, 'details': 'Retail garden center + contractors yard, Sherwood, OR'},
    'quinceflowers.com': {'count': 1, 'details': '20 Wagstaff Dr, Unit 2, Toronto, ON'},
    'austinflowerdelivery.com': {'count': 1, 'details': '11215 Research Blvd, #1189, Austin, TX'},
    'theanimalhouse.net': {'count': 3, 'details': 'Damariscotta, ME; Westbrook, ME; Brunswick, ME'},
    'papertrailrhinebeck.com': {'count': 1, 'details': '6423 Montgomery St, Rhinebeck, NY'},
    'souliciousvegankitchen.com': {'count': 2, 'details': 'Orlando, FL (Market On South); Apopka, FL (Hall\'s On 5th)'},
    'shop.drclevens.com': {'count': 1, 'details': '707 W Eau Gallie Blvd, Melbourne, FL'},
    'thewatchmakersshop.com': {'count': 1, 'details': '1 Page Ave, Ste 119, Asheville, NC (Grove Arcade)'},
    'polleybuilding.com': {'count': 1, 'details': '1335 S Obrien St, Seymour, IN'},
    'americanladders.com': {'count': 2, 'details': 'Glastonbury, CT; Milford, CT showrooms'},
    'stickleyvirtualmarket.com': {'count': 5, 'details': 'Fayetteville NY; White Plains NY; Englewood CO; Superior CO; Natick MA'},
    
    # Batch 5 - Additional
    'ezvacuum.com': {'count': 1, 'details': '8645 Phoenix Dr, Manassas, VA'},
    'hanyangmart.com': {'count': 1, 'details': '150-51 Northern Boulevard, Flushing, NY'},
    'rideoutsupply.com': {'count': 1, 'details': '1260 E Woodland Ave, Springfield, PA'},
    'madronecycles.com': {'count': 1, 'details': '280 East Hersey Street, Unit 25, Ashland, OR'},
    'shop.canadawidesports.com': {'count': 1, 'details': '23 Beverly Street East, Saint George, ON, Canada'},
    'romansjewelry.com': {'count': 2, 'details': '723 Sutter St, Folsom, CA; 375 Main St, Placerville, CA'},
    'conciergediamonds.com': {'count': 1, 'details': 'Downtown Los Angeles, CA (by appointment)'},
    'janepopejewelry.com': {'count': 1, 'details': 'The JP Studio, Charleston, SC (by appointment)'},
    'gregorianrugs.com': {'count': 1, 'details': '2284 Washington Street, Newton Lower Falls, MA'},
    'bernina-jeff.myshopify.com': {'count': 1, 'details': '2584 Patterson Rd Unit B, Grand Junction, CO'},
    'allegorygoods.com': {'count': 1, 'details': '354 Pembroke Ave, Joliet, IL'},
    'hammerlyceramics.com': {'count': 1, 'details': '8127 W. 94th Ave, Broomfield, CO'},
    'mbgourds.com': {'count': 1, 'details': '125 Potato Rd, Carlisle, PA'},
    'invictajewelry.com': {'count': 3, 'details': '250 Woodbridge Center Dr, Woodbridge, NJ; 1535 Broadway, New York, NY (Times Square); 12801 W Sunrise Blvd, Sunrise, FL'},
    'polishpotterypantry.com': {'count': 1, 'details': '910 Ridgeline Rd, Copperas Cove, TX'},
    'plusskateshop.com': {'count': 2, 'details': '186 Miracle Strip Pkwy SE, Fort Walton Beach, FL; 1646 East Colonial Drive, Orlando, FL'},
    
    # Batch 6 - Additional
    'shop.howlerbikepark.com': {'count': 2, 'details': '3410 US-65, Walnut Shade, MO; 615 S Pickwick Ave, Springfield, MO'},
    'allmarbletiles.com': {'count': 1, 'details': '175 Moonachie Rd, Moonachie, NJ (showroom by appointment)'},
    'pigeonmountaintrading.com': {'count': 1, 'details': '106 N Main St, La Fayette, GA'},
    'shop.atbgame.com': {'count': 1, 'details': '119 West County Center, Suite 2085, Des Peres, MO'},
    'shopify.riverboatdiscovery.com': {'count': 1, 'details': '1975 Discovery Dr, Fairbanks, AK (Discovery Trading Post)'},
    'suzybjewelry.com': {'count': 1, 'details': 'New York City showroom (by appointment)'},
}

# ============================================================
# PHASE 3: Revenue Estimates
# ============================================================

def load_revenue_data():
    """Load all revenue estimate JSON files."""
    revenue = {}
    files = [
        '/workspace/revenue_estimates_batch_a.json',
        '/workspace/batch_b_revenue_estimates.json',
        '/workspace/batch_c_revenue_estimates.json',
        '/workspace/batch_d_revenue_estimates.json',
    ]
    for f in files:
        try:
            with open(f, 'r') as fh:
                data = json.load(fh)
                for domain, info in data.items():
                    nd = normalize_domain(domain)
                    revenue[nd] = info
        except Exception as e:
            print(f"Warning: Could not load {f}: {e}")
    return revenue

# ============================================================
# Main Processing
# ============================================================

def main():
    print("=" * 60)
    print("RETAIL LOCATION VALIDATION FUNNEL - FINAL REPORT")
    print("=" * 60)
    
    # Load revenue data
    revenue_data = load_revenue_data()
    print(f"Revenue estimates loaded: {len(revenue_data)}")
    
    # Parse input CSV
    businesses = []
    with open(INPUT_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            biz = {
                'id': i + 1,
                'name': row['Business Name'].strip(),
                'web_address': row['Web Address'].strip(),
                'domain': clean_domain(row['Web Address'].strip()),
            }
            businesses.append(biz)
    
    print(f"Total businesses: {len(businesses)}")
    
    # Phase 1: Apply eligibility
    ineligible_count = 0
    review_count = 0
    eligible_count = 0
    
    for biz in businesses:
        nd = normalize_domain(biz['domain'])
        
        if nd in INELIGIBLE:
            biz['eligible'] = 'No'
            biz['elig_notes'] = INELIGIBLE[nd]
            biz['funnel'] = 'Phase 1 — Ineligible Product'
            ineligible_count += 1
        elif nd in REVIEW_NEEDED:
            biz['eligible'] = 'Review Needed'
            biz['elig_notes'] = REVIEW_NEEDED[nd]
            review_count += 1
        else:
            biz['eligible'] = 'Yes'
            biz['elig_notes'] = '\u2014'
            eligible_count += 1
    
    print(f"\nPhase 1 complete: {eligible_count} eligible, {ineligible_count} ineligible, {review_count} review needed.")
    print(f"Proceeding to Phase 2 with {eligible_count + review_count} businesses.")
    
    # Phase 2: Apply retail location data
    retail_count = 0
    no_retail_count = 0
    
    for biz in businesses:
        if biz.get('funnel') == 'Phase 1 — Ineligible Product':
            biz['has_retail'] = ''
            biz['num_loc'] = ''
            biz['loc_details'] = ''
            continue
        
        nd = normalize_domain(biz['domain'])
        
        if nd in RETAIL_LOCATIONS:
            loc = RETAIL_LOCATIONS[nd]
            biz['has_retail'] = 'TRUE'
            biz['num_loc'] = loc['count']
            biz['loc_details'] = loc['details']
            biz['funnel'] = 'Phase 3 \u2014 Qualified Lead'
            retail_count += 1
        else:
            biz['has_retail'] = 'FALSE'
            biz['num_loc'] = 0
            biz['loc_details'] = 'N/A'
            biz['funnel'] = 'Phase 2 \u2014 No Retail Locations'
            no_retail_count += 1
    
    print(f"\nPhase 2 complete: {retail_count} businesses have brand-owned retail locations, {no_retail_count} do not.")
    print(f"Proceeding to Phase 3 with {retail_count} businesses.")
    
    # Phase 3: Apply revenue estimates and ranking
    qualified = [b for b in businesses if b.get('funnel') == 'Phase 3 \u2014 Qualified Lead']
    
    for biz in qualified:
        nd = normalize_domain(biz['domain'])
        if nd in revenue_data:
            biz['revenue'] = revenue_data[nd]['estimate']
            biz['reasoning'] = revenue_data[nd]['reasoning']
            biz['sort_key'] = revenue_data[nd].get('sort_key', 0)
        else:
            biz['revenue'] = 'Data unavailable'
            biz['reasoning'] = 'Revenue research pending'
            biz['sort_key'] = 0
    
    # Sort qualified leads by sort_key (highest first) then by num_loc
    qualified.sort(key=lambda x: (x.get('sort_key', 0), x.get('num_loc', 0)), reverse=True)
    
    # Assign priority rankings
    for rank, biz in enumerate(qualified, 1):
        biz['priority'] = rank
    
    print(f"\nPhase 3 complete. Top 10 qualified leads:")
    for biz in qualified[:10]:
        print(f"  {biz['priority']}. {biz['name']} ({biz['num_loc']} locations) - {biz.get('revenue', 'N/A')}")
    
    # Generate final CSV
    phase3 = [b for b in businesses if b.get('funnel') == 'Phase 3 \u2014 Qualified Lead']
    phase3.sort(key=lambda x: x.get('priority', 999))
    phase2 = [b for b in businesses if b.get('funnel') == 'Phase 2 \u2014 No Retail Locations']
    phase1 = [b for b in businesses if b.get('funnel') == 'Phase 1 \u2014 Ineligible Product']
    
    sorted_all = phase3 + phase2 + phase1
    
    headers = [
        'Business Name', 'Web Domain', 'Eligible for Shopify Payments',
        'Eligibility Notes', 'Has Retail Locations', 'Number of Retail Locations',
        'Location Details', 'Predicted Annual Revenue', 'Revenue Reasoning',
        'Outreach Priority', 'Funnel Stage'
    ]
    
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(headers)
        
        for biz in sorted_all:
            writer.writerow([
                biz['name'],
                biz['domain'],
                biz['eligible'],
                biz['elig_notes'],
                biz.get('has_retail', ''),
                biz.get('num_loc', ''),
                biz.get('loc_details', ''),
                biz.get('revenue', ''),
                biz.get('reasoning', ''),
                biz.get('priority', ''),
                biz.get('funnel', '')
            ])
    
    print(f"\n{'=' * 60}")
    print(f"FINAL REPORT: {OUTPUT_FILE}")
    print(f"{'=' * 60}")
    print(f"Total rows: {len(sorted_all)}")
    print(f"  Phase 3 — Qualified Leads: {len(phase3)}")
    print(f"  Phase 2 — No Retail Locations: {len(phase2)}")
    print(f"  Phase 1 — Ineligible Products: {len(phase1)}")


if __name__ == '__main__':
    main()
