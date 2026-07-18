class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        # Required frequency of each character in t
        required = defaultdict(int)
        for char in t:
            required[char] += 1

        # Frequency of characters in the current window
        window = defaultdict(int)

        # Number of unique required characters
        required_count = len(required)

        # Number of unique characters whose required frequency is satisfied
        satisfied_count = 0

        left = 0

        best_start = 0
        best_length = float("inf")

        # Expand the window by moving right
        for right in range(len(s)):
            right_char = s[right]
            window[right_char] += 1

            # This character has just reached its required frequency
            if (
                right_char in required
                and window[right_char] == required[right_char]
            ):
                satisfied_count += 1

            # Shrink the window while it still contains everything in t
            while satisfied_count == required_count:
                current_length = right - left + 1

                # Save this window if it is the shortest one found
                if current_length < best_length:
                    best_start = left
                    best_length = current_length

                # Remove the leftmost character
                left_char = s[left]
                window[left_char] -= 1
                left += 1

                # The window is no longer valid if this character's
                # frequency drops below the required frequency
                if (
                    left_char in required
                    and window[left_char] < required[left_char]
                ):
                    satisfied_count -= 1

        # No valid window was found
        if best_length == float("inf"):
            return ""

        return s[best_start:best_start + best_length]