import os
import google.generativeai as genai
from PIL import Image

# --- Cấu hình API Key ---
# Lấy API Key từ Google AI Studio hoặc Google Cloud Vertex AI
# os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY" # Đặt biến môi trường
# Hoặc bạn có thể chỉ định trực tiếp:
genai.configure(api_key="AIzaSyBKhaFpwM2-0qAJ_q0V6T9BRFrS0LUekZA") # Thay YOUR_GEMINI_API_KEY bằng khóa API của bạn

def extract_structured_data_with_gemini(image_path, prompt):
    """
    Extracts structured data from an image using Gemini API.
    """
    model = genai.GenerativeModel('gemini-1.5-flash') # Sử dụng mô hình mới được đề xuất
    img = Image.open(image_path)

    response = model.generate_content([prompt, img], stream=False)
    return response.text

# Đường dẫn đến hình ảnh của bạn
image_to_process = r"D:\Vietralve\Test3\test.jpg"

# Câu lệnh (prompt) để trích xuất dữ liệu. Càng rõ ràng càng tốt.
# Bạn có thể yêu cầu JSON để dễ phân tích cú pháp sau này.
prompt_text = """
Từ bảng trong hình ảnh này, hãy trích xuất thông tin sau đây thành định dạng JSON. 
Mỗi đối tượng JSON đại diện cho một hàng và phải bao gồm các trường:"Tour code", "STT" , "Tên", "Ngày sinh", và "Số điện thoại". 
Nếu một trường không có sẵn, hãy để nó là null.
Hãy đảm bảo rằng dữ liệu được trích xuất là chính xác và đầy đủ.
Hãy trả về kết quả dưới dạng một danh sách JSON.
"""

try:
    # Trích xuất dữ liệu
    extracted_data_json = extract_structured_data_with_gemini(image_to_process, prompt_text)
    print("Dữ liệu trích xuất (JSON):")
    print(extracted_data_json)

    # Nếu muốn chuyển đổi thành Python dict/list
    # import json
    # parsed_data = json.loads(extracted_data_json)
    # print("\nDữ liệu đã phân tích cú pháp:")
    # for item in parsed_data:
    #     print(item)

except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")