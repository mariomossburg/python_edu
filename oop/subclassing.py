
class ExtendSet(set):
    """
    Extended Set with additional set-theory operations not in built-in set.
    """
    def is_proper_subset(self, other):
        """Return True if self is a proper subset of other."""
        return self < other

    def is_proper_superset(self, other):
        """Return True if self is a proper superset of other."""
        return self > other

    def complement(self, universe):
        """Return the complement of self in the given universe set."""
        return ExtendSet(universe) - self

    def cartesian_product(self, other):
        """Return the Cartesian product of self and another set as a set of tuples."""
        return ExtendSet((a, b) for a in self for b in other)

    def power_set(self):
        """Return the power set (set of all subsets) as a set of frozensets."""
        ps = [frozenset()]
        for elem in self:
            ps += [subset | {elem} for subset in ps]
        return ExtendSet(ps)

    def size_diff(self, other):
        """Return size difference: len(self) - len(other)."""
        return len(self) - len(other)

    def compare_size(self, other):
        """Return a human-readable comparison of sizes."""
        diff = self.size_diff(other)
        if diff > 0:
            return f"self is larger by {diff}"  
        if diff < 0:
            return f"self is smaller by {-diff}"
        return "self and other are equal"



a = ExtendSet(i for i in range(20))
b = ExtendSet(i for i in range(10, 30))
print('a', a)
print('b', b)    
print(a.compare_size(b))



