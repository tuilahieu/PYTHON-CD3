import numpy as np

scores = np.array([
    [8.0, 7.5, 8.5, 7.0],
    [6.5, 6.0, 7.0, 6.5],
    [9.0, 8.5, 9.0, 8.5],
    [5.0, 5.5, 6.0, 5.5],
    [7.5, 7.0, 8.0, 7.5],
    [4.5, 5.0, 5.5, 5.0],
    [8.5, 9.0, 8.0, 9.0],
    [6.0, 6.5, 6.0, 6.5],
    [7.0, 7.5, 7.0, 8.0],
    [9.5, 9.0, 9.5, 9.0]
])

print("Shape:", scores.shape)
print("Ndim:", scores.ndim)
print("Dtype:", scores.dtype)

weights = np.array([0.1, 0.2, 0.3, 0.4])
final_score = scores @ weights

print("\nĐiểm tổng kết:")
print(np.round(final_score, 2))

rank = np.empty(len(final_score), dtype="<U1")

rank[final_score >= 8.0] = "A"
rank[(final_score >= 7.0) & (final_score < 8.0)] = "B"
rank[(final_score >= 5.5) & (final_score < 7.0)] = "C"
rank[final_score < 5.5] = "D"

print("\nXếp loại:")
print(rank)

max_idx = np.argmax(final_score)
min_idx = np.argmin(final_score)

print("\nSinh viên điểm cao nhất: SV", max_idx + 1,
      "-", round(final_score[max_idx], 2))
print("Sinh viên điểm thấp nhất: SV", min_idx + 1,
      "-", round(final_score[min_idx], 2))

passed = np.where(final_score >= 7.0)[0] + 1

print("\nSinh viên có điểm tổng kết từ 7.0 trở lên:")
print("SV", passed)

low_component = np.any(scores < 5.0, axis=1)
low_students = np.where(low_component)[0] + 1

print("\nSinh viên có ít nhất một điểm dưới 5.0:")
print("SV", low_students)

rank_idx = np.argsort(final_score)[::-1]
top3 = rank_idx[:3] + 1

print("\nThứ tự điểm giảm dần:")
print(rank_idx + 1)

print("\nTop 3 sinh viên:")
print("SV", top3)

z_final_exam = (
    (scores[:, 3] - scores[:, 3].mean())
    / scores[:, 3].std()
)

print("\nZ-score điểm cuối kỳ:")
print(np.round(z_final_exam, 2))

if z_final_exam.std() > 0.8:
    print("\nChênh lệch học lực giữa các sinh viên khá nhiều.")
else:
    print("\nKhông có chênh lệch học lực.")
