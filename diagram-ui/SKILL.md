---
name: diagram-ui
description: Skill guidelines for drawing scientific, neat, and highly readable software architecture and UI diagrams (Mermaid, TikZ, etc.) for the Safe Zone DNS anti-phishing system.
---

# Hướng dẫn vẽ Sơ đồ Kiến trúc và UI (Diagram UI Skill)

Kỹ năng này định hướng các tiêu chuẩn và phương pháp tốt nhất (best practices) để tạo ra các sơ đồ kiến trúc phần mềm, luồng phân tích rủi ro, và giao diện quản trị (Operator UI) khoa học, chỉn chu và dễ hiểu — đặc biệt áp dụng cho dự án **Safe Zone**.

## 1. Nguyên tắc cốt lõi (Core Principles)
* **Xác định mục đích rõ ràng**: Mỗi sơ đồ chỉ nên giải quyết một vấn đề (VD: Luồng phân giải DNS, pipeline phân tích rủi ro, hoặc kiến trúc triển khai Docker). Tránh nhồi nhét quá nhiều thông tin vào một hình.
* **Theo đuổi sự tối giản (Minimalism)**: Loại bỏ các chi tiết thừa. Nếu sơ đồ quá lớn, hãy chia nhỏ thành các sơ đồ con (sub-processes).
* **Luồng dữ liệu logic**: Luôn duy trì hướng đi nhất quán (từ trên xuống dưới, hoặc từ trái sang phải). Không sử dụng mũi tên hai chiều nếu không thực sự cần thiết, thay vào đó dùng hai mũi tên một chiều để làm rõ request/response.
* **Sử dụng ký hiệu chuẩn**: Tuân thủ các hình khối quen thuộc (VD: Hình chữ nhật bo tròn cho dịch vụ/trạng thái, hình thoi cho rẽ nhánh logic, hình trụ cho database/cache). Luôn có chú thích (Legend) nếu dùng ký hiệu lạ.

## 2. Tiêu chuẩn màu sắc & Thẩm mỹ
* **Màu sắc nhạt, thanh lịch (Pastel/Light Colors)**: Sử dụng các gam màu nhạt (VD: `cyan!3`, `blue!3`, `gray!2` trong TikZ hoặc Hex `#F0F4F8`, `#E1F5FE` trong Web) làm nền cho các Node để làm nổi bật chữ.
* **Giới hạn số lượng màu**: Không dùng quá 3-4 màu chính. Dùng màu sắc để phân loại (VD: Màu xanh lá cho SAFE, màu vàng cho SUSPICIOUS, màu đỏ cho MALICIOUS, màu xám cho hệ thống bên thứ 3/upstream).
* **Đường nét rõ ràng (Curved/Rounded)**: Sử dụng các góc bo tròn (`rounded corners`) và mũi tên uốn cong nhẹ (`bend left`, `looseness`) để tạo cảm giác mềm mại, hiện đại, không bị cứng nhắc.
* **Căn chỉnh (Alignment)**: Các khối phải được căn chỉnh thẳng hàng, khoảng cách đều đặn. Kích thước các khối (minimum width/height) nên được đồng bộ để tạo sự chuyên nghiệp.

## 3. Kiến trúc C4 Model cho Software Architecture
Áp dụng mô hình C4 để chia mức độ trừu tượng:
1. **System Context (Mức 1)**: Bức tranh toàn cảnh. Người dùng/thiết bị DNS tương tác với hệ thống Safe Zone, upstream DNS (Cloudflare), nguồn threat feed bên ngoài.
2. **Container (Mức 2)**: Các khối kỹ thuật lớn — `core-api`, `dns-resolver`, `feed-syncd`, Redis, SQLite, Caddy (Reverse Proxy), React SPA (nhúng).
3. **Component (Mức 3)**: Chi tiết bên trong một Container — VD: bên trong `core-api`: `analysis` (lexical scoring), `risk` (orchestrator), `ai` (Gemini/Ollama), `whois`, `tlsinspect`, `osint`, `agent` (workflow engine), `store` (SQLite), `cache` (Redis).
*(Lưu ý: Thường chỉ vẽ tới mức 2 hoặc 3, mức 4 (Code) là không cần thiết trừ khi giải thích thuật toán siêu phức tạp).*

## 4. Các sơ đồ đặc thù cho Safe Zone

### 4.1 Luồng phân giải DNS (DNS Resolution Flow)
Sơ đồ dạng **Flowchart** hoặc **Sequence Diagram**. Các bước chính:
1. Client gửi DNS query (DoH/DoT) → `dns-resolver`
2. Kiểm tra whitelist (Bloom filter) → nếu có: Forward upstream
3. Kiểm tra threat feed (Redis Set) → nếu trùng: MALICIOUS → Sinkhole/NXDOMAIN/REFUSED
4. Chấm điểm ngữ vựng (lexical scoring) → 8 tín hiệu heuristic → Score 0-100
5. Nếu SUSPICIOUS: Tùy chọn AI refinement (Gemini/Ollama) → Fail-open
6. Enrichment: TLS inspection + WHOIS lookup (cache SQLite) + OSINT
7. Phán định cuối: SAFE → Forward upstream | MALICIOUS → Chặn

**Lưu ý**: Dùng nét đứt (dashed) cho các đường đi tùy chọn (AI refinement, enrichment). Dùng hình thoi cho các điểm rẽ nhánh (score thresholds).

### 4.2 Kiến trúc triển khai (Deployment Architecture)
Sơ đồ dạng **Container Diagram** hoặc **Infrastructure Diagram**:
- Caddy (Reverse Proxy, TLS) ← Internet
- core-api :8080 (API + Embedded React SPA)
- dns-resolver :8081 (DoH) + :853 (DoT)
- Redis (Cache + Pub/Sub + Threat Feed Set)
- SQLite (WHOIS cache, Config, Whitelist, Overrides, Telemetry)
- feed-syncd (Daemon, Compose profile)
- Upstream DNS (Cloudflare DoH)

**Lưu ý**: Dùng đường viền nhóm (`fit` trong TikZ hoặc `subgraph` trong Mermaid) để tách biệt: Vùng Internet, Vùng Docker (internal network), Vùng lưu trữ (Volumes).

### 4.3 Pipeline phân tích rủi ro (Risk Analysis Pipeline)
Sơ đồ dạng **Flowchart** thể hiện chuỗi xử lý trong package `risk`:
- Input: Domain → Whitelist check → Threat feed lookup → Lexical analysis (8 signals) → Cache check → AI refinement (optional) → Enrichment (TLS + WHOIS + OSINT) → Output: Verdict + Score + Confidence + Category

**Lưu ý về màu sắc**: Dùng gradient từ xanh lá (SAFE, score <40) → vàng (SUSPICIOUS, 40-69) → đỏ (MALICIOUS, ≥70) để thể hiện trực quan thang điểm rủi ro.

### 4.4 Giao diện quản trị (Operator UI)
Khi vẽ mockup hoặc wireframe của giao diện React:
- 7 trang chính: Analysis, Telemetry, Endpoints, Overrides, Reports, System, Settings
- Sidebar navigation (AppShell)
- Biểu đồ Recharts cho Telemetry (trend, score distribution, category breakdown)
- Bảng dữ liệu cho Overrides và Reports

## 5. Công cụ và "Diagrams as Code" (DaC)
Khuyến khích sử dụng cách tiếp cận Code để vẽ hình nhằm dễ dàng quản lý phiên bản (Version Control):
* **Mermaid.js**: Tuyệt vời cho flowcharts, sequence diagrams. Hỗ trợ hiển thị trực tiếp trên GitHub/Markdown.
* **LaTeX (TikZ)**: Đạt độ tùy biến cao nhất, chuẩn mực nhất cho các báo cáo khoa học, đồ án, bài báo (Paper). Dùng thư viện `positioning`, `fit`, `arrows.meta`.
* **PlantUML / Structurizr**: Chuyên dụng cho C4 model và UML.

## 6. Tham khảo các Kho lưu trữ (Repositories) và Tài liệu hữu ích
Để liên tục cập nhật phong cách và học hỏi:
* [C4 Model Official](https://c4model.com/) - Chuẩn mực vẽ sơ đồ kiến trúc.
* [Awesome Software Architecture](https://github.com/mehdihadeli/awesome-software-architecture) - Danh sách tổng hợp kiến thức kiến trúc phần mềm trên GitHub.
* [Mermaid Live Editor](https://mermaid.live/) - Phác thảo nhanh sơ đồ bằng code.
* [Diagrams (Python)](https://diagrams.mingrammer.com/) - Vẽ cấu trúc hạ tầng đám mây bằng mã Python.

## 7. Checklist trước khi hoàn thiện Sơ đồ
- [ ] Mũi tên có đi theo một hướng logic không?
- [ ] Màu sắc có bị chói, gắt hay quá nhiều không? Đã dùng đúng bộ 3 màu verdict (xanh/vàng/đỏ) cho các sơ đồ liên quan đến phán định rủi ro chưa?
- [ ] Các khối đã được nhóm (Group/Fit) vào đúng ngữ cảnh chưa (VD: Internet zone, Docker internal network, Storage volumes)?
- [ ] Khi dùng thư viện `fit` để gom nhóm, thuộc tính `label=above:` có bị đè bởi mũi tên đi từ trên xuống không? **(Khắc phục: Tăng khoảng cách tọa độ y giữa các node, đặt label sang `above left`/`above right`, hoặc dùng `shift={(x,y)}` để tách bạch văn bản và đường kẻ).**
- [ ] Chữ có bị đè lên đường kẻ hay viền khối không? (Cần điều chỉnh `inner sep` hoặc tọa độ).
- [ ] Font chữ có đồng nhất với báo cáo/tài liệu không? (VD: `\sffamily` hoặc `Times New Roman`).
- [ ] Các tên dịch vụ (`core-api`, `dns-resolver`, `feed-syncd`) và tên package (`analysis`, `risk`, `ai`, `cache`, `store`) có được ghi nhất quán với codebase không?
