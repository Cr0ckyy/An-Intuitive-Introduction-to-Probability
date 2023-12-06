# Given values from the table
A1B1 = 20
A2B1 = 10
A1B2 = 30
A2B2 = 40

# Calculating the total number of events
total_events = A1B1 + A2B1 + A1B2 + A2B2

# Calculating probabilities for each statement
prob_A1 = (A1B1 + A1B2) / total_events
prob_A1B2 = A1B2 / total_events
prob_A2B2 = A2B2 / total_events
prob_B1 = (A1B1 + A2B1) / total_events

probabilities = {
    "The probability of Event A1 to happen is": prob_A1,
    "The probability of Event A1 and B2 to happen is": prob_A1B2,
    "The probability of Event A2 and B2 to happen is": prob_A2B2,
    "The probability of Event B1 to happen is": prob_B1
}

# Print probabilities neatly on separate lines
for key, value in probabilities.items():
    print(f"{key}: {value:.2f}")
