def mask(people):
    """
    TODO: Mask emails and phone numbers:
    - keep domain part of email, mask local part
    - keep last 2 digits of phone number, mask the rest with asterisks
    - return same datastructure with masked data
    """
    result = []
    
    for person in people:

        masked_item = person.copy()

        email = person.get("email", "")
        local, domain = email.split("@")
        masked_item["email"] = f"{'*' * len(local)}@{domain}"

        phone = person.get("phone","")
        masked_item["phone"] = "*" *  (len(phone)-2) + phone[-2:]
        
        result.append(masked_item)

    return result
    
    
    
    
    
    
    
    pass