from qmdg_data import KY_MON_DATA
from super_detailed_analysis import _get_enriched_info

def test_integration():
    print("Checking ENRICHED_DATA key in KY_MON_DATA...")
    if "ENRICHED_DATA" in KY_MON_DATA:
        print("✅ ENRICHED_DATA found.")
    else:
        print("❌ ENRICHED_DATA NOT found.")
        return

    print("\nTesting _get_enriched_info for 'Thiên Bồng'...")
    info = _get_enriched_info('Thiên Bồng')
    if info:
        print(f"✅ Found Hình thái: {info.get('HÌNH THÁI', 'N/A')}")
        print(f"✅ Found Tính tình: {info.get('TÍNH TÌNH', 'N/A')}")
    else:
        print("❌ No info found for 'Thiên Bồng'.")

    print("\nTesting _get_enriched_info for 'Giáp'...")
    info = _get_enriched_info('Giáp')
    if info:
        print(f"✅ Found Khái niệm: {info.get('KHÁI NIỆM', 'N/A')}")
    else:
        print("❌ No info found for 'Giáp'.")

    print("\nChecking Stem Combos in TRUCTU_TRANH...")
    if "MậuMậu" in KY_MON_DATA["TRUCTU_TRANH"]:
        print(f"✅ 'MậuMậu' found: {KY_MON_DATA['TRUCTU_TRANH']['MậuMậu']['Luận_Giải'][:70]}...")
    else:
        print("❌ 'MậuMậu' NOT found in TRUCTU_TRANH.")

if __name__ == "__main__":
    test_integration()
