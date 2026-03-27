def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_data = []
        
    for item in data:   
        if type(item) == str and item.isdigit():
            cleaned_data.append(int(item))
        if type(item) == int:
            cleaned_data.append(item)
    
    return cleaned_data