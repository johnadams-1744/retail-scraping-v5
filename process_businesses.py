#!/usr/bin/env python3
"""
Retail Location Validation Funnel Processor
Processes businesses through a 3-phase funnel to identify qualified retail leads.
"""

import csv
import re
import json
import os

INPUT_FILE = "/home/ubuntu/.cursor/projects/workspace/uploads/potential_retail_-_Sheet1__1_.csv"
OUTPUT_FILE = "/workspace/retail_location_validation_report.csv"
WORKING_FILE = "/workspace/business_data.json"

def clean_domain(url):
    """Clean a web address to a domain."""
    url = url.strip()
    url = re.sub(r'^https?://', '', url)
    url = re.sub(r'^www\.', '', url)
    url = url.rstrip('/')
    return url

def parse_input_csv():
    """Parse the input CSV and return list of business dicts."""
    businesses = []
    with open(INPUT_FILE, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            biz = {
                'id': i + 1,
                'name': row['Business Name'].strip(),
                'web_address': row['Web Address'].strip(),
                'domain': clean_domain(row['Web Address'].strip()),
                'phase1_eligible': None,
                'phase1_notes': '',
                'has_retail': None,
                'num_locations': 0,
                'location_details': '',
                'predicted_revenue': '',
                'revenue_reasoning': '',
                'outreach_priority': None,
                'funnel_stage': ''
            }
            businesses.append(biz)
    return businesses

def identify_phase1_flags(businesses):
    """Flag businesses that might have prohibited products based on name/domain keywords."""
    prohibited_keywords = {
        'vape': 'e-cigarettes/vaping',
        'vaping': 'e-cigarettes/vaping',
        'vapor': 'e-cigarettes/vaping',
        'ecig': 'e-cigarettes/vaping',
        'e-cig': 'e-cigarettes/vaping',
        'nicotine': 'nicotine products',
        'tobacco': 'tobacco products',
        'cigar': 'tobacco products',
        'smokin': 'tobacco/smoking products',
        'smoke shop': 'tobacco/smoking products',
        'cannabis': 'cannabis/CBD/THC',
        'cbd': 'cannabis/CBD',
        'thc': 'cannabis/THC',
        'marijuana': 'cannabis/marijuana',
        'hemp': 'hemp-derived products',
        'hhc': 'hemp-derived cannabinoid (HHC)',
        'kratom': 'kratom (potential pseudo-pharmaceutical)',
        'firearm': 'firearms/weapons',
        'ammo': 'ammunition',
        'ammunition': 'ammunition',
        'weapon': 'weapons',
        'holster': 'firearm holsters',
        'armament': 'weapons/armament',
        'gun ': 'firearms',
        'guns': 'firearms',
        'rifle': 'firearms',
        'pistol': 'firearms',
        'gambling': 'gambling',
        'casino': 'gambling',
        'lottery': 'gambling',
        'crypto': 'cryptocurrency',
        'bitcoin': 'cryptocurrency',
        'payday': 'money transfer/lending',
        'check cash': 'check cashing',
        'credit repair': 'credit repair',
        'dabbing': 'potential drug paraphernalia',
    }
    
    flagged = []
    for biz in businesses:
        name_lower = biz['name'].lower()
        domain_lower = biz['domain'].lower()
        combined = name_lower + ' ' + domain_lower
        
        for keyword, category in prohibited_keywords.items():
            if keyword in combined:
                flagged.append({
                    'id': biz['id'],
                    'name': biz['name'],
                    'domain': biz['domain'],
                    'keyword': keyword,
                    'potential_category': category
                })
                break
    
    return flagged

def save_working_data(businesses):
    """Save working data to JSON for incremental processing."""
    with open(WORKING_FILE, 'w') as f:
        json.dump(businesses, f, indent=2)

def load_working_data():
    """Load working data from JSON."""
    with open(WORKING_FILE, 'r') as f:
        return json.load(f)

def generate_output_csv(businesses):
    """Generate the final output CSV."""
    phase3 = [b for b in businesses if b['funnel_stage'] == 'Phase 3 — Qualified Lead']
    phase3.sort(key=lambda x: x.get('outreach_priority', 999))
    
    phase2 = [b for b in businesses if b['funnel_stage'] == 'Phase 2 — No Retail Locations']
    phase1 = [b for b in businesses if b['funnel_stage'] == 'Phase 1 — Ineligible Product']
    
    sorted_businesses = phase3 + phase2 + phase1
    
    headers = [
        'Business Name', 'Web Domain', 'Eligible for Shopify Payments',
        'Eligibility Notes', 'Has Retail Locations', 'Number of Retail Locations',
        'Location Details', 'Predicted Annual Revenue', 'Revenue Reasoning',
        'Outreach Priority', 'Funnel Stage'
    ]
    
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headers)
        
        for biz in sorted_businesses:
            eligible = biz.get('phase1_eligible', '')
            if eligible == True:
                eligible_str = 'Yes'
            elif eligible == False:
                eligible_str = 'No'
            elif eligible == 'review':
                eligible_str = 'Review Needed'
            else:
                eligible_str = 'Yes'
            
            notes = biz.get('phase1_notes', '—')
            if not notes or notes == '':
                notes = '—'
            
            has_retail = biz.get('has_retail', '')
            if biz['funnel_stage'] == 'Phase 1 — Ineligible Product':
                has_retail_str = ''
                num_loc = ''
                loc_details = ''
            elif has_retail == True:
                has_retail_str = 'TRUE'
                num_loc = biz.get('num_locations', 0)
                loc_details = biz.get('location_details', 'N/A')
            elif has_retail == 'unknown':
                has_retail_str = 'UNKNOWN'
                num_loc = 0
                loc_details = biz.get('location_details', 'N/A')
            else:
                has_retail_str = 'FALSE'
                num_loc = 0
                loc_details = biz.get('location_details', 'N/A')
            
            revenue = biz.get('predicted_revenue', '')
            reasoning = biz.get('revenue_reasoning', '')
            priority = biz.get('outreach_priority', '')
            if priority is None:
                priority = ''
            
            writer.writerow([
                biz['name'],
                biz['domain'],
                eligible_str,
                notes,
                has_retail_str,
                num_loc,
                loc_details,
                revenue,
                reasoning,
                priority,
                biz['funnel_stage']
            ])
    
    print(f"Output written to {OUTPUT_FILE}")
    return OUTPUT_FILE


if __name__ == '__main__':
    print("Parsing input CSV...")
    businesses = parse_input_csv()
    print(f"Total businesses: {len(businesses)}")
    
    print("\nPhase 1: Flagging potential prohibited products...")
    flagged = identify_phase1_flags(businesses)
    print(f"Flagged for review: {len(flagged)}")
    for f in flagged:
        print(f"  - {f['name']} ({f['domain']}): {f['potential_category']}")
    
    save_working_data(businesses)
    print(f"\nWorking data saved to {WORKING_FILE}")
