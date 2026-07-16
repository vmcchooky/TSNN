---
name: writing-style
description: Kỹ năng viết báo cáo kỹ thuật với văn phong học thuật chuẩn mực, cân bằng (Moderate Perplexity & Burstiness), chính xác, logic và không lạm dụng từ vựng ẩn dụ hay sáo rỗng.
---

# Kỹ năng Viết Báo cáo Kỹ thuật (Writing Style Skill)

Kỹ năng này định hướng cách viết nội dung báo cáo học thuật, kỹ thuật (đặc biệt áp dụng cho dự án **Safe Zone** — Hệ thống chống lừa đảo ở mức DNS) nhằm đảm bảo văn phong tự nhiên, chuyên nghiệp, logic mạch lạc và tránh xa lối viết rập khuôn của AI nhưng cũng không bị "làm lố" (over-engineered) bằng từ vựng quá kịch tính.

## 1. Mục tiêu cốt lõi (Core Objectives)
- **Giọng văn kỹ sư chuyên nghiệp**: Thể hiện tư duy phản biện và sự am hiểu tường tận về hệ thống thông qua ngôn từ khách quan, rành mạch.
- **Tính chính xác kỹ thuật**: Mọi thông tin về kiến trúc DNS, luồng phân tích, thuật toán chấm điểm, cơ chế đồng bộ dữ liệu phải bám sát thực tế dự án. Có tài liệu tham khảo khi nhắc đến các tiêu chuẩn (VD: RFC 8484 cho DoH, RFC 7858 cho DoT).
- **Mạch lạc và súc tích**: Mô tả đầy đủ, rõ ý, đi thẳng vào trọng tâm, không dông dài.
- **Góc nhìn đa chiều (Perspectives)**: Đưa ra các góc nhìn sắc sảo (ví dụ: sự đánh đổi (trade-off) giữa hiệu năng phân giải DNS và độ sâu phân tích rủi ro, hoặc phân tích dưới góc nhìn của kẻ tấn công lừa đảo) bằng ngôn ngữ điềm đạm, không cường điệu hóa.

## 2. Tiết chế Perplexity và Burstiness (Balanced Style)
Thay vì đẩy Perplexity và Burstiness lên mức tối đa gây cảm giác "gồng" và nặng nề, hãy giữ ở mức **cân bằng (moderate)**:
* **Burstiness (Nhịp điệu câu tự nhiên)**: Đan xen hợp lý giữa câu ngắn (nhấn mạnh ý chính) và câu dài (giải thích logic). Không cố ý băm nát câu một cách khiên cưỡng.
* **Perplexity (Từ vựng kỹ thuật chuẩn xác)**: Dùng từ ngữ đa dạng nhưng phải đúng chuẩn ngành An ninh mạng / Hệ thống mạng. Không dùng từ vựng mang tính văn chương, ẩn dụ quá đà. 

## 3. Danh sách các lỗi hành văn CẦN XÓA BỎ
- ❌ **Tránh các "AI Cliches" (sáo rỗng)**: "Có thể nói rằng", "Nhìn chung", "Tóm lại", "Đóng vai trò quan trọng", "Như chúng ta đã biết".
- ❌ **Tránh dịch word-by-word**: "Đi sâu vào" (Delve into), "Điều mấu chốt là" (It is pivotal), "Hơn thế nữa/Ngoài ra" ở đầu đoạn.
- ❌ **Tránh các từ ngữ tuyệt đối hóa**: "Bảo mật tuyệt đối", "An toàn 100%", "Xóa bỏ hoàn toàn", "Giải quyết triệt để". Hãy dùng: "Giảm thiểu tối đa", "Hạn chế đáng kể", "Gia tăng độ khó".
- ❌ **Tránh từ vựng ẩn dụ/kịch tính hóa (Over-engineered)**: Không dùng các từ đao to búa lớn mang tính điện ảnh như *"quyền sinh sát", "rào chắn sinh tồn", "đập tan", "kẻ thù", "bòn rút"*. Hãy dùng ngôn ngữ kỹ thuật khách quan: *"quyền kiểm soát", "cơ chế bảo vệ", "ngăn chặn", "tin tặc/kẻ tấn công", "thu thập trái phép"*.

## 4. Phương pháp luận viết Học thuật (Academic Writing)
1. **Tính khách quan**: Viết dưới góc nhìn ngôi thứ ba ("Hệ thống xử lý", "Nghiên cứu chỉ ra").
2. **Cấu trúc P-E-E (Point - Evidence - Explain)**: 
   - Đưa ra luận điểm (Ví dụ: Phân tích ngữ vựng cho phép phát hiện tên miền lừa đảo mà không cần truy vấn nguồn bên ngoài).
   - Nêu bằng chứng kỹ thuật (Ví dụ: Thuật toán tính Shannon Entropy trên nhãn chính của tên miền, kết hợp phát hiện Punycode và từ khóa lừa đảo tiếng Việt).
   - Giải thích giá trị (Ví dụ: Nhờ đó, độ trễ phân giải DNS được giữ ở mức tối thiểu trong khi vẫn duy trì khả năng phát hiện DGA và tấn công đồng hình IDN).
3. **Mỗi đoạn văn một ý chính**: Bắt đầu bằng câu chủ đề (Topic sentence), phần còn lại để chứng minh luận điểm đó.

## 5. Ví dụ So sánh thực tế
* **Văn phong AI (Sáo rỗng, rập khuôn)**: 
  *"Dự án Safe Zone đóng vai trò quan trọng trong việc bảo vệ người dùng. Hơn nữa, nó sử dụng DNS over HTTPS để mang lại sự an toàn tuyệt đối cho mọi truy vấn."* 
* **Văn phong Over-engineered (Làm lố, kịch tính)**:
  *"Safe Zone đập tan mọi âm mưu lừa đảo ngay từ tầng DNS. Bọn tội phạm mạng sẽ chỉ nhận lại sự bất lực khi tên miền giả mạo bị nuốt chửng vào hố sinkhole."*
* **Văn phong Chuẩn Kỹ sư (Cân bằng, khách quan)**:
  *"Tấn công lừa đảo qua tên miền giả mạo đang gia tăng tại Việt Nam, đặc biệt nhắm vào các cổng dịch vụ công trực tuyến. Safe Zone tiếp cận bài toán này từ tầng phân giải DNS, nơi mỗi truy vấn được đối chiếu với nguồn dữ liệu đe dọa (threat feed) và qua bộ chấm điểm heuristic trước khi quyết định cho phép hoặc chặn. Kiến trúc fail-open đảm bảo rằng khi một thành phần phụ trợ (Redis, AI) gặp sự cố, dịch vụ phân giải vẫn hoạt động liên tục thay vì từ chối mọi truy vấn."*

## 6. Thuật ngữ chuyên ngành cho Safe Zone
Khi viết báo cáo, sử dụng nhất quán các thuật ngữ kỹ thuật sau:

| Tiếng Anh | Tiếng Việt (học thuật) | Ngữ cảnh |
|-----------|----------------------|----------|
| Phishing | Tấn công giả mạo (lừa đảo trực tuyến) | Mô hình đe dọa chính |
| DNS sinkhole | Hố DNS (DNS sinkhole) | Chiến lược chặn: chuyển hướng tên miền độc hại |
| Threat intelligence | Tình báo mối đe dọa | Nguồn dữ liệu URLhaus, OpenPhish |
| Lexical scoring | Chấm điểm ngữ vựng (phân tích heuristic) | Phân tích xác định luận (deterministic) |
| Domain risk scoring | Chấm điểm rủi ro tên miền | Thang điểm 0-100 với phán định |
| Brand spoofing | Giả mạo thương hiệu | Phát hiện typosquatting |
| DGA (Domain Generation Algorithm) | Thuật toán sinh tên miền tự động | Phát hiện qua Shannon Entropy |
| Bloom filter | Bộ lọc Bloom | Tra cứu whitelist xác suất |
| Fail-open | Mở khi lỗi (fail-open) | Triết lý: dịch vụ tiếp tục khi thành phần phụ gặp sự cố |
| Reverse proxy | Proxy ngược | Caddy |
| Embedded SPA | Ứng dụng trang đơn nhúng | React UI nhúng vào Go binary |
| Hot-reload | Tải lại nóng | Cấu hình phân tích qua Pub/Sub |

## 7. Lời nhắc (Prompt Checklist) cho AI
Mỗi khi viết, hãy tự kiểm duyệt trong "Suy nghĩ" (Thought):
- Đã xóa các "AI cliches", từ tuyệt đối hóa (hoàn toàn, triệt để) chưa?
- **Đã "hạ nhiệt" (tone down) các từ vựng ẩn dụ, đảm bảo không bị kịch tính hóa (over-engineered) chưa?**
- Góc nhìn đa chiều và tính kỹ thuật có được giữ vững bằng ngôn ngữ khách quan không?
- Đã trích dẫn (citation) đầy đủ cho các tiêu chuẩn công nghệ (RFC, NIST, W3C) chưa?
- Các thuật ngữ chuyên ngành DNS/An ninh mạng đã được sử dụng nhất quán theo bảng thuật ngữ chưa?
