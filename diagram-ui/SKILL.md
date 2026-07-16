---
name: diagram-ui
description: Skill guidelines for drawing scientific, neat, and highly readable software architecture and UI diagrams (Mermaid, TikZ, etc.).
---

# Hướng dẫn vẽ Sơ đồ Kiến trúc và UI (Diagram UI Skill)

Kỹ năng này định hướng các tiêu chuẩn và phương pháp tốt nhất (best practices) để tạo ra các sơ đồ kiến trúc phần mềm, luồng người dùng (user flow), và UI/UX khoa học, chỉn chu và dễ hiểu.

## 1. Nguyên tắc cốt lõi (Core Principles)
* **Xác định mục đích rõ ràng**: Mỗi sơ đồ chỉ nên giải quyết một vấn đề (VD: Luồng dữ liệu, kiến trúc hạ tầng, hoặc hành trình người dùng). Tránh nhồi nhét quá nhiều thông tin vào một hình.
* **Theo đuổi sự tối giản (Minimalism)**: Loại bỏ các chi tiết thừa. Nếu sơ đồ quá lớn, hãy chia nhỏ thành các sơ đồ con (sub-processes).
* **Luồng dữ liệu logic**: Luôn duy trì hướng đi nhất quán (từ trên xuống dưới, hoặc từ trái sang phải). Không sử dụng mũi tên hai chiều nếu không thực sự cần thiết, thay vào đó dùng hai mũi tên một chiều để làm rõ request/response.
* **Sử dụng ký hiệu chuẩn**: Tuân thủ các hình khối quen thuộc (VD: Hình chữ nhật bo tròn cho trạng thái/nút, hình thoi cho rẽ nhánh logic, hình trụ cho database). Luôn có chú thích (Legend) nếu dùng ký hiệu lạ.

## 2. Tiêu chuẩn màu sắc & Thẩm mỹ
* **Màu sắc nhạt, thanh lịch (Pastel/Light Colors)**: Sử dụng các gam màu nhạt (VD: `cyan!3`, `blue!3`, `gray!2` trong TikZ hoặc Hex `#F0F4F8`, `#E1F5FE` trong Web) làm nền cho các Node để làm nổi bật chữ.
* **Giới hạn số lượng màu**: Không dùng quá 3-4 màu chính. Dùng màu sắc để phân loại (VD: Màu xanh cho thao tác thành công, màu đỏ cho lỗi, màu xám cho hệ thống bên thứ 3).
* **Đường nét rõ ràng (Curved/Rounded)**: Sử dụng các góc bo tròn (`rounded corners`) và mũi tên uốn cong nhẹ (`bend left`, `looseness`) để tạo cảm giác mềm mại, hiện đại, không bị cứng nhắc.
* **Căn chỉnh (Alignment)**: Các khối phải được căn chỉnh thẳng hàng, khoảng cách đều đặn. Kích thước các khối (minimum width/height) nên được đồng bộ để tạo sự chuyên nghiệp.

## 3. Kiến trúc C4 Model cho Software Architecture
Áp dụng mô hình C4 để chia mức độ trừu tượng:
1. **System Context (Mức 1)**: Bức tranh toàn cảnh. Người dùng tương tác với hệ thống nào.
2. **Container (Mức 2)**: Các khối kỹ thuật lớn (Web App, Database, Microservices).
3. **Component (Mức 3)**: Chi tiết bên trong một Container (Controllers, Services, Repositories).
*(Lưu ý: Thường chỉ vẽ tới mức 2 hoặc 3, mức 4 (Code) là không cần thiết trừ khi giải thích thuật toán siêu phức tạp).*

## 4. Công cụ và "Diagrams as Code" (DaC)
Khuyến khích sử dụng cách tiếp cận Code để vẽ hình nhằm dễ dàng quản lý phiên bản (Version Control):
* **Mermaid.js**: Tuyệt vời cho flowcharts, sequence diagrams. Hỗ trợ hiển thị trực tiếp trên GitHub/Markdown.
* **LaTeX (TikZ)**: Đạt độ tùy biến cao nhất, chuẩn mực nhất cho các báo cáo khoa học, đồ án, bài báo (Paper). Dùng thư viện `positioning`, `fit`, `arrows.meta`.
* **PlantUML / Structurizr**: Chuyên dụng cho C4 model và UML.

## 5. Tham khảo các Kho lưu trữ (Repositories) và Tài liệu hữu ích
Để liên tục cập nhật phong cách và học hỏi:
* [C4 Model Official](https://c4model.com/) - Chuẩn mực vẽ sơ đồ kiến trúc.
* [Awesome Software Architecture](https://github.com/mehdihadeli/awesome-software-architecture) - Danh sách tổng hợp kiến thức kiến trúc phần mềm trên GitHub.
* [Mermaid Live Editor](https://mermaid.live/) - Phác thảo nhanh sơ đồ bằng code.
* [Diagrams (Python)](https://diagrams.mingrammer.com/) - Vẽ cấu trúc hạ tầng đám mây bằng mã Python.

## 6. Checklist trước khi hoàn thiện Sơ đồ
- [ ] Mũi tên có đi theo một hướng logic không?
- [ ] Màu sắc có bị chói, gắt hay quá nhiều không?
- [ ] Các khối đã được nhóm (Group/Fit) vào đúng ngữ cảnh chưa (VD: User, Server, Database)?
- [ ] Khi dùng thư viện `fit` để gom nhóm, thuộc tính `label=above:` có bị đè bởi mũi tên đi từ trên xuống không? **(Khắc phục: Tăng khoảng cách tọa độ y giữa các node, đặt label sang `above left`/`above right`, hoặc dùng `shift={(x,y)}` để tách bạch văn bản và đường kẻ).**
- [ ] Chữ có bị đè lên đường kẻ hay viền khối không? (Cần điều chỉnh `inner sep` hoặc tọa độ).
- [ ] Font chữ có đồng nhất với báo cáo/tài liệu không? (VD: `\sffamily` hoặc `Times New Roman`).
