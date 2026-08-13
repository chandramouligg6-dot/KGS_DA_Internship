#Movie Ticket Generator 

movie_name = input("Enter the movie ticket UID: ")

first_five = movie_name[:5]

last_four = movie_name[-4:]

reversed_name = movie_name[::-1]

index_2_to_7 = movie_name[2:8]

print("Movie Name              :", movie_name)
print("---------------------------------------")
print("First 5 Characters      :", first_five)
print("Last 4 Characters       :", last_four)
print("Reversed Movie Name     :", reversed_name)
print("Characters from index 2-7:", index_2_to_7)