class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        size = len(nums)  # Number of binary strings in the input list

        # Sort the input list in lexicographical order
        nums.sort()

        pointer = 0  # Pointer to track the expected decimal value for the next binary string

        # Iterate through the sorted binary strings
        for i in range(size):
            # Convert the current binary string to decimal
            decimal_value = int(nums[i], 2)

            # Check if the decimal value matches the expected value
            if decimal_value == pointer:
                pointer += 1
            else:
                # If not, return the binary representation of the expected value with appropriate length
                return format(pointer, f'0{size}b')

        # If no unique binary string is found, return the binary representation of the next expected value
        return format(pointer, f'0{size}b')