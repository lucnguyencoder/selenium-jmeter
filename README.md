BÁO CÁO KIỂM THỬ HIỆU NĂNG (LOAD TESTING) VỚI JMETER



Người Kiểm Thử: Nguyễn Tiến Lực MSV: 23010862

1. Mục Tiêu Kiểm Thử
Sử dụng Apache JMeter để giả lập hàng loạt người dùng ảo (Virtual Users) cùng truy cập vào hệ thống API tại cùng một thời điểm. Mục tiêu là đánh giá hiệu suất, thời gian phản hồi (Response Time) và giới hạn chịu tải của máy chủ.

2. Môi Trường Kiểm Thử
Công cụ: Apache JMeter (Desktop App)
Nền tảng mục tiêu: https://reqres.in
Loại kiểm thử: Load Testing (Kiểm thử chịu tải)
3. Cấu Hình Kịch Bản (Test Plan)
Test Plan được thiết lập bao gồm các thành phần:

Thread Group: Định nghĩa số lượng người dùng ảo và thời gian chạy.
HTTP Request Defaults: Cấu hình Server Name mặc định là reqres.in, giao thức https.
HTTP Request: Gọi API GET /api/users?page=2.
Listeners: Sử dụng View Results Tree (xem chi tiết từng request) và Summary Report (xem thống kê tổng quan).
4. Các Kịch Bản Chịu Tải (Thread Groups)
Kịch Bản 1: Tải nhẹ (10 Người dùng ảo)
Cấu hình Thread Group:
Number of Threads (users): 10
Ramp-up period (seconds): 5 (Thời gian để JMeter tạo đủ 10 users là 5 giây)
Loop Count: 1
Mục Đích: Kiểm tra hệ thống ở mức độ truy cập bình thường.
Kết Quả Mong Đợi: 100% Request thành công (Status 200), thời gian phản hồi trung bình < 500ms.
Kết Quả Thực Tế: Hệ thống phản hồi nhanh, không có request nào bị lỗi (Error = 0%). Thời gian phản hồi trung bình (Average) đạt yêu cầu.
Ảnh minh họa (View Results Tree): <img width="1074" height="607" alt="anh111" src="https://github.com/user-attachments/assets/d6eb15d4-602f-4090-835f-ed7ab4150b02" />


Kịch Bản 2: Tải trung bình (100 Người dùng ảo)
Cấu hình Thread Group:
Number of Threads (users): 100
Ramp-up period (seconds): 10 (Trung bình mỗi giây thêm 10 users)
Loop Count: 2 (Mỗi user chạy lại kịch bản 2 lần, tổng cộng 200 requests)
Mục Đích: Đánh giá khả năng xử lý đồng thời khi lượng truy cập tăng đột biến.
Kết Quả Mong Đợi: Hệ thống vẫn giữ được độ ổn định, tỉ lệ lỗi (Error Rate) dưới 1%, thời gian phản hồi tối đa (Max) không vượt quá 2000ms.
Kết Quả Thực Tế: Cả 200 requests đều hoàn thành. Thông lượng (Throughput) đạt mức cao.
Ảnh minh họa (Summary Report): <img width="1070" height="602" alt="anh2222" src="https://github.com/user-attachments/assets/26036efc-071e-44dd-8d35-6bd55856f9c2" />


5. Đánh Giá & Kết Luận
Khả năng đáp ứng: Hệ thống Reqres.in có khả năng chịu tải rất tốt đối với các kịch bản kiểm thử với 100 người dùng truy cập đồng thời.
Phát hiện lỗi (Bottleneck): Không phát hiện lỗi quá tải (HTTP Error 503) hay lỗi hết thời gian chờ (Timeout) trong phạm vi bài test này. Mức độ sử dụng tài nguyên của API Server ổn định.
