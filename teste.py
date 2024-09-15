from qualitag import CodingProject

project = CodingProject()
project.tags_manager.create_tag("tag1", "red")
project.tags_manager.create_tag("tag2", "blue")
project.tags_manager.create_tag("tag3", "green")
project.save("project.pkl")