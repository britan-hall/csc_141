def build_profile(first, last, **user_info):
    """Build a dictionary containing user information."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Britan', 'Hall',
                            location='Bernville',
                            age=17,
                            field='Computer Science')

print("User Profile:")
print(f"First Name: {user_profile['first_name']}")
print(f"Last Name: {user_profile['last_name']}")
print(f"Location: {user_profile.get('location', 'Not provided')}")
print(f"Age: {user_profile.get('age', 'Not provided')}")
print(f"Field: {user_profile.get('field', 'Not provided')}")
