import utils as u


url = u.BASE_URL+u.EXTENSION_BLUE


a, status_code = u.get_items(url)

for i in a:
    print(i)

# implement print fancy function & add to utils!!
