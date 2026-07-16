---
name: writing-style
description: Kỹ năng viết báo cáo kỹ thuật với văn phong học thuật chuẩn mực, cân bằng (Moderate Perplexity & Burstiness), chính xác, logic và không lạm dụng từ vựng ẩn dụ hay sáo rỗng.
---

# Kỹ năng Viết Báo cáo Kỹ thuật (Writing Style Skill)

Kỹ năng này định hướng cách viết nội dung báo cáo học thuật, kỹ thuật (đặc biệt áp dụng cho dự án **Secret Letter**) nhằm đảm bảo văn phong tự nhiên, chuyên nghiệp, logic mạch lạc và tránh xa lối viết rập khuôn của AI nhưng cũng không bị "làm lố" (over-engineered) bằng từ vựng quá kịch tính.

## 1. Mục tiêu cốt lõi (Core Objectives)
- **Giọng văn kỹ sư chuyên nghiệp**: Thể hiện tư duy phản biện và sự am hiểu tường tận về hệ thống thông qua ngôn từ khách quan, rành mạch.
- **Tính chính xác kỹ thuật**: Mọi thông tin, thuật toán, luồng dữ liệu phải bám sát thực tế dự án. Có tài liệu tham khảo khi nhắc đến các tiêu chuẩn (VD: NIST, W3C).
- **Mạch lạc và súc tích**: Mô tả đầy đủ, rõ ý, đi thẳng vào trọng tâm, không dông dài.
- **Góc nhìn đa chiều (Perspectives)**: Đưa ra các góc nhìn hay, sắc sảo (ví dụ: sự đánh đổi (trade-off) hoặc phân tích dưới góc nhìn của kẻ tấn công) bằng ngôn ngữ điềm đạm, không cường điệu hóa.

## 2. Tiết chế Perplexity và Burstiness (Balanced Style)
Thay vì đẩy Perplexity và Burstiness lên mức tối đa gây cảm giác "gồng" và nặng nề, hãy giữ ở mức **cân bằng (moderate)**:
* **Burstiness (Nhịp điệu câu tự nhiên)**: Đan xen hợp lý giữa câu ngắn (nhấn mạnh ý chính) và câu dài (giải thích logic). Không cố ý băm nát câu một cách khiên cưỡng.
* **Perplexity (Từ vựng kỹ thuật chuẩn xác)**: Dùng từ ngữ đa dạng nhưng phải đúng chuẩn ngành IT/An toàn thông tin. Không dùng từ vựng mang tính văn chương, ẩn dụ quá đà. 

## 3. Danh sách các lỗi hành văn CẦN XÓA BỎ
- ❌ **Tránh các "AI Cliches" (sáo rỗng)**: "Có thể nói rằng", "Nhìn chung", "Tóm lại", "Đóng vai trò quan trọng", "Như chúng ta đã biết".
- ❌ **Tránh dịch word-by-word**: "Đi sâu vào" (Delve into), "Điều mấu chốt là" (It is pivotal), "Hơn thế nữa/Ngoài ra" ở đầu đoạn.
- ❌ **Tránh các từ ngữ tuyệt đối hóa**: "Bảo mật tuyệt đối", "An toàn 100%", "Xóa bỏ hoàn toàn", "Giải quyết triệt để". Hãy dùng: "Giảm thiểu tối đa", "Hạn chế đáng kể", "Gia tăng độ khó".
- ❌ **Tránh từ vựng ẩn dụ/kịch tính hóa (Over-engineered)**: Không dùng các từ đao to búa lớn mang tính điện ảnh như *"quyền sinh sát", "rào chắn sinh tồn", "đập tan", "kẻ thù", "bòn rút"*. Hãy dùng ngôn ngữ kỹ thuật khách quan: *"quyền kiểm soát", "cơ chế bảo vệ", "ngăn chặn", "tin tặc/kẻ tấn công", "thu thập trái phép"*.

## 4. Phương pháp luận viết Học thuật (Academic Writing)
1. **Tính khách quan**: Viết dưới góc nhìn ngôi thứ ba ("Hệ thống xử lý", "Nghiên cứu chỉ ra").
2. **Cấu trúc P-E-E (Point - Evidence - Explain)**: 
   - Đưa ra luận điểm (Ví dụ: Server không thể đọc dữ liệu).
   - Nêu bằng chứng kỹ thuật (Ví dụ: Khóa giải mã nằm trong URL Fragment).
   - Giải thích giá trị (Ví dụ: Đáp ứng mô hình Zero-Knowledge).
3. **Mỗi đoạn văn một ý chính**: Bắt đầu bằng câu chủ đề (Topic sentence), phần còn lại để chứng minh luận điểm đó.

## 5. Ví dụ So sánh thực tế
* **Văn phong AI (Sáo rỗng, rập khuôn)**: 
  *"Dự án Secret Letter đóng vai trò quan trọng. Hơn nữa, nó sử dụng thuật toán AES-256-GCM để mang lại sự bảo mật tuyệt đối."* 
* **Văn phong Over-engineered (Làm lố, kịch tính)**:
  *"Secret Letter tước đoạt quyền sinh sát của máy chủ, đập tan mọi nỗ lực nhòm ngó của kẻ thù. Bọn chúng sẽ chỉ nhận lại sự tuyệt vọng khi cố gắng giải mã."*
* **Văn phong Chuẩn Kỹ sư (Cân bằng, khách quan)**:
  *"Lộ lọt dữ liệu từ các máy chủ trung gian là một rủi ro hiện hữu. Bằng cách thực thi mã hóa cục bộ qua WebCrypto API trước khi truyền tải, Secret Letter thu hẹp đáng kể quyền truy cập của Backend. Trách nhiệm bảo mật được dịch chuyển về thiết bị đầu cuối, từ đó kiến tạo một hệ thống Zero-Knowledge thực tiễn."*

## 6. Lời nhắc (Prompt Checklist) cho AI
Mỗi khi viết, hãy tự kiểm duyệt trong "Suy nghĩ" (Thought):
- Đã xóa các "AI cliches", từ tuyệt đối hóa (hoàn toàn, triệt để) chưa?
- **Đã "hạ nhiệt" (tone down) các từ vựng ẩn dụ, đảm bảo không bị kịch tính hóa (over-engineered) chưa?**
- Góc nhìn đa chiều và tính kỹ thuật có được giữ vững bằng ngôn ngữ khách quan không?
- Đã trích dẫn (citation) đầy đủ cho các tiêu chuẩn công nghệ chưa?
