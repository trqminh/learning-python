import copy


class IncrementalArray:

    @staticmethod
    def create_min_array(s):
        min_arr = [0 for i in range(len(s))]
        min_arr[0] = -1
        for j in range(2, len(s)):
            if s[min_arr[j - 1]] > s[j - 1]:
                min_arr[j] = j - 1
            else:
                min_arr[j] = min_arr[j - 1]

        return min_arr

    def __init__(self, s):
        self.__s = copy.deepcopy(s)
        self.__len = len(s)
        self.__min_arr = IncrementalArray.create_min_array(self.__s)

    def __repr__(self):
        return str(self.__s)

    @classmethod
    def create_incre_array_from(cls, arr):
        n = len(arr)
        s = [0 for k in range(n + 1)]
        s[0] = 0
        for i in range(1, n + 1):
            s[i] = s[i - 1] + arr[i - 1]

        return cls(s)

    def interval_sum_zero(self):
        for i in range(self.__len):
            for j in range(i + 1, self.__len):
                if self.__s[i] == self.__s[j]:
                    return (i + 1, j)

        return (-1, -1)

    def interval_sum_max(self):
        ans = self.__s[1] - self.__s[self.__min_arr[1]]
        j_index = 1
        i_index = 0
        for j in range(2, self.__len):
            if ans < self.__s[j] - self.__s[self.__min_arr[j]]:
                ans = self.__s[j] - self.__s[self.__min_arr[j]]
                j_index = j
                i_index = self.__min_arr[j]

        return (i_index + 1, j_index, ans)

    def longest_interval_sum_positive(self):
        j = self.__len - 1
        result_len = 0
        i_index = 0
        j_index = 0
        found = False

        while j > 0:
            i = self.__min_arr[j]
            backup = i
            while i >= 0 and self.__s[j] - self.__s[i] > 0:
                backup = i
                i = self.__min_arr[i]

            if self.__s[j] - self.__s[backup] > 0 and result_len < j - backup:
                found = True
                result_len = j - backup
                i_index = backup
                j_index = j

            j -= 1

        if found:
            return (i_index + 1, j_index)

        return None
