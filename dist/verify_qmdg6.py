from qmdg_data import lap_ban_qmdg, an_bai_luc_nghi
import datetime
import sys

# Windows console fix
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def test_logic():
    print("Testing QMDG Logic...")
    
    # Test Case 1: Yang Ju 1, Hour Giap Ty
    cuc = 1
    is_duong_don = True
    truc_phu = "Thiên Bồng" 
    truc_su = "Hưu" 
    can_gio = "Giáp"
    chi_gio = "Tý"
    
    print(f"\n--- Test Case 1: Ju {cuc}, Yang: {is_duong_don}, Hour: {can_gio} {chi_gio} ---")

    # 1. Earth Plate Check
    dia_ban = an_bai_luc_nghi(cuc, is_duong_don)
    print("Earth Plate:", dia_ban)
    if dia_ban[1] == "Mậu" and dia_ban[2] == "Kỷ":
        print("PASS: Earth Plate Sequence (Yang Ju 1)")
    else:
        print("FAIL: Earth Plate Sequence")

    # 2. Heaven Plate Check
    thien_ban, can_thien_ban, nhan_ban, than_ban, dest_cung = lap_ban_qmdg(
        cuc, truc_phu, truc_su, can_gio, chi_gio, is_duong_don
    )
    print(f"Lead Star Dest: {dest_cung}")
    
    if dest_cung == 1 and thien_ban[1] == "Thiên Bồng":
        print("PASS: Lead Star Movement")

    # Test Case 4: Verify Door Logic
    # Yang Ju 1. Leader (Giap Ty) at Palace 1.
    # Hour: Binh Dan (Diff = 2 hours from Giap Ty).
    # Door Start: 1 (Hưu is at 1 in Local Plate for Ju 1? Wait, Standard Static Plate: Hưu at 1).
    # Steps: 2.
    # Path: 1 -> 2 -> 3. Correct?
    # Yang: 1->2->3.
    # So Lead Door (Hưu) moves to Palace 3 (Zhen).
    
    can_gio_4 = "Bính"
    chi_gio_4 = "Dần"
    print(f"\n--- Test Case 4: Hour {can_gio_4} {chi_gio_4} ---")
    
    _, _, nhan_ban_4, _, _ = lap_ban_qmdg(
        cuc, truc_phu, truc_su, can_gio_4, chi_gio_4, is_duong_don
    )
    
    # Check if Hưu is at 3
    if nhan_ban_4.get(3) == "Hưu": # Original Hưu
       print("PASS: Door Movement (Huu -> 3)")
    else:
       # Find where Huu is
       pos = "Unknown"
       for k, v in nhan_ban_4.items():
            if v == "Hưu" or v == "Hưu Môn": pos = k
       print(f"FAIL: Door Movement. Expected Huu at 3. Got Huu at {pos}")

if __name__ == "__main__":
    test_logic()
