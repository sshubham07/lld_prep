from Person import Person

class Admin(Person):
    def add_show(self, show):
        print("Show added by admin.")
        return True

    def update_show(self, show):
        print("Show updated by admin.")
        return True

    def delete_show(self, show):
        print("Show deleted by admin.")
        return True

    def add_movie(self, movie):
        print("Movie added by admin.")
        return True

    def delete_movie(self, movie):
        print("Movie deleted by admin.")
        return True
