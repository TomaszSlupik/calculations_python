# Oblicz total cost i avg
num_of_cars = 100
num_of_parts = 1000
cost_per_part = 10
total_cost = num_of_cars * num_of_parts * cost_per_part
avg_cost_per_car = total_cost / num_of_cars

print(f"Total cost of manufacturing all the cars: {total_cost}")
print(f"Average cost per car: {avg_cost_per_car}")

print("---")

# Oblicz srednią liczbę postów na użytkownika
# oraz średnią liczbę polubień na post
num_of_users = 9045
num_of_posts = 54822
num_of_likes = 251561

avg_posts_per_user = num_of_posts / num_of_users
avg_likes_per_post = num_of_likes / num_of_posts

print(f"Average number of posts per user: {avg_posts_per_user :.2f}")
print(f"Average number of likes per post: {avg_likes_per_post :.2f}")

print('---')

# Obliczyć resztę z dzielenia employee_id
# Przekonwertuj username_number na łańcuch znaków
# Połącz łańcuch znaków 
employee_id = 123451612

username_number = employee_id % 10001
username_suffix = str(username_number) 
username = 'user_' + username_suffix
print(username)

print('---')

# napisanie programu, który obliczy całkowitą liczbę stron wymaganych do wyświetlenia wszystkich postów. 
total_num_posts = 47
posts_per_page = 10
total_page = round(47 / 10, 0)

print(f"The total number of pages required to display all the posts is: {total_page :.0f}")

print('---')

# Twoim zadaniem jest napisanie programu, 
# który obliczy dzienną wydajność systemu paneli 
# słonecznych oraz liczbę dni, przez które bateria może 
# zasilać system, zanim będzie trzeba ją naładować

daily_energy = 6000
system_efficiency = 85
battery_capacity = 30000

system_output = daily_energy * system_efficiency / 100
days = int(battery_capacity // system_output)
 
print(f'The solar panel system output: {system_output} watt-hours/day.')
print(f'The battery can power the system for {days} days.')