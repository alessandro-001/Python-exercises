weight = 1.5

# ground shipping
cost_ground = 0

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

print("Standard ground shipping cost: £", cost_ground)

# premium ground shipping
cost_premium_ground = 125.00

print("Premium ground shipping: £", cost_premium_ground)

# drone shipping
drone_cost = 0
if weight <= 2:
  drone_cost = weight * 4.5
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.75

print("Drone shipping cost: £", drone_cost)
