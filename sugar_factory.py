
print("=" * 50)
print("   SUGAR FACTORY CLIMATE IMPACT ANALYSIS")
print("=" * 50)

# Input environmental data
temperature = float(input("\nEnter Temperature (°C): "))
rainfall = float(input("Enter Seasonal Rainfall (mm): "))

# Temperature suitability analysis
if 25 <= temperature <= 32:
    temp_score = 100
elif temperature < 25:
    temp_score = max(0, 100 - (25 - temperature) * 5)
else:
    temp_score = max(0, 100 - (temperature - 32) * 8)

# Rainfall suitability analysis
if 1000 <= rainfall <= 1500:
    rain_score = 100
elif rainfall < 1000:
    rain_score = max(0, 100 - (1000 - rainfall) * 0.12)
else:
    rain_score = max(0, 100 - (rainfall - 1500) * 0.12)

# Overall climate score
climate_score = (temp_score + rain_score) / 2

# Factory efficiency estimate
factory_efficiency = max(
    0, min(100, 100 - max(0, temperature - 32) * 2)
)

# Sugarcane yield suitability
yield_score = climate_score

# Sustainability score
sustainability = (yield_score + factory_efficiency) / 2

# Climate condition
if climate_score >= 80:
    condition = "FAVOURABLE CLIMATE"
elif climate_score >= 50:
    condition = "MODERATE CLIMATE IMPACT"
else:
    condition = "HIGH CLIMATE IMPACT"

# Display results
print("\n" + "=" * 50)
print("             ANALYSIS RESULTS")
print("=" * 50)

print(f"\nTemperature Suitability : {temp_score:.1f}%")
print(f"Rainfall Suitability    : {rain_score:.1f}%")
print(f"Sugarcane Yield Score   : {yield_score:.1f}%")
print(f"Factory Efficiency      : {factory_efficiency:.1f}%")
print(f"Sustainability Score    : {sustainability:.1f}%")

print("\nOverall Climate Condition:")
print(condition)

print("\n" + "=" * 50)
print("           ANALYSIS COMPLETED")
print("=" * 50)
