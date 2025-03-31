# quan_ly_sinh_vien.py

class QuanLySinhVien:
    def __init__(self):
        self.sinh_vien = {}  # Từ điển để lưu trữ dữ liệu sinh viên {id: tên}

    def them_sinh_vien(self, ma_sv, ten_sv):
        if ma_sv in self.sinh_vien:
            print("Mã sinh viên đã tồn tại.")
        else:
            self.sinh_vien[ma_sv] = ten_sv
            print("Thêm sinh viên thành công.")

    def xoa_sinh_vien(self, ma_sv):
        if ma_sv in self.sinh_vien:
            del self.sinh_vien[ma_sv]
            print("Xóa sinh viên thành công.")
        else:
            print("Không tìm thấy mã sinh viên.")

    def tim_sinh_vien_theo_ma(self, ma_sv):
        return self.sinh_vien.get(ma_sv, "Không tìm thấy mã sinh viên.")

    def danh_sach_sinh_vien(self):
        sinh_vien_sap_xep = sorted(self.sinh_vien.items())
        print("Danh sách sinh viên:")
        for ma_sv, ten_sv in sinh_vien_sap_xep:
            print(f"Mã: {ma_sv}, Tên: {ten_sv}")


def main():
    qlsv = QuanLySinhVien()

    while True:
        print("\nHệ Thống Quản Lý Sinh Viên")
        print("1. Thêm Sinh Viên")
        print("2. Xóa Sinh Viên")
        print("3. Tìm Sinh Viên Theo Mã")
        print("4. Danh Sách Sinh Viên")
        print("5. Thoát")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == "1":
            ma_sv = input("Nhập mã sinh viên: ")
            ten_sv = input("Nhập tên sinh viên: ")
            qlsv.them_sinh_vien(ma_sv, ten_sv)
        elif lua_chon == "2":
            ma_sv = input("Nhập mã sinh viên cần xóa: ")
            qlsv.xoa_sinh_vien(ma_sv)
        elif lua_chon == "3":
            ma_sv = input("Nhập mã sinh viên cần tìm: ")
            print(qlsv.tim_sinh_vien_theo_ma(ma_sv))
        elif lua_chon == "4":
            qlsv.danh_sach_sinh_vien()
        elif lua_chon == "5":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
