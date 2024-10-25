import qrcode
import cv2
from tkinter import filedialog, Tk, simpledialog, messagebox
from PIL import Image

#QR Code creation function
def create_qr_code():
    # ขอข้อมูลจากผู้ใช้ (ลิงค์หรือข้อความ)
    data = simpledialog.askstring("สร้าง QR Code", "ใส่ข้อความหรือลิงค์ที่ต้องการสร้าง QR Code:")
    
    if data:
        # สร้าง QR Code
        qr = qrcode.QRCode(
            version=1, 
            error_correction=qrcode.constants.ERROR_CORRECT_L, 
            box_size=10, 
            border=4
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill="black", back_color="white")
        
#Let the user choose the address and file name to save.
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")])
        if file_path:
            img.save(file_path)
            messagebox.showinfo("สำเร็จ", f"บันทึก QR Code ไว้ที่: {file_path}")

#QR Code decoding function
def decode_qr_code():
# Let the user select the image file they want to decode.
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp"), ("All Files", "*.*")])
    
    if file_path:
# Use OpenCV to decode QR Code
        d = cv2.QRCodeDetector()
        val, _, _ = d.detectAndDecode(cv2.imread(file_path))
        
        if val:
            messagebox.showinfo("ผลลัพธ์", f"ข้อความที่ถอดรหัสได้: {val}")
        else:
            messagebox.showwarning("ไม่สำเร็จ", "ไม่พบ QR Code ในรูปภาพนี้")

#Main functions of the program
def main():
    root = Tk()
    root.withdraw()  # Hide main window
    
    while True:
#Let the user choose the function to use
        choice = simpledialog.askstring("โปรแกรม QR Code", "เลือกฟังก์ชัน:\n1. สร้าง QR Code\n2. ถอดรหัส QR Code\n3. ออกจากโปรแกรม")
        
        if choice == "1":
            create_qr_code()
        elif choice == "2":
            decode_qr_code()
        elif choice == "3":
            messagebox.showinfo("ออกจากโปรแกรม", "กำลังปิดโปรแกรม")
            break
        else:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกตัวเลือกที่ถูกต้อง")

if __name__ == "__main__":
    main()
