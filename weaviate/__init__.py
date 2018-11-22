import json

class Database:
    def slurp_by_file_name(schema_file_name):
        with open(schema_file_name) as schema_file_handle:
            # with open(dataset_file_name) as dataset_file_handle:
            return Database.slurp(schema_file_handle)

    def slurp(schema_file_handle):
        schema = Schema.slurp(schema_file_handle)
        #dataset = Dataset.slurp(dataset_file_handle)
        return Database(schema)

    def __init__(self, schema):
        self.schema = schema
        # self.dataset = dataset

    def name(self):
        return self.schema.name

class Schema:
    """Models a Weaviate schema"""
    def slurp(file_handle):
        data = json.loads(file_handle.read())
        schema = Schema(name=data["name"])
        schema.classes = [WClass.from_dict(d, schema) for d in data["classes"]]
        return schema

    def __init__(self, name, classes=[]):
        self.name = name
        self.classes = classes

    def __repr__(self):
        return "<Schema name=\"{}\" classes={}\">".format(self.name, self.classes.__repr__())

class WClass:
    """Models a class, in a Weaviate schema"""
    def slurp(file_handle):
        data = json.loads(file_handle.read())
        schema = Schema(name=data["name"])
        schema.classes = [WClass.from_dict(d, schema) for d in data["classes"]]
        return schema

    def from_dict(d, schema=None):
        c = WClass(schema, d["class"], d["description"])
        c.properties = [Property.from_dict(p) for p in d["properties"]]
        return c

    def __init__(self, schema, class_name, description, properties = []):
        self.schema = schema
        self.class_name = class_name
        self.description = description
        self.properties = properties

    def __repr__(self):
        return "<WClass class_name=\"{}\">".format(self.class_name)

class Property:
    """Models a property, in a Weaviate schema"""
    def from_dict(d):
        return Property(d["name"], d["@dataType"], d["description"])

    def __init__(self, name, datatype, description):
        self.name = name
        self.datatype = datatype
        self.description = description

# class Dataset:
#     def slurp(dataset_file_handle):
#         data = json.loads(dataset_file_handle.read())
#         things = list(map(Thing.from_dict, data["things"]))
#         return Dataset(things)

#     def __init__(self, things):
#         self.things = things

#     def __repr__(self):
#         return "<Dataset things={}>".format(self.things.__repr__())

class Thing:
    def from_dict(d):
        return Thing(d["class"], d["id"], d["schema"])

    def __init__(self, class_name, id, properties):
        self.class_name = class_name
        self.id = id
        self.properties = properties

    def __repr__(self):
        return "<{} id={} properties={}>".format(self.class_name, self.id, self.properties.__repr__())
