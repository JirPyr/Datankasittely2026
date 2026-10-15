from datetime import datetime

def anonymize(people):

    result = []
    """
    TODO: Anonymize data:
    - remove name
    - keep only birth year
    - keep only first letter of city
    - return same datastructure with anonymized data
    """
   

    for person in people:

        anonymized_item = person.copy()

        anonymized_item["birth_year"]= int(person["birthdate"][:4])
        anonymized_item["city_initial"] = person["city"][0] 

        del anonymized_item["name"]
        del anonymized_item["city"]
        del anonymized_item["birthdate"]
        

        result.append(anonymized_item)
    return result
pass