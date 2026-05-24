def generate_password(
    fname,
    lname,
    joining_date
):

    first_part = fname[-2:].lower()

    second_part = lname[:2].lower()

    time_part = joining_date.strftime("%H%M%d")

    password = (
        first_part
        + second_part
        + time_part
    )

    return password