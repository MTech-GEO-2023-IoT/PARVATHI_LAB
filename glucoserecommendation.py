# Assume glucose_level is the variable that holds the glucose level obtained from the API
#glucose_level = get_glucose_level_from_api()  # Function to fetch the glucose level from the API
glucose_level = int(input("enter your glucose value here    "))
# Assume diabetes_type is the variable that holds the type of diabetes (e.g., "Type 1", "Type 2", etc.)
#diabetes_type = get_diabetes_type()  # Function to fetch the diabetes type from user input or other sources
diabetes_type = int(input("enter your diabetes type here    "))
# Recommend immediate measures based on glucose level and diabetes type
if glucose_level < 70:
    print("Low glucose level. Take the following immediate measures:")
    print("- Consume 15-20 grams of fast-acting carbohydrates (e.g., glucose tablets, fruit juice, or candy).")
    print("- Recheck glucose level after 15 minutes.")
    print("- If glucose level does not rise, seek medical attention.")

elif 70 <= glucose_level <= 180:
    print("Normal glucose level. Maintain healthy habits to manage glucose levels effectively.")
    print("- Eat a balanced diet.")
    print("- Engage in regular physical activity.")
    print("- Take prescribed medications as directed.")
    print("- Regularly monitor glucose levels.")

    if diabetes_type == 1:
        print("- Adjust insulin dosage as per healthcare provider's recommendations.")
        print("- Carry glucose tablets or fast-acting carbohydrates in case of hypoglycemia.")

    elif diabetes_type == 2:
        print("- Follow the prescribed medication regimen.")
        print("- Monitor blood sugar levels regularly.")
        print("- Manage weight through healthy eating and physical activity.")

elif 180 < glucose_level <= 240:
    print("Elevated glucose level. Take the following immediate measures:")
    print("- Drink plenty of water.")
    print("- Engage in light physical activity (e.g., walking) to help lower glucose levels.")
    print("- Monitor glucose levels closely.")

    if diabetes_type == 1:
        print("- Check for ketones if glucose level remains consistently high.")
        print("- Adjust insulin dosage as per healthcare provider's recommendations.")

    elif diabetes_type == 2:
        print("- Follow the prescribed medication regimen.")
        print("- Adjust diet to include low glycemic index foods.")

elif glucose_level > 240:
    print("High glucose level. Take the following immediate measures:")
    print("- Check for ketones if you have type 1 diabetes or symptoms of diabetic ketoacidosis (DKA).")
    print("- Follow your healthcare provider's instructions for managing high glucose levels.")
    print("- Seek medical attention if glucose levels remain consistently high.")

    if diabetes_type == 1:
        print("- Adjust insulin dosage as per healthcare provider's recommendations.")
        print("- Follow sick day rules if necessary.")

    elif diabetes_type == 2:
        print("- Consult with your healthcare provider for medication adjustments.")
        print("- Monitor glucose levels closely.")

else:
    print("Invalid glucose level. Please check the API response and try again.")
