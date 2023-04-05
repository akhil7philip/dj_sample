class SalesRouter:
    
    """
    A router to control all database operations on models in ev_service app
    """

    route_app_labels = {'app_one'}
    db_name = 'sales'

    def db_for_read(self, model, **hints):
        """
        Attempts to read models that go to OEM_CFT_MIS
        """
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write models that go to OEM_CFT_MIS
        """
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the ev_service application is involved
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure these models only appear in the 'OEM_CFT_MIS' database
        """
        if db == app_label:
            return True
        elif db == 'default':
            return True
        else:
            return False
