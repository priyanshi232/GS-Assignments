class SubsetGenerator:
    def __init__(self):
        self.subsets = []
    def generate_subsets(self, nums):
        self._generate([], nums)
        return self.subsets
    def _generate(self, current_subset, remaining_nums):
        self.subsets.append(current_subset[:])
        for i in range(len(remaining_nums)):
            new_subset = current_subset + [remaining_nums[i]]
            new_remaining = remaining_nums[i+1:]
            self._generate(new_subset, new_remaining)
