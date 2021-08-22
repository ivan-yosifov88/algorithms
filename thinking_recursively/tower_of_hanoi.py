def tower_of_hanoi(num_disks, first, final, middle):
    if num_disks == 1:
        print(f"Moving the disk 1 from {first} to the {final}")
    else:
        tower_of_hanoi(num_disks - 1, first, middle, final)
        print(f"Moving the {num_disks} from {first} to the {final}")
        tower_of_hanoi(num_disks - 1, middle, final, first)

tower_of_hanoi(3, "First", "Final", "Middle")
