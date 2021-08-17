days=365
weeks=52
months=12
life_span=65

age_now=int(input("Enter your age :"))
left_years=life_span-age_now
left_months=left_years*months
left_weeks=left_months*weeks
left_days=left_months*days

print(f"months to live : {left_months}, weeks to live : {left_weeks}, days to live : {left_days}")


