#!/usr/bin/env python3
"""
Retail Location Validation Funnel - Full Report Builder
Processes businesses through 3-phase funnel and generates output CSV.
"""

import csv
import re
import json

INPUT_FILE = "/home/ubuntu/.cursor/projects/workspace/uploads/potential_retail_-_Sheet1__1_.csv"
OUTPUT_FILE = "/workspace/retail_location_validation_report.csv"
PHASE2_CANDIDATES_FILE = "/workspace/phase2_candidates.json"

def clean_domain(url):
    url = url.strip()
    url = re.sub(r'^https?://', '', url)
    url = re.sub(r'^www\.', '', url)
    url = url.rstrip('/')
    return url

# Phase 1 determinations from web research
INELIGIBLE = {
    'fogervapes.com': ('No', 'Prohibited: e-cigarettes, vaping devices, and nicotine products'),
    'hiddenhybridholsters.com': ('No', 'Prohibited: firearm holsters'),
    'bakedhhc.com': ('No', 'Prohibited: HHC (hemp-derived cannabinoid) vape products'),
    'piedmonthempco.com': ('No', 'Prohibited: hemp/CBD products including tinctures and CBD-infused balms'),
    'iloveexcitementsmokin.com': ('No', 'Prohibited: smoking paraphernalia and drug paraphernalia (head shop selling dab rigs, water pipes, nectar collectors)'),
    'dabbingwarehouse.com': ('No', 'Prohibited: drug paraphernalia (dabbing equipment, dab rigs, quartz bangers for cannabis consumption)'),
}

REVIEW_NEEDED = {
    'highmonkkratom.com': ('Review Needed', 'Gray area: kratom products — may be classified as pseudo-pharmaceutical with unverified health claims'),
    'cryokratom.com': ('Review Needed', 'Gray area: kratom extract products — may be classified as pseudo-pharmaceutical with unverified health claims'),
    'armament.com': ('Review Needed', 'Gray area: military weapon sighting systems and riflescopes — closely associated with firearms use'),
    'blackmarketgear.com': ('Review Needed', 'Gray area: tactical surplus gear including holsters (a prohibited category) as part of broader inventory'),
    'opticsforce.com': ('Review Needed', 'Gray area: primary products are rifle scopes and firearm optics (557 products) — closely associated with firearms use'),
    'nightprowleroptics.com': ('Review Needed', 'Gray area: thermal scopes and night vision equipment primarily used for hunting/firearms'),
}

# Phase 2 research results - businesses confirmed to have brand-owned retail locations
# Format: domain -> {has_retail, count, details}
RETAIL_LOCATIONS = {
    'store.thearmoury.com': {
        'has_retail': True, 'count': 4,
        'details': '168 Duane Street, New York, NY 10013 (Tribeca); 13 East 69th Street, New York, NY 10021 (Upper East Side); 501 Pedder Building, 12 Pedder Street, Central, Hong Kong (Pedder Arcade); Rosewood Hotel, Floor 55, 18 Salisbury Road, Tsim Sha Tsui, Hong Kong (Carlyle Club, by appointment)'
    },
    'baltimorebilliards.com': {
        'has_retail': True, 'count': 1,
        'details': '8906 Waltham Woods Rd, Parkville, MD 21234'
    },
    'frawleysvarietystore.com': {
        'has_retail': True, 'count': 1,
        'details': '225 Main Street SW, New Albin, IA 52160'
    },
    'thefurniture-nest.com': {
        'has_retail': True, 'count': 1,
        'details': '329 Civic Ave, Salisbury, MD 21804 (Twilley Shopping Center)'
    },
    'galeriajoliet.com': {
        'has_retail': True, 'count': 2,
        'details': '692 Theodore St #A, Joliet, IL 60435; 2134 West Jefferson Street, Joliet, IL 60435 (Marycrest Shopping Center)'
    },
    'hadleyolivia.com': {
        'has_retail': True, 'count': 1,
        'details': '31896 Plaza Drive Suite D1, San Juan Capistrano, CA 92675'
    },
    'marksfurnituredirect.com': {
        'has_retail': True, 'count': 1,
        'details': '2180 GI Maddox Parkway Suite A, Chatsworth, GA 30705'
    },
    'rework-furniture.com': {
        'has_retail': True, 'count': 1,
        'details': '7550 Roosevelt Rd, Forest Park, IL 60130 (showroom by appointment)'
    },
    'furnituredepot.ca': {
        'has_retail': True, 'count': 1,
        'details': '6075 Mavis Rd, Mississauga, ON L5R 4G6 (Heartland Town Centre)'
    },
    'cheapoliberty.com': {
        'has_retail': True, 'count': 1,
        'details': '1915 Industrial Dr, Liberty, MO 64068'
    },
    'americanhomeexpress.com': {
        'has_retail': True, 'count': 1,
        'details': '4722 Eisenhauer Rd #105, San Antonio, TX 78218'
    },
    'shop.thehotelemma.com': {
        'has_retail': True, 'count': 1,
        'details': '136 E. Grayson Street, San Antonio, TX 78215 (Curio gift shop at Hotel Emma, Pearl District)'
    },
    'royhenryvickers.com': {
        'has_retail': True, 'count': 1,
        'details': '350 Campbell Street, Tofino, BC V0R 2Z0 (Eagle Aerie Gallery)'
    },
    'kincaidsmusic.com': {
        'has_retail': True, 'count': 1,
        'details': '1325 W 1st St, Springfield, OH 45504'
    },
    'shop.jessebrowns.com': {
        'has_retail': True, 'count': 1,
        'details': '4732 Sharon Road, Suite 2M, Charlotte, NC 28210 (Sharon Corners at SouthPark)'
    },
    'libertysafeofcollegestation.com': {
        'has_retail': True, 'count': 1,
        'details': '1055 Texas Ave S, Suite 104, College Station, TX 77840'
    },
    'recreationsoutlet.com': {
        'has_retail': True, 'count': 2,
        'details': '885 Business 28, Milford, OH 45150 (Cincinnati area); 484 W Olentangy/Powell Road, Powell, OH 43065 (Columbus area)'
    },
    'shop.btbconsignments.com': {
        'has_retail': True, 'count': 2,
        'details': '1820-A2 6th Avenue SE, Decatur, AL 35601 (Gateway Shopping Center); 124 4th Street Southwest, Cullman, AL 35055'
    },
    'giftcorral.com': {
        'has_retail': True, 'count': 5,
        'details': '237 E. Main St., Bozeman, MT 59715 (Historic Downtown); 1500 N. 7th Ave., Bozeman, MT 59715 (Bozeman Walmart); 850 Gallatin Field Road, Belgrade, MT 59714 (Bozeman Yellowstone International Airport); 117 W. Front Street, Missoula, MT 59802 (Downtown Missoula); 1455 Hwy. 2 E., Whitehall, MT 59759 (Lewis & Clark Caverns State Park, seasonal)'
    },
    'tigertraditions.com': {
        'has_retail': True, 'count': 2,
        'details': '5134 Sunset Blvd., Lexington, SC 29072 (Traditions Fine Jewelers); 481 Town Center Place, Columbia, SC 29229 (Village of Sandhill)'
    },
    'holidaywarehouse.com': {
        'has_retail': True, 'count': 1,
        'details': '2819 W 15th St, Plano, TX 75075 (30,000 sq ft showroom)'
    },
    'quiltexpressions.com': {
        'has_retail': True, 'count': 1,
        'details': '1200 East Watertower Street, Suite 120, Meridian, ID 83642 (by appointment)'
    },
}

# Phase 2 candidates - businesses most likely to have retail locations based on name/context
# These need web research to confirm
PHASE2_HIGH_PRIORITY = []

def parse_input():
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
    return businesses

def apply_phase1(businesses):
    eligible_count = 0
    ineligible_count = 0
    review_count = 0
    
    for biz in businesses:
        domain = biz['domain'].lower()
        domain_no_www = re.sub(r'^www\.', '', domain)
        
        if domain_no_www in INELIGIBLE:
            biz['phase1'] = INELIGIBLE[domain_no_www][0]
            biz['phase1_notes'] = INELIGIBLE[domain_no_www][1]
            biz['funnel_stage'] = 'Phase 1 — Ineligible Product'
            ineligible_count += 1
        elif domain_no_www in REVIEW_NEEDED:
            biz['phase1'] = REVIEW_NEEDED[domain_no_www][0]
            biz['phase1_notes'] = REVIEW_NEEDED[domain_no_www][1]
            biz['funnel_stage'] = ''  # Will be determined in Phase 2
            review_count += 1
        else:
            biz['phase1'] = 'Yes'
            biz['phase1_notes'] = '\u2014'
            biz['funnel_stage'] = ''  # Will be determined in Phase 2
            eligible_count += 1
    
    print(f"Phase 1 complete: {eligible_count} eligible, {ineligible_count} ineligible, {review_count} review needed.")
    print(f"Proceeding to Phase 2 with {eligible_count + review_count} businesses.")
    return businesses

def identify_phase2_candidates(businesses):
    """Identify businesses most likely to have physical retail locations."""
    retail_keywords = [
        'store', 'shop', 'boutique', 'gallery', 'cafe', 'coffee',
        'bakery', 'pastry', 'kitchen', 'restaurant', 'grill', 'deli',
        'hardware', 'furniture', 'mattress', 'spa', 'salon', 'market',
        'jeweler', 'shoes', 'boots', 'locker', 'skate', 'bike',
        'farm', 'nursery', 'florist', 'flower', 'pet', 'candy',
        'sweet', 'chocolate', 'brewery', 'winery', 'roast', 'meat',
        'butcher', 'outlet', 'depot', 'supply', 'warehouse',
        'consignment', 'vintage', 'thrift', 'emporium', 'general store',
        'instrument', 'music', 'hotel', 'billiard', 'arcade',
    ]
    
    candidates = []
    for biz in businesses:
        if biz.get('funnel_stage') == 'Phase 1 — Ineligible Product':
            continue
        
        name_lower = biz['name'].lower()
        domain_lower = biz['domain'].lower()
        combined = name_lower + ' ' + domain_lower
        
        is_candidate = False
        for kw in retail_keywords:
            if kw in combined:
                is_candidate = True
                break
        
        if is_candidate:
            candidates.append({
                'id': biz['id'],
                'name': biz['name'],
                'domain': biz['domain'],
            })
    
    return candidates


def apply_phase2(businesses, retail_data):
    """Apply Phase 2 retail location data."""
    retail_count = 0
    no_retail_count = 0
    
    for biz in businesses:
        if biz.get('funnel_stage') == 'Phase 1 — Ineligible Product':
            biz['has_retail'] = ''
            biz['num_locations'] = ''
            biz['location_details'] = ''
            continue
        
        domain = biz['domain'].lower()
        domain_no_www = re.sub(r'^www\.', '', domain)
        
        if domain_no_www in retail_data:
            info = retail_data[domain_no_www]
            biz['has_retail'] = 'TRUE'
            biz['num_locations'] = info['count']
            biz['location_details'] = info['details']
            biz['funnel_stage'] = 'Phase 3 — Qualified Lead'
            retail_count += 1
        else:
            biz['has_retail'] = 'FALSE'
            biz['num_locations'] = 0
            biz['location_details'] = 'N/A'
            if not biz.get('funnel_stage'):
                biz['funnel_stage'] = 'Phase 2 — No Retail Locations'
            no_retail_count += 1
    
    print(f"Phase 2 complete: {retail_count} businesses have brand-owned retail locations, {no_retail_count} do not.")
    print(f"Proceeding to Phase 3 with {retail_count} businesses.")
    return businesses


def apply_phase3(businesses, revenue_data):
    """Apply Phase 3 revenue estimates and priority rankings."""
    qualified = [(b, revenue_data.get(re.sub(r'^www\.', '', b['domain'].lower()), {}))
                 for b in businesses
                 if b.get('funnel_stage') == 'Phase 3 — Qualified Lead']
    
    # Sort by estimated revenue (higher = higher priority) and number of locations
    qualified.sort(key=lambda x: (x[1].get('sort_key', 0), x[0].get('num_locations', 0)), reverse=True)
    
    for rank, (biz, rev_info) in enumerate(qualified, 1):
        domain = re.sub(r'^www\.', '', biz['domain'].lower())
        if domain in revenue_data:
            biz['predicted_revenue'] = revenue_data[domain]['estimate']
            biz['revenue_reasoning'] = revenue_data[domain]['reasoning']
        biz['outreach_priority'] = rank
    
    return businesses


def generate_csv(businesses):
    headers = [
        'Business Name', 'Web Domain', 'Eligible for Shopify Payments',
        'Eligibility Notes', 'Has Retail Locations', 'Number of Retail Locations',
        'Location Details', 'Predicted Annual Revenue', 'Revenue Reasoning',
        'Outreach Priority', 'Funnel Stage'
    ]
    
    phase3 = [b for b in businesses if b.get('funnel_stage') == 'Phase 3 — Qualified Lead']
    phase3.sort(key=lambda x: x.get('outreach_priority', 999))
    phase2 = [b for b in businesses if b.get('funnel_stage') == 'Phase 2 — No Retail Locations']
    phase1 = [b for b in businesses if b.get('funnel_stage') == 'Phase 1 — Ineligible Product']
    
    sorted_biz = phase3 + phase2 + phase1
    
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        
        for biz in sorted_biz:
            writer.writerow([
                biz['name'],
                biz['domain'],
                biz.get('phase1', 'Yes'),
                biz.get('phase1_notes', '\u2014'),
                biz.get('has_retail', ''),
                biz.get('num_locations', ''),
                biz.get('location_details', ''),
                biz.get('predicted_revenue', ''),
                biz.get('revenue_reasoning', ''),
                biz.get('outreach_priority', ''),
                biz.get('funnel_stage', '')
            ])
    
    print(f"\nFinal CSV written to {OUTPUT_FILE}")
    print(f"Total rows: {len(sorted_biz)}")
    print(f"  Phase 3 qualified leads: {len(phase3)}")
    print(f"  Phase 2 no retail: {len(phase2)}")
    print(f"  Phase 1 ineligible: {len(phase1)}")


if __name__ == '__main__':
    print("=" * 60)
    print("RETAIL LOCATION VALIDATION FUNNEL")
    print("=" * 60)
    
    businesses = parse_input()
    print(f"\nTotal businesses loaded: {len(businesses)}")
    
    print("\n--- PHASE 1: Product Eligibility Screen ---")
    businesses = apply_phase1(businesses)
    
    print("\n--- Identifying Phase 2 Candidates ---")
    candidates = identify_phase2_candidates(businesses)
    print(f"High-priority candidates for retail location research: {len(candidates)}")
    
    with open(PHASE2_CANDIDATES_FILE, 'w') as f:
        json.dump(candidates, f, indent=2)
    print(f"Candidates saved to {PHASE2_CANDIDATES_FILE}")
    
    for c in candidates:
        print(f"  - {c['name']} ({c['domain']})")
