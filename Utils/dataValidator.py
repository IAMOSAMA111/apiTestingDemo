from colorama import Fore


def validateJsonData(response, expectedData):
    var = sorted(response) == sorted(expectedData)
    if var:
        print(Fore.GREEN+"Data Validation : ",var)
        return True
    else:
        print(Fore.RED + "Data Validation: ", var)
        return False
