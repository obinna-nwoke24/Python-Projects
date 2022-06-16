import math


class Client:
    """
    This creates a client class with the following:

    Name: First and Last

    Height: inches

    Weight: lbs

    Gender: either Male or Female

    Age
    """
    goal = ['weight loss', 'weight gain', 'build muscle', 'maintain weight']
    specific_areas = ['arms', 'legs', 'back', 'chest', 'abs']
    activity = {'sedentary': [1.2, 'little to no exercise'],
                'lightly active': [1.375, 'light exercise (1-2 times per week)'],
                'moderately active': [1.55, 'moderate exercise (2-3 times per week)'],
                'very active': [1.725, 'hard exercise (4-5 times per week)'],
                'extra active': [1.9, 'physical job or hard exercise (6-7 times per week)']
                }

    def __init__(self, name: str, height: int, weight: int, gender: str, age: int = 0, activity_response: str = ""):
        """
        Creates a client using the following params

        *allows for either user input or preset params*

        :param name: Name of the client
        :param height: Height of the client in inches
        :param weight: Weight of the client in lbs
        :param gender: Gender of the client [male, female]
        :param age: Set to 0 to allow for preset values
        :param activity_response: Set to blank to allow for preset values
        """
        self.name = name
        self.height = height
        self.weight = weight
        genders = ['male', 'female']
        if gender.lower() in genders:
            if gender.lower() == genders[0]:
                self.gender = 'male'
            else:
                self.gender = 'female'
        else:
            print("Gender is not in available genders!")
            self.set_gender(input("Gender: "))
        self.bmr, self.maintenance, self.age, self.activity_level = self.generate_maintenance(age, activity_response)
        self.nutrition_split = self.generate_nutrition_split()

    def split_name(self):
        """
        This method takes the name initialized and separates it by first and last

        :return: Tuple (First Name, Last Name)
        """
        first_and_last = self.name.split()
        return first_and_last[0], first_and_last[1]

    def set_gender(self, gender: str = ""):
        """
        Sets the gender of the client. Only to be used if the gender is not accepted the first time.

        :param gender: String
        :return: None
        """
        genders = ['male', 'female']
        if gender.lower() in genders:
            if gender.lower() == genders[0]:
                self.gender = 'male'
            else:
                self.gender = 'female'
        else:
            print("Gender is not in available genders!")
            self.set_gender(input("Gender: "))

    def convert_height(self):
        """
        Converts given height to feet and inches

        :return: String
        """
        height = self.height
        feet = height // 12
        inches = height % 12
        return "{}' {}".format(feet, inches)

    def client_description(self):
        """
        Prints the description of the client

        :return: None
        """
        print("Name: {}\n".format(self.name) +
              "Height: {}\n".format(self.convert_height()) +
              "Weight: {} lbs\n".format(self.weight) +
              "Gender: {}".format(self.gender))

    def generate_maintenance(self, age: int = 0, ans: str = ""):
        """
        Calculates BMR using the Harris-Benedict equation

        Then uses activity rate from scale to determine maintenance

        :return: int
        """
        if self.gender == 'male':
            if age == 0:
                age = int(input("How old is {}?: ".format(self.split_name()[0])))
            bmr = 66.5 + (13.75 * (self.weight * 0.45359237)) + (5.003 * (self.height * 2.54)) - \
                  (6.75 * age)
            """
            print("\n{}'s BMR (basal metabolic rate) is {} calories per day".format(self.split_name()[0],
                                                                                    math.ceil(bmr)))
                                                                                    """

            if ans == "":
                print()
                for level in self.activity.keys():
                    print(level)

            def prompt(answer=ans):
                if answer == "":
                    answer = input("Which level best describes {}? (type help to see descriptions): ".format(
                        self.split_name()[0]
                    ))
                if answer.lower() == 'help':
                    print()
                    for key in self.activity.keys():
                        print("{} - {}".format(key, self.activity[key][1]))
                    answer = prompt()
                return answer

            response = prompt()
            while response not in list(self.activity.keys()):
                print("\nResponse is not in the activity levels!\n")
                for level in self.activity.keys():
                    print(level)
                response = prompt()

            self.maintenance = math.ceil(bmr * self.activity[response][0])
            # print("Maintenance calories: {} calories per day".format(self.maintenance))
            return math.ceil(bmr), self.maintenance, age, response

        else:
            if age == 0:
                age = int(input("How old is {}?: ".format(self.split_name()[0])))
            bmr = 655.1 + (9.563 * (self.weight * 0.45359237)) + (1.850 * (self.height * 2.54)) - \
                  (4.676 * age)
            """
            print("\n{}'s BMR (basal metabolic rate) is {} calories per day\n".format(self.split_name()[0],
                                                                                      math.ceil(bmr)))"""

            if ans == "":
                print()
                for level in self.activity.keys():
                    print(level)

            def prompt(answer=ans):
                if answer == "":
                    answer = input("Which level best describes {}? (type help to see descriptions): ".format(
                        self.split_name()[0]
                    ))
                if answer.lower() == 'help':
                    print()
                    for key in self.activity.keys():
                        print("{} - {}".format(key, self.activity[key][1]))
                    answer = prompt()
                return answer

            response = prompt()
            while response not in list(self.activity.keys()):
                print("\nResponse is not in the activity levels!\n")
                for level in self.activity.keys():
                    print(level)
                response = prompt()

            self.maintenance = math.ceil(bmr * self.activity[response][0])
            # print("Your maintenance calories is {} calories per day".format(self.maintenance))
            return math.ceil(bmr), self.maintenance, age, response

    def lose_weight(self, minus=1):
        """
        Returns the weight in lbs to lose given the parameter

        :param minus:
        :return: Calories
        """
        calories = self.maintenance
        try:
            if (minus <= 0) or (minus >= 3):
                raise ValueError
            else:
                calories -= minus * 500
                return int(calories)
        except ValueError:
            if minus <= 0:
                print("Cannot lose 0 or less lbs")
                print("Resetting weight to maintenance")
                return int(calories)
            if minus >= 3:
                print("We do not recommend losing 3 or more lbs per week.")
                print("Resetting weight to maintenance")
                return int(calories)

    def gain_weight(self, plus=1):
        """
        Returns the weight in lbs to gain given the parameter

        :param plus:
        :return: Calories
        """
        calories = self.maintenance
        try:
            if (plus <= 0) or (plus >= 3):
                raise ValueError
            else:
                calories += plus * 500
                return calories
        except ValueError:
            print("Value Error")

    def set_goal(self, calories=0):
        """
        *this method is still in development*

        :param calories:
        :return:
        """
        for num in range(len(self.goal)):
            print("#{}: {}".format(num + 1, self.goal[num]))
        choice = int(input("Which goal best aligns to you? "))
        optional = input("Do you have a second choice (type 'no' or a number)? ")
        goal = ""
        if optional.lower() == 'no':
            # instruction for the one goal
            if choice == 1:
                goal += 'Calories to maintain weight {} kcal'.format(self.maintenance)
                goal += '\n{} kcal/day to lose 1lb per week'.format(self.maintenance - 500)
                goal += '{}'.format(self.generate_nutrition_split(calories=self.maintenance - 500))
                goal += '\n{} kcal/day to lose 2lbs per week'.format(self.maintenance - 1000)
                goal += '{}'.format(self.generate_nutrition_split(calories=self.maintenance - 1000))
                print(goal)
            elif int(optional) == 2:
                pass
            elif int(optional) == 3:
                pass
            elif int(optional) == 4:
                pass
            else:
                print("Invalid option!")
                self.set_goal()
            pass

    def generate_nutrition_split(self, calories=0, protein=.25, carbs=.50, fat=.25):
        """
        Generates macronutrients from calories

        25% protein, 45% carbs, 30% fats

        :param calories:
        :param protein:
        :param carbs:
        :param fat:
        :return: String of the nutrition plan
        """
        nutrition_plan = "\n{}'s Nutrition Split\nDaily Macronutrients - Maintenance {} kcal\n". \
            format(self.split_name()[0], self.maintenance)
        if calories == 0:
            calories = self.maintenance
        grams_protein = math.floor(calories * protein / 4)
        grams_carbs = math.floor(calories * carbs / 4)
        grams_fat = math.floor(calories * fat / 9)
        nutrition_plan += "Protein: {}g\n".format(grams_protein)
        nutrition_plan += "Carbohydrates: {}g\n".format(grams_carbs)
        nutrition_plan += "Fats: {}g\n".format(grams_fat)

        calories = self.maintenance + 500
        nutrition_plan += "\nDaily Macronutrients -> +1 Lb/Week {} kcal\n".format(calories)
        grams_protein = math.floor(calories * protein / 4)
        grams_carbs = math.floor(calories * carbs / 4)
        grams_fat = math.floor(calories * fat / 9)
        nutrition_plan += "Protein: {}g\n".format(grams_protein)
        nutrition_plan += "Carbohydrates: {}g\n".format(grams_carbs)
        nutrition_plan += "Fats: {}g\n".format(grams_fat)

        calories = self.maintenance - 500
        nutrition_plan += "\nDaily Macronutrients -> -1 Lb/Week {} kcal\n".format(calories)
        grams_protein = math.floor(calories * protein / 4)
        grams_carbs = math.floor(calories * carbs / 4)
        grams_fat = math.floor(calories * fat / 9)
        nutrition_plan += "Protein: {}g\n".format(grams_protein)
        nutrition_plan += "Carbohydrates: {}g\n".format(grams_carbs)
        nutrition_plan += "Fats: {}g\n".format(grams_fat)
        return nutrition_plan
