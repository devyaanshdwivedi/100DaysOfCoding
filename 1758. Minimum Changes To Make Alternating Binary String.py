class Solution:
    def min_operations(self, s: str) -> int:
        role_number_one = 0
        role_number_two = 0
        n = len(s)

        if n % 2 == 1:
            if s[n - 1] == '1':
                role_number_two += 1
            else:
                role_number_one += 1

        for i in range(0, n - 1, 2):
            if s[i] != '1' and s[i + 1] != '0':
                role_number_one += 2
            if s[i] == '1' and s[i + 1] != '0':
                role_number_one += 1
            if s[i] != '1' and s[i + 1] == '0':
                role_number_one += 1

            if s[i] != '0' and s[i + 1] != '1':
                role_number_two += 2
            if s[i] != '0' and s[i + 1] == '1':
                role_number_two += 1
            if s[i] == '0' and s[i + 1] != '1':
                role_number_two += 1

        return min(role_number_one, role_number_two)