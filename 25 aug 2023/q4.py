try:
    my_list = [1, 2, 3]
    # Trying to access an attribute that doesn't exist
    average = my_list.avg()
    print("Average:", average)
except AttributeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")





