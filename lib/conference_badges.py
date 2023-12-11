def badge_maker(name):
    print(f"Hello, my name is {name}")
    return "Hello, my name is {}.".format(name)
# print(badge_maker("Ariel"))
def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(names):
    return ["Hello, {}! You'll be assigned to room {}!".format(name, index + 1) for index, name in enumerate(names)]

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in room_assignments:
        print(assignment)

# Example usage
names = ["Arel", "Carol"]
printer(names)
