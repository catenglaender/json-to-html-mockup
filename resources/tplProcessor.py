import re

class placeholder():
    def __init__(self, name, content, partialTemplate=None, rendering=""):
        self.name = name
        self.content = content
        self.partialTemplate = partialTemplate
        self.rendering = rendering
    
class placeholderCollection():
    def __init__(self, placeholders):
        self.placeholders = placeholders

class template():
    def __init__(self, template):
        self.template = template

class renderer():
    def fillPlaceholdersFromDict(template,substitutions):
        search = re.findall('(@@(.+)@@)', template)
        print(search)
        for placeholder, placeholdername in search:
            if placeholdername in substitutions.keys():
                template = template.replace(placeholder, substitutions.get(placeholdername, placeholder))
            if placeholdername not in substitutions.keys():
                print(f"Placeholder key '{placeholdername}' cannot be found in substitution dictionary.")
        return template

    def fillPlaceholdersFromCollection(template,collection):
        if not isinstance(collection, placeholderCollection):
            raise ValueError("collection must be placeholderCollection object")
        if isinstance(collection, placeholderCollection):
            for placeholder in collection.placeholders:
                if placeholder.partialTemplate:
                    for i in placeholder.content:
                        placeholder.rendering = renderer.fillPlaceholdersFromDict(placeholder.partialTemplate, {"placeholder": i})
                if placeholder.partialTemplate is None:
                    for i in placeholder.content:
                        placeholder.rendering += i
        placeholderDict = {}
        for placholder in collection.placeholders:
            placeholderDict[placholder.name] = placholder.rendering
        return renderer.fillPlaceholdersFromDict(template,placeholderDict)
