import streamlit as st
from transformers import pipeline
# --- TẢI MÔ HÌNH (chỉ tải một lần và lưu lại) ---
# @st.cache_resource là một "decorator" đặc biệt của Streamlit
# nó báo cho Streamlit biết chỉ cần chạy hàm này một lần duy nhất
# và lưu kết quả (mô hình đã tải) vào bộ nhớ đệm.
# Điều này giúp ứng dụng không phải tải lại mô hình mỗi lần người dùng tương tác.
@st.cache_resource
def load_model():
    print('Đang tải mô hình')
    model_pipeline = pipeline('sentiment-analysis')
    print('Tải mô hình thành công')
    return model_pipeline
sentiment_pipeline = load_model()
# st.title(): Tạo tiêu đề cho trang web
st.title('Ứng Dụng Phân tích cảm xúc tích cực/tiêu cực của bình luận')
# st.text_area(): Tạo một ô văn bản lớn để người dùng nhập liệu
user_input = st.text_area('Nhập Bình luận bằng tiếng Anh')
# st.button(): Tạo một nút bấm
if st.button('Phân tích'):
    if user_input:
        result = sentiment_pipeline(user_input)
        #In kết quả ra trang web
        st.write('---Kết quả---')
        label = result[0]['label']
        score = result[0]['score']
        if label == 'POSITIVE':
            # st.success() hiển thị một hộp thông báo màu xanh lá
            st.success(f"Kết quả: Tích cực (POSITIVE) - Độ tin cậy: {score:.2%}")
        else:
            # st.error() hiển thị một hộp thông báo màu đỏ
            st.error(f"Kết quả: Tiêu cực (NEGATIVE) - Độ tin cậy: {score:.2%}")
    else:
        st.warning("Vui lòng nhập một bình luận để phân tích.")

