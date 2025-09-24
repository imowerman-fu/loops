def main():
     bark(get_reps())

def get_reps():
     while True:
        number_reps = int(input("Enter the number of times to bark: ")  )
        if number_reps <= 0:
            print("Please enter a non-negative integer and non-zero.")
            continue
        else:
            break
     return (number_reps)

def bark(x):
    for _ in range(int(x)):
        print("Woof!")

main()