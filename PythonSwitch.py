def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something is not right with the internet."


# Can also do some cool things with match
def check_location(coord):
    match coord:
        case (0, 0):
            print("Home")
        case (0, y):
            print(f"Y={y}")
        case _:
            raise ValueError("Nil poit!")
