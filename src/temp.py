import json

# The given JSON data
data = {
    "finCode": 233727,
    "bseScripCode": 710045,
    "bseScripName": "JCOPOCRPS1",
    "bseScripGroup": None,
    "name": "JCOPOCRPS1",
    "industryCode": 113,
    "industry": "Unspecified",
    "hseCode": 206,
    "ticker": None,
    "nseSeries": None,
    "isin": "INE666A03065",
    "shortName": "JCOPOCRPS1",
    "incMonth": "-",
    "incYear": None,
    "status": "Preference",
    "sublisting": None,
    "bseScripId": "JCOPOCRPS1",
    "bseSublisting": None,
    "nseSublisting": None,
    "flag": "A",
    "securityType": "EQUITIES",
    "internalSecurityId": 2599172046,
    "sector": "Materials",
    "sectorExposure": {"Materials": 100.0},
    "category": "Others",
    "sizeExposure": {"Others": 100.0},
    "assetAllocation": {"equity": 100.0},
    "companyDescription": "Jhagadia Copper Limited manufactures copper cathodes, alloy wires, rods, bearing materials, and other related products."
}

# Extract and display assetAllocation
asset_allocation = data.get("assetAllocation", {})
print("Asset Allocation:")
for key, value in asset_allocation.items():
    print(f"{key}: {value}%")