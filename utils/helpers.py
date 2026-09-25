"""
Clinical logic helpers: BMI calculations, Blood Pressure classifications, and input validation.
"""

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """Calculate Body Mass Index (BMI)."""
    if height_cm <= 0:
        return 0.0
    height_m = height_cm / 100.0
    return round(weight_kg / (height_m ** 2), 2)

def get_bmi_category(bmi: float) -> tuple[str, str, str]:
    """
    Returns (category_name, color_hex, badge_class)
    """
    if bmi < 18.5:
        return ("Underweight", "#38BDF8", "info")
    elif 18.5 <= bmi <= 24.9:
        return ("Normal", "#10B981", "success")
    elif 25.0 <= bmi <= 29.9:
        return ("Overweight", "#F59E0B", "warning")
    else:
        return ("Obesity", "#E11D48", "danger")

def classify_blood_pressure(ap_hi: int, ap_lo: int) -> tuple[str, str]:
    """
    Returns (stage_description, color_hex) based on AHA guidelines.
    """
    if ap_hi < 120 and ap_lo < 80:
        return ("Normal (<120/80 mmHg)", "#10B981")
    elif 120 <= ap_hi <= 129 and ap_lo < 80:
        return ("Elevated (120-129 / <80 mmHg)", "#10B981")
    elif (130 <= ap_hi <= 139) or (80 <= ap_lo <= 89):
        return ("Stage 1 Hypertension (130-139 / 80-89 mmHg)", "#F59E0B")
    elif ap_hi >= 180 or ap_lo >= 120:
        return ("Hypertensive Crisis (≥180 and/or ≥120 mmHg)", "#E11D48")
    elif (ap_hi >= 140) or (ap_lo >= 90):
        return ("Stage 2 Hypertension (≥140 or ≥90 mmHg)", "#E11D48")
    else:
        return ("Varies", "#94A3B8")

def validate_patient_inputs(*args, **kwargs) -> list[str]:
    """
    Validates patient biometric and vital inputs.
    Accepts:
    - validate_patient_inputs(patient_dict)
    - validate_patient_inputs(age, height, weight, ap_hi, ap_lo)
    - validate_patient_inputs(age=..., height=..., weight=..., ap_hi=..., ap_lo=...)
    Returns list of error messages (empty if valid).
    """
    if len(args) == 1 and isinstance(args[0], dict):
        data = args[0]
        age = data.get("age_years", data.get("age", 50))
        height = data.get("height", 165)
        weight = data.get("weight", 70)
        ap_hi = data.get("ap_hi", 120)
        ap_lo = data.get("ap_lo", 80)
    elif len(args) >= 5:
        age, height, weight, ap_hi, ap_lo = args[:5]
    else:
        age = kwargs.get("age_years", kwargs.get("age", 50))
        height = kwargs.get("height", 165)
        weight = kwargs.get("weight", 70)
        ap_hi = kwargs.get("ap_hi", 120)
        ap_lo = kwargs.get("ap_lo", 80)

    errors = []
    if age < 18 or age > 110:
        errors.append("Age must be between 18 and 110 years.")
    if height < 100 or height > 240:
        errors.append("Height must be realistic (100 cm to 240 cm).")
    if weight < 30 or weight > 250:
        errors.append("Weight must be realistic (30 kg to 250 kg).")
    if ap_hi < 60 or ap_hi > 260:
        errors.append("Systolic Blood Pressure must be between 60 and 260 mmHg.")
    if ap_lo < 40 or ap_lo > 180:
        errors.append("Diastolic Blood Pressure must be between 40 and 180 mmHg.")
    if ap_lo >= ap_hi:
        errors.append("Diastolic pressure cannot be greater than or equal to systolic pressure.")
    return errors

def analyze_key_factors(patient_data: dict, bmi: float = None) -> list[dict]:
    """
    Evaluates individual patient factors against healthy baselines for explainability.
    """
    factors = []
    
    # Blood pressure
    ap_hi = patient_data["ap_hi"]
    ap_lo = patient_data["ap_lo"]
    if ap_hi >= 140 or ap_lo >= 90:
        factors.append({
            "name": "Blood Pressure",
            "value": f"{ap_hi}/{ap_lo} mmHg",
            "status": "High (Stage 2)",
            "impact": "High Risk Driver",
            "color": "#E11D48",
            "icon": "❤️"
        })
    elif ap_hi >= 130 or ap_lo >= 80:
        factors.append({
            "name": "Blood Pressure",
            "value": f"{ap_hi}/{ap_lo} mmHg",
            "status": "Stage 1 Elevated",
            "impact": "Moderate Impact",
            "color": "#F59E0B",
            "icon": "❤️"
        })
    else:
        factors.append({
            "name": "Blood Pressure",
            "value": f"{ap_hi}/{ap_lo} mmHg",
            "status": "Normal Range",
            "impact": "Protective",
            "color": "#10B981",
            "icon": "❤️"
        })

    # BMI
    if bmi is None:
        bmi = calculate_bmi(patient_data["weight"], patient_data["height"])
    bmi_cat, bmi_color, _ = get_bmi_category(bmi)
    factors.append({
        "name": "Body Mass Index (BMI)",
        "value": f"{bmi:.1f} kg/m²",
        "status": bmi_cat,
        "impact": "Risk Factor" if bmi >= 25 else "Healthy",
        "color": bmi_color,
        "icon": "⚖️"
    })

    # Cholesterol
    chol = patient_data["cholesterol"]
    chol_map = {1: ("Normal (< 200 mg/dL)", "#10B981"), 2: ("Above Normal (200-239)", "#F59E0B"), 3: ("High (≥ 240 mg/dL)", "#E11D48")}
    chol_label, chol_col = chol_map.get(chol, ("Unknown", "#94A3B8"))
    factors.append({
        "name": "Serum Cholesterol",
        "value": chol_label,
        "status": chol_label,
        "impact": "Elevated Risk" if chol > 1 else "Optimal",
        "color": chol_col,
        "icon": "🧪"
    })

    # Glucose
    gluc = patient_data["gluc"]
    gluc_map = {1: ("Normal (< 100 mg/dL)", "#10B981"), 2: ("Above Normal (100-125)", "#F59E0B"), 3: ("High (≥ 126 mg/dL)", "#E11D48")}
    gluc_label, gluc_col = gluc_map.get(gluc, ("Unknown", "#94A3B8"))
    factors.append({
        "name": "Fasting Glucose",
        "value": gluc_label,
        "status": gluc_label,
        "impact": "Elevated Risk" if gluc > 1 else "Optimal",
        "color": gluc_col,
        "icon": "🩸"
    })

    # Smoking
    smoke = patient_data["smoke"]
    factors.append({
        "name": "Tobacco Use",
        "value": "Yes (Smoker)" if smoke == 1 else "No (Non-smoker)",
        "status": "Active Smoker" if smoke == 1 else "Non-smoker",
        "impact": "Vascular Strain" if smoke == 1 else "Cardioprotective",
        "color": "#E11D48" if smoke == 1 else "#10B981",
        "icon": "🚭" if smoke == 0 else "🚬"
    })

    # Physical Activity
    active = patient_data["active"]
    factors.append({
        "name": "Physical Activity",
        "value": "Active" if active == 1 else "Sedentary",
        "status": "Regular Exercise" if active == 1 else "Low Activity",
        "impact": "Cardioprotective" if active == 1 else "Risk Factor",
        "color": "#10B981" if active == 1 else "#F59E0B",
        "icon": "🏃"
    })

    return factors
