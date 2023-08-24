#!/usr/bin/env python
# coding: utf-8

# In[1]:


class IntegerToRoman:
    def __init__(self):
        self.values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        self.roman_numerals = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
    def int_to_roman(self, num):
        roman_numeral = ""
        i = 0
        while num > 0:
            for _ in range(num // self.values[i]):
                roman_numeral += self.roman_numerals[i]
                num -= self.values[i]
            i += 1
        return roman_numeral







# In[2]:


obj=IntegerToRoman()


# In[3]:


n=1789
roman=obj.int_to_roman(n)


# In[4]:


print(roman)


# In[5]:


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


# In[6]:


subset=SubsetGenerator()


# In[7]:


ans=subset.generate_subsets([1,2,3])


# In[8]:


for i in ans:
    print(i)


# In[1]:


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
    def display_attributes(self):
        attributes = vars(self)
        for attr, value in attributes.items():
            print(f"{attr}: {value}")
# Create an instance of the Student class
student1 = Student(1, "Ram Seeta")
# Display attributes and values
print("Attributes and values before removal:")
student1.display_attributes()
# Remove the student_name attribute
del student1.student_name
# Display attributes and values after removal
print("\nAttributes and values after removal:")
student1.display_attributes()


# In[ ]:
