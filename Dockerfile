# Bước 1: Sử dụng một Image Python 3.11 chính thức làm nền tảng
FROM python:3.11-slim

# Bước 2: Đặt thư mục làm việc bên trong container là /app
WORKDIR /app

# Bước 3: Copy file requirements vào trước để tận dụng cache của Docker
COPY requirements.txt .

# Bước 4: Chạy pip để cài đặt các thư viện từ file requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Bước 5: Copy toàn bộ code của dự án (sentiment_app.py, ...) vào thư mục làm việc /app
COPY . .

# Bước 6: Mở cổng 8501 để Streamlit có thể giao tiếp ra bên ngoài
EXPOSE 8501

# Bước 7: Lệnh sẽ được chạy khi container khởi động
# Lệnh này tương đương với việc bạn gõ "streamlit run sentiment_app.py" trong terminal
CMD ["streamlit", "run", "sentiment_app.py"]
