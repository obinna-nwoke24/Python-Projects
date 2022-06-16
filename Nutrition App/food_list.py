import Client


class FoodList:
    def __init__(self, client: Client.Client, preset: bool = True):
        """
        Creates a food list of carbs, proteins, and fats

        Preset data is for weight loss
        """
        self.food_list = self.generate_food_list(client, preset=preset)
        self.carb_list, self.protein_list, self.fat_list = self.list_toText(self.food_list)

    def generate_food_list(self, client: Client.Client, preset: bool = True):
        """
        Creates a food list of carbs, proteins, and fats

        Weight loss
        :return: food list dictionary
        """
        if preset:
            carb_list = [
                'Whole grain foods (breads, pasta, rice)',
                'Oats',
                'Fruits & Veggies'
            ]
            protein_list = [
                'Chicken breast',
                'Ground Chicken (as lean as you can get)',
                'Ground Turkey (as lean as you can get)',
                'Eggs (whites have the protein in them) *use more whites than whole eggs*',
                'Fish (of choice)',
                'Protein powder *optional*'
            ]
            fat_list = [
                'Nuts (almonds, peanuts, cashews, walnuts, etc.)',
                'Oils (olive oil, etc.) *minimize*'
            ]
        else:
            carb_list = input("Write a list of carbs to eat for {} (separated by comma): ".
                              format(client.split_name()[0]))
            carb_list = carb_list.split(sep=',')
            carb_list = [word.strip().capitalize() for word in carb_list]

            protein_list = input("Write a list of proteins to eat for {} (separated by comma): ".
                                 format(client.split_name()[0]))
            protein_list = protein_list.split(sep=',')
            protein_list = [word.strip().capitalize() for word in protein_list]

            fat_list = input("Write a list of fats to eat for {} (separated by comma): "
                             .format(client.split_name()[0]))
            fat_list = fat_list.split(sep=',')
            fat_list = [word.strip().capitalize() for word in fat_list]

        food_list = {'Carbs': carb_list, 'Proteins': protein_list, 'Fats': fat_list}
        return food_list

    def list_toText(self, lst: dict):
        """
        Returns the string version of a food list

        Only compatible with the pdf_api
        :param lst:
        :return: carb text formatted, protein text formatted, fat text formatted
        """

        carb_text = "Carbs:\n"
        for carb in lst['Carbs']:
            carb_text += '\n- {}'.format(carb)
        protein_text = "Proteins:\n"
        for protein in lst['Proteins']:
            protein_text += '\n- {}'.format(protein)
        fat_text = "Fats:\n"
        for fat in lst['Fats']:
            fat_text += '\n- {}'.format(fat)
        return carb_text, protein_text, fat_text
