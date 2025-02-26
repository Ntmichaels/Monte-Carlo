import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo Simulation for Investment Growth
def monte_carlo_investment(initial_investment=10000, years=30, mean_return=0.07, std_dev=0.15, simulations=1000):
    """
    Simulates the future value of an investment using Monte Carlo analysis.
    
    Parameters:
    - initial_investment: Starting amount of investment
    - years: Number of years to simulate
    - mean_return: Expected annual return (7% for the S&P 500)
    - std_dev: Expected annual volatility (standard deviation)
    - simulations: Number of simulations to run
    
    Returns:
    - A list of final portfolio values from all simulations
    """
    
    final_values = []
    
    for _ in range(simulations):
        portfolio_value = initial_investment
        for _ in range(years):
            annual_return = np.random.normal(mean_return, std_dev)  # Random return based on normal distribution
            portfolio_value *= (1 + annual_return)  # Apply return to portfolio
        final_values.append(portfolio_value)
    
    return final_values

# Run the simulation
simulated_results = monte_carlo_investment()

# Plot results
plt.figure(figsize=(10, 5))
plt.hist(simulated_results, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(np.median(simulated_results), color='red', linestyle='dashed', linewidth=2, label="Median Value")
plt.xlabel("Final Portfolio Value")
plt.ylabel("Frequency")
plt.title("Monte Carlo Simulation of Investment Growth")
plt.legend()
plt.show()

# Print summary statistics
median_value = np.median(simulated_results)
percentile_10 = np.percentile(simulated_results, 10)
percentile_90 = np.percentile(simulated_results, 90)

print(f"Median Final Portfolio Value: ${median_value:,.2f}")
print(f"10th Percentile (worst case): ${percentile_10:,.2f}")
print(f"90th Percentile (best case): ${percentile_90:,.2f}")