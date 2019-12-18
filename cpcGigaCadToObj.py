import struct, sys, os.path

def convertCpcGigaCad(filename):
    # read in file
    f = open(filename, "rb")
    data = f.read()
    f.close()
	
    # length
    length,_ = struct.unpack_from("<hh", data, 0)
    length += 4
    
    # matrix
    m00, m01, m02, m03, s0 = struct.unpack_from("<hhhhh", data, 4)
    print (m00, m01, m02, m03, s0)
    m10, m11, m12, m13, s1 = struct.unpack_from("<hhhhh", data, 14)
    print (m10, m11, m12, m13, s1)
    m20, m21, m22, m23, s2 = struct.unpack_from("<hhhhh", data, 24)
    print (m20, m21, m22, m23, s2)
    
    # light pos
    lx, ly, lz = struct.unpack_from("<hhh", data, 34)
    print (lx, ly, lz)

    # coordinate min
    sx, sy, sz = struct.unpack_from("<hhh", data, 40)
    print (sx, sy, sz)

    # coordinate max
    ex, ey, ez = struct.unpack_from("<hhh", data, 46)
    print (ex, ey, ez)

    objects = []
    vertices = []
    obj = []
    pos = 52
    while pos < length:
        count = data[pos]
        pos+=1
        if count == 0xFF:
            if len(obj) > 0:
                objects.append(obj)
                obj = []
        elif count == 0x00:
            break
        else:
            face = []
            for i in range(count & 31):
                x,y,z = struct.unpack_from("<hhh", data, pos)
                idx = len(vertices)
                vertices.append((x,y,z))
                face.append(idx)
                pos += 6
            x = data[pos]
            pos += 1
            obj.append(face)
    if len(obj) > 0:
        objects.append(obj)

    # generate wavefront filename
    dirname,filename = os.path.split(filename)
    name,_ = os.path.splitext(filename)

    with open(os.path.join(dirname, name + "_wf.obj"), "wt") as f:
        # write vertices
        for a in vertices:
                f.write ("v %i %i %i\n" % a)

        # write faces grouped by object
        for i in range(len(objects)):
            f.write("o obj%i\n" % i)
            for j in range(len(objects[i])):
                face = objects[i][j]
                f.write ("f " + " ".join([str(x + 1) for x in face]) + "\n")
        f.close()

                                
def main():
    for i in sys.argv[1:]:
        convertCpcGigaCad(i)

if __name__ == "__main__":
    main()
