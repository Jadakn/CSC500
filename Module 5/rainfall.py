
def get_inches_for_month(year_num, month_num):
    attempts = 0
    while attempts < 5:
        try:
            num_inches_per_month = float(input("Enter the amount of inches of rain received for year " + str(year_num) + " month " + str(month_num) + ': '))
            if num_inches_per_month < 0:
                raise ValueError
            return num_inches_per_month
        except ValueError:
            print("Error: Please enter a positive numeric float (decimal) value for the number of inches of rain received for year", str(year_num), "month", str(month_num))
            attempts += 1
    print('Error: Maximum number of input attempts exceeded.')
    exit()

if __name__ == "__main__":
    try:
        num_years = int(input("Enter the number of years to calculate average rainfall over: "))
        if num_years < 0:
            raise ValueError
    except ValueError:
        print("Error: Please enter a positive integer for the number of years of rain that has fallen.")
        exit()
    
    total_inches_of_rainfall = 0.0
    total_num_months = 0
    for year in range(num_years):
        for month in range(12):
            total_num_months += 1
            total_inches_of_rainfall += get_inches_for_month(year + 1, month + 1)

    average_rainfall_per_month = total_inches_of_rainfall / total_num_months
    print("The total number of months is :", str(total_num_months))
    print("The total inches of rainfall is :", str(total_inches_of_rainfall))
    print("The average rainfall per month over", str(num_years), "years is :", "{:.2f}".format(average_rainfall_per_month))
