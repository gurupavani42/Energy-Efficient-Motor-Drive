## Energy-Efficient Motor Drive

This program calculates the **motor power consumption** and checks whether the motor is operating efficiently.

```
# Energy-Efficient Motor Drive

input_power = float(input("Enter Input Power (kW): "))
output_power = float(input("Enter Output Power (kW): "))

efficiency = (output_power / input_power) * 100

print("\n--- Motor Drive ---")
print("Input Power =", input_power, "kW")
print("Output Power =", output_power, "kW")
print("Motor Efficiency =", efficiency, "%")

if efficiency >= 90:
    print("Motor Status: HIGH EFFICIENCY")
elif efficiency >= 75:
    print("Motor Status: NORMAL EFFICIENCY")
else:
    print("Motor Status: LOW EFFICIENCY")
    print("Energy Saving Required")
```

### Example Output

```
Enter Input Power (kW): 10
Enter Output Power (kW): 9

--- Motor Drive ---
Input Power = 10.0 kW
Output Power = 9.0 kW
Motor Efficiency = 90.0 %
Motor Status: HIGH EFFICIENCY
```

### Energy Saving Calculation

```
input_power = float(input("Enter Motor Input Power (kW): "))
efficiency = float(input("Enter Motor Efficiency (%): "))

output_power = input_power * efficiency / 100
power_loss = input_power - output_power

print("Useful Output Power =", output_power, "kW")
print("Power Loss =", power_loss, "kW")

if power_loss <= input_power * 0.1:
    print("Motor is Energy Efficient")
else:
    print("Motor Needs Improvement")
```

**Project name:** Energy-Efficient Motor Drive

**Main concepts:**

- Motor input power
- Motor output power
- Efficiency
- Power loss
- Energy saving
- Motor performance monitoring
