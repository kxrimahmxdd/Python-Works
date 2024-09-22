slices_per_person = 0
total_people = 4
slices_per_pizza = 8
total_slices = slices_per_person * total_people
pizzas_required = total_slices // slices_per_pizza
leftover_slices = total_slices % slices_per_pizza

print(f"Pizza's required for test case 1: {pizzas_required}")
print(f"Leftover slices for test case 1: {leftover_slices}")