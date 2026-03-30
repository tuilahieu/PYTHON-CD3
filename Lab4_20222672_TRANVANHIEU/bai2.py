import numpy as np

attendance = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,0,1,1,0,1,1],
    [1,0,0,1,1,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,1,1,0,1,1,1,0],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,1,0],
    [1,1,1,1,1,1,1,0],
    [0,0,1,1,0,1,1,1],
    [1,1,1,0,1,1,1,1],
    [1,1,0,0,1,0,1,1],
    [1,1,1,1,1,0,1,1]
])

present_count = attendance.sum(axis=1)

print("Số buổi đi học của từng sinh viên:")
for i, count in enumerate(present_count, start=1):
    print(f"SV{i}: {count} buổi")

rate = present_count / attendance.shape[1] * 100

print("\nTỉ lệ chuyên cần:")
for i, r in enumerate(rate, start=1):
    print(f"SV{i}: {r:.1f}%")

warning_idx = np.where(rate < 75)[0] + 1

print("\nSinh viên bị cảnh báo học vụ (< 75%):")
print("SV", warning_idx)

absent_count_by_session = (attendance == 0).sum(axis=0)
worst_session = np.argmax(absent_count_by_session) + 1

print("\nSố sinh viên vắng theo từng buổi:")
print(absent_count_by_session)
print(f"Buổi vắng nhiều nhất: Buổi {worst_session}")

full_attendance = np.where(np.all(attendance == 1, axis=1))[0] + 1

print("\nSinh viên đi học đầy đủ cả 8 buổi:")
print("SV", full_attendance)

two_absent_in_row = np.where(
    np.any(
        (attendance[:, :-1] == 0) & (attendance[:, 1:] == 0),
        axis=1
    )
)[0] + 1

print("\nSinh viên có ít nhất 2 buổi vắng liên tiếp:")
print("SV", two_absent_in_row)

avg_rate = rate.mean()

print("\nNhận xét:")
print(f"Tỉ lệ chuyên cần trung bình của lớp: {avg_rate:.1f}%")

if avg_rate >= 80:
    print("Ý thức học tập của lớp khá tốt, đa số sinh viên đi học đầy đủ.")
elif avg_rate >= 70:
    print("Ý thức học tập ở mức trung bình, vẫn còn một số sinh viên nghỉ học khá nhiều.")
else:
    print("Ý thức học tập của lớp chưa tốt, cần tăng cường nhắc nhở và quản lý chuyên cần.")

if len(warning_idx) > 0:
    print("Một số sinh viên cần được cảnh báo vì tỉ lệ chuyên cần thấp.")

if len(two_absent_in_row) > 0:
    print("Có sinh viên nghỉ liên tiếp nhiều buổi, cần theo dõi thêm.")