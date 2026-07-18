class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        left = 0
        result = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            most_frequent_key = max(counts, key=counts.get)
            max_frequency = counts[most_frequent_key]
            length_window = right - left + 1
            while length_window - max_frequency > k:
                counts[s[left]] -= 1
                left += 1
                most_frequent_key = max(counts, key=counts.get)
                length_window = right - left + 1
                max_frequency = counts[most_frequent_key]
            result = max(result, length_window)
        return result