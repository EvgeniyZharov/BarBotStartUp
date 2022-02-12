import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import config


class FirebaseWork:

    def __init__(self):
        self.cred = credentials.Certificate(config.firebase_path_to_key)
        firebase_admin.initialize_app(self.cred, {
            "databaseURL": config.firebase_link_to_db
        })
        self.ref = db.reference('/')
        try:
            check_status_db = self.ref.get()
            if "db_status" not in check_status_db:
                self.ref.set(config.template_json)
        except Exception as ex:
            self.ref.set(config.template_json)

    def set(self, new_dict):
        self.ref.set(new_dict)

    def get(self):
        return self.ref.get()

    def check_exist_user(self, user_id):
        data = self.get()
        if user_id in data["users"]:
            return True
        else:
            return False

    def set_new_user(self, user_id, data_reg):
        try:
            data = self.get()
            template_user = config.user_templates_json
            template_user[config.keys_for_user_json[4]] = data_reg
            data["users"][user_id] = template_user
            self.set(data)
            return [True]
        except Exception:
            return [False]

    def change_user_status(self, user_id, new_status):
        try:
            data = self.get()
            data["users"][user_id][config.keys_for_user_json[0]] = new_status
            self.set(data)
            return [True]
        except Exception:
            return [False]

    def change_user_menu_status(self, user_id, new_menu_status):
        try:
            data = self.get()
            data["users"][user_id][config.keys_for_user_json[1]] = new_menu_status
            self.set(data)
            return [True]
        except Exception:
            return [False]

    def change_user_help_info(self, user_id, new_help_info):
        try:
            data = self.get()
            data["users"][user_id][config.keys_for_user_json[2]] = new_help_info
            self.set(data)
            return [True]
        except Exception:
            return [False]

    def set_new_activity(self, title, country, city, district, category, time, rating):
        try:
            data = self.get()
            template_activity = config.place_template_json

            template_activity[config.keys_for_place_json[0]] = category
            template_activity[config.keys_for_place_json[1]] = time
            template_activity[config.keys_for_place_json[3]] = rating
            template_activity[config.keys_for_place_json[6]] = country
            template_activity[config.keys_for_place_json[7]] = city
            template_activity[config.keys_for_place_json[8]] = district
            data["activity"][title] = template_activity
            self.set(data)
            return [True]
        except Exception:
            return [False]




