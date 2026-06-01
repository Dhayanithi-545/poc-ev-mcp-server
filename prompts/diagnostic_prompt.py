def diagnostic_summary_prompt(vehicle_id: str) -> str:
    return f"""
Generate a professional diagnostic report
for vehicle {vehicle_id}.

Include:
1. Battery Health
2. Motor Temperature
3. Range Performance
4. Risk Level
5. Maintenance Recommendation
"""