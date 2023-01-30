# The following code will print the keyword arguments 
# passed to the function


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Albert, 'Einstein',
                            location = 'Princeton', 
                            field = 'physics')
print(user_profile)

user_profile2 = build_profile("Janice", "Cotcher",
                             location = "Regina",
                             field = "Computer Science",
                             position = "Teacher")
print(user_profile2)