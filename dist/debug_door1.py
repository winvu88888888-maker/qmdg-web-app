from qmdg_calc import calculate_qmdg_params
from qmdg_data import lap_ban_qmdg, an_bai_luc_nghi
import datetime
import sys

# Windows console fix
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def debug_now():
    # Use User's time context: 2025-12-06 15:49
    # Format: day/month/year hour:minute
    # String to datetime
    dt = datetime.datetime(2025, 12, 6, 15, 49)
    print(f"Debug Time: {dt}")
    
    # 1. Calc Params
    params = calculate_qmdg_params(dt)
    print("Params:", params)
    
    cuc = params['cuc']
    is_duong_don = params['is_duong_don']
    truc_phu = params['truc_phu']
    truc_su = params['truc_su']
    can_gio = params['can_gio']
    chi_gio = params['chi_gio']
    
    print(f"Ju: {cuc}, Yang: {is_duong_don}, LeaderStar: {truc_phu}, LeaderDoor: {truc_su}")
    print(f"Hour: {can_gio} {chi_gio}")
    
    # 2. Lap Ban
    thien_ban, can_thien_ban, nhan_ban, than_ban, cung_dich_truc_phu = lap_ban_qmdg(
        cuc, truc_phu, truc_su, can_gio, chi_gio, is_duong_don
    )
    
    print("Nhan Ban (Doors):", nhan_ban)
    
    # check Door at Palace 1
    door1 = nhan_ban.get(1, "N/A")
    print(f"Door at Palace 1: {door1}")
    
    expected = "Kinh"
    if door1 == expected or door1 == expected + " Môn":
        print("MATCH: Door at 1 is Kinh.")
    else:
        print(f"MISMATCH: Expected Kinh at 1. Got {door1}.")

if __name__ == "__main__":
    debug_now()
