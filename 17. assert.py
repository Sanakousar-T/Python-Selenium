"""
assert:
-------
*assert is a keyword it is used for conditional checking.
*we will specify the condition in assert, id condition is True then it will continue
the execution, if condition become False then it will stop the execution and throw
"AssertionError".
syntax: assert condition, ["message"]
"""

# example on assert condtion True
"""
assert 10==10, "number not matches"
print("same")
print("end")
# same
# end
"""
# example on assert condtion False
"""
assert 10==100, "number not matches"
print("same")
print("end")
#AssertionError: number not matches
"""