try:
    from qmdg_data import tinh_dia_chi_gio, TOPIC_INTERPRETATIONS
    print("Import qmdg_data successful")
    print(f"tinh_dia_chi_gio(12): {tinh_dia_chi_gio(12)}")
    print(f"TOPIC keys: {list(TOPIC_INTERPRETATIONS.keys())}")
except Exception as e:
    print(f"Import qmdg_data failed: {e}")

try:
    import qmdg_calc
    from datetime import datetime
    print("Import qmdg_calc successful")
    params = qmdg_calc.calculate_qmdg_params(datetime.now())
    print(f"Params: {params}")
except Exception as e:
    print(f"Import qmdg_calc failed: {e}")