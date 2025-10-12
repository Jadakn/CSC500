def get_num_books_purchased_from_input():
    attempts = 0
    while attempts < 5:
        try:
            num_books_purchased = int(input('Enter the number of books you have purchased this month: '))
            if num_books_purchased < 0:
                raise ValueError
            return num_books_purchased
        except ValueError:
            print('Please enter a postive integer value')
            attempts += 1
    print('You have exceeded the maximum amount of input attempts...')
    exit()

fast_point_check_dict = {
    0 : 0,
    1 : 0,
    2 : 5,
    3 : 5,
    4 : 15,
    5 : 15,
    6 : 30,
    7 : 30
}

num_books_purchased = get_num_books_purchased_from_input()
num_points_awarded = 60
if num_books_purchased in fast_point_check_dict:
    num_points_awarded = fast_point_check_dict[num_books_purchased]

print('Congradulations! You have been awarded', num_points_awarded, 'points!')