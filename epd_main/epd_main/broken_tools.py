import pkg_resources

# while this seemingly works, it make static analysis impossible and should be avoided
for ep in pkg_resources.iter_entry_points(group='epd_group_id'):
    globals()[ep.name] = ep.load()

del(ep, pkg_resources)
