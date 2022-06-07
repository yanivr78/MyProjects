#/usr/bin/python3

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]
# Endless loop below (DO NOT RUN ! its just an example)
# for i in states_of_america:
#    states_of_america.append("i")

# states_of_america[1] = " Pencilavania" # Will replace Pennsylvania with Pencilavania
print(states_of_america)
states_of_america.extend(["New York", "Texas", "Wyoming"])
print(states_of_america)