def generate_corporate_mail(fname, lname):

    corporate_mail = (
        fname[0].lower()
        + lname.lower()
        + "@miraclesoft.com"
    )

    return corporate_mail