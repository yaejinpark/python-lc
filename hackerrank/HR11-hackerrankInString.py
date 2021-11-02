import re

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        print('YES' if re.search(r'.*h.*a.*c.*k.*e.*r.*r.*a.*n.*k.*',input().strip()) else 'NO')