import matplotlib.pyplot as plt

# 논문별 실험조건 데이터 (각 논문마다 Ca, M 값 튜플 리스트)
# 아래 예시는 임의 데이터
data = {
    1: [(1, 10), (2, 20), (3, 30)],          # 논문 1
    2: [(0.5, 5), (1.5, 15)],                 # 논문 2
    3: [(2.2, 25), (3.1, 35), (4.0, 45), (5.2, 55)]  # 논문 3
}

plt.figure(figsize=(8, 6))
colors = ['blue', 'green', 'red', 'orange', 'purple']  # 논문별 색상 지정

# 각 논문과 실험조건에 대해 scatter plot 및 텍스트 라벨 추가
for paper_idx, conditions in data.items():
    Ca_vals = [cond[0] for cond in conditions]
    M_vals  = [cond[1] for cond in conditions]
    color = colors[(paper_idx - 1) % len(colors)]
    plt.scatter(Ca_vals, M_vals, color=color, label=f'논문 {paper_idx}')
    for cond_idx, (Ca, M) in enumerate(conditions, start=1):
        plt.text(Ca, M, f'{paper_idx}-{cond_idx}', fontsize=9,
                 ha='right', va='bottom', color=color)

# x, y축을 로그 스케일로 설정
plt.xscale('log')
plt.yscale('log')

plt.xlabel('Ca')
plt.ylabel('M')
plt.title('논문별 실험 조건 (Log Scale)')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()
