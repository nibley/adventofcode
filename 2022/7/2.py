def clean_path(path):
    if '..' not in path:
        return path

    first_up_index = path.index('..')
    path = tuple( path[i]
        for i in range(len(path))
        if i not in (first_up_index - 1, first_up_index) )

    return clean_path(path)

filesystem_raw = {}
current_path = ()
current_listing = []
did_listing = False
while True:
    try:
        line = input()
    except EOFError:
        filesystem_raw[clean_path(current_path)] = current_listing
        current_listing = []

        break

    if line.startswith('$'):
        if did_listing:
            filesystem_raw[clean_path(current_path)] = current_listing
            current_listing = []

        if line[2:].startswith('cd'):
            cd_arg = line[5:]
            if cd_arg == '/':
                current_path = ()
            else:
                current_path += (cd_arg, )

            did_listing = False
        elif line[2:].startswith('ls'):
            did_listing = True
    else:
        current_listing.append(line)

dir_sizes = {}
def parse_filesystem(path):
    listing = filesystem_raw[path]

    files = [ int(item.split(' ')[0])
        for item in listing
        if not item.startswith('dir') ]

    size = sum(files)

    subpaths = [ path + (item.split(' ')[1], )
        for item in listing
        if item.startswith('dir') ]

    subdirs = tuple([ parse_filesystem(subpath)
        for subpath in subpaths ])

    for subdir in subdirs:
        size += subdir[1]

    dir_sizes[path] = size

    return (path, size, subdirs)

parse_filesystem(())

free_space = 70_000_000 - dir_sizes[ () ]
needed_space = 30_000_000 - free_space

print(sorted(size
    for path, size in dir_sizes.items()
    if size >= needed_space)[0])
