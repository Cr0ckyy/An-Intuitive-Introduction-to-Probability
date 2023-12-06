# Recalculating for clarity

# Question 1 Calculations
# Given values
P_B_given_A_q1 = 0.8
P_A_q1 = 0.3
P_B_q1 = 0.9

# Calculate P(A ∩ B) using the given P(B|A) and P(A)
P_A_and_B_q1 = P_B_given_A_q1 * P_A_q1

# Calculate P(A|B) using the calculated P(A ∩ B) and the given P(B)
P_A_given_B_q1 = P_A_and_B_q1 / P_B_q1

# Question 2 Calculations
# Given values
P_A_and_B_q2 = 0.3
P_B_q2 = 0.4

# Calculate P(A|B) using the given P(A ∩ B) and P(B)
P_A_given_B_q2 = P_A_and_B_q2 / P_B_q2

# Print the results for Question 1 and Question 2
print("Question 1:")
print(f"P(A∩B) for Question 1 is: {P_A_given_B_q1:.2f}")

print("\nQuestion 2:")
print(f"P(A|B) for Question 2 is: {P_A_given_B_q2:.2f}")
