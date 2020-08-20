# 각 학생의 이름과 성적 정보가 주어질 때 성적이 낮은 순서대로 학생 이름을 출력


# def setting(data):  # key 사용을 위한 함수
#     return data[1]
#
#
# N = int(input())
# array = []
# for i in range(N):
#     array.append(tuple(input().split(' ')))
# result = sorted(array, key=setting)  # 정렬된 리스트
#
# for i in range(N):
#     print(result[i][0], end=' ')

array = []
N = int(input())
for i in range(N):
    data = input().split()
    array.append((data[0], int(data[1])))  # 문자형 맞춰서 저장

array = sorted(array, key=lambda i: i[1])

for student in array:
    print(student[0], end=' ')
