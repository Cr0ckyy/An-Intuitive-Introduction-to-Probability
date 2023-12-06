# For both problems, we need to calculate P(A ∩ B) using the General Multiplication Rule.
# The General Multiplication Rule states that P(A ∩ B) = P(A|B) * P(B) for problem 1
# and P(A ∩ B) = P(B|A) * P(A) for problem 2.

# Problem 1:
P_A_given_B_1 = 0.8  # P(A|B)
P_B_1 = 0.1  # P(B)

# Calculate P(A ∩ B) for problem 1
P_A_and_B_1 = P_A_given_B_1 * P_B_1

# Problem 2:
P_B_given_A_2 = 0.6  # P(B|A)
P_A_2 = 0.2  # P(A)

# Calculate P(A ∩ B) for problem 2
P_A_and_B_2 = P_B_given_A_2 * P_A_2

print(P_A_and_B_1, P_A_and_B_2)
