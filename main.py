import re
import resources

# objectName = resources.placeholder("object")

# output = resources.pageView(tplPage="templates/page/default.html").HTMLoutput()
# file = open("output.html","w")
# file.write(output)
# file.close()

templateText = """This is a template
And whatever I want to insert should go right here:
@@boldtext@@
It should have been replaced.
Same with the following animal: @@animal@@!
Does one exist for this one? @@fail@@
"""


placeholderBoldText = resources.placeholder("boldtext",{"This text is bold"},"<strong>@@placeholder@@<strong>")
placeholderTiger = resources.placeholder("animal",{"tiger", "elephant"})

allPlaceholders = resources.placeholderCollection((placeholderBoldText, placeholderTiger))

pagetemplate = resources.template(templateText)


output = resources.renderer.fillPlaceholdersFromCollection(pagetemplate.template, allPlaceholders)

print(output)