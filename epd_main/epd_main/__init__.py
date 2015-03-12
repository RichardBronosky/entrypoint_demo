import pkg_resources

class ToolSet(object):
  pass

my_tools = ToolSet()
for ep in pkg_resources.iter_entry_points(group='epd_group_id'):
    setattr(my_tools, ep.name, ep.load())
