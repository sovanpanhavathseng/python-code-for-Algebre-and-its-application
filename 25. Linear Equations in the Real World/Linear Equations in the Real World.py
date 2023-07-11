def mileage_rate(distance, hours):
  """Calculates the mileage rate given the distance and hours."""
  mileage_rate = distance / hours
  return mileage_rate

def income_estimate(current_income, annual_increase, years):
  """Estimates the income in the future given the current income, annual increase, and years."""
  estimated_income = current_income + annual_increase * years
  return estimated_income

def compare_rates(job_1, job_2):
  """Compares the rates of pay for two jobs."""
  if job_1["salary"] > job_2["salary"]:
    print("Job 1 pays a higher rate.")
  elif job_1["salary"] < job_2["salary"]:
    print("Job 2 pays a higher rate.")
  else:
    print("The two jobs pay the same rate.")

def profit_prediction(cost, price):
  """Predicts the profit given the cost and price."""
  profit = price - cost
  return profit

if __name__ == "__main__":
  print("Mileage rate:", mileage_rate(100, 2))
  print("Income estimate:", income_estimate(50000, 5000, 5))
  compare_rates({"salary": 40000}, {"salary": 20 * 60})
  print("Profit prediction:", profit_prediction(10, 20))

// This code shows how linear equations can be used to solve real-world problems. For example, the mileage_rate() function calculates the mileage rate given the distance and hours. The income_estimate() function estimates the income in the future given the current income, annual increase, and years. The compare_rates() function compares the rates of pay for two jobs. And the profit_prediction() function predicts the profit given the cost and price.

// This is just a simple example of how linear equations can be used in Python. There are many other ways to use linear equations in Python, and the possibilities are endless.
