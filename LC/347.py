class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        time complexity: O(n)
        space complexity: O(n)
        """
        num_count = {} #{number: number_count}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        bucket_arr = [[] for num in range(len(nums)+1)]

        for number, number_count in num_count.items():
            bucket_arr[number_count].append(number)

        results = []
        for i in range(len(bucket_arr)-1, 0, -1):
            bucket = bucket_arr[i]
            for number in bucket:
                results.append(number)
                if len(results) == k:
                    return results

        return results


    def topKFrequentprev(self, nums: List[int], k: int) -> List[int]:
        """
        worst case:
        time complexity: O(nlogn)
        space complexity: O(n)
        """
        d = {}
        for n in nums:
            if n in d:
                d[n]+=1
            else:
                d[n]=1

        count_arr = [(num, count) for num, count in d.items()]

        count_arr = sorted(count_arr, key=lambda x: x[1], reverse=True)

        ks = []
        for i, (num, count) in enumerate(count_arr):
            if i<k:
                ks.append(num)
            else:
                break

        return ks
                