import struct, sys, os.path, re

def convertGigaCadPlus(filename):
    # read in file
    f = open(filename, "rb")
    data = f.read()
    f.close()

    # read header
    p = 0
    tmp = ""
    while data[p] != 0xD:
            tmp += chr(data[p])
            p += 1
    p += 1
    polygon_count = int(tmp)
    tmp = ""
    while data[p] != 0xD:
            tmp += chr(data[p])
            p += 1
    p += 1
    vertex_count = int(tmp)
    tmp = ""
    while data[p] != 0xD:
            tmp += chr(data[p])
            p += 1
    p += 1
    object_count = int(tmp)

    # read polygons
    polygons = []
    for i in range(polygon_count):
            a,b = struct.unpack_from("<hb", data, p)
            p += 3
            obj = b & 63
            flags = b>>6
            if a > 0:
                polygons.append((a, obj, flags))
    polygons.append((vertex_count, 0, 0))

    # unknown (offset?)
    x,y,z = struct.unpack_from("<hhh", data, p)
    p += 6

    # read vertices
    vertices = []
    for i in range(vertex_count):
            x,y,z = struct.unpack_from("<hhh", data, p)
            p += 6
            vertices.append((x,y,z))

    # read object names
    object_names = []
    for i in range(object_count):
            tmp = ""
            while data[p] != 0xD:
                    tmp += chr(data[p])
                    p += 1
            p += 1
            object_names.append(tmp)

    # generate wavefront filename
    dirname,filename = os.path.split(filename)
    m = re.match(r"^(?:ob\.)?(.*?)(?:\.seq)?$", filename, re.I)
    if m:
        name = m.group(1)
    else:
        name = filename

    with open(os.path.join(dirname, name + ".obj"), "wt") as f:
        # write vertices
        for a in vertices:
                f.write ("v %i %i %i\n" % a)

        # repack objects
        objects = []
        for i in range(object_count + 1):
            objects.append([])
        for i in range(len(polygons)-1):
            start, obj, flags = polygons[i]
            count = polygons[i+1][0] - start
            objects[obj].append((start, count))

        # write faces grouped by object
        for i in range(len(objects)):
                if len(objects[i]) > 0:
                    if i > 0:
                        f.write("o %s\n" % object_names[i-1])
                    for j in range(len(objects[i])):
                        start, count = objects[i][j]
                        face = []
                        for k in range(count):
                                face.append(start + k)
                        f.write ("f " + " ".join([str(x) for x in face]) + "\n")
        f.close()

def main():
    for i in sys.argv[1:]:
        convertGigaCadPlus(i)

if __name__ == "__main__":
	main()
